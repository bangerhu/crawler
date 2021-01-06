# 入口方法

from apscheduler.schedulers.blocking import BlockingScheduler

import btc.crawler as crawler

# 实例化一个调度器
scheduler = BlockingScheduler()

# 添加任务并设置触发方式为3s一次
scheduler.add_job(crawler.crawler, 'interval', hours=1)

# 开始运行调度器
scheduler.start()
