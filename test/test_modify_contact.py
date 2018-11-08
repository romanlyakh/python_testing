from model.contact import Contact


def test_modify_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Семён", middlename="Иванович", lastname="Петров", nickname="ivanov", title="test_title", company="company_test", address="address_test",
                                home="+74951397247", mobile="+79061397247", work="+780080012014", fax="+780080012567", email="mail@gmail.com",
                                email2="mail2@gmail.com", email3="mail3@gmail.com", homepage="ivanov.ru", byear="1980", ayear="2020", address2="address_test2",
                                phone2="home_test", bday="//option[@value='19']", bmonth="//option[@value='January']", notes="notes_test",
                                aday="(//option[@value='20'])[2]", amonth="(//option[@value='January'])[2]"))
    app.session.logout()
