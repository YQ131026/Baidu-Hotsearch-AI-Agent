# Baidu Hotsearch AI Agent

A Python-based agent that automatically fetches, processes, translates, and emails the latest Baidu hotsearch data. This tool helps keep you updated with trending topics in China by providing bilingual (Chinese and English) summaries delivered straight to your inbox.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
  - [Configuring `settings.py`](#configuring-settingspy)
- [Usage](#usage)
  - [Running the Agent](#running-the-agent)
  - [Scheduling Tasks](#scheduling-tasks)
- [Logging](#logging)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

---

## Features

- **Automated Data Fetching**: Retrieves the latest real-time hotsearch data from Baidu.
- **Data Cleaning**: Processes and cleans the raw data for consistency and readability.
- **Bilingual Translation**: Utilizes OpenAI's API to translate hotsearch topics into English alongside the original Chinese.
- **Email Notifications**: Sends formatted emails containing the latest hotsearch topics to specified recipients.
- **Robust Logging**: Maintains detailed logs of operations, ensuring easy debugging and monitoring.
- **Configurable Scheduling**: Allows users to set intervals for automatic data fetching and emailing.

---

## Project Structure

```plaintext
Baidu-Hotsearch-Agent/
├── config/
│   ├── settings.py           # Main configuration file
│   └── settings.py.example   # Example configuration template
├── data/
│   └── logs/                 # Directory for log files
├── src/
│   ├── agent/
│   │   ├── baidu_scraper.py        # Module for fetching Baidu hotsearch data
│   │   ├── data_cleaner.py         # Module for cleaning fetched data
│   │   ├── openai_translation.py   # Module for translating data using OpenAI API
│   │   └── task_scheduler.py       # Module for scheduling and orchestrating tasks
│   ├── core/
│   │   ├── email_sender.py         # Module for sending emails
│   │   └── logger.py               # Module for logging operations
│   └── main.py                     # Entry point for running the agent
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **OpenAI API Key**: Acquire an API key by signing up at [OpenAI](https://openai.com/).
- **SMTP Email Account**: An email account configured to send emails via SMTP. Gmail, for example, can be configured for this purpose.

---

## Installation

Follow these steps to set up and run the Baidu Hotsearch Agent on your local machine.

### 1. Clone the Repository

```bash
git clone git clone git@github.com:YQ131026/Baidu-Hotsearch-AI-Agent.git
cd Baidu-Hotsearch-AI-Agent
```

### 2. Create a Virtual Environment (Optional but Recommended)

**Using `venv`:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the agent, you need to configure the necessary settings.

### Setting Up Environment Variables

It's recommended to store sensitive information such as API keys and passwords as environment variables.

**On Linux/MacOS:**

```bash
export OPENAI_API_KEY='your_openai_api_key'
export EMAIL_PASSWORD='your_email_password'
```

**On Windows:**

```cmd
set OPENAI_API_KEY=your_openai_api_key
set EMAIL_PASSWORD=your_email_password
```

### Configuring `settings.py`

1. **Create `settings.py` from the example template:**

   ```bash
   cp config/settings.py.example config/settings.py
   ```

2. **Edit `config/settings.py`** with your preferred text editor and update the configurations accordingly.

**`config/settings.py` Example:**

```python
import os

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

# Baidu Hotsearch URL
BAIDU_HOTSEARCH_URL = "https://top.baidu.com/board?tab=realtime"

# Logging Configuration
LOG_FILE_PATH = os.path.join(os.getcwd(), "data/logs/agent.log")

# Task Scheduling Configuration
SCHEDULE_INTERVAL = 3600  # Time in seconds between each fetch (default: 1 hour)

# Email Configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVERS = ["receiver1@example.com", "receiver2@example.com"]
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_email_password")
```

**Configuration Parameters Description:**

- `OPENAI_API_KEY`: Your OpenAI API key for accessing translation services.
- `OPENAI_API_BASE`: Base URL for the OpenAI API; usually defaults to `https://api.openai.com/v1`.
- `BAIDU_HOTSEARCH_URL`: The URL from which to fetch Baidu hotsearch data.
- `LOG_FILE_PATH`: File path where logs will be stored.
- `SCHEDULE_INTERVAL`: Time interval (in seconds) between each automated task execution.
- `SMTP_SERVER`: Your email service provider's SMTP server address.
- `SMTP_PORT`: Port number for the SMTP server (commonly 587 for TLS).
- `EMAIL_SENDER`: The email address that will send the hotsearch reports.
- `EMAIL_RECEIVERS`: A list of recipient email addresses.
- `EMAIL_PASSWORD`: Password or app-specific password for the sender email account.

**Note:** Ensure all configurations, especially email and API credentials, are correctly set to avoid runtime errors.

---

## Usage

### Running the Agent

After configuring the settings and installing dependencies, run the agent using:

```bash
python src/main.py
```

**Expected Output:**

```
========== Task Execution Started ==========
[Step 0] Current China Date: 今日2024年08月21日
[Step 1] Fetching Baidu hotsearch data...
[Step 1] Fetched 50 items from Baidu.
[Step 2] Cleaning data...
[Step 2] Cleaned Baidu data contains 50 items.
[Step 3] Baidu Hotsearch Content:
1. 热搜话题1
2. 热搜话题2
...
[Step 4] Translating content to Chinese and English...
[Step 4] Translation completed successfully.
[Step 5] Translated Baidu Hotsearch Content:
1. 热搜话题1
   Hotsearch Topic 1
2. 热搜话题2
   Hotsearch Topic 2
...
[Step 6] Content formatted successfully.
Log directory already exists: /path/to/Baidu-Hotsearch-Agent/data/logs
[Step 7] Logging translation...
[Step 7] Translation logged.
[Step 8] Sending email with translated content...
[Step 8] Email sent successfully.
========== Task Execution Completed ==========
```

### Scheduling Tasks

The agent is designed to run continuously, fetching and emailing hotsearch data at intervals defined by `SCHEDULE_INTERVAL` in `settings.py`.

**To run the agent continuously:**

```bash
python src/main.py
```

**To run the agent in the background (Linux/MacOS):**

```bash
nohup python src/main.py &
```

**Using Task Schedulers:**

For more control over scheduling, consider using system schedulers like `cron` (Linux/MacOS) or Task Scheduler (Windows).

---

## Logging

- **Log File Path**: Logs are stored in the path specified by `LOG_FILE_PATH` in your `settings.py`.
- **Automatic Directory Creation**: If the log directory does not exist, it will be automatically created when the agent runs.
- **Log Contents**: Logs include timestamps and detailed information about each step of the process, including errors and successful operations.

**Sample Log Entry:**

```
[2024-08-21 10:00:00] INFO: Task Execution Started
[2024-08-21 10:00:05] INFO: Fetched 50 items from Baidu.
[2024-08-21 10:00:10] INFO: Cleaned Baidu data contains 50 items.
[2024-08-21 10:00:30] INFO: Translation completed successfully.
[2024-08-21 10:00:35] INFO: Content formatted successfully.
[2024-08-21 10:00:36] INFO: Translation logged.
[2024-08-21 10:00:40] INFO: Email sent successfully.
[2024-08-21 10:00:41] INFO: Task Execution Completed
```

