import pytest
import logging
from Pages.ManageAccountPage import AddManageAccountsCls
from Testcases import test_login
from Testcases.BaseTest import BaseClass
from Utilities import DataProvider
from Utilities.LogUtil import Logger

# Logging the information
log = Logger(__name__, logging.INFO)


class Test_AddProvisionAccount(BaseClass):

    # Importing the driver from basepage
    # driver = BaseClass.driver

    # Testcase for logging in to the dashboard
    def test_loginToDashboard(self):
        log.logger.info("Start login to ShiftERP")
        test_login.Test_LoginCls.test_DoLogin(self, "admin", "12345678")
        log.logger.info("Login to ShiftERP successfully executed")

        # Go to provision accounts listing

    def test_accountlisting(self):
        log.logger.info("Go to manage accounts listing in super admin dashboard")
        add = AddManageAccountsCls(self.driver)
        add.manageAccount_selectors()
        log.logger.info("Manage accounts listing successfully accessed")

    # Go to add provision accounts form
    def test_addProvisionForm(self):
        log.logger.info("Test Go to add provision accounts")
        addProvision = AddManageAccountsCls(self.driver)
        addProvision.addProvision_selectors()
        log.logger.info("Test go to provision successfully executed ")

    # Add business info in provision accounts
    @pytest.mark.parametrize("businessInfoname, businessInfoaddress, dba, businessInfocity, businessInfophone, "
                             "businessInfostate, businessInfozip",
                             DataProvider.ManageAccoubtsData("ManageAccount-businessTest"))
    def test_addBusinessInfo(self, businessInfoname, businessInfoaddress, dba, businessInfocity,
                             businessInfophone, businessInfostate, businessInfozip):
        log.logger.info("Test add business info started")
        businessInfo = AddManageAccountsCls(self.driver)
        businessInfo.addBusinessInfo_selectors(businessInfoname, businessInfoaddress, dba, businessInfocity,
                                               str(businessInfophone), businessInfostate, businessInfozip)
        log.logger.info("Test add business info successfully executed")

    # Add billing details function
    @pytest.mark.parametrize("billingfirstname, billinglastname, billingaddress, billingtitle, billingcity,"
                             "billingphone, billingstate, billingzip, billingemail",
                             DataProvider.ManageAccoubtsData("ManageAccounts-billingTest"))
    def test_addBilling(self, billingfirstname, billinglastname, billingaddress, billingtitle, billingcity,
                        billingphone, billingstate, billingzip, billingemail):
        log.logger.info("Test add business info started")
        businessInfo = AddManageAccountsCls(self.driver)
        businessInfo.addBilling_selectors(billingfirstname, billinglastname, billingaddress, billingtitle, billingcity,
                                          billingphone, billingstate, billingzip, billingemail)
        log.logger.info("Test add business info successfully executed")

    # Choose subscription and add details function
    @pytest.mark.parametrize("recurringdate, setupfeedate, setupfee",
                             DataProvider.ManageAccoubtsData("ManageAccounts-subTest"))
    def test_addSubscription(self, recurringdate, setupfeedate, setupfee):
        log.logger.info("Test add subscription started")
        subscription = AddManageAccountsCls(self.driver)
        subscription.addSubscription_selectors(recurringdate, setupfeedate, setupfee)
        log.logger.info("Test subscription successfully executed")

    # Choose subscription and add details function
    @pytest.mark.parametrize("settingsfirstname, settingslastname, settingsusername, settingsemail, settingsphone",
                             DataProvider.ManageAccoubtsData("ManageAccounts-settingsTest"))
    def test_addSettings(self, settingsfirstname, settingslastname, settingsusername, settingsemail, settingsphone):
        log.logger.info("Test add settings started")
        settings = AddManageAccountsCls(self.driver)
        settings.settings_selectors(settingsfirstname, settingslastname, settingsusername, settingsemail, settingsphone)
        log.logger.info("Test add settings successfully executed")

    # Go save the form
    def test_saveProvision(self):
        log.logger.info("Test add provision started")
        settings = AddManageAccountsCls(self.driver)
        settings.clickProvisionbtn_selector()
        log.logger.info("Test add provision successfully executed")
