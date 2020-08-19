import sys
import os


class Configuration(object):
    credentials_file = 'credentials.json'
    credentials_pickle_file = 'token.pickle'
    scopes = ['https://www.googleapis.com/auth/gmail.readonly']
    storage_path = os.path.join(os.path.abspath(os.getcwd()), "data")
    data_files = ['Basic.txt', 'Delux.txt', 'Total.txt']
    email_keyword_query = 'cupcakes'