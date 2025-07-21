import datetime
import os
import time


# 修改 settings.py 文件
def update_settings(start_date, end_date):
    with open('weibo/settings.py', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('weibo/settings.py', 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith('START_DATE'):
                file.write(f"START_DATE = '{start_date}'\n")
            elif line.startswith('END_DATE'):
                file.write(f"END_DATE = '{end_date}'\n")
            else:
                file.write(line)
    print(f"Updated settings: START_DATE={start_date}, END_DATE={end_date}")


# 自动生成时间区间并运行爬虫
# start_date = datetime.date(2024, 1, 1)
# start_date = datetime.date(2021, 7, 1)
start_date = datetime.date(2021, 10, 11)
end_date = datetime.date(2025, 3, 17)
delta = datetime.timedelta(days=1)  # 每次爬取的时间间隔
next_date = start_date

# 创建日志目录
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

while start_date <= end_date:
    # 更新 settings.py 文件
    update_settings(start_date, next_date)

    # 定义日志文件名
    log_file = os.path.join(log_dir, f"{start_date}_to_{next_date}.log")

    # 运行爬虫命令，并将日志输出到文件
    print(f"Running spider for {start_date} to {next_date}...")
    os.system(f"scrapy crawl search -s JOBDIR=crawls/search -s LOG_FILE={log_file}")
    time.sleep(1)
    # 更新开始日期
    next_date += delta
    start_date = next_date
