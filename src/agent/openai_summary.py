import openai
from config.settings import OPENAI_API_KEY, OPENAI_API_BASE
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class OpenAISummary:
    def __init__(self):
        # 设置API密钥和自定义API基地址
        openai.api_key = OPENAI_API_KEY
        openai.api_base = OPENAI_API_BASE  # 设置自定义的API调用地址

        # 创建一个自定义的requests会话
        self.session = requests.Session()

        # 设置超时和重试策略
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        # 将自定义会话设置为openai的默认会话
        openai.requestssession = self.session

    def generate_summary(self, data):
        # 设置超时为300秒
        timeout = 300

        try:
            # 使用OpenAI API生成热搜摘要
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # 使用对话模型
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": self._build_prompt(data)}
                ],
                max_tokens=150,
                timeout=timeout  # 这里设置超时为300秒
            )
            # 从API响应中提取生成的摘要文本
            summary = response.choices[0].message['content'].strip()
            return summary
        except requests.exceptions.Timeout:
            print("The request to OpenAI API timed out.")
            return "Error: The request to OpenAI API timed out."
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while connecting to OpenAI API: {e}")
            return f"Error: {str(e)}"

    def _build_prompt(self, data):
        # 构建一个提示文本，包含所有清洗后的热搜条目
        prompt = "Generate a concise summary for the following Baidu hotsearch topics:\n"
        for i, item in enumerate(data, 1):
            prompt += f"{i}. {item}\n"
        return prompt

