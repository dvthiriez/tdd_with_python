from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://192.168.1.17:8000')

assert 'Django' in browser.title

