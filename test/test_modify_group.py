from model.group import Group


def test_modify_first_group_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="testname_Edit"))
    app.session.logout()


def test_modify_first_group_header(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="testheader_Edit"))
    app.session.logout()