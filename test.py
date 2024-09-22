from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

# נתיב לכרום דרייב
chrome_driver_path = r"F:\Desktop\Projects\MsoftFacebook\chromedrive\chromedriver.exe"

# הגדר את ה-ChromeService עם הנתיב שלך
chrome_service = ChromeService(executable_path=chrome_driver_path)

# ציין את ה-ChromeService כפרמטר ל־webdriver.Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def open_chrome_and_go_to_link():
    # פתח את כרום דרייב
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    # פתח את הדף
    driver.get("https://www.couchpotatoil.co.il/bb24winner/%D7%94%D7%90%D7%97-%D7%94%D7%92%D7%93%D7%95%D7%9C/")
    
    # השהייה כדי לוודא שהדף נטען
    time.sleep(2)
    
    # שינוי גודל חלון לפני המקסום (אופציונלי)
    driver.set_window_size(1024, 768)
    
    # מקסימום חלון
    driver.maximize_window()
    
    # השהייה כדי לוודא שהמקסום הצליח
    time.sleep(2)
    
    return driver

def scroll_down():
    # גלול למטה
    pyautogui.moveTo(1697, 505)
    pyautogui.scroll(-2700)

def close_chrome(driver):
    # סגור את הדפדפן
    driver.quit()


def ClickAtYosi():
    time.sleep(0.5)
    try:
        # ניסיון למצוא את האלמנט הראשון וללחוץ עליו
        picpost = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[8]/div[2]/div[1]/div/article/div[1]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div/div[2]/label[6]/div/div[2]/div[2]')
        picpost.click()
    except:
        try:
            # אם האלמנט הראשון לא נמצא, ננסה את האלמנט השני (תמונה זו)
            picpost = driver.find_element(By.XPATH, '//img[@src="https://www.couchpotatoil.co.il/wp-content/uploads/2024/06/בטטת-כורסה-יוסי-פריאנטי-האח-הגדול-2024-e1718280318740.webp"]')
            picpost.click()
        except:
            print("Both elements not found or other issue occurred.")
    time.sleep(0.5)


# לולאה שתחזור 3 פעמים על פתיחת כרום כל 6 שעות, גלילה וסגירה
for _ in range(3):
    driver = open_chrome_and_go_to_link()
    scroll_down()
    time.sleep(1)
    ClickAtYosi()
    time.sleep(10)
    close_chrome(driver)
    time.sleep(5)  # המתנה לפני פתיחה מחודשת של הדפדפן

time.sleep(6 * 60 * 60)  # המתנה של 6 שעות (ב-שניות)

