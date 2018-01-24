import requests
import json

UPDATE_HANDLER = "update/json?commit=true"
SOLR_URL = "http://{}:{}/solr"

class Solr_client:
    def __init__(self, host="localhost", port=8983):
        self.host = host
        self.port = port
        self.url = SOLR_URL.format(host, port)
        self.update_handler = UPDATE_HANDLER
        
    def update(self, collection_name, data):
        '''
        data (dict): A dict object which will be updated to the specific solr collection as a structured document. 
        collection_name(str): Name of the target collection.
        '''
        post_data_str = str(json.dumps([data]))
        post_url = "{}/{}/{}".format(self.url, collection_name, self.update_handler)

        res = requests.post(post_url, data=post_data_str)
        return res.text
