import os
from base_classes.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from loguru import logger

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Functions:
    """
    Functions for parser work
    """

    def __init__(self):
        self.driver = Driver().get_driver()

    def registration(self, url=os.environ.get('REG_URL'), username=None, password=None, email=None):
        """
        Registration in website
        """
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='username']"))
            ).send_keys(username)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='email']"))
            ).send_keys(email)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='password1']"))
            ).send_keys(password)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='password2']"))
            ).send_keys(password)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-outline-info']"))
            ).click()

        except Exception as e:
            logger.error(f"Registration failed ->{e}")

    def auth(self, url=os.getenv("AUTH_URL"), username=None, password=None):
        """
        Authenticate in website
        """
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='username']"))
            ).send_keys(username)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='password']"))
            ).send_keys(password)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-outline-info']"))
            ).click()

        except Exception as e:
            logger.error(f"Auth failed ->{e}")

    def add_post(self, url=os.environ.get('POST_URL'), title=None, content=None):
        """
        Add a new post to the website
        """
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='title']"))
            ).send_keys(title)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//textarea[@name='content']"))
            ).send_keys(content)

            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-outline-info']"))
            ).click()

        except Exception as e:
            logger.error(f"Add new post failed ->{e}")
