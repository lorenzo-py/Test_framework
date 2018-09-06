import time, sys
import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from test.suit import myunit
from test.pages.LoginPage import *


class TestBaiDu(myunit.BaseTest):
    '''百度页面简单测试'''
    def test_search(self):
        '''循环搜索测试'''
        try:
            page = LoginPage(self.driver)
            self.excel = DATA_PATH + '/baidu.xlsx'
            datas = ExcelReader(self.excel).data
            for d in datas:
                page.search01(d['search'])
                time.sleep(2)
                links = page.find_elements(*page.locator_result)
                for link in links:
                    logger.info(link.text)
                self.driver.back()
                time.sleep(1)
        except Exception as e:
            self.driver.get_screenshot_as_file(REPORT_PATH+'\\images\\%s.png'%(sys._getframe().f_code.co_name))
            raise

    def test_search_01(self):
        '''点击测试'''
        try:
            page = LoginPage(self.driver)
            page.search01('csdn')
            time.sleep(2)
            page.find_element(*page.locator_csdn).click()
            time.sleep(5)
            assert u'csdn_百度搜索' in self.driver.title
        except Exception as e:
            self.driver.get_screenshot_as_file(REPORT_PATH+'\\images\\%s.png'%(sys._getframe().f_code.co_name))
            raise


if __name__ == '__main__':
    unittest.main()