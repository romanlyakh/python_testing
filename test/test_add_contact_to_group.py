from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())

    if len(orm.get_contacts_not_in_group(group=group)) == 0:
        app.contact.add(Contact(firstname="", middlename="", lastname="", nickname="",
                                title="", company="", address="",
                                home="", mobile="", work="",
                                fax="", email="",
                                email2="", email3="", homepage="",
                                byear="1980", ayear="2020", address2="address_test2",
                                phone2="home_test", bday="//option[@value='11']",
                                bmonth="//option[@value='January']", notes="notes_test",
                                aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]"))
    contact = random.choice(orm.get_contacts_not_in_group(group=group))
    old_contacts_in_group = orm.get_contacts_in_group(group=group)
    old_contacts_in_group.append(contact)
    app.contact.add_contact_to_group(id=contact.id, group_id=group.id)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(orm.get_contacts_in_group(group=group), key=Contact.id_or_max)