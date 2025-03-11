#函数声明
from email.message import Message

from requests import request
import json

def get_access_token():
    """
    使用应用API Key，应用Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=luojBOGFP24t9QOZhduHK5UK&client_secret=2iO51lBsRcMFEXQkiMOMRZIXFyNwYQom"
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


#question为字典
def ask(question,personality):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": question,
        'temperature':0.6,
        'top_p':0.7,
        'system':personality
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = request("POST", url, headers=headers, data=payload)
    return json.loads(response.text).get('result')

def read_file(file_path):
    with open(file_path,'read') as f:
        return f.read()

def write_file(file_path,content):
    with open(file_path,'a') as f:
        f.write(content)


chara='勤劳，爱财，上进，争强好胜，刚愎自用'
task='我将扮演你的同事，你需要回复我的话，我将劝说你以身体健康为重按时下班回家，你需要反驳我的回答，最终有小概率可能你答应了我的要求'
ai_request='保证你的回答不超过40字，不需要模拟我的对话，保证与上文逻辑连贯，回答内容不要与之前的回答有重复之处，回答风格模仿我的回答'
first_sentence='只有多工作才能多挣钱'
first_question=f'{task},要求：{ai_request},Amily所说的第一句话已经给出：{first_sentence},你无需回复'
personality=f'你是Amily,你是一个年轻的公司职员，你有可观的薪水，但你仍然嫌少，希望通过加班获得更多钱，我是你的同事，你的性格是：{chara}'
memory=[{'role':'user','content':first_question}]
ask(memory,personality)
print(first_sentence)
while True:
    question = input('输入:')
    memory.append({'role':'user','content':question})
    if question=='结束':
        break
    reply=ask(memory,personality)
    print(reply)
    memory.append({'role': 'assistant', 'content': reply})



#加班伤害身体