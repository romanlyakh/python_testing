from model.group import Group


def test_modify_first_group_name(app):
    app.open_home_page()
    app.group.modify_first_group(Group(name="testname_Edit"))

def test_modify_first_group_header(app):
    app.open_home_page()
    app.group.modify_first_group(Group(header="testheader_Edit"))