import random
from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Denis", middlename="Timurovich", lastname="Iavorskii",
                                               address="Moscow", mobile="+79167774455", email="yavorskiy.dt@gmail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    mod_contact = Contact(firstname="NewDenis", middlename="NewTimurovich", lastname="NewIavorskii")
    mod_contact.id = contact.id
    old_contacts.remove(contact)
    app.contact.modify_contact_by_id(contact.id, mod_contact)
    old_contacts.append(mod_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(),
                                                                     key=Contact.id_or_max)