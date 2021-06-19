from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="NewDenis", middlename="NewTimurovich", lastname="NewIavorskii",
                                            address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))
    app.session.logout()