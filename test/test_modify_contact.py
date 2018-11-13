from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Святослав"))
    app.session.logout()


def test_modify_first_contact_lastname(app):
    app.open_home_page()
   # app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Смитт"))
    app.session.logout()
