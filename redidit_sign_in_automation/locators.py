from selenium.webdriver.common.by import By

USERNAME = (By.ID, "loginUsername")
PASSWORD = (By.ID, "loginPassword")
LOGIN = (By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")
page_reached = (By.ID, "header-search-bar")