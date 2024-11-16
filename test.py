from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

# Path to Chrome Driver
chrome_driver_path = r"F:\Desktop\Projects\MsoftFacebook\chromedrive\chromedriver.exe"

# Set up ChromeService with your driver path
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Specify the ChromeService as a parameter for webdriver.Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def open_chrome_and_go_to_link():
    # Open Chrome Driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    # Open the webpage
    driver.get("https://www.couchpotatoil.co.il/bb24winner/%D7%94%D7%90%D7%97-%D7%94%D7%92%D7%93%D7%95%D7%9C/")
    
    # Wait to ensure the page has loaded
    time.sleep(2)
    
    # Resize the window before maximizing (optional)
    driver.set_window_size(1024, 768)
    
    # Maximize the window
    driver.maximize_window()
    
    # Wait to ensure the maximization was successful
    time.sleep(2)
    
    return driver

def scroll_down():
    # Scroll down
    pyautogui.moveTo(1697, 505)
    pyautogui.scroll(-2700)

def close_chrome(driver):
    # Close the browser
    driver.quit()


def ClickAtYosi():
    time.sleep(0.5)
    try:
        # Attempt to find the first element and click on it
        picpost = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[8]/div[2]/div[1]/div/article/div[1]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div/div[2]/label[6]/div/div[2]/div[2]')
        picpost.click()
    except:
        try:
            # If the first element is not found, try the second element (this image)
            picpost = driver.find_element(By.XPATH, '//img[@src="https://www.couchpotatoil.co.il/wp-content/uploads/2024/06/בטטת-כורסה-יוסי-פריאנטי-האח-הגדול-2024-e1718280318740.webp"]')
            picpost.click()
        except:
            print("Both elements not found or other issue occurred.")
    time.sleep(0.5)


# A loop that repeats 3 times to open Chrome every 6 hours, scroll, and close
for _ in range(3):
    driver = open_chrome_and_go_to_link()
    scroll_down()
    time.sleep(1)
    ClickAtYosi()
    time.sleep(10)
    close_chrome(driver)
    time.sleep(5)  # Wait before reopening the browser

time.sleep(6 * 60 * 60)  # Wait for 6 hours (in seconds)

