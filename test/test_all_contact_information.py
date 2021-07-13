from random import randrange
from model.contact import Contact
import re


def test_all_information_fields_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                                               nickname="Vano", company="Company", title="Title",
                                               address="Moscow, Street, 14", homephone="+7(916)5554433",
                                               mobile="+79167774455", workphone="79165554400", fax="1-2-3-4",
                                               email="qwedwqe@gmail.com", email2="124@gmail.com",
                                               email3="5551@gmail.com", homepage="localhost",
                                               address2="Moscow, Street, 15", secondaryphone="7(916)555-44-00",
                                               notes="abc"))
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact_information_from_home_page = app.contact.get_contact_list()[index]
    contact_information_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_information_from_home_page.firstname == contact_information_from_edit_page.firstname
    assert contact_information_from_home_page.lastname == contact_information_from_edit_page.lastname
    assert contact_information_from_home_page.address == contact_information_from_edit_page.address
    assert contact_information_from_home_page.all_phones_from_home_page == \
           merge_phones_like_on_home_page(contact_information_from_edit_page)
    assert contact_information_from_home_page.all_emails_from_home_page == \
           merge_emails_like_on_home_page(contact_information_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))