project_name = "StockData"

settings = {
    "provider":{
        "tse": "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={y}{m}{d}&type=ALLBUT0999",
        "otc": "https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyQuotes?date={y}/{m}/{d}&id=&response=json",
    },
    "transformer":{
    }
}