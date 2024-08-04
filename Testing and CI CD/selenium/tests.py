import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):  # takes the file and gets the uri
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        """Make sure the title of the webpage is correct"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        """Make sure the increase button works"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(by=By.ID, value="increase")
        increase.click()
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value='h1').text, "1")

    def test_decrease(self):
        """Make sure the decrease button works"""
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element(by=By.ID, value="decrease")
        decrease.click()
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value='h1').text, "-1")

    def test_multiple_increase(self):
        """Make sure the increase button works multiple times"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(by=By.ID, value="increase")
        n = 100
        for _ in range(n):
            increase.click()
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value='h1').text, str(n))


if __name__ == "__main__":
    unittest.main()
