from selenium import webdriver
from selenium.webdriver.common.by import By
from assignment4_dynamic.utilities import custome_logger as cl
import logging

class WebTable():

    def __init__(self, driver):
        self.driver = driver

    log = cl.customLogger(logging.DEBUG)

    def get_num_rows(self):
        num_rows = len(self.driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr"))
        self.log.info("Rows in table are: " + str(num_rows))

    def get_num_col(self):
        num_col = len(self.driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/th"))
        self.log.info("Columns in table are: " + str(num_col))

    def get_all_data(self):
        no_of_rows = len(self.driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr"))
        # get number of columns
        no_of_columns = len(self.driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/th"))
        all_data = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(2, no_of_rows+1):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, no_of_columns + 1):
                # get text from the i th row and j th column
                ro.append(self.driver.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text)

            # add the row data to allData of the self.table
            all_data.append(ro)
        self.log.info("Table data:" + str(all_data))
