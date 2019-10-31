import urllib.request
import os
# If you are using Python 3+, import urllib instead of urllib2

import json 

### TODO: Need to edit data variable to match in view.py
data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["gender", "age", "size", "weight"],
                    "Values": [ [ "0", "0", "0", "0" ], [ "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

### TODO: Update url, api_key.
url = os.environ.get('URL','https://ussouthcentral.services.azureml.net/workspaces/91af20abfc58455182eaaa615d581c59/services/da7cdb9359a443f0abdef36d30ce8f1c/execute?api-version=2.0&details=true')
api_key = os.environ.get('API_KEY','3ykY3j9WZDYvS0Dvf5VoJ1kA0yVT5HVzT+foY4SzKvD6LJhHoysBjlEQWaOniNQCGqsjKrytONq1kdxEWo3Scg==') # Replace this with the API key for the web service)
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

# API_KEY = os.environ.get('API_KEY', "bqbOx/ih7sqf0YpFbTEBf9wyPA7WPcGGOomvMrTvwq4CC0KxgVPkU2grDnzYN/zqpx5xFUNWl1LOEK+C8L5zMw==")
# URL = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/db57e3c91aeb4c4c8c5b831eb3aa0bd5/services/375cb1234d0d4dc0b29774e6212acee5/execute?api-version=2.0&details=true")



req =urllib.request.Request(url, body, headers) 

try:
    response =urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 