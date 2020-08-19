from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_cv_display_and_edit_cv(self):
        
        # 用户登录
        self.browser.get('http://localhost:8000/admin')
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('aabb')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('abababab')
        password.send_keys(Keys.ENTER)
        time.sleep(1)

        
        # 打开自己的 Django 项目的主页
        self.browser.get('http://localhost:8000')

        # 页面标题和头部内容中包含 Django 内容
        self.assertIn('Django', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Django', header_text)

        # 页面中有个链接，链接到简历页面
        cv_link = self.browser.find_element_by_id('mycv')
        self.assertEqual(cv_link.get_attribute('href'), 'http://localhost:8000/cv')


        # 点击 CV 页面链接，跳转到 CV 页面, 标题中包含 mycv 的内容
        cv_link.click()
        time.sleep(1)

        self.assertIn('mycv', self.browser.title)
        

        # 页面显示内容包含姓名 生日 联系电话 邮箱信息
        table = self.browser.find_element_by_id('base_info')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn('Name:', [row.text for row in rows])
        self.assertIn('Birth:', [row.text for row in rows])
        self.assertIn('Telephone:', [row.text for row in rows])
        self.assertIn('Email:', [row.text for row in rows])


        # 页面包含工作经历
        work_title = self.browser.find_element_by_id('work_title')
        self.assertIn('Work Experience', work_title.text)

        # 点击添加工作经历按钮，跳转到添加页面
        add_link = self.browser.find_element_by_id('add_work_exp')
        add_link.click()
        time.sleep(1)
        h2s = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('New workexp', [h2.text for h2 in h2s])

        # 页面上有输入框和文本框共四个需要填写的内容 
        start_time = self.browser.find_element_by_id('id_startTime')
        end_time = self.browser.find_element_by_id('id_endTime')
        company = self.browser.find_element_by_id('id_company')
        desc = self.browser.find_element_by_id('id_desc')



        # 输入工作经历的开始时间 
        start_time.send_keys('2020-02-02')

        # 输入工作经历的结束时间 
        end_time.send_keys('2020-08-02')

        # 输入工作经历的内容 
        company.send_keys('google')

        # 输入公司名称
        desc.send_keys('work as a tester')

        # 点击提交按钮
        submit_btn = self.browser.find_element_by_id('submit')
        submit_btn.click()
        time.sleep(3)

        # 回到简历页面，显示刚输入的工作经历
        paragraphs = self.browser.find_elements_by_tag_name('p')
        
        self.assertIn('Company: google', [p.text for p in paragraphs])
        self.assertIn('work as a tester', [p.text for p in paragraphs])




if __name__ == '__main__':
    unittest.main()