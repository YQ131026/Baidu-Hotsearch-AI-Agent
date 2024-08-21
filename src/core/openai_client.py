import openai
from config.settings import OPENAI_API_KEY, OPENAI_API_BASE

class OpenAIClient:
    def __init__(self):
        # 设置API密钥和自定义API基地址
        openai.api_key = OPENAI_API_KEY
        openai.api_base = OPENAI_API_BASE  # 设置自定义的API调用地址

    def complete(self, prompt, max_tokens=100):
        # 调用OpenAI API生成文本
        response = openai.Completion.create(
            engine="davinci",  # 选择模型
            prompt=prompt,  # 生成文本的提示
            max_tokens=max_tokens  # 设置最大生成文本长度
        )
        # 返回生成的文本
        return response.choices[0].text.strip()

