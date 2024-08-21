from agent.task_scheduler import TaskScheduler

if __name__ == "__main__":
    # 创建并启动任务调度器
    scheduler = TaskScheduler()
    
    # 开始定时任务，每隔一小时执行一次
    scheduler.schedule_task()

