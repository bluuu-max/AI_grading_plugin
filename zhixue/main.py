sys.path.append("""C:/Users/Administrator/AppData/Local/Programs/Python/Python311/Lib/site-packages""")
sys.path.append("""C:/Users/Administrator/AppData/Local/Programs/Python/Python311/Lib""")
import requests
import json
import base64
import re
from openai import OpenAI

client = OpenAI(
    api_key = "your_kimi_api_key",
    base_url =  "https://api.moonshot.cn/v1"
)




def get_score(base64_image,client=client):
    response = client.chat.completions.create(
        model="moonshot-v1-8k-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": "题目: 编写一个程序，输入两个浮点数，计算它们的和。图片中是26题学生写的答案, 评分标准:完全正确得5分,空白为0分,写对部分酌情给分. 请给分并给出理由,格式为{'score':3,'reason':'...'}"
                    }
                ]
            }
        ]
    )
    content = response.choices[0].message.content
    print("收到内容：", content)
    # 使用正则表达式查找包含'score'的模式
    match = re.search(r'["\']score["\']:\s*(\d+)', content)
    if match:
        score=int(match.group(1))
        print("匹配到分数：", score)
        return score
    print("未匹配到分数!")
    return -1


self.score=get_score(self.base64_image)

# 没有返回正确分数,可能是产生幻觉,则让大模型继续改分,注意这里设置分值范围
while self.score==-1 or (self.score not in list(range(0,6))):
    self.score = get_score(self.base64_image)
# 文件路径
    file_path = "xunfei_rec_result.txt"

    # 打开文件，追加模式
    with open(file_path, 'a', encoding='utf-8') as file:
        # 将字符串写入文件
        file.write( " \n得分：" + str(self.score))

print("本张试卷得分：",self.score)
