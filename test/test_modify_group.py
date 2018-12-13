from model.group import Group
from random import randrange

def test_modify_some_group_name(app, db, check_ui):
    app.open_home_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="testname_Edit")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        new_groups = map(app.group.clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

