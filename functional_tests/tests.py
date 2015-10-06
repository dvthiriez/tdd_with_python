from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

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
        self.browser.get(self.live_server_url)

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

        # When he hits enter, he is taken to a new URL, and now a the page
        # lists "1: Change to stock exhaust on MSM for smog check" as an
        # item in to-do list
        inputbox.send_keys(Keys.ENTER)
        david_list_url = self.browser.current_url
        self.assertRegex(david_list_url, '/lists/.+')
        self.check_for_rows_in_list_table('1: Change to stock exhaust on MSM for smog check')

        # There is still a text box inviting her to add another item. He
        # enters "Take car to smog check station"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Take car to smog check station')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.check_for_rows_in_list_table('1: Change to stock exhaust on MSM for smog check')
        self.check_for_rows_in_list_table('2: Take car to smog check station')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of David's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of David's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Change to stock exhaust on MSM for smog check', page_text)
        self.assertNotIn('Take car to smog check station', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, david_list_url)

        # Again, there is no trace of David's list
        page_text = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('Change to stock exhaust on MSM for smog check', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep

