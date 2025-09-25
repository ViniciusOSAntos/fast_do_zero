from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_do_zero.app import app


def test_read_root_must_return_ok_and_hello_world():
    client = TestClient(app) # arrange
    response = client.get('/') # act
    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == {'message': 'Olá Mundo', 'test': 'teste'}
