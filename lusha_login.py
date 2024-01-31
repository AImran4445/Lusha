import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://auth.lusha.com/login?returnUrl=https%3A%2F%2Fdashboard.lusha.com%2F')
driver.maximize_window()
username = "2019cs628@student.uet.edu.pk"
password = "Aliimran@098"
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'email'))
)
email_input.send_keys(username)
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'password'))
)
password_input.send_keys(password)
driver.find_element(By.CLASS_NAME, 'StyledButton-sc-1etz1jd-0').click()
prospecting_link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[1]/div/a[1]'))
)
prospecting_link.click()

get_data_link = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH , '/html/body/div[2]/div[4]/div/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div[1]'))
)
get_data_link.click()

save_search_link = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH , '/html/body/div[2]/div[4]/div/div[1]/div[1]/div/div[2]/button[2]'))
)
save_search_link.click()

cross_link = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH , '/html/body/div[10]/div[2]/div[1]'))
)
cross_link.click()

#For all show details button
show_details_buttons = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'show-button'))
)
show_details_buttons.click()
# show_details_buttons.click()

select_list = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div[1]'))
)
select_list.click()

selected_list = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'list-select-container-1id560u-menu'))
)

selected_list.click()

save_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[4]/div/button'))
)

save_button.click()



