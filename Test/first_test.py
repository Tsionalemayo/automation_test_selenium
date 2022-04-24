from selenium import webdriver
from selenium.webdriver.common.by import By

#דפדפן CHROM
driver = webdriver.Chrome('..\Driver\chromedriver.exe')
driver.get("https://he-il.facebook.com/")


#דפדפן FIREFOX
driver1 = webdriver.Firefox(executable_path=r'..\Driver\geckodriver.exe')
driver1.get("https://he-il.facebook.com/")
#
# #דפדפן MICROSOFT EDGE
driver2 = webdriver.Edge('..\Driver\msedgedriver.exe')
driver2.get("https://he-il.facebook.com/")

# לחיצה על כפתור שכחת סיסמא
driver.find_element(By.XPATH,"//a[contains(text(),'שכחת את הסיסמה?')]").click()

#לחיצה על כפתור יצירת חשבון חדש
driver.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[5]/a[1]").click()
