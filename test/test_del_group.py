from model.group import Group


def test_delete_first_group(app):
    app.open_home_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
