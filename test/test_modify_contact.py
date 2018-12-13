from model.contact import Contact
from random import randrange

def test_modify_some_contact_firstname(app, db, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
       app.contact.add(Contact(firstname="", middlename="", lastname="", nickname="",
                                title="", company="", address="",
                                home="", mobile="", work="",
                                fax="", email="",
                                email2="", email3="", homepage="",
                                byear="1980", ayear="2020", address2="address_test2",
                                phone2="home_test", bday="//option[@value='11']",
                                bmonth="//option[@value='January']", notes="notes_test",
                                aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]"))

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Святослав", middlename="Анатольевич", lastname="Иванов", nickname="",
                                title="", company="", address="",
                                home="", mobile="", work="",
                                fax="", email="",
                                email2="", email3="", homepage="",
                                byear="1990", ayear="", address2="address_test2",
                                phone2="home_test", bday="//option[@value='25']",
                                bmonth="//option[@value='January']", aday="(//option[@value='-'])[2]", amonth="(//option[@value='-'])[2]",notes="notes_test")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
