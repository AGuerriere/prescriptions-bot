'''This is a program to order my prescriptions online from my GP'''

#The os module is needed to say it's done in the end
import os

import sys
import tkinter as tk
from selenium import webdriver
#the following import allows the program to send text to the browser including enter.
from selenium.webdriver.common.keys import Keys
#this is needed for waiting for the page to fully load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def order_prescriptions():
    #now we tell python where to find chromedriver
    PATH = 'path'#Replace PATH with the local path of the chrome webdriver you donwloaded
    driver = webdriver.Chrome(PATH)

    #This opens the target website, instead of 'url' you need to use the url of the website that you want to control
    driver.get('url')
    #This is a link to the entrybox where we want to enter the login username
    search = driver.find_element_by_name('ctl00$ContentPlaceHolder1$logon_email')
    search.send_keys('youremail@email.com')
    #This is is a link to the entrybox where we want to enter the login password
    search = driver.find_element_by_name('ctl00$ContentPlaceHolder1$logon_password')
    search.send_keys('YOURpassword')
    #press enter
    search.send_keys(Keys.RETURN)

    #click on next page - We use try and except to wait for 5 seconds, in case the page doesn't load in time for the click
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_TabContainer1_Panel1 > div:nth-child(1) > div > input"))
        )
        element.click()
    except:
        driver.quit()

    #click on next page again
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_TabContainer1_Panel2 > div > div > input:nth-child(1)"))
        )
        element.click()
    except:
        driver.quit()

    #This clicks or 'request email confirmation'
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_TabContainer1_Panel3_confirmation"))
        )
        element.click()
    except:
        driver.quit()

    #This is the final confirmation click - If you don't want to actually send the request, comment it out
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_TabContainer1_Panel3_buttonSend"))
        )
        element.click()
    except:
        driver.quit()
    #This says out loud "it's done, but if you are not using a Terminal that supports this, you can delete line 67"
    os.system('say It is done')
    #This exits the program at the end. Comment it out if you want to stay on the last page before leaving.
    sys.exit()

root = tk.Tk()
root.title('Prescription Bot')
root.configure(background='white')
root.bind("<FocusIn>")


btn1 = tk.Button(root, text='Yes', command=order_prescriptions)
btn2 = tk.Button(root, text='Exit', command=sys.exit)

lbl = tk.Label(root, text='Are you sure you want to proceed?')

lbl.grid(row=0, column=0, padx=100, pady=10)
btn1.grid(row=1, column=0, padx=40, pady=10)
btn2.grid(row=2, column=0, padx=40, pady=10)

root.mainloop()

