from selenium import webdriver

driver = webdriver.Chrome('E:\Download\Compressed\chromedriver')
driver.get('https://web.whatsapp.com/')
i=0
names =[]
while (True):
    names.append(input('enter the names'))
    if names[i]=='!' :
        break
    i=i+1
names.remove('!') 

msg = input('Enter your message : ')

input('Enter anything after scanning QR code')
for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')


    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()