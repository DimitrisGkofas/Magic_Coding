import requests

def is_internet_connected():
    try:
        # Try to send a GET request to a reliable website, like Google.
        response = requests.get("http://www.google.com", timeout=2)
        # If the request was successful (status code 200), return True.
        return response.status_code == 200
    except requests.ConnectionError:
        # If there's a connection error, return False.
        return False