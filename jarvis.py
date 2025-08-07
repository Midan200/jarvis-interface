import functions_framework
import json
import os
import requests

@functions_framework.http
def jarvis_backend(request):
    """Responds to an HTTP request with a message from Jarvis.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`.
    """
    if request.method == 'OPTIONS':
        # Handle preflight CORS request
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Ages': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}
    request_json = request.get_json(silent=True)
    user_message = request_json.get('message', '') if request_json else ''

    # Jarvis's core logic will be implemented here
    # We will expand this code to be the real brain of Jarvis.
    
    jarvis_response = "Jarvis received your message and is processing it in the cloud."

    response_data = {'response': jarvis_response}
    return (json.dumps(response_data), 200, headers)
