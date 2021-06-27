from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Denis", middlename="Timurovich", lastname="Iavorskii",
                                               address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))
    app.contact.delete_first_contact()