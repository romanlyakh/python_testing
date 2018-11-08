from model.group import Group


def test_modify_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="testname_Edit", header="testheader_Edit", footer="testfooter_Edit"))
    app.session.logout()
