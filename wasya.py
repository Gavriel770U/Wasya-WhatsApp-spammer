from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def search_chat(driver, chat_name: str) -> None:
  """
  Function that searches a What'sApp chat.
  :param driver: selenium webdriver 
  :type driver: webdriver.any 
  :param chat_name: the name of the chat to search 
  :type chat_name: str
  :return: None
  :rtype: None
  """
  search_bar = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
  search_bar.send_keys(chat_name)
  search_bar.send_keys(Keys.ENTER)

def send_message(driver, message: str) -> None:
  """
  Function that sends a What'sApp message.
  :param driver: selenium webdriver 
  :type driver: webdriver.any 
  :param message: a message to send
  :type message: str
  :return: None
  :rtype: None
  """
  message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
  message_box.send_keys(message)
  message_box.send_keys(Keys.ENTER)

def send_messages(driver, messages: iter) -> None:
  """
  Function that sends What'sApp messages.
  :param driver: selenium webdriver 
  :type driver: webdriver.any 
  :param messages: messages to send
  :type messages: iter
  :return: None
  :rtype: None
  """
  for message in messages:
    send_message(driver, message)

def wasya_run() -> None:
  url = 'https://web.whatsapp.com/'
  
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get(url)

  input("SCAN QR-CODE AND PRESS ENTER TO CONTINUE")
  
  search_chat(driver, "GADOL")
  
  time.sleep(5)
  messages = ["Hello, this is from python :)"] * 200
  send_messages(driver, messages)
  
  input("PRESS ENTER TO CLOSE THE APP")
  driver.close()
  
  print("Good run")