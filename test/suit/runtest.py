import unittest
import time
import yagmail
import os
from HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PATH,Config

sender = Config().myget('sender')
password = Config().myget('password')
host = Config().myget('host')
receiver = Config().myget('receiver')

test_dir_0 = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
test_dir = os.path.join(test_dir_0,'case')
now = time.strftime('%Y-%m-%d %H-%M-%S')
filename=REPORT_PATH + '\\web_report_%s.html' % now


if __name__ == '__main__':

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='GS70REPORT', description='环境：win10 浏览器：chrome')
        runner.run(discover)

    yag = yagmail.SMTP(user=sender, password=password, host=host)
    contents = ['HELLO EVERYONE:\nTHIS IS GS70 REPORT!']
    yag.send(to=receiver, subject='自动化-青衣py', contents=contents, attachments=[filename], cc=sender)