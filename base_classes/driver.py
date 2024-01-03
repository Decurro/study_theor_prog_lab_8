import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")


class Driver:
    """Класс для работы с вебдрайверами Selenium."""

    def __init__(self):
        """Инициализировать объект класса Driver."""
        if os.name == 'nt':
            self.__chromedriver_path = os.environ.get("CHROMEDRIVER_PATH_NT")
        elif os.name == 'posix':
            self.__chromedriver_path = os.environ.get("CHROMEDRIVER_PATH_POSIX")
        self.__driver = self.__initialize_driver()

    def __enter__(self):
        """Для менеджера контекста (with Driver() as *)"""
        return self.__driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Для менеджера контекста (with Driver() as *)"""
        self.__driver.close()
        self.__driver.quit()

    def get_driver(self):
        return self.__driver

    def __initialize_driver(self) -> webdriver:
        """Инициализировать драйвер с готовыми настройками.

        :return: драйвер с готовыми настройками.
        """
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--blink-settings=imagesEnabled=false')

        options.add_argument('--disable-infobars')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--disable-gpu')

        options.add_argument('--log-level=3')
        options.add_experimental_option("detach", True)

        s = Service(executable_path=self.__chromedriver_path)
        driver = webdriver.Chrome(service=s, options=options)

        return driver
