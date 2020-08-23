import sys
import os


class Configuration(object):
    credentials_file = 'credentials.json'
    credentials_pickle_file = 'token.pickle'
    scopes = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']
    storage_path = os.path.join(os.path.abspath(os.getcwd()), "data")
    data_files = ['Basic.txt', 'Delux.txt', 'Total.txt']
    email_keyword_query = 'cupcakes'
    cost_of_basic = 5  # $5 dollars
    cost_of_delux = 6  # $6 dollars
    email = {
        "to": os.environ['CUPCAKE_TO_EMAIL'],
        "from": os.environ['CUPCAKE_FROM_EMAIL'],
        "subject": 'Matilda Cupcakes Financials',
        "template": """
        <div id="container" style="border: 1px solid #CCC; padding: 10px;">
            <h3>{titleEmail}</h3>
            <h5>{periodTime}</h5>
            <div id="sub-container" style="border: 1px solid #CCC; padding: 5px;">
                {resultsList}
            </div>
        </div>                        
        """
    }
