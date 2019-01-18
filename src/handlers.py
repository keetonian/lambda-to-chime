"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import config
import lambdalogging
import chime
from exceptions import InputError

LOG = lambdalogging.getLogger(__name__)


def post_to_chime(event, context):
    """Lambda function handler."""
    LOG.info('Received event: %s', event)

    if not isinstance(event, list):
        # error
        raise InputError(event, "Input needs to be a json array")

    for message in event:
        chime.post_message(config.CHIME_URL, message)
