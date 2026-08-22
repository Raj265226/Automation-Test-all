import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='module')
def api_request():
    with sync_playwright() as p:
        request = p.request.new_context(
            base_url='https://rahulshettyacademy.com',
            ignore_https_errors=True
        )
        yield request
        request.dispose()


def test_get(api_request):
    response = api_request.get('/Library.GetBook.php',params={'AuthorName': 'Rohit'})
    print('Get response status ->', response.status)

def test_post(api_request):
    payload = {
        'name': 'Playwright',
        'isbn': 'Abcd',
        'aisle': '1234',
        'author': 'rohit'
    }

    response = api_request.post('/Library/Addbook.php',data=payload)
    print('Post response status ->', response.status)
    print('Post response json ->', response.json)

def test_put(api_request):
    payload = {
        'name': 'Rohit',
        'job': 'Lead'
    }

    response = api_request.put('https://reqres.in/api/users/2',data=payload)
    print('Put response status ->', response.status)
    print('Put response json ->', response.json)

def test_delete(api_request):
    response = api_request.delete('https://reqres.in/api/users/2')
    print('Delete response status ->', response.status)
    print('Delete response json ->', response.json)