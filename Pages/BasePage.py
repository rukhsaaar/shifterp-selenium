from Utilities import ConfigReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, element_driver=None):
        driver = element_driver if element_driver else self.driver
        if str(locator).endswith("_XPATH"):
            driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS_SELECTOR"):
            driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_TAG_NAME"):
            driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_LINK_TEXT"):
            driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CLASS_NAME"):
            driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).click()

    def type(self, locator, value, element_driver = None):
        driver = element_driver if element_driver else self.driver
        if str(locator).endswith("_XPATH"):
            driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS_SELECTOR"):
            driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_TAG_NAME"):
            driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_LINK_TEXT"):
            driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASS_NAME"):
            driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)

    def select(self, locator, value, element_driver=None):
        driver = element_driver if element_driver else self.driver
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS_SELECTOR"):
            dropdown = driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            dropdown = driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            dropdown = driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_TAG_NAME"):
            dropdown = driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_LINK_TEXT"):
            dropdown = driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            dropdown = driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASS_NAME"):
            dropdown = driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        select = Select()
        select.select_by_visible_text(value)

    def go_to_element(self, locator, element_driver=None, multi_elements=False):
        driver = element_driver if element_driver else self.driver
        if str(locator).endswith("_XPATH"):
            return driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS_SELECTOR"):
            return driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            return driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_NAME"):
            return driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_TAG_NAME"):
            return driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_LINK_TEXT"):
            return driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            return driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CLASS_NAME"):
            return driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)) \
                if not multi_elements else \
                driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", locator))
