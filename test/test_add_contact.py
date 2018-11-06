# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.add_contact(Contact(firstname="Петр", middlename="Анатольевич", lastname="Иванов", nickname="ivanov", title="test_title", company="company_test", address="address_test",
                         home="+74951397247", mobile="+79061397247", work="+780080012014", fax="+780080012567", email="mail@gmail.com",
                         email2="mail2@gmail.com", email3="mail3@gmail.com", homepage="ivanov.ru", byear="1980", ayear="2020", address2="address_test2",
                         phone2="home_test", bday="//option[@value='11']", bmonth="//option[@value='January']", notes="notes_test",
                         aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]"))
        app.return_home_page()
        app.session.logout()


def test_add_contact_two(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.add_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                                     title="", company="", address="",
                                     home="", mobile="", work="",
                                     fax="", email="",
                                     email2="", email3="", homepage="",
                                     byear="1980", ayear="2020", address2="address_test2",
                                     phone2="home_test", bday="//option[@value='11']",
                                     bmonth="//option[@value='January']", notes="notes_test",
                                     aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]"))
        app.return_home_page()
        app.session.logout()

