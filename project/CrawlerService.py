
class CrawlerService(object):
    def __init__(self, provider, transformer, send_msg, date):
        self.provider = provider
        self.transformer = transformer
        self.send_msg = send_msg
        self.date = date


    def get_stock_datas(self):
        for stock_type, stock_api_data in self.provider.get_html_data(self.date):
            stock = self.transformer.parse(stock_type, stock_api_data)
            print(stock_type, stock)
            print("="*70)