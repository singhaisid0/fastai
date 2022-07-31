from fastapi import FastAPI
#import uvicorn
from pydantic import BaseModel
from elasticsearchquerygenerator.elasticsearchquerygenerator import ElasticSearchQuery
from elasticsearch import Elasticsearch




# Declaring our FastAPI instance
app = FastAPI()
 
output = {}

class request_body(BaseModel):
    sentsent : str

@app.post('/predict')
def predict(data : request_body):
    test_data = data.sentsent

    query_input = test_data

    cloudid = "ES_deployment_syndicate:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDgwZjUwNmIyMmYwOTRmYWQ4Yjk1NzE1YzIxMTEzZGIwJDBhZjM3OWE5ZGFlMTRjYmZhNjRkMDY3OTcwNDVlNDcy"
    user = "elastic"
    password = "t1ykTWNHHJY778GG5SasPrih"

    es_client = Elasticsearch(cloud_id=cloudid, http_auth=(user, password))
    body = {
           "_source": ["Description"],
           "size": 20,
           "min_score": 0.6,
           "query": {
              "bool": {
                 "must": [],
                 "filter": [],
                 "should": [
                    
                    {
                       "multi_match": {
                             "query": query_input,
                             "type" : "cross_fields",
                             "fields" : ["Description"],
                             "operator" : "or"                    
                       }
                    }         
                 ]
              }
           }
        }
    return (es_client.search(index="south_africa_shows", body=body))