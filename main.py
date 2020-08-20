import os
import sys
import argparse
from support.gmail_api import GmailService
from config import Configuration
from support.model_builder import ModelBuilder


def files_exist():
    data_files = Configuration.data_files
    for file in data_files:
        if not os.path.exists(os.path.join(Configuration.storage_path, file)):
            return False
    return True


def filter_model_by_args(args, model):
    results_model = ModelBuilder.build_results_model()
    results_model['type'] = args.type
    results_model['model'] = model[args.type]
    if args.year:
        results_model['year'] = int(args.year)
        # filter to year
        results_model['model'] = [m for m in results_model['model'] if m['year'] == results_model['year']]

    if args.month:
        results_model['month'] = int(args.month)
        # filter to month
        results_model['model'] = [m for m in results_model['model'] if m['month'] == results_model['month']]

    if args.week:
        results_model['week'] = int(args.week)
        # filter to week
        results_model['model'] = [m for m in results_model['model'] if m['week'] == results_model['week']]

    return results_model


def calculate_revenue(model):
    if model['type'] == 'total':
        total = sum([r['amount'] for r in model['model']])
        model['revenue'] = "${:,.2f}".format(total)
    elif model['type'] == 'basic':
        total = sum([Configuration.cost_of_basic * r['amount'] for r in model['model']])
        model['revenue'] = "${:,.2f}".format(total)
    elif model['type'] == 'delux':
        total = sum([Configuration.cost_of_delux * r['amount'] for r in model['model']])
        model['revenue'] = "${:,.2f}".format(total)
    return model


def main():
    # Init command-line arguments parser
    parser = argparse.ArgumentParser(
        description="Matilda Cupcakes Financials Calculator"
    )
    parser.add_argument('-y', '--year', help="Calculate by year", type=int)
    parser.add_argument('-m', '--month', help="Calculate by month", type=int)
    parser.add_argument('-w', '--week', help="Calculate by week", type=int)
    parser.add_argument('-t', '--type', help="Calculate by type", type=str, required=True, choices=['basic', 'delux', 'total'])
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
    results_model = None
    if status and total_records > 0:
        filtered_model = filter_model_by_args(args, model)
        results_model = calculate_revenue(filtered_model)
        print("3. Calculating financials with arguments: {arguments}".format(arguments=args))
        print(" - Total revenue for period: {revenue}".format(revenue=results_model['revenue']))
    else:
        print("ERROR: status: {status} - total_records: {totalRecords}".format(totalRecords=total_records, status=status))

    # Step 4: Generate email to send report
    if results_model['revenue']:
        # TODO
        pass


if __name__ == '__main__':
    main()