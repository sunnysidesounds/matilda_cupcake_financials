import os
import sys
from support.gmail_api import GmailService
from config import Configuration
from support.model_builder import ModelBuilder


def files_exist():
    data_files = Configuration.data_files
    for file in data_files:
        if not os.path.exists(os.path.join(Configuration.storage_path, file)):
            return False
    return True


def main():

    # Step 1: Connect to gmail service download email attachments from most recent `cupcakes` subjected email
    service = GmailService(Configuration.credentials_file, Configuration.credentials_pickle_file, Configuration.scopes)
    most_recent_msg_id = service.search_msg_ids_containing(Configuration.email_keyword_query).pop()
    downloaded_attachments = service.get_attachments('me', most_recent_msg_id, Configuration.storage_path)
    if downloaded_attachments:
        print("1. Downloaded {files} with message_id: {messageId}".format(files=', '.join(downloaded_attachments), messageId=most_recent_msg_id))
    else:
        print("ERROR. No email attachments don't exist can't proceed, exiting!")
        sys.exit()

    # Step 2: Parse files of Basic.txt, Delux.txt, and Total.txt and build a dictionary model of dates and amounts
    # Example: {"basic": [{"date": '1-1-2020', "amount": 2}], "delux": [], "total": []}
    model_builder = ModelBuilder()
    total_records = 0
    if files_exist():
        model = model_builder.get_model()
        if len(model['basic']) == len(model['delux']) and len(model['basic']) == len(model['total']):
            total_records = len(model['basic'])
            status = 'PASSED'
        else:
            status = 'FAILED'
        print("2. Building model with data received, total records: {totalRecords} - {status}".format(totalRecords=total_records, status=status))
    else:
        print("ERROR. No files don't exist can't proceed, exiting!")
        sys.exit()

    # Step 3: Calculate Financial Data


    # Step 4: Generate email to send report


if __name__ == '__main__':
    main()