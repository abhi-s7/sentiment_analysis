''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
        Testing: curl "http://localhost:5000/sentimentAnalyzer?textToAnalyze=I%20love%20Python"
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    #print(f'textToAnalyze is: {textToAnalyze}')

    if not text_to_analyze.strip():
        return 'No text provided. Please enter some text to analyze.'

    # Calling Sentiment Analyzer and passing the text
    response = sentiment_analyzer(text_to_analyze)
    # print(f'response is: {response}')

    if 'error' in response:
        print(f"Error: {response['error']}")
        return "Invalid input! Try again."

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."

    # Return a formatted string
    return f"The given text is {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

def run_app():
    """
    This function executes the Flask app and deploys it on localhost:5000.
    """
    # In Python, docstrings should be placed inside functions, classes, or modules
    # not inside arbitrary code blocks like if __name__ == "__main__":.
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_app()

# pylint server.py -> 10/10
