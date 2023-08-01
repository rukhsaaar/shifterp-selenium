import pytest
import logging
from Utilities import DataProvider
from Utilities.LogUtil import Logger
from Testcases.BaseTest import BaseClass
from Pages.ForgetPasswordPage import ForgetPassCls

# Logging the information
log = Logger(__name__, logging.INFO)


# Testcase for forget password
class Test_ForgetPassword(BaseClass):

    @pytest.mark.parametrize("email", DataProvider.GetData("ForgetPass"))
    def test_DoLogin(self, email):
        log.logger.info("Start login to ShiftERP")
        Forget = ForgetPassCls(self.driver)
        Forget.forgetpass_selectors(email)
        log.logger.info("Login too ShiftERP successfully executed")
