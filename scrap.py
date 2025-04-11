from selenium import webdriver
from selenium.webdriver.common.by import By
import json

url = "https://www.ciceksepeti.com/s/cicek-icin-ozel-gunler"
item_list = []

driver = webdriver.Chrome()
driver.get(url)

table = driver.find_elements(By.TAG_NAME, "ul")

for ele in table:
    items = ele.find_elements(By.TAG_NAME, "li")

    for elem in items:
        item_dict = {}

        try:
            text_box = elem.find_element(By.CSS_SELECTOR, "div[class='text']")
        except:
            pass
        
        try:
            name = text_box.find_element(By.CSS_SELECTOR, "p[class='name']")
        except:
            pass

        try:
            date = text_box.find_element(By.CSS_SELECTOR, "p[class='day']")
        except:
            pass

        item_dict['name'] = name.text
        item_dict['date'] = date.text

        print(item_dict)

        item_list.append(item_dict)

with open("./data.json", 'w') as f:
    f.write(json.dumps(item_list, indent=4))        


