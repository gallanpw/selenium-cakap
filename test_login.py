import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://staging.student.cakap.com/login?returnUrl=%2Fcourse%2Fcalendar")
    self.driver.set_window_size(1299, 741)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .text-center").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'email\']").send_keys("gallan.widyanto@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".mt > .text-center").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mt > .text-center").send_keys("123456aB")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".m-n").click()
  
