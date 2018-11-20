from model.contact import Contact

def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
       app.contact.add(Contact(firstname="", middlename="", lastname="", nickname="",
                                title="", company="", address="",
                                home="", mobile="", work="",
                                fax="", email="",
                                email2="", email3="", homepage="",
                                byear="1980", ayear="2020", address2="address_test2",
                                phone2="home_test", bday="//option[@value='11']",
                                bmonth="//option[@value='January']", notes="notes_test",
                                aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


