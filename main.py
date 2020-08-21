import os
import sys
import argparse
from tabulate import tabulate
from support.gmail_api import GmailService
from config import Configuration
from support.model_manipulator import ModelBuilder
from support.financial_calulator import FinancialCalculator


def files_exist():
    data_files = Configuration.data_files
    for file in data_files:
        if not os.path.exists(os.path.join(Configuration.storage_path, file)):
            return False
    return True


def main():
    # Init command-line arguments parser
    parser = argparse.ArgumentParser(
        description="Matilda Cupcakes Financials Calculator"
    )
    parser.add_argument('-y', '--year', help="Calculate by year", type=int)
    parser.add_argument('-m', '--month', help="Calculate by month", type=int)
    parser.add_argument('-w', '--week', help="Calculate by week", type=int)
    parser.add_argument('-t', '--type', help="Calculate by type", type=str, required=True, choices=['basic', 'delux', 'total', 'all'])

    try:
        args = parser.parse_args()

        # Step 1: Connect to gmail service download email attachments from most recent `cupcakes` subjected email
        service = GmailService(Configuration.credentials_file, Configuration.credentials_pickle_file, Configuration.scopes)
        most_recent_msg_id = service.search_msg_ids_containing(Configuration.email_keyword_query).pop()
        downloaded_attachments = service.get_attachments('me', most_recent_msg_id, Configuration.storage_path)
        if downloaded_attachments:
            print("1. Downloaded {files} with message_id: {messageId}".format(files=', '.join(downloaded_attachments), messageId=most_recent_msg_id))
        else:
            print("ERROR: No email attachments don't exist can't proceed, exiting!")
            sys.exit()

        # Step 2: Parse files of Basic.txt, Delux.txt, and Total.txt and build a dictionary model of dates and amounts
        # Example: {"basic": [{"date": '1-1-2020', "amount": 2, ... }], "delux": [], "total": []}
        model_builder = ModelBuilder()
        total_records = 0
        status = False
        if files_exist():
            model = model_builder.get_model()
            if len(model['basic']) == len(model['delux']) and len(model['basic']) == len(model['total']):
                total_records = len(model['basic'])
                status = True
                print("2. Building model with data received, total records: {totalRecords} - status: {status}".format(totalRecords=total_records, status=status))
            else:
                print("ERROR: In building model with data total records: {totalRecords} - status: {status}".format(totalRecords=total_records, status=status))

        else:
            print("ERROR: No files don't exist can't proceed, exiting!")
            sys.exit()

        # Step 3: Filter dataset and calculate Financial Data
        results_model_list = []

        if status and total_records > 0:
            print("3. Calculating financials with arguments: {arguments}".format(arguments=args))
            if args.type == 'all':
                for type in ['basic', 'delux', 'total']:
                    args.type = type
                    filtered_model = model_builder.filter_model_by_args(args)
                    results_model = FinancialCalculator.calculate_revenue(filtered_model)
                    results_model_list.append(results_model)
            else:
                filtered_model = model_builder.filter_model_by_args(args)
                results_model = FinancialCalculator.calculate_revenue(filtered_model)
                results_model_list.append(results_model)

        else:
            print("ERROR: status: {status} - total_records: {totalRecords}".format(totalRecords=total_records, status=status))

        # Step 4: Generate email to send report
        if len(results_model_list) > 0:
            message = Configuration.email['subject'] + ": <br/>"
            message += "Year={year}, Week={week}, Month={month}<br/><br/>".format(year=args.year, week=args.week, month=args.month)
            for result_model in results_model_list:

                message += "- {type} : {revenue} <br/>".format(type=result_model['type'], revenue=result_model['revenue'])

                print(" - Total revenue with type: {type} - revenue: {revenue}".format(type=result_model['type'], revenue=result_model['revenue']))


            sent_message = service.send_message(Configuration.email['from'], Configuration.email['to'], Configuration.email['subject'], message, message)

            print("4. Sending calulated data to {toEmail} - message_id: {messageId}".format(toEmail=Configuration.email["to"], messageId=sent_message['id']))

        else:
            print("ERROR: No revenue could be calculated for these arguments {arguments}".format(arguments=args))

    except Exception as e:
        print(e)
        sys.exit(0)


if __name__ == '__main__':
    main()
