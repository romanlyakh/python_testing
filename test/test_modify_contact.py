from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.open_home_page()
    app.contact.modify_first_contact(Contact(firstname="Святослав"))



def test_modify_first_contact_lastname(app):
    app.open_home_page()
    app.contact.modify_first_contact(Contact(lastname="Смитт"))
