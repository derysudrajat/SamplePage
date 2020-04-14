import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_id('row_todo')
        self.assertIn(row_text, [row.tex for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/todolist/')

        self.assertIn('Todo-List | Dery Sudrajat', self.browser.title)
        header_text = self.browser.find_element_by_id('header_text')
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('id_new_item'),
            'Do you want to create new Todo Dery?'
        )

        inputbox.send_keys('Jangan lupa tugas SCM')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        self.check_for_row_in_list_table('1 Jangan lupa tugas SCM')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Jangan lupa tugas Agile juga')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        self.check_for_row_in_list_table('2 Jangan lupa tugas Agile juga')
        self.check_for_row_in_list_table('1 Jangan lupa tugas SCM')

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warning='ignore')
