import requests
from requests.exceptions import HTTPError


def fetch_get(url: str) -> any:
    try:
        response = requests.get(url)
        print(f'encoding: {response.encoding}')
        print(f'headers: {response.headers}')
        if response.status_code == 200:
            json_response = response.json()
            print(f'json response: {json_response}')
            print(f'json response title: {json_response["title"]}')
            return json_response
        else:
            print(f"response error: {response.status_code}")
            return None
    except HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        return None
    except Exception as err:
        print(f"Ether error: {err}")
        return None


def fetch_post(url: str, data: any) -> any:
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200 or response.status_code == 201:
            json_response = response.json()
            print(f'json response: {json_response}')
            return json_response
        else:
            print(f"response error: {response.status_code}")
            return None
    except HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        return None
    except Exception as err:
        print(f"Exception error: {err}")
        return None


url_get_succes = 'https://jsonplaceholder.typicode.com/posts/4'
url_get_exception = 'https://jsonplaceholder.typicode.com'
url_get_error_404 = 'https://jsonplaceholder.typicode.com/posts/101'
url_post = 'https://jsonplaceholder.typicode.com/posts'


fetch_get(url_get_succes)
fetch_get(url_get_exception)
fetch_get(url_get_error_404)

new_data = {
    'userId': 999,
    'title': 'Test title',
    'body': 'Test body'
}

fetch_post(url_post, new_data)
