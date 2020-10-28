# coding=utf-8
import json


class OperationJson:
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = 'E:\AutomationApiTest\Config\Json_Ui_Data_Register'
        self.data = self.get_data()

    def get_data(self):
        fp = open(self.file_name)
        data = json.load(fp)
        fp.close()
        return data

    def get_value(self, id):
        return self.data[id]


if __name__ == '__main__':
    opers = OperationJson()

