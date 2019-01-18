import pytest
import handlers
import requests
import chime
from exceptions import InputError

import test_constants


def test_post_to_chime(mocker):
    mocker.patch.object(chime, 'post_message')
    handlers.post_to_chime(test_constants.EVENT, None)
    chime.post_message.assert_any_call(test_constants.CHIME_URL, test_constants.EVENT[0])
    chime.post_message.assert_any_call(test_constants.CHIME_URL, test_constants.EVENT[1])
    chime.post_message.assert_any_call(test_constants.CHIME_URL, test_constants.EVENT[2])

def test_post_to_chime_input_error(mocker):
    mocker.patch.object(chime, 'post_message')
    with pytest.raises(InputError):
        handlers.post_to_chime(test_constants.INVALID_EVENT, None)
