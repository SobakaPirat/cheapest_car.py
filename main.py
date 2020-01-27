from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time



browser = webdriver.Firefox('C:/Users/egor/geckodriver')
browser.get('https://www.lacentrale.fr/%27')


BpCote = browser.find_element_by_link_text('Cote')
BpCote.click()
time.sleep(1)


Immatrecherche = browser.find_element_by_id('immatCote')
Immatrecherche.send_keys('AE073KW')
time.sleep(1)
Kmrecherche = browser.find_element_by_xpath('//*[@id="formCote"]/div[3]/input')
Kmrecherche.send_keys('12000')
time.sleep(1)


BpValider = browser.find_element_by_xpath('//*[@id="formCote"]/div[5]/button')
browser.execute_script('arguments[0].click();', BpValider)
time.sleep(1)

cars = browser.find_elements_by_class_name('listingResultLine.auto')
count_of_cars = len(cars)
car_number = 0
car_name = ""
cheapest_car = ""
cheapest_car_money = 99999999

while car_number < count_of_cars:
    try:
        cars = browser.find_elements_by_class_name('listingResultLine.auto')
        link = cars[car_number].find_element_by_partial_link_text('')
        car_characteristic = link.text
        cars[car_number].click()
        time.sleep(2)
        price = browser.find_element_by_class_name('jsRefinedQuot.sizeD.bold')
        price = price.text
        price = int(price.replace(" ", ""))
        car_name = browser.find_element_by_class_name('clearPhone')
        car_name = car_name.text
        print(car_characteristic)
        print(car_name)
        print('price = ', price)
        print() 
        if price < cheapest_car_money:
            cheapest_car = car_characteristic + "\n" + car_name
            cheapest_car_money = price
        browser.back()
        time.sleep(2)
        car_number += 1
    except:
        browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(2)

print('*****************************')
print(cheapest_car)
print(cheapest_car_money)
print('*****************************')








