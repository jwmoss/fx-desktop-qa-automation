# This test searches for soccer tricks on TikTok.

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test(unittest.TestCase):
    def setUp(self):
        # Create a new instance of the browser
        self.options = Options()

        # Firefox Location
        # options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"

        # Nightly Location
        self.options.binary_location = "/Applications/Firefox Nightly.app/Contents/MacOS/firefox-bin"

        # self.options.add_argument("-headless")

        self.driver = webdriver.Firefox(options=self.options)

        # Remove navigator.webdriver Flag using JavaScript to avoid bot detection by TikTok
        # NOTE: This doesn't work. TikTok has a puzzle piece captcha against search results.
        # self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def test_new_tab(self):

        print(" - TEST: Verify a user can search on TikTok")
        try:
            # Navigate to Amazon
            test_url = "https://www.tiktok.com"
            self.driver.get(test_url)
            WebDriverWait(self.driver, 10).until(EC.url_contains("https://www.tiktok.com"))

            # Verify the Amazon page is loaded
            WebDriverWait(self.driver, 10).until(EC.title_contains("videos on TikTok"))
            page_title = self.driver.title
            self.assertEqual(page_title, "Explore - Find your favourite videos on TikTok")
            print("Title of the web page is: " + page_title)

            # Find the search input field and enter "soccer tricks"
            # CSS SELECTOR: .tiktok-1yf5w3n-InputElement
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tiktok-1yf5w3n-InputElement"))
            )
            time.sleep(2)
            search_input.send_keys("soccer tricks", Keys.RETURN)

            # Wait for the search results to load
            # CSS SELECTOR: #search_user-item-user-link-0 > a:nth-child(2) > p:nth-child(3) > strong:nth-child(1)
            # XPATH: /html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/a[2]/p[2]/strong
            item_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/a[2]/p[2]/strong")))
            item_element_text = item_element.text
            print("Element found by class name:", item_element_text)
            self.assertIn("Soccer trick", item_element_text)

            time.sleep(2)

        finally:
            # Close the browser after the test is complete
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()