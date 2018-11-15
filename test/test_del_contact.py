from model.contact import Contact

def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
       app.contact.add(Contact(firstname="test"))
    app.contact.delete_first_contact()
