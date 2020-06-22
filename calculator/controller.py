from calculator.model import Model
from calculator.service import Service

class Controller:

    #def __init__(self):   #한번도 안쓰고 pass만 썼으므로 생략가능
        #pass

    def calc(self , num1, num2,opcode):
        model = Model()          #new Model 과 같다
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = Service(model)
        if opcode == '+': result = service.add()           # 자바 스크립트와 달리 파이썬은 ' '  이것이 == 과같은 역할을 한다
        if opcode == '-': result = service.minus()
        if opcode == '*': result = service.multi()
        if opcode == '/': result = service.divide()
        return result