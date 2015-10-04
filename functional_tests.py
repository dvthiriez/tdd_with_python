from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # David has heard about a cool new online to-do app. He goes
        # to check out tits homepage
        self.browser.get('http://192.168.1.17:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Change to stock exhaust on MSM for smog check" into
        # a text box (David has to get his car smogged in the next week)

        # When he hits enter, the page updates, and now a the page lists
        # "1: Change to stock exhaust on MSM for smog check" as an item in
        # to-do list

        # There is still a text box inviting her to add another item. He
        # enters "Take car to smog check station"

        # The page updates again, and now shows both items on his list

        # David wonders whether the site will remember his list. Then he see
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
