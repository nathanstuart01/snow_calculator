from crontab import CronTab 

my_cron = CronTab(user='jessicastuart')

crawl_cron = my_cron.new(
	command='/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/jessicastuart/desktop/nathan-code/python_work/snow_calculator/utahskiareas/gather_snow_stats.py')

crawl_cron.setall('16 8 * * *')

my_cron.write()