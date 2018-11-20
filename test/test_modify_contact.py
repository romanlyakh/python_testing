from model.contact import Contact


def test_modify_first_contact_firstname(app):
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
    contact=Contact(firstname="Святослав", middlename="Анатольевич", lastname="Иванов", nickname="",
                                title="", company="", address="",
                                home="", mobile="", work="",
                                fax="", email="",
                                email2="", email3="", homepage="",
                                byear="1990", ayear="2040", address2="address_test2",
                                phone2="home_test", bday="//option[@value='25']",
                                bmonth="//option[@value='January']", aday="(//option[@value='25'])[2]", amonth="(//option[@value='January'])[2]",notes="notes_test")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







#def test_modify_first_contact_lastname(app):
#    app.open_home_page()
#    app.contact.modify_first_contact(Contact(lastname="Смитт",byear="1980", ayear="2020", address2="address_test2",
#                                phone2="home_test", bday="//option[@value='11']",
#                                bmonth="//option[@value='January']", notes="notes_test",
#
#                               aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]"))
