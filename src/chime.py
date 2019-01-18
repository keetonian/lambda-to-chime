"""Functions for interacting with chime."""
import json
import requests

import lambdalogging

LOG = lambdalogging.getLogger(__name__)
JSON_HEADER = {'Content-Type': 'application/json'}


def post_message(url, message):
    """Post a message to chime using a webhook url."""
    data = {'Content': message}
    response = requests.post(url, data=json.dumps(data), headers=JSON_HEADER)
    LOG.info('Sent message: %s\nUrl: %s\nResponse: %s', message, url, response)
    return response.status_code
