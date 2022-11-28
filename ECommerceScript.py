import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(ChromeDriverManager().install())

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]").click()
driver.find_element(By.ID, "email_create").send_keys("sairam123456@gmail.com")
driver.find_element(By.ID, "SubmitCreate").click()
driver.implicitly_wait(10)

#driver.find_element(By.ID, 'id_gender1').click()
driver.find_element(By.ID, "customer_firstname").send_keys("SaiR")
driver.find_element(By.ID, "customer_lastname").send_keys("Yashu")
driver.find_element(By.ID, "passwd").send_keys("Password*123")

date = Select(driver.find_element(By.ID, 'days'))
date.select_by_value('13')
time.sleep(3)

month = Select(driver.find_element(By.ID, 'months'))
month.select_by_value('9')
time.sleep(2)

Year = Select(driver.find_element(By.ID, 'years'))
Year.select_by_value('2009')

time.sleep(3)

driver.find_element(By.ID, 'newsletter').click()
driver.find_element(By.ID, 'firstname').send_keys("  ")
driver.find_element(By.ID, 'lastname').send_keys("  ")
driver.find_element(By.ID, 'company').send_keys("HCL Software Tech")
driver.find_element(By.ID, 'address1').send_keys("PO BOX 1409, Hyderabad")
driver.find_element(By.ID, 'city').send_keys("Hyderbad")
State = Select(driver.find_element(By.ID, 'id_state'))
State.select_by_value('32')
driver.find_element(By.ID, 'postcode').send_keys("10005")
driver.find_element(By.ID, 'other').send_keys("This is an Automate code")
driver.find_element(By.ID, 'phone').send_keys("9876544322")
driver.find_element(By.ID, 'phone_mobile').send_keys("9886543280")
driver.find_element(By.ID, 'alias').send_keys("New York")

#driver.find_element(By.ID, 'submitAccount').click()

time.sleep(3)
driver.quit()
