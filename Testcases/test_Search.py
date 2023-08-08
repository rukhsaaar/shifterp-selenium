import pytest
import logging
from Testcases import test_login
from Testcases.BaseTest import BaseClass
from Testcases.test_ManageAccountsAdd import Test_AddProvisionAccount
from Utilities import DataProvider
from Utilities.LogUtil import Logger
from Pages.ManageAccountPage import AddManageAccountsCls


# Logging the information
log = Logger(__name__, logging.INFO)


class Test_SearchCls(BaseClass):

    # Testcase for logging in to the dashboard
    def test_loginToDashboard(self):
        log.logger.info("Start login to ShiftERP")
        test_login.Test_LoginCls.test_DoLogin(self, "admin", "12345678")
        log.logger.info("Login to ShiftERP successfully executed")

    #  Go to list function
    def test_GotoList(self):
        log.logger.info("Go to listing started")
        Test_AddProvisionAccount.test_accountlisting(self)
        log.logger.info("Got list successfully")

    # Search and veify resuults
    def test_searchInput(self):
        pass