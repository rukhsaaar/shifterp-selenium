import pytest

from Pages.BasePage import BasePage


# Defined a class with the page element to fetch them into the testcase
class AddManageAccountsCls(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Go to account listing function
    def manageAccount_selectors(self):
        self.click("accountListing_XPATH")

    # Go to add provision accounts form
    def addProvision_selectors(self):
        self.click("manage_XPATH")

    # Business info selector function
    def addBusinessInfo_selectors(self, businessInfoname, businessInfoaddress, dba, businessInfocity, businessInfophone,
                                  businessInfostate, businessInfozip):
        self.type("businessInfoName_NAME", businessInfoname)
        self.type("businessInfoAddress_NAME", businessInfoaddress)
        self.type("businessIfoDBA_NAME", dba)
        self.type("businessInfoCity_NAME", businessInfocity)
        self.type("businessInfoPhone_XPATH", businessInfophone)
        self.type("businessInfoState_NAME", businessInfostate)
        self.type("businessInfoZip_NAME", businessInfozip)
        self.click("businessInfoStatus_XPATH")

    # Billing info selector function
    def addBilling_selectors(self,  billingfirstname, billinglastname, billingaddress, billingtitle, billingcity,
                             billingphone, billingstate, billingzip, billingemail):
        self.type("billingFirst_NAME", billingfirstname)
        self.type("billingLast_NAME", billinglastname)
        self.type("billingAddress_NAME", billingaddress)
        self.type("billingTitle_NAME", billingtitle)
        self.type("billingCity_NAME", billingcity)
        self.type("billingPhone_XPATH", billingphone)
        self.type("billingState_NAME", billingstate)
        self.type("billingZip_NAME", billingzip)
        self.type("billingEmail_NAME", billingemail)

    #  Subscription selector function
    def addSubscription_selectors(self, subrecurringdate, subsetupfeedate, subsetupfee):
        self.click("subSection_XPATH")
        self.click("subBasic_XPATH")
        # self.verify("userlimit_XPATH")
        # self.verify("facility_XPATH")
        # self.verify("pricePerLicense_XPATH")
        self.type("subrecurringdate_XPATH", subrecurringdate)
        self.type("subsetupfeedate_XPATH", subsetupfeedate)
        self.type("subsetupfee_NAME", subsetupfee)

    # Settings selector function
    def settings_selectors(self, settingsfirstname, settingslastname, settingsusername, settingsemail, settingsphone):
        self.click("settings_XPATH")
        self.click("adminInfoBtn_XPATH")
        self.type("adminFname_NAME", settingsfirstname)
        self.type("adminLname_NAME", settingslastname)
        self.type("adminUser_NAME", settingsusername)
        self.type("adminEmail_NAME", settingsemail)
        self.type("adminPhone_XPATH", settingsphone)
        self.click("adminSaveBtn_XPATH")

    # Add provision account button
    def clickProvisionbtn_selector(self):
        self.click("addProvAccBtn_XPATH")

    def totalRecords_Selectors(self):
        self.go_to_element("dataTable_XPATH")




