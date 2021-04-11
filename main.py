from selenium import webdriver
from sys import stdout
import time
import os

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# go to webpage
driver.get("https://www.worldometers.info/world-population/")


# get all required data form website
def get_data():
    # global data
    # Current World Population
    current_population = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='current_population']").text

    # Today
    birthT = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='births_today']").text
    deathT = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='dth1s_today']").text
    population_GrowthT = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='absolute_growth']").text

    # This year
    birthY = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='births_this_year']").text
    deathY = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='dth1s_this_year']").text
    population_GrowthY = driver.find_element_by_xpath("//span[@class='rts-counter' and @rel='absolute_growth_year']").text

    data = f"""Current Population: {current_population}, Today's Data --> Birth Today : {birthT}, Death Today : {deathT}, Population Growth Today : {population_GrowthT}. This Year's Data --> Birth This Year : {birthY}, Death This Year : {deathY}, Population Growth This Year : {population_GrowthY}"""
    return data


current_time = time.time()
run_for_seconds = 20

# scrap data for 20 seconds
while True:
    loop_time = time.time()
    difference = loop_time - current_time

    if difference > run_for_seconds:
        print(f"\n\n*** Data Scrapped For {run_for_seconds} seconds ***")
        break
    else:
        os.system('CLS')
        data = get_data()

    # print(data)
    stdout.write('\r' + data)
    stdout.flush()
    # time.sleep(0.3) # --> Uncomment this to see how data is changing dynamically

time.sleep(3)
driver.close()
driver.quit()
