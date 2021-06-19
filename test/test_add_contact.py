# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(firstname="Denis", middlename="Timurovich", lastname="Iavorskii",
                                            address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))
    app.session.logout()
