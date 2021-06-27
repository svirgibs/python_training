from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Denis", middlename="Timurovich", lastname="Iavorskii",
                                               address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))
    app.contact.modify_first_contact(Contact(firstname="NewDenis", middlename="NewTimurovich", lastname="NewIavorskii",
                                            address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))