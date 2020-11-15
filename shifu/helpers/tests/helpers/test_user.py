import mock
import pytest

from shifu.exceptions.users import UserPayloadValidationException
from shifu.helpers.user import encrypt_password, serialize_user_payload


@pytest.fixture
def user_payload():
    return {
        'password': '123'
    }


@pytest.fixture
def user_json():
    return '''
    {
        "name": "lu",
        "email": "teste@teste.com",
        "role": "user",
        "password": "123"
    }
    '''


@pytest.fixture
def user_invalid_json():
    return '{"name": "xablau"}'


@pytest.fixture
def encrypted_password():
    return 'encrypted_xablau'


@pytest.fixture
def mock_decode(encrypted_password):
    encoded = mock.MagicMock()
    encoded.decode.return_value = encrypted_password
    return encoded


@pytest.fixture
def mock_hashpw_decode(mock_decode):
    with mock.patch(
        'shifu.helpers.user.hashpw'
    ) as mocked_method:
        mocked_method.return_value = mock_decode
        yield mocked_method


def test_should_return_payload_with_encrypted_password(
    user_payload,
    mock_hashpw_decode,
    encrypted_password
):

    response = encrypt_password(user_payload)
    assert response['password'] == encrypted_password


def test_should_load_valid_request_payload_into_user_payload(
    user_json
):
    user = serialize_user_payload(user_json)
    assert isinstance(user, dict)


def test_should_raise_validation_user_payload_error(user_invalid_json):
    with pytest.raises(UserPayloadValidationException):
        serialize_user_payload(user_invalid_json)
