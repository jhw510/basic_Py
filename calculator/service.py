
class Service:

    def __init__(self, paylode ):  # payload에 num1,2 를 담는다 가능한이유? 문법이 서로 공유됌
        self._num1 = paylode.num1
        self._num2 = paylode.num2



    #@staticmethod                        #이것을 붙여주면 일반 파라미터로 바뀜
    #def add:                 #(self)를 지운다
    def add(self):
        return self._num1 + self._num2

    def minus(self):
        return self._num1 + self._num2

    def multi(self):
        return self._num1 * self._num2

    def divide(self):
        return self._num1 / self._num2
