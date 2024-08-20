# นางสาวปวีณ์สุดา ทิพยนาสา 653380137-5
from io import BytesIO
from requests.models import Response

def get_mock_currency_api_response(base_currency="THB", target_currency="KRW", rate=38.69):
    """
    Create a mock response for the currency API.
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200
    mock_api_response._content = (f'{{"base": "{base_currency}", "result": {{"{target_currency}": {rate}}}}}').encode('utf-8')
    return mock_api_response


# example =  get_mock_currency_api_response().json()
# print(type(example), example)
