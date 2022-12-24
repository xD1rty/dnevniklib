import io
import json
import os
import sys
import tarfile 
import requests
import zipfile
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome, ChromeOptions

class UserToken:
    def __init__(self, _login, _password, browser, config_file) -> None:
        # ПРЕДУПРЕЖДЕНИЕ: используется Selenium. 
        # В browser 2 значения "chrome", "firefox" 
        # Перед стартом вашего проекта библиотека при использовании модуля
        # Установит драйвер вашего браузера
        # Процесс поиска токена займет 10-20 сек
        # Для использования класса следует установить Chromium-подобный браузер или Gecko
        self.browser = None
        self.path_to_browser_driver = None
        try:
            self.configuration_file_read = json.loads(open(config_file, "r").read())
            self.browser = self.configuration_file_read["browser"]
            self.path_to_browser_driver = self.configuration_file_read["driver"]
        except:
            self.browser = browser
        self.login = _login
        self.password = _password
        
        self.config_file = config_file
            


        
    
    def configuration(self) -> None:
        if sys.platform == 'linux' or 'linux2':
            print("Ваша OС: linux")
            if self.browser == "chrome":
                r = requests.get("https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_linux64.zip")
                z = zipfile.ZipFile(io.BytesIO(r.content))
                print("Файл создан")
                z.extractall()
                self.path_to_browser_driver = "chromedriver"
                self.json_settings = json.dumps({
                    "browser": "chrome",
                    "driver": self.path_to_browser_driver
                })
                self.configuration_file_write = open(self.config_file, "w").write(self.json_settings)
                print("Сделано!")
                z.close()
                os.remove("chromedriver.zip")
            if self.browser == "firefox":
                r = requests.get("https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz")
                f = open("firefox.tar.gz", "wb")
                f.write(r.content)
                f.close()
                print("Файл создан")
                tar = tarfile.open("firefox.tar.gz", "r:gz")
                tar.extractall()
                self.path_to_browser_driver = "geckodriver"
                self.json_settings = json.dumps({
                    "browser": "firefox",
                    "driver": self.path_to_browser_driver
                })
                self.configuration_file_write = open(self.config_file, "w").write(self.json_settings)
                print("Сделано!")
                tar.close()
                os.remove("firefox.tar.gz")
        elif "win" in sys.platform:
            print("Ваша ОС: windows")
            if self.browser == "chrome":
                r = requests.get("https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_win32.zip")
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall()
                self.path_to_browser_driver = "chromedriver.exe"
                self.json_settings = json.dumps({
                    "browser": "chrome",
                    "driver": self.path_to_browser_driver
                })
                self.configuration_file_write = open(self.config_file, "w").write(self.json_settings)
                print("done")
                z.close()
                os.remove("chromedriver.zip")
            if self.browser == "firefox":
                r = requests.get("https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win32.zip")
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall()
                self.path_to_browser_driver = "geckodriver.exe"
                self.json_settings = json.dumps({
                    "browser": "firefox",
                    "driver": self.path_to_browser_driver
                })
                self.configuration_file_write = open(self.config_file, "w").write(self.json_settings)
                print("done")
                z.close()
                os.remove("firefox.zip")
        elif sys.platform == 'darwin':
            print("Ваша OС: MAC OS")
            if self.browser == "chrome":
                r = requests.get("https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_mac64.zip")
                z = zipfile.ZipFile(io.BytesIO(r.content))
                print("Файл создан")
                z.extractall()
                self.path_to_browser_driver = "chromedriver"
                self.json_settings = json.dumps({
                    "browser": "chrome",
                    "driver": self.path_to_browser_driver
                })
                self.configuration_file_write = open(self.config_file, "w").write(self.json_settings)
                print("Сделано!")
                z.close()
                os.remove("chromedriver.zip")
            if self.browser == "firefox":
                r = requests.get("https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-macos.tar.gz")
                f = open("firefox.tar.gz", "wb")
                f.write(r.content)
                f.close()
                print("Файл создан")
                tar = tarfile.open("firefox.tar.gz", "r:gz")
                tar.extractall()
                self.path_to_browser_driver = "geckodriver"
                self.json_settings = json.dumps({
                    "browser": "firefox",
                    "driver": self.path_to_browser_driver
                })
                self.configuration_file_write = open(self.config_file, "w").write(self.json_settings)
                print("Сделано!")
                tar.close()
                os.remove("firefox.tar.gz")
    def get_token(self):
        if self.browser == "firefox":
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
        elif self.browser == "chrome":
            options = ChromeOptions()
            options.headless = True
            driver = Chrome(options=options)
        driver.get("https://login.mos.ru/sps/login/methods/password?bo=/sps/oauth/ae?response_type=code%26access_type=offline%26client_id=dnevnik.mos.ru%26scope=openid+profile+birthday+contacts+snils+blitz_user_rights+blitz_change_password%26redirect_uri=https%3A%2F%2Fschool.mos.ru%2Fv3%2Fauth%2Fsudir%2Fcallback")
        time.sleep(2)
        login_input = driver.find_element(By.XPATH, '//*[@id="login"]') # type: ignore
        login_input.send_keys(self.login)
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys(self.password)
        button = driver.find_element(By.XPATH, '//*[@id="bind"]')
        button.click()
        time.sleep(1)
        data = driver.get_cookie("aupd_token")
        driver.close()
        return data["value"]