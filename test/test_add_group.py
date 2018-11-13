# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    app.group.return_to_groups_page()


def test_add_empty_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
