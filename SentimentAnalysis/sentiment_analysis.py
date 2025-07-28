"""Module for performing sentiment analysis using IBM Watson NLP API."""

import json
import requests


def sentiment_analyzer(text_to_analyze):
    """
    Analyze the sentiment of the given text using IBM Watson NLP API.

    Parameters:
        text_to_analyze (str): The input text to analyze.

    Returns:
        dict: A dictionary containing the sentiment label and score,
              or an error message if input is invalid or empty.
    """

    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    payload = {"raw_document": {"text": text_to_analyze}}
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f'Status code is: {response.status_code}')
        formatted_response = json.loads(response.text)

        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
            return {'label': label, 'score': score}

        if response.status_code == 400:
            return {
                'error': 'Invalid text. The input may be in an unsupported language or malformed.'
            }

        return {'error': f'Unexpected error. Status code: {response.status_code}'}

    except requests.exceptions.RequestException as e:
        return {'error': f'Connection error: {str(e)}'}
