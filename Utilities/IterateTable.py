from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Testcases.BaseTest import BaseClass
from Pages.TotalCountPage import TotalRecordPageCls


class datatableCls(BasePage):
    def iterateTable(self):
        total_records = 0
        while True:

            table = TotalRecordPageCls(self.driver)

            go_to_table = table.table_selectors()
            rows = len(table.getTableRows_selectors(go_to_table, multi_elements=True))
            cols = len(table.getTableCols_selectors(go_to_table, multi_elements=True))
            next_btn = table.nextButton_Selectors(go_to_table)
            btn_class = next_btn.get_attribute('class')
            try:
                for i in range(1, rows + 1):
                    for j in range(1, cols + 1):
                        cell_data = go_to_table.find_element(By.XPATH, "//tr[" + str(i) + "]//td[" + str(j) + "]").text
                        # print(cell_data, end='\t')
                    total_records += 1
                    # print()
                if 'disabled' in btn_class:
                    # print("Reached the end of records. Exiting loop")
                    break
                else:
                    next_btn.click()
            # Throw exceptions
            except:
                print("Exception Occured")
                break
        return total_records