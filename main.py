# -*- coding: utf-8 -*-
# 固定写法，导入相关类库和函数
from util import WoxEx, WoxAPI, load_module, Log

# 统一加载模块
with load_module():
    import pyperclip
    import datetime
    import sys, time


class Main(WoxEx):  # 继承WoxEx

    def query(self, keyword):
        try:
            timestamp = int(time.time())
            if keyword in ['', ' ', 'n', 'now']:
                pass
            else:
                try:
                    ts = time.strptime(keyword, "%Y-%m-%d %H:%M:%S")
                    timestamp = int(time.mktime(ts))
                except Exception as e:
                    timestamp = int(keyword)
            values = [str(timestamp),
                datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            ]

            results = list()
            for val in values:
                results.append({
                    "Title": val,
                    "SubTitle": None,
                    "IcoPath": "Images/ico.ico",
                    "JsonRPCAction": {
                        "method": "clip_copy",
                        "parameters": [val],
                        "dontHideAfterAction": False
                    }
                })
            return results

        except Exception as e2:
            return [{
                "Title": "出现错误，请检查输入",
                "SubTitle": "错误信息：" + str(e2),
                "IcoPath": "Images/ico.ico"
            }]

    def clip_copy(self, keyword):
        pyperclip.copy(keyword)


if __name__ == "__main__":
    Main()