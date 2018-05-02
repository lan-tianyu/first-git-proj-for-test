# -*- coding:UTF8 -*-

import logging
import logging.config
import uuid

class Logger(object):
    '''
    @note:日志处理对象,对logging的封装
    在有多个相互关联的文件都需要用到python的日志系统时，不要用默认的root logger。因为所有的名称都会继承root导致重复打印，用logger时一定要起名字
    '''
    def __init__(self, logName, logLevel):
        logger = "logger_" + str(uuid.uuid4())
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logName)  
        fh.setLevel(logLevel) 
        
        # 再创建一个handler，用于输出到控制台  
        ch = logging.StreamHandler()  
        ch.setLevel(logLevel)  
  
        # 定义handler的输出格式  
        self.formatstr = '[%(asctime)s] [pid:%(process)d] [%(filename)s:%(lineno)d] [%(funcName)s] %(levelname)s: %(message)s'
        log_format = logging.Formatter(self.formatstr)
        fh.setFormatter(log_format)  
        ch.setFormatter(log_format)  
  
        # 给logger添加handler  
        self.logger.addHandler(fh)  
        self.logger.addHandler(ch)  
     
    def init_logger(self):  
        return self.logger

