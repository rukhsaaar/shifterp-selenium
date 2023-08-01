from Pages.BasePage import BasePage


# Defined a class with the page element to fetch them into the testcase
class ForgetPassCls(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def forgetpass_selectors(self, email):
        self.click("forgetpage_XPATH")
        self.type("email_XPATH", email)
        self.click("resetbtn_XPATH")
        self.click("backbtn_XPATH")

    def error_selectors(self, wrongmail):
        self.click("forgetpage_XPATH")
        self.type("email_XPATH", wrongmail)



