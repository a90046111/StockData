import DataProvider
import AppSettings
import DataTransformer
import CrawlerService
import traceback
from pathlib import Path
from datetime import datetime
import sys

def send_msg(msg = "", level = "Error"):
    color = {
        "Information":"97", #白
        "Error": "91", #紅
        "Warning": "91", #紅
        "Critical": "94", #藍
        "Trace": "94", #藍
        "Debug": "94", #藍
    }
    sys_log = traceback.format_exc()
    send_message = msg if sys_log == "NoneType: None\n" else f"{msg}\n{sys_log}"
    print(f"\033[{color[level]}m{level}: {send_message}\033[0m")

def get_version():
    """使用最後一個更新的.py來當作版本
    Returns:
        str: "2025-03-04 15:20:52"
    """
    subdir = Path.cwd() / "project"
    return (max([datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S') for file in subdir.iterdir()]))


def main():
    """需額外在TERMINAL輸入的參數為日期, 可以得到該日期的股票基本訊息
    """
    try:
        date = sys.argv[1]
        version = get_version()
        project_name = AppSettings.project_name
        settings = AppSettings.settings
        send_msg(msg=f"{project_name} starts, version is {version}", level="Information")
        provider = DataProvider.DataProvider(send_msg, settings["provider"])
        transformer = DataTransformer.DataTransformer(send_msg, settings["transformer"])
        CrawlerService.CrawlerService(provider, transformer, send_msg, date).get_stock_datas()
    except:
        send_msg()
        return

if __name__ == "__main__":
    main()