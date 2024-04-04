from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless') 
driver = webdriver.Chrome(options=chrome_options)

companyDetails=[]
Path = '/html/body/div[3]/div[4]/div/div[2]/div/div[4]/div[2]/div[2]/div/div/table/tbody/'

driver.get("https://in.tradingview.com/markets/stocks-usa/market-movers-penny-stocks/")
for i in range(1,101):
    companyCode =  driver.find_element(By.XPATH, Path+'tr['+ str(i) +']/td[1]/span/a').text
    companyName = driver.find_element(By.XPATH, Path+'tr['+ str(i) +']/td[1]/span/sup').text
    companyPrice = driver.find_element(By.XPATH, Path+'tr['+ str(i) +']/td[2]').text 
    companyChange = driver.find_element(By.XPATH,Path+'tr['+ str(i) +']/td[3]/span').text
    companyVolume = driver.find_element(By.XPATH,Path+'tr['+ str(i) +']/td[4]').text
    companyCap = driver.find_element(By.XPATH,Path+'tr['+ str(i) +']/td[6]').text
    sector = driver.find_element(By.XPATH,Path+'tr['+ str(i) +']/td[11]/a').text

    companyDetails.append({"companyCode":companyCode,"companyName":companyName, "companyPrice":companyPrice, "companyChange":companyChange, "companyVolume":companyVolume, "companyCap":companyCap, "sector":sector})
for item in companyDetails:
    print(item)    
driver.quit()