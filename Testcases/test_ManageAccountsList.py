import pytest
import logging
from Testcases.BaseTest import BaseClass
from Utilities import DataProvider
from Utilities.LogUtil import Logger
from Testcases import test_login
from Testcases import test_ManageAccountsAdd
from Pages.ManageAccountPage import AddManageAccountsCls


# Logging the information
log = Logger(__name__, logging.INFO)


class Test_ManageAccountsList(BaseClass):

    def test_loginToDashboard(self):
        log.logger.info("Start login to ShiftERP")
        test_login.Test_LoginCls.test_DoLogin(self, "admin", "12345678")
        log.logger.info("Login to ShiftERP successfully executed")

    def test_addProvisionForm(self):
        log.logger.info("Go to manage accounts listing in super admin dashboard")
        test_ManageAccountsAdd.Test_AddProvisionAccount.test_accountlisting(self)
        log.logger.info("Manage accounts listing successfully accessed")

    def test_totalRecords(self):
        log.logger.info("Count total records started")
        total = AddManageAccountsCls(self.driver)
        total.totalRecords_Selectors()
        log.logger.info("Search Completed")
