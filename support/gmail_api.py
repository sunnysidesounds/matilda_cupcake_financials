import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from apiclient import errors


class GmailService(object):

    def __init__(self, credentials_path, token_name, scopes):
        #TODO : Use an interface to abstract this dependency : GmailAuthenticator
        self.credentials = GmailAuthenticator(credentials_path, token_name, scopes).get_credentials()
        self.service = None
        if self.credentials:
            self.service = self.get_service()

    def get_service(self):
        return build('gmail', 'v1', credentials=self.credentials)

    def search_messages(self, search_query):
        if self.service:
            results = self.service.users().messages().list(userId='me', q=search_query).execute()
            return results['messages']
        else:
            print("Gmail servie not available")
            return []

    def search_msg_ids_containing(self, search_query):
        return [msg['id'] for msg in self.search_messages(search_query)]

    def get_attachments(self, user_id, msg_id, store_dir):
        downloaded_attachments = []
        try:
            message = self.service.users().messages().get(userId=user_id, id=msg_id).execute()

            for part in message['payload']['parts']:
                if part['filename']:
                    attachment = self.service.users().messages().attachments().get(userId=user_id, messageId=message['id'], id=part['body']['attachmentId']).execute()
                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))

                    path = os.path.join(store_dir, part['filename'])
                    downloaded_attachments.append(part['filename'])

                    with open(path, 'wb') as f:
                        f.write(file_data)
                        f.close()

            return downloaded_attachments

        except errors.HttpError as error:
            print(f'An error occurred: {error}')


class GmailAuthenticator(object):

    def __init__(self, credentials_path, token_name, scopes):
        self.credentials = credentials_path
        self.token_name = token_name
        self.scopes = scopes

    def get_credentials(self):
        creds = None
        if os.path.exists(self.token_name):
            with open(self.token_name, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials, self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_name, 'wb') as token:
                pickle.dump(creds, token)

        return creds



