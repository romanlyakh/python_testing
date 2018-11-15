class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        #self.return_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit modify contact
        wd.find_element_by_name("update").click()
        self.return_home_page()

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
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath(contact.bday).click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath(contact.bmonth).click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # Anniversary
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath(contact.aday).click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath(contact.amonth).click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

        # add address2
        self.change_field_value("address2", contact.address2)
        # add home
        self.change_field_value("phone2", contact.phone2)
        # add notes
        self.change_field_value("notes", contact.notes)

    def change_field_value_day(self, field_day, birthday):
        wd = self.app.wd
        if birthday is not None:
         wd.find_element_by_name(field_day).click()
         wd.find_element_by_xpath(field_day).click()

    def change_field_value_month(self, field_month, birthmon):
        wd = self.app.wd
        if birthmon is not None:
            wd.find_element_by_name(field_month).click()
            wd.find_element_by_xpath(field_month).click()

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
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))