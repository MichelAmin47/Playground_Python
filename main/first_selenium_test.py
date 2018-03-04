from main.browserControl.browserFactory import BrowserFactory

driver = BrowserFactory().get_chrome_driver

driver.maximize_window()

driver.get("https://www.nu.nl")

driver.quit()
