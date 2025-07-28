# Sentiment Analysis Web Application

A full-stack Python web application for sentiment analysis using Flask and IBM Watson NLP API. This application provides a user-friendly interface to analyze the sentiment of text input using BERT-based natural language processing.

## 🚀 Features

- **Real-time Sentiment Analysis**: Analyze text sentiment using IBM Watson NLP API
- **Web Interface**: Clean, responsive web interface built with Flask and Bootstrap
- **RESTful API**: JSON-based API endpoints for programmatic access
- **Error Handling**: Comprehensive error handling for invalid inputs and API failures
- **Unit Testing**: Complete test suite for sentiment analysis functionality
- **Code Quality**: Pylint-based code quality checks (10/10 score)

## 🏗️ Project Structure

```
sentiment_analysis/
├── server.py                          # Main Flask application server
├── SentimentAnalysis/
│   ├── __init__.py                   # Package initialization
│   ├── sentiment_analysis.py         # Core sentiment analysis logic
│   └── sentiment_analysis_old.py     # Legacy implementation
├── templates/
│   └── index.html                    # Main web interface template
├── static/
│   └── mywebscript.js               # Frontend JavaScript functionality
├── test_sentiment_analysis.py        # Unit tests
└── README.md                         # Project documentation
```

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 4
- **NLP API**: IBM Watson NLP (BERT-based sentiment analysis)
- **Testing**: Python unittest framework
- **Code Quality**: Pylint

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Internet connection (for IBM Watson API access)

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sentiment_analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

You can run the application using either method:

**Method 1: Traditional Python execution**
```bash
python server.py
```

**Method 2: Modern Flask CLI (Recommended)**
```bash
flask --app server --debug run
```

The application will start and be available at `http://localhost:5000`

## 🎯 Usage

### Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Enter the text you want to analyze in the input field
3. Click "Run Sentiment Analysis" button
4. View the sentiment result and confidence score

### API Endpoint

You can also use the API directly:

```bash
curl "http://localhost:5000/sentimentAnalyzer?textToAnalyze=I%20love%20Python"
```

**Response Format:**
```
The given text is POSITIVE with a score of 0.9876.
```

### Programmatic Usage

```python
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Analyze sentiment
result = sentiment_analyzer("I love working with Python")
print(result)
# Output: {'label': 'SENT_POSITIVE', 'score': 0.9876}
```

## 🧪 Testing

Run the unit tests to verify functionality:

```bash
python test_sentiment_analysis.py
```

The test suite includes:
- Positive sentiment analysis
- Negative sentiment analysis  
- Neutral sentiment analysis

## 🔧 API Details

### Sentiment Analysis Function

```python
sentiment_analyzer(text_to_analyze)
```

**Parameters:**
- `text_to_analyze` (str): Input text for sentiment analysis

**Returns:**
- `dict`: Contains sentiment label and confidence score
  - `label`: Sentiment classification (SENT_POSITIVE, SENT_NEGATIVE, SENT_NEUTRAL)
  - `score`: Confidence score (0.0 to 1.0)

**Error Handling:**
- Returns error dictionary for invalid inputs or API failures
- Handles network timeouts and connection errors

### IBM Watson NLP API

The application uses IBM Watson's BERT-based sentiment analysis model:
- **Model**: `sentiment_aggregated-bert-workflow_lang_multi_stock`
- **Endpoint**: IBM Watson NLP API
- **Features**: Multi-language support, high accuracy

## 🚨 Error Handling

The application handles various error scenarios:

- **Empty Input**: Returns "No text provided. Please enter some text to analyze."
- **Invalid Input**: Returns "Invalid input! Try again."
- **API Errors**: Handles HTTP 400, 500, and connection errors
- **Network Issues**: Graceful handling of timeouts and connection failures

## 📊 Code Quality

The project maintains high code quality standards:
- **Pylint Score**: 10/10
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Robust exception handling
- **Testing**: Complete unit test coverage

## 🎓 Learning Outcomes

This project demonstrates:
- Flask web application development
- RESTful API design and implementation
- Integration with external NLP APIs
- Frontend-backend communication
- Unit testing practices
- Error handling and user experience
- Code quality maintenance with Pylint

---

## 🧪 **Benefits of adding pytest:**

- **Better test discovery**: Automatically finds test files
- **More readable assertions**: `assert result['label'] == 'SENT_POSITIVE'`
- **Rich test output**: Better error messages and reporting
- **Fixtures support**: Reusable test setup code
- **Plugin ecosystem**: Coverage, Flask testing, etc.

## 🔍 **Benefits of adding pylint:**

- **Code quality checks**: Catches potential bugs and style issues
- **Consistent code style**: Enforces PEP 8 standards
- **Documentation**: Checks for proper docstrings
- **Complexity analysis**: Identifies overly complex functions
- **Import organization**: Ensures proper import structure
