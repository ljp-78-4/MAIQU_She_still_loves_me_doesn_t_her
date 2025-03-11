#类型声明

class memory:
    def __init__(self):
        self._memory=[]
    #参数为字符串，下同
    def add_memory(self,new_memory):
        self._memory.append(new_memory)
    def remove_memory(self,removing):
        self._memory.remove(removing)
    def change_memory(self,old,new):
        for i in range(len(self._memory)):
            if self._memory[i]==old:
                self._memory[i]=new
                return 0
    def get_memory(self):
        return self._memory

class characteristic:
    #chara人格列表
    def __init__(self,chara):
        self.characteristic=chara
    def change_characteristic(self,new):
        self.characteristic=new
    def get_characteristic(self):
        return self.characteristic

class relationship:
    #参数类型为字典
    def __init__(self,relationship):
        self.relationship=relationship
    #参数类型为字典
    def change_relationship(self,change):
        self.relationship.update(change)
    def get_relationship(self):
        return self.relationship

class npc:
    #position为职位，chara为人格列表,rela为关系字典
    def __init__(self,position,chara,rela):
        self.postion=position
        self.memory=memory()
        self.characteristic=characteristic(chara)
        self.relationship=relationship(rela)
        self.time=0

class palyer(npc):
    # position为职位，chara为人格列表,rela为关系字典
    def __init__(self, position, chara, rela):
        self.postion = position
        self.memory = memory()
        self.characteristic = characteristic(chara)
        self.relationship = relationship(rela)
        self.time = 0