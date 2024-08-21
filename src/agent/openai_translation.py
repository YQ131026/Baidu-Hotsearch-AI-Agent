import openai
from config.settings import OPENAI_API_KEY, OPENAI_API_BASE
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class OpenAITranslation:
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

    def translate_to_bilingual(self, data):
        # 设置超时为300秒
        timeout = 300
        translations = []

        try:
            for item in data:
                # 使用OpenAI API将内容翻译为中英双语
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",  # 使用对话模型
                    messages=[
                        {"role": "system", "content": "You are a translator."},
                        {"role": "user", "content": f"Translate the following text to Chinese and English, and separate the two translations with a '|' symbol:\n{item}"}
                    ],
                    max_tokens=150,
                    timeout=timeout  # 这里设置超时为300秒
                )
                # 从API响应中提取生成的翻译文本
                translation = response.choices[0].message['content'].strip()
                
                # 尝试用 '|' 分隔翻译结果
                if '|' in translation:
                    chinese, english = translation.split("|", 1)
                    translations.append({"chinese": chinese.strip(), "english": english.strip()})
                else:
                    # 如果没有 '|' 分隔符，假设返回的第一个句子为中文，第二个句子为英文
                    lines = translation.split("\n")
                    if len(lines) >= 2:
                        translations.append({"chinese": lines[0].strip(), "english": lines[1].strip()})
                    else:
                        # 如果格式不匹配，记录为错误
                        translations.append({"chinese": "Error: Invalid Translation Format", "english": translation})
                        
            return translations
        except requests.exceptions.Timeout:
            print("The request to OpenAI API timed out.")
            return [{"chinese": "Error: Timeout", "english": "Error: Timeout"}]
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while connecting to OpenAI API: {e}")
            return [{"chinese": "Error: Request Failed", "english": str(e)}]

