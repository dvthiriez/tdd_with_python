from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_rows_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # David has heard about a cool new online to-do app. He goes
        # to check out tits homepage
        self.browser.get('http://192.168.1.17:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Change to stock exhaust on MSM for smog check" into
        # a text box (David has to get his car smogged in the next week)
        inputbox.send_keys('Change to stock exhaust on MSM for smog check')

        # When he hits enter, the page updates, and now a the page lists
        # "1: Change to stock exhaust on MSM for smog check" as an item in
        # to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_rows_in_list_table('1: Change to stock exhaust on MSM for smog check')

        # There is still a text box inviting her to add another item. He
        # enters "Take car to smog check station"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Take car to smog check station')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.check_for_rows_in_list_table('1: Change to stock exhaust on MSM for smog check')
        self.check_for_rows_in_list_table('2: Take car to smog check station')

        # David wonders whether the site will remember his list. Then he see
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
