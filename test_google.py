from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome() #Change this according to your chosen browser
driver.get("http://google.com")

search_bar=driver.find_element_by_name("q")
search_bar.send_keys('"info"')
search_bar.send_keys(Keys.ENTER)

webdriver.support.wait.WebDriverWait(driver,1) #wait for request and response to be sent and page to load

results=driver.find_element_by_id("center_col")
assert results.text.find("info") #check that the results contian the search query word
