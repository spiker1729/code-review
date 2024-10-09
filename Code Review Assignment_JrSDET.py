# Third-party import should be followed after standard imports
from selenium import webdriver 
# Third-party import should be followed after standard imports
from selenium.webdriver.common.by import By 
# Third-party import should be followed after \
# standard imports
from selenium.webdriver.common.action_chains import ActionChains #
# Third-party import should be followed after standard imports
from selenium.webdriver.common.keys import Keys 
# Standard libraries like time should be imported first followed by \
# third-party imports and followed by helper \
# function file import from common workflow directory
import time 

#class name should be based on feature \
# The class setup method is missing \
# The test setup method is missing \
# The test case metadata is missing metadata shows the feat number \
# to which the test case belongs and much other information including the\
# test steps, Many functionalities are being tested in a single method \
# which can be split into various other methods.
class Testcase101: 
    # method name should be descriptive and should be based on what feature \
    # this test case will test like "def test_validate_ticket_creation(self)" \
    # should be declared in the class setup.
    def main(self): 
        driver = webdriver.Firefox(executable_path="C:\\Users\\Johny\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver.get("https://interview.supporthive.com/staff/")
        driver.implicitly_wait(30) # webdriverwait should be used to prevent flakiness
        driver.maximize_window()
         # helper function should be used to get the element and avoid using a \
        # hardcoded username instead get it from some config file 
        driver.find_element(By.ID, "id_username").send_keys("Agent")
        # avoid using hardcoded passwords instead get it from some config file or \
        # use environment variables.
        driver.find_element(By.ID, "id_password").send_keys("Agent@123")
        # helper function should be used to get the element and use the "data-test" \
        # attribute to avoid flakiness upon some changes in the product 
        driver.find_element(By.ID, "btn-submit").click() 
        tickets = driver.find_element(By.ID, "ember29")
        action = ActionChains(driver) # object should be created in class setup 
        action.move_to_element(tickets).perform()
        # helper file/method should be used to get elements by id, by.xpath, by \ 
        # data-test(data-test is one of the best locators)
        statuses = driver.find_element(By.LINK_TEXT, "Statuses") 
        statuses.click()
        # click() should not be used \
        # directly first get the object in variable \
        # check if it is visible and clickable post that click the button
        driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click() 
        # proper steps should be displayed by logging(printing the steps)\
        driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")
        # at various steps to ease the debugging.
        statusColourSelect = driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        #click() should not be used directly first get the object in the variable and check if it is visible \ 
        # and clickable, post that click the button
        statusColourSelect.click()
        statusColourEnter = driver.find_element(By.XPATH, "//input[@class='sp-input']")
        statusColourEnter.clear()
        statusColourEnter.send_keys("#47963f")
        # no such class defined 
        r = Robot() 
        # k is unknown since the "robot()" class is not defined 
        r.keyPress(KeyEvent.VK_ESCAPE) 
        # variable name should be descriptive 
        firstElement = driver.find_element(By.XPATH, "//a[@id='first-link']") 
        #click() should not be used directly first get the object in a variable \
        # check if it is visible and clickable, post that click the button
        firstElement.click() 
        secondElement = driver.find_element(By.XPATH, "//a[@id='second-link']")
        #click() should not be used directly first get the object in variable \
        # check if it is visible and clickable post that click the button
        secondElement.click()
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
        # data-test is recommended to find the element 
        addCreate = driver.find_element(By.XPATH, "//button[@class ='hf-entity-footer_primary hf-primary-action ember-view']") 
        addCreate.click()
        # webdriverwait should be used to prevent flakiness and inconsistent wait strategies implemented
        time.sleep(3) 
        moveTo = driver.find_element(By.XPATH, "//td[@class ='lt-cell align-center hf-mod-no-padding ember-view']")
        action.move_to_element(moveTo).perform()
        moveTo.click()
         # webdriverwait should be used to prevent flakiness
        time.sleep(9)
        issue = driver.find_element(By.XPATH, "//div[contains(text(),'Issue Created')]")
        action.move_to_element(issue).perform()
        make = driver.find_element(By.LINK_TEXT, "Make Default")
        # check if it is visible and clickable, post that click the button
        make.click()
        driver.find_element(By.LINK_TEXT, "Priorities").click() 
        driver.find_element(By.XPATH, "//header/button[1]").click()
        driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
        button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']")
        # check if it is visible and clickable, post that click the button
        button.click()
        time.sleep(9)
        tickets2 = driver.find_element(By.ID, "ember29")
        action.move_to_element(tickets2).perform()
        priorities2 = driver.find_element(By.LINK_TEXT, "Priorities")
        # check if it is visible and clickable, post that click the button
        priorities2.click()
        # inconsistent/mix wait strategy,avoid using inconsistent methods throughout \
        # the code use only one type of wait/sleep . 
        driver.implicitly_wait(20) 
        #  use relative XPath or other selectors its too long for readability
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[2]").click()
        driver.find_element(By.LINK_TEXT, "Delete").click()
        delete = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
        delete.click()
        time.sleep(9) 
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/header[1]/div[2]/nav[1]/div[7]/div[1]/div[1]").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        
# not a descriptive class name , class name should provide some high level information
class PagesforAutomationAssignment:
    def main(self):
        driver = webdriver.Chrome() 
        driver.get("https://www.happyfox.com")

        loginPage = LoginPage(driver)
        loginPage.login("username", "password") # Avoid hardcoding credentials,use environment \ 
        # variables or config files.


        homePage = HomePage(driver)
        homePage.verifyHomePage()

        driver.quit()

class BasePage: 
    def __init__(self, driver): # add type hint like driver : webdriver 
        self.driver = driver

class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username) # error handling is not done, \
        # check if the element is visible and clickable, post that only click the element. 
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()

    def forgotPassword(self): # method not used 
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

class HomePage(BasePage):

    def verifyHomePage(self):
        # instead assert can be used 
        if self.driver.current_url != "https://www.happyfox.com/home": 
            # create a custom exception using assert 
            raise Exception("Not on the home page") 
    # method not used 
    def navigateToProfile(self): 
        # error handling is not done, check if the element is visible and clickable, \
        # post that only click the element.
        self.driver.find_element(By.ID, "profileLink").click() 
        

class TablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")
    
    def retrieveRowTexts(self):
        rows = self.driver.find_elements(self.rowLocator) 
    # error handling is not done if there's no data present in rows 
        # use enumerate(rows) to make it more pythonic
        for i in range(len(rows)): 
            row = rows[i]
            rowText = row.text
            print("Row " + str(i) + " Text: " + rowText)

''' overall comment 
Make use of code reusability and  all common entities(if required) to be tested, create all at once 
in the class setup, try to minimize the no of lines by using helper files to retrieve elements,
use abstraction by using common workflow helpers, keep proper logging of every step to ease 
debugging and better readability, maintain document for the all test case '''





