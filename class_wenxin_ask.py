from requests import request
import json

#文心一言AI提问类
#使用示例
'''
#从文件中导入User类
from class_wenxin_ask import User
#初始化User类
user=User()
#提问
print(user.ask('1=1=？'))
#继续提问
print(user.ask('再加1呢？'))
#打印对话记录
user.show_record()
#清空对话记录
user.clear_record()
#打印对话记录
user.show_record()
'''
class User:
    #参数初始化
    #temperture、top_p参数均与回答多样性有关，数值越小越保守
    #record为历史聊天记录
    #status为ai在对话中的角色定位
    def __init__(self,tem=0.6,top=0.7,status=None):
        self.client_id='luojBOGFP24t9QOZhduHK5UK'
        self.client_secret='2iO51lBsRcMFEXQkiMOMRZIXFyNwYQom'
        self.temperature=tem
        self.top_p=top
        self.status=status
        self.record=[]

    #获取链接密钥函数
    def get_access_token(self):
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}"
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")

    # 提问函数
    # questiont提问内容
    #返回AI回答字符串
    def ask(self,question):
        #添加用户提问记录
        self.add_message({'role':'user','content':question})
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + self.get_access_token()
        payload = json.dumps({
            "messages": self.record,
            'temperature': self.temperature,
            'top_p': self.top_p,
            'system': self.status
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = request("POST", url, headers=headers, data=payload)
        #添加ai回答记录
        self.add_message({'role':'assistant','content':json.loads(response.text).get('result')})
        return json.loads(response.text).get('result')

    #添加消息记录
    #message为字典类型，形如：{'role'='user(或assistant)','content'='内容'}
    def add_message(self,message:dict):
        self.record.append(message)

    #清空历史记录
    def clear_record(self):
        self.record=[]
    #打印对话记录
    def show_record(self):
        for note in self.record:
            print(note.get('role')+':'+note.get('content'))

