import pytest
import requests

@pytest.fixture(scope='module')
def api_request():
    session = requests.Session()
    session.verify = False
    yield session
    session.close()

def test_get(api_request):
    response = api_request.get('https://rahulshettyacademy.com/Library/GetBook.php',params={'AuthorName': 'Rohit'})
    print('Get response status ->', response.status_code)
    assert response.status_code == 200


def test_post(api_request):
    payload = {
        'name': 'Playwright',
        'isbn': 'abcd',
        'aisle': '1234',
        'author': 'rohit'
    }

    response = api_request.post('https://rahulshettyacademy.com/Library/Addbook.php',data=payload)
    print('Post response status ->', response.status_code)

def test_put(api_request):
    payload = {
        'name': 'Rohit',
        'job': 'Lead'
    }
    response = api_request.put('https://reqres.in/api/users/2',data=payload)
    print('Put response status ->', response.status_code)
    print('Put response json ->', response.json())

def test_delete(api_request):
    response = api_request.delete('https://reqres.in/api/users/2')
    print('Delete response status ->', response.status_code)
    print('Delete response json ->', response.json())