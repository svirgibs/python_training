# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_new_contact(Contact(firstname="Denis", middlename="Timurovich", lastname="Iavorskii",
                                            address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))
