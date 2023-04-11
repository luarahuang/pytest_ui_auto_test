# import sys
# sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import logging
import os
from pathlib import Path
from util.time import formattime

class GetLogger():
    '''日志类封装'''
    def __init__(self):
        #创建日志器对象
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
    
    def console_handler(self):
        #创建一个终端日志处理器
        console_handler = logging.StreamHandler()
        #终端日志处理器格式
        console_handler.setFormatter(self.formatters()[0])
        console_handler.setLevel(logging.INFO)
        return console_handler
    
    def logfile_handler(self):
        #创建一个文件日志处理器
        logfile_handler = logging.FileHandler(filename=self.logfile_path(),mode='a',encoding='utf-8')
        #日志格式
        logfile_handler.setFormatter(self.formatters()[1])
        logfile_handler.setLevel(logging.INFO)
        return logfile_handler
    
    def logfile_path(self):
        #定义log文件存储位置和文件名称格式,文件以日期命名
        logfile_base_dir = './logs'
        logfile_path = Path(logfile_base_dir,'Log'+formattime("%Y%m%d")+'.log')
        return logfile_path
        
    
    def formatters(self):
        #定义日志输出格式
        console_formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)')
        filelog_formatter = logging.Formatter(fmt='%(levelname)s -%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d -  %(message)s')
        return console_formatter,filelog_formatter

    def log_handlers(self):
        #将终端和文件日志处理器都加入到创建日志器对象中，返回logger实例化对象
        self.logger.addHandler(self.console_handler())
        self.logger.addHandler(self.logfile_handler())
        return self.logger
    
if __name__ == '__main__':
    logger = GetLogger().log_handlers()
    logger.info('信息')
    logger.error('错误')
    logger.debug('调试')
    