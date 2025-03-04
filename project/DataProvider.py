import requests

class DataProvider(object):
    def __init__(self, send_msg, settings):
        self.send_msg = send_msg
        self.settings = settings


    def get_html_data(self, date):
        y, m, d = date.split("-")
        date_config = {"y": y, "m": m, "d": d}
        for stock_type, url_config in self.settings.items():
            try:
                url = url_config.format(**date_config)
                stock_api_data = requests.get(url).json()
                yield stock_type, stock_api_data
            except:
                self.send_msg(msg=f"stock_type: {stock_type}")
