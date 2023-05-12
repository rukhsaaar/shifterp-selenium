import pytest
from Pages.LoginPage import loginPageCls
from Testcases.BaseTest import BaseClass
from Utilities import DataProvider
import logging
from Utilities.LogUtil import Logger

# Logging the information
log = Logger(__name__, logging.INFO)


# Testcase for logging in to the dashboard
class Test_LoginCls(BaseClass):

    @pytest.mark.parametrize("username, password", DataProvider.LoginData("LoginTest"))
    def test_DoLogin(self,  username, password):
        log.logger.info("Start login to ShiftERP")
        login = loginPageCls(self.driver)
        login.login_selectors(username, str(password))
        log.logger.info("Login too ShiftERP successfully executed")
