from selenium import webdriver


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://www.google.com/maps/')

def Execution(valeur):
    search = driver.find_element_by_id("searchboxinput")
    search.send_keys(valeur)

    lance_search = driver.find_element_by_class_name("nhb85d-BIqFsb")
    lance_search.click()


