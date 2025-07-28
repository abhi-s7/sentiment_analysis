from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    # Test case for positive sentiment
    def test_positive_sentiment(self):
        result = sentiment_analyzer('I love working with Python')
        self.assertEqual(result['label'], 'SENT_POSITIVE')

    # Test case for negative sentiment
    def test_negative_sentiment(self):
        result = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result['label'], 'SENT_NEGATIVE')

    # Test case for neutral sentiment
    def test_neutral_sentiment(self):
        result = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result['label'], 'SENT_NEUTRAL')

if __name__ == '__main__':
    # Run all the test cases when this file is executed
    unittest.main()