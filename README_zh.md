# Baidu Hotsearch AI Agent

一个用于自动抓取、处理、翻译并发送百度热搜数据的Python代理程序。该程序帮助您获取最新热门话题，并将其翻译为中英双语后，通过电子邮件发送到指定的收件人。

## 项目结构

```plaintext
baidu-hotsearch-ai-agent/
├── config/
│   └── settings.py           # 配置文件
│   └── settings.py.example   # 配置示例文件
├── data/
│   └── logs/                 # 日志文件存放目录
├── src/
│   ├── agent/
│   │   ├── baidu_scraper.py       # 百度热搜抓取代码
│   │   ├── data_cleaner.py        # 数据清洗代码
│   │   ├── task_scheduler.py      # 任务调度代码
│   │   └── openai_translation.py  # OpenAI 翻译功能
│   ├── core/
│   │   ├── email_sender.py        # 邮件发送代码
│   │   ├── logging.py             # 日志处理代码
│   └── main.py                    # 主程序入口
├── requirements.txt               # 依赖文件
└── README.md                      # 项目说明文件
```

## 快速开始

1. **创建虚拟环境并激活**：

    ```bash
    python3 -m venv hotsearch
    source hotsearch/bin/activate
    ```

2. **进入项目目录并安装依赖**：

    ```bash
    git clone git@github.com:YQ131026/Baidu-Hotsearch-AI-Agent.git
    cd Baidu-Hotsearch-AI-Agent/
    pip install -r requirements.txt

3. **后台运行主程序**：

    ```bash
    nohup python src/main.py > output.log 2>&1 &
    ```

## 说明

- **配置文件**：`config/settings.py` 包含所有项目运行所需的配置。可根据 `settings.py.example` 文件进行自定义设置。
- **日志文件**：所有运行日志将保存到 `data/logs/` 目录中。
- **后台运行**：使用 `nohup` 命令可以使程序在后台运行，并将输出记录到 `output.log` 中。


