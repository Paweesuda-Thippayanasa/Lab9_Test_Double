# นางสาวปวีณ์สุดา ทิพยนาสา 653380137-5
from unittest.mock import patch
import unittest
import sys
import os

# Add the project root directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source.currency_exchanger import CurrencyExchanger
from test.utils import get_mock_currency_api_response

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")
        # self.exchanger = CurrencyExchanger()
        self.mock_response = get_mock_currency_api_response("THB", "KRW", 38.69)

    @patch('source.currency_exchanger.requests.get')  # Adjust based on your file location
    def test_get_currency_rate(self, mock_get):
        # Set up the mock response
        mock_get.return_value = self.mock_response
        
        # Call the method
        self.exchanger.get_currency_rate()
        
        # Check that requests.get was called with the correct parameters
        mock_get.assert_called_once_with(
            'https://coc-kku-bank.com/foreign-exchange',
            params={'from': 'THB', 'to': 'KRW'}
        )
        
        # Assert that the API response is correctly set in the exchanger
        self.assertEqual(self.exchanger.api_response, self.mock_response.json())
    
    @patch('source.currency_exchanger.requests.get')  # Adjust based on your file location
    def test_currency_exchange(self, mock_get):
        # Set up the mock response
        mock_get.return_value = self.mock_response
        
        # Call get_currency_rate first to ensure the rate is fetched
        self.exchanger.get_currency_rate()
        
        # Perform the currency exchange
        amount = 500
        result = self.exchanger.currency_exchange(amount)
        
        # Check that the result is as expected
        expected_result = amount * self.mock_response.json()['result']['KRW']
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
