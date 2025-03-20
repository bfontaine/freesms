import pytest
from httmock import all_requests, response, HTTMock

from freesms import FreeClient, FreeResponse

CODES = [200, 400, 500]


@all_requests
def smsapi_mock(url, _request):
    qry = url.query
    for code in CODES:
        if "code%s" % code in qry:
            return response(code)
    return response(404)


@pytest.fixture(scope="session")
def client():
    return FreeClient(user="someuser", passwd="secret")


def test_500(client):
    with HTTMock(smsapi_mock):
        resp = client.send_sms("oops code500 error")

    assert not resp
    assert resp.status_code == 500
    assert not resp.success()
    assert resp.error()


def test_400(client):
    with HTTMock(smsapi_mock):
        resp = client.send_sms("oops code400 error")

    assert not resp
    assert resp.status_code == 400


def test_200(client):
    with HTTMock(smsapi_mock):
        resp = client.send_sms("code200")

    assert resp
    assert resp.status_code == 200
    assert resp.success()
    assert not resp.error()


def test_py2_bool_resp():
    ok = FreeResponse(response(200))
    ko = FreeResponse(response(400))

    assert ok.__nonzero__() is True
    assert ko.__nonzero__() is False


def test_py3_bool_resp():
    ok = FreeResponse(response(200))
    ko = FreeResponse(response(400))

    assert ok.__bool__() is True
    assert ko.__bool__() is False
