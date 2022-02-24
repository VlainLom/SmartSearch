from selenium import webdriver


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://duckduckgo.com/')

def Execution1(value):
    search = driver.find_element_by_id("search_form_input_homepage")
    search.send_keys(value)

    lance_search = driver.find_element_by_class_name("js-search-button")
    lance_search.click()




