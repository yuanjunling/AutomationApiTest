# coding=utf-8
import json
from Driver.base_request import request
from Driver.handle_excle import handle
from Driver.handle_init import handle_ini


class RunMain:
    def run_case(self):
        #获取mock全部数据
        rootpath = handle_ini.get_value('rootpath')
        url = rootpath+"Data\case_01.xlsx"
        rows = handle.get_rows(url)
        for i in range(rows):
            data = handle.get_rows_value(url, i + 2)
            is_run = data[2]
            if is_run =='yes':
                method = data[6]
                log_url = data[5]
                json1 =eval(data[7])
                headers = eval(data[9])
                res=request.run_main(method, log_url, headers, json1)
                json_res = res
                json.dumps(json_res, indent=2, ensure_ascii=False)
        return json_res


run_case=RunMain()
if __name__=="__main__":
    run = RunMain()
    run.run_case()
