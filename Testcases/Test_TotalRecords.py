import logging
from Testcases.BaseTest import BaseClass
from Utilities.LogUtil import Logger
from Testcases import test_login
from Utilities.IterateTable import datatableCls
from Pages.TotalCountPage import TotalRecordPageCls
from Testcases.test_ManageAccountsAdd import Test_AddProvisionAccount


# Logging the information
log = Logger(__name__, logging.INFO)


class Test_TotalRecordsCls(BaseClass):

    def test_loginToDashboard(self):
        log.logger.info("Start login to ShiftERP")
        test_login.Test_LoginCls.test_DoLogin(self, "admin", "12345678")
        log.logger.info("Login to ShiftERP successfully executed")

    def test_GotoList(self):
        log.logger.info("Go to listing started")
        Test_AddProvisionAccount.test_accountlisting(self)
        log.logger.info("Got list successfully")

    def test_GetTotalRecords(self):
        log.logger.info("Total records started successfully")
        getValue = TotalRecordPageCls(self.driver)
        total_count = getValue.paginationText_Selectors()
        text = datatableCls.iterateTable(self)
        assert text == int(total_count)
        log.logger.info("Records matched successfully")


