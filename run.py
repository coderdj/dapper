import bcrypt
from eve import Eve
from eve.auth import BasicAuth
from pymongo import MongoClient
import os

import logging
logger = logging.getLogger(__name__)

class BCryptAuth(BasicAuth):
    def __init__(self):
        client = MongoClient("mongodb://%s:%s@%s:%s/%s"%(
            os.environ["RUN_USERNAME"],
            os.environ["RUN_PASSWORD"],
            os.environ["RUN_HOST"],
            os.environ["RUN_PORT"],
            os.environ["RUN_DB"]))
        self.user_collection = client['run']['users']
    
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used        
        account = self.user_collection.find_one({'api_username': username})
        print(username)
        print(password)
        logger.debug(username)
        logger.debug(password)
        return (account and \
            bcrypt.hashpw(password.encode('utf-8'),
                          account['api_key'].encode('utf-8')) == account['api_key'].encode('utf-8'))

app = Eve(auth=BCryptAuth)
if __name__ == '__main__':
    app.run(debug=True)
