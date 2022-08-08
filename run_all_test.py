import pytest
import os



path = os.path.dirname(__file__)
path = path + "/report/"
pytest.main(["-s","--alluredir={}".format(path),"test_case"])#运行 test_case下所有测试用例



pytest.main(["-s", "--alluredir=report", "test_case"] )  # 运行 cases下所有测试用例
result = os.system(r"allure serve {}".format(path))
print("result={}".format(result))