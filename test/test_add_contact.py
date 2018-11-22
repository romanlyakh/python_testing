# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.open_home_page()
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="Петр", middlename="Анатольевич", lastname="Иванов", nickname="ivanov", title="test_title", company="company_test", address="address_test",
                                home="+74951397247", mobile="+79061397247", work="+780080012014", fax="+780080012567", email="mail@gmail.com",
                                email2="mail2@gmail.com", email3="mail3@gmail.com", homepage="ivanov.ru", byear="1980", ayear="2020", address2="address_test2",
                                phone2="home_test", bday="//option[@value='11']", bmonth="//option[@value='January']", notes="notes_test",
                                aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]")
        app.contact.add(contact)
        new_contacts = app.contact.get_contact_list()
       # assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        app.contact.return_home_page()


#def test_add_contact_two(app):
        #app.open_home_page()
       # old_contacts = app.contact.get_contact_list()
       # contact = Contact(firstname="", middlename="", lastname="", nickname="",
        #                        title="", company="", address="",
        #                        home="", mobile="", work="",
         #                       fax="", email="",
         #                       email2="", email3="", homepage="",
          #                      byear="1980", ayear="2020", address2="address_test2",
          #                      phone2="home_test", bday="//option[@value='11']",
           #                     bmonth="//option[@value='January']", notes="notes_test",
           #                     aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]")
        #app.contact.add(contact)
        #new_contacts = app.contact.get_contact_list()
       # assert len(old_contacts) + 1 == len(new_contacts)
       # old_contacts.append(contact)
       # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

      #  app.contact.return_home_page()

