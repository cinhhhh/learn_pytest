"""
@Time : 2022-08-08 11:25
@Author : admin
@Project : pytest_test
"""
import os
import logging
import time


class fileProcess:

    def get_root_path(self):
        """
        获取当前文件根目录
        :return: root_path
        """
        try:
            cur_path = os.path.abspath(os.path.dirname(__file__))
            logging.info('当前文件目录：{cur_path}'.format(cur_path=cur_path))
            root_path = cur_path[:cur_path.find("{}\\".format(cur_path)) + len("{}\\".format(cur_path))]
            logging.debug('当前文件的根路径：{root}'.format(root=root_path))
            roott = root_path.split('\\')[-1]
            logging.debug('根目录：{root}'.format(root=roott))
            return root_path
        except Exception as e:
            logging.error("错误信息：{error}".format(error=repr(e)))


class dataProcess:

    def read_data(self, filename, index):
        print("hello")

    def write_data(self, filename, index):
        pass


class timeProcess:

    def get_now_time(self):
        now = time.localtime()
        now_time = time.strftime("%Y%m%d", now)
        return now_time

if __name__ == '__main__':
    print(timeProcess().get_now_time())

