import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.safari.webdriver import SafariDriver

# List of resolutions
resolutions = {
    "Desktop_1920x1080": (1920, 1080),
    "Desktop_1366x768": (1366, 768),
    "Desktop_1536x864": (1536, 864),
    "Mobile_360x640": (360, 640),
    "Mobile_414x896": (414, 896),
    "Mobile_375x667": (375, 667)
}

# URLs to be tested 
urls = [
    "https://www.getcalley.com/",
    "https://www.getcalley.com/calley-lifetime-offer/",
    "https://www.getcalley.com/see-a-demo/",
    "https://www.getcalley.com/calley-teams-features/",
    "https://www.getcalley.com/calley-pro-features/"
]

# Function for saving screenshots
def save_screenshot(driver, browser_name, resolution_name, url):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    domain = url.split("//")[1].split("/")[0]
    folder_path = f"screenshots/{browser_name}/{resolution_name}/{domain}/{timestamp}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    screenshot_path = f"{folder_path}/screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot: {screenshot_path}")

#Function for test
def perform_test(driver, browser_name):
    try:
        for url in urls:
            for resolution_name, resolution in resolutions.items():
                width, height = resolution
                driver.set_window_size(width, height)
                driver.get(url)
                time.sleep(3)  
                save_screenshot(driver, browser_name, resolution_name, url)
    finally:
        driver.quit()

#Chrome Browser Testing
chrome_options = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
perform_test(chrome_driver, "Chrome")

#Firefox Browser Testing
firefox_options = webdriver.FirefoxOptions()
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
perform_test(firefox_driver, "Firefox")
