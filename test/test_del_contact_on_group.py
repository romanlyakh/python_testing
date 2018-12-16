from model.group import Group
from model.contact import Contact
import random


def test_del_contact_on_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="Тест", lastname="Тестов"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    id_group = app.group.select_id_group()
    contact_from_group = app.contact.get_contacts_list_in_group(id_group)
    if len(contact_from_group) == 0:
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
        id_group = app.group.select_id_group()
        app.contact.add_contact_to_group(contact.id, id_group)
    else:
        contact = random.choice(contact_from_group)
        app.contact.del_contact_from_group(contact.id, id_group)
        new_contacts = app.contact.get_contacts_list_in_group(id_group)
        list_orm = orm.get_contacts_in_group(Group(id=id_group))
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(list_orm, key=Contact.id_or_max)