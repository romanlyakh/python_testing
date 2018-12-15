#
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.home()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.home()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None


    def home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('http://localhost/addressbook/') and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_for_modif_by_index(self, index):
            wd = self.app.wd
            wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_contact_for_modif_by_id(self, id):
            wd = self.app.wd
            wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.home()
        self.select_contact_for_modif_by_index(index)

        self.fill_contact_form(new_contact_data)
        # submit modify contact
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.home()
        self.select_contact_for_modif_by_id(id)

        self.fill_contact_form(new_contact_data)
        # submit modify contact
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fio
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        # company details
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # email
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        # homepage
        self.change_field_value("homepage", contact.homepage)
        # Birthday
        #self.change_field_value("bday", contact.bday)
        #wd.find_element_by_name("bday").click()
        #wd.find_element_by_xpath(contact.bday).click()
        #wd.find_element_by_name("bmonth").click()
        #wd.find_element_by_xpath(contact.bmonth).click()
        #self.change_field_value("byear", contact.byear)
        # Anniversary
        #wd.find_element_by_name("aday").click()
        #wd.find_element_by_xpath(contact.aday).click()
        #wd.find_element_by_name("amonth").click()
        #wd.find_element_by_xpath(contact.amonth).click()
        #self.change_field_value("ayear", contact.ayear)

        # add address2
        self.change_field_value("address2", contact.address2)
        # add home
        self.change_field_value("phone2", contact.phone2)
        # add notes
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
         wd.find_element_by_name(field_name).click()
         wd.find_element_by_name(field_name).clear()
         wd.find_element_by_name(field_name).send_keys(text)

    def add(self, contact):
        wd = self.app.wd
        # option add new
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # save contact
        wd.find_element_by_css_selector('input[value="Enter"]').click()
        self.return_home_page()
        self.contact_cache=None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.home()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname,lastname=lastname, address=address, id=id, home=home, work=work, mobile=mobile, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)