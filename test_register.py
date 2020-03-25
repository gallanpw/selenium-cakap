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

class TestRegister():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_register(self):
    self.driver.get("https://staging.student.cakap.com/login/register/email")
    self.driver.set_window_size(1299, 741)
    self.driver.find_element(By.ID, "inputemail").click()
    self.driver.find_element(By.ID, "inputemail").send_keys("gallan.widyanto@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".blueborder > span").click()
    self.driver.find_element(By.ID, "inputfirst").click()
    self.driver.find_element(By.ID, "inputfirst").send_keys("gallan")
    self.driver.find_element(By.ID, "inputlast").click()
    self.driver.find_element(By.ID, "inputlast").send_keys("widyanto")
    self.driver.find_element(By.ID, "inputpassword").click()
    self.driver.find_element(By.ID, "inputpassword").send_keys("123456aB")
    self.driver.find_element(By.ID, "inputconfirmpass").click()
    self.driver.find_element(By.ID, "inputconfirmpass").send_keys("123456aB")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-6:nth-child(2) .country-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "input-phone").click()
    self.driver.find_element(By.ID, "input-phone").click()
    self.driver.find_element(By.ID, "input-phone").send_keys("87750981398")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button-box").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".head-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col").click()
  
