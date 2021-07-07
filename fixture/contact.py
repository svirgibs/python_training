from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.init_add_new_contact()
        # fill form
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # alert accept
        wd.switch_to_alert().accept()
        # wait
        wd.find_element_by_xpath("//input[@value='Delete']")
        self.contact_cache = None

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init modify
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill new data
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def init_add_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//input[@value='Enter']")) > 0):
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_css_selector("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=cells[1].text, firstname=cells[2].text, id=id))
        return list(self.contact_cache)

