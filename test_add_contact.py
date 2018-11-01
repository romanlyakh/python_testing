# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, firstname="Петр", middlename="Анатольевич", lastname="Иванов", nickname="ivanov", title="test_title", company="company_test", address="address_test",
                         home="+74951397247", mobile="+79061397247", work="+780080012014", fax="+780080012567", email="mail@gmail.com",
                         email2="mail2@gmail.com", email3="mail3@gmail.com", homepage="ivanov.ru", byear="1980", ayear="2020", address2="address_test2",
                         phone2="home_test", bday="//option[@value='11']", bmonth="//option[@value='January']", notes="notes_test",
                         aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]")
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_contact_two(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, firstname="Василий", middlename="Сергеевич", lastname="Петров", nickname="",title="", company="", address="",
                        home="", mobile="+79061397247", work="", fax="",email="mail@gmail.com",email2="", email3="", homepage="", byear="1980",ayear="2020", address2="address_test2", phone2="home_test", bday="//option[@value='11']", bmonth="//option[@value='January']",
                        notes="notes_test",
                        aday="(//option[@value='11'])[2]", amonth="(//option[@value='January'])[2]")
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def add_contact(self, wd, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work,
                    fax, email, email2, email3, homepage, byear, ayear, address2, phone2, bday, bmonth, notes, aday,
                    amonth):
        # option add new
        wd.find_element_by_link_text("add new").click()
        #fio
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        #company details
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        # telephone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        #email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        #homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        #Birthday
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath(bday).click()
        wd.find_element_by_xpath(bmonth).click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        #Anniversary
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath(aday).click()
        wd.find_element_by_xpath(amonth).click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)
        # add address2
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        #add home
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        #add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        # save contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
