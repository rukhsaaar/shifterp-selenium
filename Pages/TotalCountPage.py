from selenium.webdriver import Keys
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


# Defined a class with the page element to fetch them into the testcase
class TotalRecordPageCls(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def table_selectors(self):
        return self.go_to_element('webTable_XPATH')

    def getTableRows_selectors(self, web_driver, multi_elements=False):
        return self.go_to_element('tableRows_XPATH', element_driver=web_driver, multi_elements=multi_elements)

    def getTableCols_selectors(self, web_driver, multi_elements=False):
        return self.go_to_element('tableCols_XPATH', element_driver=web_driver, multi_elements=multi_elements)

    def nextButton_Selectors(self, web_driver):
        return self.go_to_element('nextBtn_XPATH', element_driver=web_driver)

    def paginationText_Selectors(self, web_driver):
        pagination_text = self.go_to_element('totalCount_XPATH', element_driver=web_driver).text
        splittext = pagination_text.split()
        return splittext[2]

    def search_and_enter(self, search_text):
        search_input = self.go_to_element('searchbar_XPATH')
        search_input.send_keys(search_text)
        self.action.send_keys(Keys.ENTER).perform()

    def get_table_data(self, web_driver):
        data_table = self.go_to_element('webTable_XPATH', element_driver=web_driver).text
        return data_table

    def is_data_present(self, data_table):
        return 'No data added to the table.' not in data_table

    def open_original(self):
        self.click('cancelbtn_XPATH')

