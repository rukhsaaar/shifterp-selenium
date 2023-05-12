from Pages.BasePage import BasePage


# Defined a class with the page element to fetch them into the testcase
class loginPageCls(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login_selectors(self, username, password):
        self.type("username_NAME", username)
        self.type("password_NAME", password)
        self.click("Login_btn_XPATH")
