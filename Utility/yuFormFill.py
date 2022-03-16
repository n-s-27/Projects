import time
import sms4
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.yu.edu/covid19')
time.sleep(1)

fnb = driver.find_element_by_id('NextButton')
fnb.click()

#				END PAGE 1            #

time.sleep(1)

firstNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[2]/label[1]'
bubble1 = driver.find_element_by_xpath(firstNoXP).click()



secondNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[2]/label[1]'
bubble2 = driver.find_element_by_xpath(secondNoXP).click()

thirdNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[2]/label[1]'
bubble3 = driver.find_element_by_xpath(thirdNoXP).click()

fourthNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[4]/td[2]/label[1]'
bubble4 = driver.find_element_by_xpath(fourthNoXP).click()

fifthNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[5]/td[2]/label[1]'
bubble5 = driver.find_element_by_xpath(fifthNoXP).click()

sixthNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[6]/td[2]/label[1]'
bubble6 = driver.find_element_by_xpath(sixthNoXP).click()

seventhNoXP = '/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/table/tbody/tr[7]/td[2]/label[1]'
bubble7 = driver.find_element_by_xpath(seventhNoXP).click()

lastNoXP = '//*[@id="QID135-2-label"]'

bubble8 = driver.find_element_by_xpath(lastNoXP).click()

driver.find_element_by_id("NextButton").click()

# 			END PAGE 2
time.sleep(1)
p2No1xpath = '//*[@id="QR~QID132~2"]'

p2No1cssPath = '//*[@id="QID132-2-label"]'
p2Bubble1 = driver.find_element_by_xpath(p2No1cssPath)
p2Bubble1.click()

#If vaccinated answer yes
p2No2xpath = '//*[@id="QID134-5-label"]'
p2Yes2xpath = '//*[@id="QID134-4-label"]'

p2Bubble2 = driver.find_element_by_xpath(p2No2xpath).click()

driver.find_element_by_id("NextButton").click()

# 				END PAGE 3
time.sleep(1)
p3No1XP = '//*[@id="QID127-5-label"]'
p3Bubble1 = driver.find_element_by_xpath(p3No1XP).click()

p3No2XP = '//*[@id="QID117-4-label"]'
p3Bubble2 = driver.find_element_by_xpath(p3No2XP).click()

p3No3XP = '//*[@id="QID118-3-label"]'
p3Bubble3 = driver.find_element_by_xpath(p3No3XP).click()

p3No4XP = '//*[@id="QID138-2-label"]'
p3Bubble4 = driver.find_element_by_xpath(p3No4XP).click()


# THIS MUST BE YES
p3Yes5XP = '//*[@id="QID105-1-label"]'
p3Bubble5 = driver.find_element_by_xpath(p3Yes5XP).click()

driver.find_element_by_id("NextButton").click()

# END PAGE 4
time.sleep(1)
firstName = #enter first name 
fnID = '//*[@id="QR~QID25~1"]'
driver.find_element_by_xpath(fnID).click()
driver.find_element_by_css_selector('#QR\~QID25\~1').send_keys("Noah")
lastName = #enter last name
lnXP = '//*[@id="QR~QID25~2"]'
lnCss = '#QR\~QID25\~2'
driver.find_element_by_xpath(lnXP).click()
driver.find_element_by_css_selector(lnCss).send_keys(lastName)


yEmail = #enter your email
emXP = '//*[@id="QR~QID25~3"]'
emCSS = '#QR\~QID25\~3'
driver.find_element_by_xpath(emXP).click()
driver.find_element_by_css_selector(emCSS).send_keys(yEmail)

pNum = '1'
pnXP = '//*[@id="QR~QID25~4"]'
pnCSS = '#QR\~QID25\~4'
driver.find_element_by_xpath(pnXP).click()
driver.find_element_by_css_selector(pnCSS).send_keys(pNum)

roleSelectXP = '//*[@id="QID110-1-label"]'
driver.find_element_by_xpath(roleSelectXP).click()
campusSelectXP = '//*[@id="QID112-1-label"]'
driver.find_element_by_xpath(campusSelectXP).click()
driver.find_element_by_id("NextButton").click()

# Now we have our go-ahead we need to screenshot it and have it sent to user phone for convenient presentation to campus security

# to save screenshot - by date or number



pic = driver.save_screenshot('./image.png')

# result is a json server response. see docs for details
result = sms4.send('xxx-xxx-xxxx', 'The server is down!')
print(result)



sender_email = "sender@sender.com"
receiver_email = "recipient@mail.com"

password = input("Type your password and press enter: ")



contents = '\image.png'




