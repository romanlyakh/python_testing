import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app(request):
    global fixture
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
