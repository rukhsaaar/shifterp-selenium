from selenium.webdriver.common.by import By


def search(self, data, locator):
    # verify the data by getting the size of the element matches based on the text/data passed
    dataSize = len(self.table.find_elements(By.XPATH, "//td[normalize-space(text())='" + data + "']"))
    presence = False
    if dataSize > 0:
        presence = True
    return presence2
