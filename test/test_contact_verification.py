
import re
from random import randrange
from model.contact import Contact

def test_contact_verif_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
        return re.sub("[() -]", "", s)

def clear_for_address(s):
    return re.sub("\\r", "", s)

def merge_phones_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3]))))


def test_home_contact_compare_db(app, db):
    db_contacts = db.get_contact_list()
    home_contacts = app.contact.get_contact_list()
    assert sorted(home_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)

    for item in home_contacts:
        db_contact = list(filter(lambda x: x.id == item.id, db_contacts))[0]
        assert item.address == clear_for_address(db_contact.address)
        assert item.all_phones_from_home_page == merge_phones_like_on_home_page(
            db_contact)
        assert item.all_emails_from_home_page == merge_emails_like_on_home_page(
            db_contact)









def contact_on_home_page(self, contact):
    firstname = contact.firstname.strip()
    lastname = contact.lastname.strip()
    all_phones = self.merge_phones_like_on_home_page(contact)
    all_emails = self.merge_emails_like_on_home_page(contact)
    return Contact(lastname=lastname, firstname=firstname, id=contact.id,
                       all_phones_from_home_page=all_phones, address=contact.address,
                       all_emails_from_home_page=all_emails)