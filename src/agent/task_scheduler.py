import time
import os
from datetime import datetime
import pytz
from agent.baidu_scraper import BaiduScraper
from agent.data_cleaner import DataCleaner
from agent.openai_translation import OpenAITranslation
from core.logging import Logger
from core.email_sender import EmailSender
from config.settings import BAIDU_HOTSEARCH_URL, SCHEDULE_INTERVAL, LOG_FILE_PATH

class TaskScheduler:
    def __init__(self):
        # 检查并创建日志目录
        self.ensure_log_directory_exists(LOG_FILE_PATH)
        
        # 初始化各个模块
        self.baidu_scraper = BaiduScraper(BAIDU_HOTSEARCH_URL)
        self.cleaner = DataCleaner()
        self.translator = OpenAITranslation()
        self.logger = Logger()
        self.email_sender = EmailSender()

    def ensure_log_directory_exists(self, log_file_path):
        log_dir = os.path.dirname(log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"Log directory created: {log_dir}")
        else:
            print(f"Log directory already exists: {log_dir}")

    def schedule_task(self):
        # 定期调度任务
        while True:
            self.run_task()
            time.sleep(SCHEDULE_INTERVAL)

    def run_task(self):
        print("========== Task Execution Started ==========")
        try:
            # 获取中国标准时间的当前日期
            current_date = self.get_china_date()
            print(f"[Step 0] Current China Date: {current_date}")

            # 1. 抓取百度热搜数据
            print("[Step 1] Fetching Baidu hotsearch data...")
            baidu_raw_data = self.baidu_scraper.get_hot_searches()
            print(f"[Step 1] Fetched {len(baidu_raw_data)} items from Baidu.")

            # 2. 清洗数据
            print("[Step 2] Cleaning data...")
            baidu_cleaned_data = self.cleaner.clean_data(baidu_raw_data)
            print(f"[Step 2] Cleaned Baidu data contains {len(baidu_cleaned_data)} items.")

            # 3. 控制台打印清洗后的百度热搜内容
            print("[Step 3] Baidu Hotsearch Content:")
            for idx, item in enumerate(baidu_cleaned_data, 1):
                print(f"{idx}. {item}")

            # 4. 翻译内容为中英双语
            print("[Step 4] Translating content to Chinese and English...")
            translated_baidu_content = self.translator.translate_to_bilingual(baidu_cleaned_data)
            print("[Step 4] Translation completed successfully.")

            # 5. 控制台打印翻译后的中英双语内容
            print("[Step 5] Translated Baidu Hotsearch Content:")
            for idx, item in enumerate(translated_baidu_content, 1):
                print(f"{idx}. {item['chinese']}\n   {item['english']}")

            # 6. 格式化邮件内容
            formatted_content = self.format_email_content(current_date, translated_baidu_content)
            print("[Step 6] Content formatted successfully.")

            # 7. 记录日志
            print("[Step 7] Logging translation...")
            self.logger.log(formatted_content)
            print("[Step 7] Translation logged.")

            # 8. 发送邮件，内容为翻译后的内容
            print("[Step 8] Sending email with translated content...")
            self.email_sender.send_email("Baidu Hotsearch Bilingual Translation", formatted_content)
            print("[Step 8] Email sent successfully.")
        except Exception as e:
            # 如果有错误发生，记录错误信息并输出到控制台
            error_message = f"Error during task execution: {str(e)}"
            print(error_message)
            self.logger.log(error_message)
        print("========== Task Execution Completed ==========\n")

    def get_china_date(self):
        # 获取中国标准时间的当前日期，格式为 "今日X年X月X日"
        china_tz = pytz.timezone('Asia/Shanghai')
        china_date = datetime.now(china_tz).strftime('今日%Y年%m月%d日')
        return china_date

    def format_email_content(self, current_date, translated_baidu_content):
        formatted = f"### Baidu Hotsearch Bilingual Translation\n\n"
        formatted += f"**China Date:** {current_date}\n\n"
        
        formatted += f"**Baidu Hotsearch:**\n"
        for idx, item in enumerate(translated_baidu_content, 1):
            formatted += f"{idx}. {item['chinese']}\n   {item['english']}\n"
        
        return formatted

