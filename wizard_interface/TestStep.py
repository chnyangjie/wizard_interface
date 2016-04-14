# coding=utf-8
'''
@author yangjie
'''


class BaseTestStep():

    def __init__(self, logger):
        self.set_logger(logger)

    def set_logger(self, logger):
        self.logger = logger

    def set_logger_level(self, logger_level="INFO"):
        self.logger.setLevel(logger_level)

    def request(self):
        pass

    def execute(self):
        pass

    def _read_result(self):
        pass

    def get_data(self):
        pass

    def _get_data_from_file(self):
        pass

    def _get_data_from_dict(self):
        pass

    def _get_data_from_list(self):
        pass
