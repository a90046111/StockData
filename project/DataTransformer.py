import re


class DataTransformer():
    def __init__(self, send_msg, settings):
        self.send_msg = send_msg
        self.settings = settings

    def parse(self, stock_type, stock_api_data):
        try:
            data = []
            if stock_type == "tse":
                data = self.get_tse_stock_data(stock_api_data)
            elif stock_type == "otc":
                data = self.get_otc_stock_data(stock_api_data)

        except:
            self.send_msg()
        return data


    def get_tse_stock_data(self, stock_api_data): #上市股票資料
        stock_data_list = []
        for stock_details in stock_api_data["tables"]:
            if "每日收盤行情" not in stock_details.get("title", ""): continue
            for stock_detail in stock_details["data"]:
                try:
                    stock_data_list.append({
                        "證卷代號": stock_detail[0], #證卷代號
                        "證券名稱": stock_detail[1], #證券名稱
                        "成交股數": stock_detail[2], #成交股數
                        "成交筆數": stock_detail[3], #成交筆數
                        "成交金額": stock_detail[4], #成交金額
                        "開盤價": stock_detail[5], #開盤價
                        "最高價": stock_detail[6], #最高價
                        "最低價": stock_detail[7], #最低價
                        "收盤價": stock_detail[8], #收盤價
                        "價差": re.search(r'>(.*?)<', stock_detail[9]).group(1)+stock_detail[10],
                        "本益比":stock_detail[15] , #本益比
                    })
                except:
                    self.send_msg(msg=stock_detail)
        return stock_data_list


    def get_otc_stock_data(self, stock_api_data):#上櫃股票資料
        stock_data_list = []
        for stock_detail in stock_api_data["tables"][0]["data"]:
            try:
                stock_data_list.append({
                    "代號": stock_detail[0],
                    "名稱": stock_detail[1],
                    "收盤": stock_detail[2],
                    "漲跌": stock_detail[3],
                    "開盤": stock_detail[4],
                    "最高": stock_detail[5],
                    "最低": stock_detail[6],
                    "均價": stock_detail[7],
                    "成交股數": stock_detail[8],
                    "成交金額(元)": stock_detail[9],
                    "成交筆數": stock_detail[10],
                })
            except:
                self.send_msg(msg=stock_detail)
        return stock_data_list