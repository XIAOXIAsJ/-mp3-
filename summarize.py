import os
from openai import OpenAI

with open("transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://bala-ai.cc"
)

response = client.responses.create(
    model="gpt-5.5",
    input=[
        {
            "role": "system",
            "content": "你是一个听课总结助手，请用中文整理重点，不要编造内容。"
        },
        {
            "role": "user",
            "content": f"""
请根据以下课堂转写内容生成总结，包含：
1. 一句话摘要
2. 核心知识点
3. 详细总结
4. 作业或待办事项
5. 需要进一步理解的问题

课堂转写：
{transcript}
"""
        }
    ]
)

with open("summary.md", "w", encoding="utf-8") as file:
    file.write(response.output_text)

print("总结完成，已保存到 summary.md")