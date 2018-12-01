# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string



def random_string (prefix, maxlen):
    symbols=string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_tel (prefix, maxlen):
    symbols=string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
           Contact(firstname=firstname, lastname=lastname, home=home)
            for firstname in ["", random_string("firstname", 15)]
            for lastname in ["", random_string("lastname", 15)]
            for home in ["", random_tel("home", 10)]
            ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.add(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





