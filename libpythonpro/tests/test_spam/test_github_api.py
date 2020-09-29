from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/69490377?v=4'
    resp_mock.json.return_value = {
        'login': 'brjatoba92', 'id': 69490377,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('brjatoba92')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars3.githubusercontent.com/u/3457115?v=4' == url
