# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="aasdasdasd", header="asdasdasd", footer="asdsad"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def logout(self, wd):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        wd = self.wd
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def open_groups_page(self, wd):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd = self.wd
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
