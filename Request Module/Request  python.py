# get(url, params=None, **kwargs): Sends a GET request to the specified URL.
# post(url, data=None, json=None, **kwargs): Sends a POST request to the specified URL.
# put(url, data=None, **kwargs): Sends a PUT request to the specified URL.
# delete(url, **kwargs): Sends a DELETE request to the specified URL.

# status_code: The HTTP status code of the response (e.g., 200 for success, 404 for not found).
# text: The response content as a string.
# json(): Parses the response content as JSON and returns a Python dictionary.
# headers: A dictionary containing the response headers.

#Note: # use : https://httpbin.org/   for testing  ................


# 1. Sending a GET request:

# import requests

# response = requests.get('https://httpbin.org')
# print(response.status_code)  # Print the status code
# print(response.text)  # Print the response content

# 2 .Sending a POST request with JSON data:

# import requests

# data = {
#     'name': 'John Doe',
#     'email': 'john.doe@example.com'
# }

# response = requests.post('https://httpbin.org/post', json=data)
# print(response.status_code)
# print(response.text)
# print(response.json())  # Parse response as JSON

# 3.Adding parameters and headers to a GET request/put:

# import requests

# params = {
#     'q': 'openai',
#     'sort': 'stars',
#     'order': 'desc'
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0',
#     'Authorization': 'Bearer'
# }


# response = requests.put('https://httpbin.org/put', params=params, headers=headers)
# print(response.status_code)
# print(response.json())

# 4.Handling errors:

# import requests

# try:
#     response = requests.get('https://httpbin.org/get')
#     response.raise_for_status()  # Raise an exception for status codes >= 400
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error occurred: {err}")
# except requests.exceptions.RequestException as err:
#     print(f"An error occurred: {err}")


# use : https://httpbin.org/   for testing  ................

