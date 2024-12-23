from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time
janela = webdriver.Chrome()
janela.get('https://web.whatsapp.com/')
pyautogui.sleep(35)
nome = 'ONLY CARGUYS'
janela.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(nome)
pyautogui.sleep(2)
pyautogui.press('enter')
for mensagem in range(0, 20):
    janela.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys('@Pato')
    pyautogui.press('enter')
time.sleep(3)
