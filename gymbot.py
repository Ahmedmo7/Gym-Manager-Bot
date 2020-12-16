from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time as t
import datetime

class Bot:

    """
    Constructor
    Creates headless Chrome webdriver (with false window)
    Opens gym link
    """
    def __init__(self):
        headless = webdriver.ChromeOptions()
        headless.add_argument("headless")
        headless.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=headless)
        self.driver.get("https://myfit4less.gymmanager.com/portal/booking/index.asp")

    """
    Helper function to click elements
    First scrolls element onto screen view, then clicks
    This is necessary to avoid accidentally clicking overlays
    """
    def scroll_click(self, id):
        elem = self.driver.find_element_by_id(id)
        header = self.driver.find_element_by_class_name("header")
        self.driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -arguments[1].offsetheight); arguments[0].click();", elem, header)

    """
    Sends user input to email and password fields
    Clicks login button
    """
    def login(self, email, pwd):
        self.driver.find_element_by_id("emailaddress").send_keys(email)
        self.driver.find_element_by_id("password").send_keys(pwd)
        self.scroll_click("loginButton")

    """
    Clicks club select button
    Finds inputted club and selects it
    """
    def select_club(self, name):
        self.scroll_click("btn_club_select")
        club_xpath = "//div[text()='" + name + "']"
        club = self.driver.find_element_by_xpath(club_xpath)
        self.scroll_click(club.get_attribute("id"))

    """
    Takes date input in format yyyy-mm-dd
    Clicks date select button
    Finds inputted date and selects it
    If target date is not there, refreshes window every 1 second until it is found
    """
    def choose_date(self, date):
        while True:
            try:
                self.scroll_click("btn_date_select")
                self.scroll_click("date_" + date)
                break
            except NoSuchElementException:
                print("No date")
                time.sleep(1)
                self.driver.refresh()

    """
    When specific time is selected
    Converts date from yyyy-mm-dd to 'Day, date month year'
    Converts time to 'at time'
    Finds inputted time slot and selects it
    If target time slot is not there, refresh window every 1 second until it is found
    Confirms booking, tells user bot has completed, and closes webdriver
    """
    
    def choose_time_slot(self, date, time):
        year, month, day = (int(x) for x in date.split("-"))
        long_date = datetime.date(year, month, day)
        day_of_week = long_date.strftime("%A")
        string_month = long_date.strftime("%B")
        target_date = day_of_week + ", " + str(day) + " " + string_month + " " + str(year)
        target_time = "at " + time
        target_xpath = "//div[@data-slotdate='" + target_date + "'][@data-slottime='" + target_time + "']"
        while True:
            try:
                time_slot = self.driver.find_element_by_xpath(target_xpath)
                break
            except NoSuchElementException:
                print("No time")
                t.sleep(10)
                self.driver.refresh()
        
        self.scroll_click(time_slot.get_attribute("id"))
        self.scroll_click("dialog_book_yes")
        print("Booked!")
        self.driver.quit()
    
    """
    When specific time is not selected
    Finds first available time slot and selects it
    If no time slot is available, refresh window every 1 second until one is found
    Confirms booking, tells user bot has completed, and closes webdriver
    # TEST METHOD NOT IMPLEMENTED YET
    def choose_time_slot(self):
        while True:
            try:
                time_slot = self.driver.find_element_by_xpath("//div[test()='Click to reserve']")
                break
            except NoSuchElementException:
                print("No time")
                time.sleep(10)
                self.driver.refresh()
        self.scroll_click(time_slot.get_attribute("id"))
        self.scroll_click("dialog_book_yes")
        print("Booked!")
        self.driver.quit()
    """