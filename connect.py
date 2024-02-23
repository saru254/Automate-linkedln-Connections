#connect python with webbrowser chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag

def login():

    #getting the login element
    username = driver.find_element_by_id("login-email")

    #sending the keys for username
    username.send_keys("username")

    #sending the keys for password
    password.send_keys("password")

    #getting the tag for submit button
    driver.find_element_by_id("login-submit").click()

    
