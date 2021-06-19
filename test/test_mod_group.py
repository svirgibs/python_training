from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="new abc", header="new qwe", footer="new asd"))
    app.session.logout()