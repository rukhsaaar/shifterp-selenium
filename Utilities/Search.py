from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.TotalCountPage import TotalRecordPageCls

class search(BasePage):

    def Search_Input(self):
        search_text = input('Please enter search key:')
        return search_text
