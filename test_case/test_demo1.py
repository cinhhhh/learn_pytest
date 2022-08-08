"""  
@Project : pytest_study  
@Time    : 2020/8/5 
@Auth    : duan
"""

import pytest
import public_method as pm
import logging


def fun1(x):
    return x+1

def test_funn1():
    logging.debug('这是一条测试信息')
    pm.read_data()
    assert fun1(1) == 3, "判断失败"

if __name__ == '__main__':
    pytest.main(['-s', 'test_demo1.py'])