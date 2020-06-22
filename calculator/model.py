class Model:

    def __init__(self):          # __init__는 생성자 , self 는 this 의 의미를 갖는다 .
        self._num1 = 0       #언더바 하나 _를 걸어주면  protect 라는 뜻    언더바 두개 __는 private
        self._num2 = 0
        self._opcode = ''         #' ' 싱글쿼터를 쓸것

    @property
    def num1(self) -> int: return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num1

    @num2.setter
    def num2(self, num2): self._num2 = num2

    @property
    def opcode(self) -> str: return self._opcode

    @opcode.setter
    def opcode(self,opcode): self._opcode = opcode

