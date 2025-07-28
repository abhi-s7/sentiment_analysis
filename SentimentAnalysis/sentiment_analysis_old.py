# Import the necessary libraries for making web requests and handling JSON data
import requests
import json

def sentiment_analyzer(text_to_analyze):
    # This is the API endpoint where the sentiment analysis happens
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # We prepare the data we want to send in the request
    myobj = { "raw_document": { "text": text_to_analyze } }

    # This header tells the API which model to use for analysis
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Send the text to the API using a POST request
    response = requests.post(url, json=myobj, headers=header)

    # Checking the status code
    # print(f'Status code is: {response.status_code}')
    print(f'Status code is: {response.status_code}')

    # Convert the response (which is text) into a Python dictionary
    formatted_response = json.loads(response.text)

     # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Get the sentiment label (like positive/negative) and its score
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    elif response.status_code == 500:
        label = None
        score = None

    # Return both values as a dictionary
    return {'label': label, 'score': score}