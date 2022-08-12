"""
@Time : 2022-08-12 9:46
@Author : duan
@Project : pytest_test
"""

import logging
import time
import datetime
import os
import colorlog  # 日志颜色

log_colors_config = {
    'DEBUG': 'bg_white',
    'INFO': 'green',
    'WARNING': 'bg_yellow',
    'ERROR': 'bg_red',
    'CRITICAL': 'red',
}


class ConsoleLog:
    def __init__(self):
        """
        日志格式化，输出级别设置
        """
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s]  [%(levelname)s]- %(message)s',

            log_colors=log_colors_config
        )

    def TimeStampToTime(self, timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    def __console(self, level, message):
        """
        创建streamHandler,输出日志信息到控制台
        :param level: 日志级别
        :param message: 日志信息
        :return: None
        """
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    pass