"""
@auth: duan
"""


import pytest
import logging



class Test_test:
    def setup(self):
        print('-----------this is a new test_case example--------------')

    def teardown(self):
        print('-------------this test_case is done--------------')

    # @pytest.mark.skip  跳过该条用例
    def test01(self):
        log = logging.getLogger('test1')
        log.debug("debug msg ")
        print('this is test01')

    def test02(self):
        print('this is test02')

    # @pytest.mark.run(order=1)   用例执行顺序
    def test03(self):
        print('this is test03')

if __name__ == '__main__':
    pytest.main(['-s', 'test_demo2.py'])