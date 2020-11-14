import mock
import pytest

from shifu.helpers.user import encrypt_password


@pytest.fixture
def user_payload():
    return {
        'password': '123'
    }


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
