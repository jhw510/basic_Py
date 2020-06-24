#!/usr/bin/env python
# coding: utf-8

# In[2]:


#def가붙어있으면 함수다.
#클래스 외부에 있는 메서드 (클래스와 관계 없음)라고 생각하면 된다 

def times(a,b):
    return a*b
#여기서 출력된 숫자가 객체가 위치하는 메모리 주소값이다.
#c,c++스타일로 얘기하면 포인터이고
#자바스타일로 이야기하면 객체
#나오는 숫자값은 근시대의 컴퓨터16자리가 나올것이다
#이유는 포인터의 크기가 64비트 컴퓨터에서 8byte이기 때문 
#8바이트라는것은 16진수로 표기했을때 16자리가 나옴
#1바이트 16진수 2자리
#16진수 1자리는 4비트(bit)
#WebAssembly(웹어쎔블리)=웹기술 + c++
print(times)
print(times(3,7))
#(built-in)   별도의 import없이도 사용할 수 있는 내장 함수들
#globals() 라는 것은 현재 파이썬이 구동되면서
#활용할 수 있는 함수들의 리스트를 보여준다
print(globals())


# In[3]:


#times라는 함수의 객체정보를 pointerOfFunction 이 받아서 저장한다 
#변수의 진정한 정의??
#state 어느정도 무방 
#어떤 값이 저장되는 공간
#특정한 데이터 타입이 저장되는 공간
#자바에서는 객체를 출력하면 @샬라샬라  가 보이는데 
#이것이 바로 메모리 주소값에 해당하는것
pointerOfFunction = times
#즉 pointerOfFunction을 times 함수처럼 활용할 수 있게 된다.
res = pointerOfFunction(7,7)
print(res)


# In[4]:


#>????? 왜 인터페이스? 
def add(a,b):
    return a+b
# 현재 여기서는 pof변수가 add 함수의 주소를 저장한다 
pof=add
#그러므로 이것은 add(3,7)과 같다
res=pof(3,7)
print("res=",res)

#여기서는 pof변수가 times 함수의 주소를 저장한다
pof=times
#이것은 times(3,7)과 같다 
res=pof(3,7)
print("res =",res)
#경우에 따라서 덧셈 ,뺄셈,곱셈 등등을 자유롭게 수행할 수 있게 해주는 기법
#자바에서는 인터페이스에 해당하는 내용이다

#인터페이스를 사용하는 이유 
#RPG게임을 구현한다고 가정할때
# 전사,마법사,궁수등등 각각의 1차 ,2차,3차 전직등등이 있을 것이다 
#이때 calculateDamage()라는 메소드를 각 직업별로 구현한다고 하면
#calculateWarrDamage(),calculateMagicDamage()...
#1차 직업용 데미지 계산 ㅡ2차용 ,3차용 
#관리 포인트가 늘어나게 된다 ,
#그러나 인터페이스를 사용하여 calculateDamage()로 퉁치면
#모든 데이지계산은 calculateDamage()메서드로 일관되게 처리할수 있으며
#해당 인터페이스를 implement한 클래스 별로
#서로 다른 데이지 계산 공식을 활용할 수 있다 


# In[10]:


def intersect(prelist,postlist):
    retList=[]
    #리스트 (prelist)에서 글자 하나씩 뽑아 온다
    for x in prelist:
        print("x(prelist)=",x)
        #리스트(postlist)에서 글자를 뽑아 위에서 가져온 값고 일치하는지 비교한다 
        if x in postlist:
            #일치한다면 해당 내용은 retList리스트에 추가
            print("x(postlist)=",x)
            retList.append(x)
    return retList

list1="Apple"
list2="Onion"

print(intersect(list1,list2))

print(intersect(list1,['H','A','M']))

        


# In[11]:


#아래를 자바버전으로 한다면
#public void smap(int x,int y){
# int temp= x;
# x=y;
#y=temp;
#}

#파이썬에서는 자바처럼 번거로운 작업없이 그냥 위치를 바꿔서 쓰면됨
def smap(x,y):
    return y,x                                 #내부적으로는 한번 감싸서 리턴한다

print(smap(3,7))

#두개를 리턴하니 아래와 같이 두개에 값을 받을수도 있다.
a,b=smap(33,77)
print(a,b)
#그리고 n개를 하나로 아래와같이 한개로 받을 수도 있다.
#이런식으로 값을 받게 되면 튜플(tuple)이란것이 된다 
x=smap(333,777)
print(x)
print(type(x))


# In[12]:


#자바에서 출력할때 sys.o.p("헬로우 자바")
#"헬로우자바"->[0][1][2][3][4][5][6][7][8][9]
#               H e  l  l   o    j  a  v  a
#해당 데이터는 메모리 섹션"data"fksms rhtdp wjwkdehoa
def change(x):
    x[0]='H'
    
wordlist=['J','A','M']
print(wordlist)

change(wordlist)
print(wordlist)


# In[16]:


def change2(x):                                                                             #실행순서 4번 (함수여서 먼저 실행이 안된다)
    #x[:] 는 새로운 동일 객체를 만든다.                                                       
    #그러므로 인자로 돌아온 x와 여기서 새로만든 x가 분리가 된다
    #인자로 들어온 x를 변경하지 않은 상태로 
    #값을 가공하고자 할 때 주로 사용하는 기법이다
    x=x[:]
    x[0]='H'
    print(x)   # 리턴을 안해서 이 안에서만 살고있다                                          #실행순서 5번
    print('**********************************************')
                                                                        
    
wordlist=['J','A','M']                                                                         #실행순서 1 번  
print(wordlist)                                                                                #실행순서 2번

change2(wordlist)                                                                             #실행순서 3번
print(wordlist)    # 다시 돌아왔을때는 jam되어있는것                                         #실행순서  6번


# In[17]:


#변수 glob를 선언함 
glob=1
print(glob)

def xchGscope(x):
    #glob은 전역변수로 지정
    global glob
    #최상위에 있는 glob를이 1->7로 변경
    glob = 7
    return glob + x

print(xchGscope(3))
print(glob)


# In[18]:


#인자가 없을 경우 a와 b와 초기값을 10,20으로 지정하는것 
def times(a=10,b=20):
    return a*b
#a=10,b=20->200
print(times())
#a=5,b=20->100
print(times(5))
#a=3,b=7->21
print(times(3,7))


# In[20]:


def connectURL(server,port):
    str ="http://"+server+":"+port
    return str

name="test.com"
service="8080"
#파이썬은 아래 보이는것과 같이 
#인자의 순서를 지키지 않아도 인자를 받을 수 있다.
print(connectURL("test.com","8000"))

print(connectURL(port="8000",server ="test.com"))

print(connectURL("test.com",port="8000"))

print(connectURL(name,service))


# In[21]:


#가변 인자로 값을 처리하게 되면 튜플 타입이 된다ㅣ.  인자하나로 여러개를 담는것도 튜플이 된다
def test(*args):
    print(type(args))
    
    
test(1,2,3)    


# In[22]:


#*(에스테릭)-포인터x
#파이썬에서 가변인자(파라미터)를 받을 경우 *을 붙인다
def union2(*ar):
    res=[]
    #ar 튜플에서 각각의 요소를 item으로 뺀다
    for item in ar:
        #item 에 있는 글자 한개씩 x로 뺀다
        for x in item:
            #res라는 리스트와 값이 같은지를 확인하고
            #같은것이 없다면 x를 res리스트에 추가한다
            if not x in res:
                res.append(x)
                
    return res
#중복 문자를 제외하고 사용된 모든 문자
print(union2("ham","egg","poteto"))

print(union2("test","tdd","junit"))


# In[26]:


#변수는 언제 할당될까?
#자바에서 int num :변수 할당 x ,선언만 하면 변수가 할당된것이 아니다
#값을 집어넣어야 변수가 할당되면서 메모리가 잡힌다.
g= lambda x,y:x*y
print(g(2,3))

# 즉 메모리 할당을 받지 않으면 완벽한 익명객체가 된다
print((lambda x:x*x)(3))

onemore=lambda x,y,z:x*y*z
print(onemore(2,3,4))

re=lambda *argv:argv[0]

print(globals())


# In[27]:


# def로 선언한 함수들은 
#메모리의 구조상 Text라는 영역에 잡히게 된다
#가상메모리 개념에 보면 text|data|heap|stack
#상수는 전부 data에 배치됨
#new한것들은 전부 heap에 배치됨
#그 외의 변수들은 stack에 배치 

#a.자바  , b.자바 ,  c.자바   와같이 파일이 3개 존재한다고 할떄 
#javac.a.class ,  b.classs , c.class
# w자바를 통해서 각각의 클래스들을 구동시킴

#ex)a는 text를 40000~50000,heap10000~20000
#   b는 text를 60000~70000,heap15000~20000

# 시스템 언어들은 이것을 컴파일 시점에 링킹이란 작업을 통해 완벽하게 겹치지 않게 조정한다
#반면 인터프리팅 방식의 언어들은 이것을 Run-Time(실행중) 동적으로 조정한다
#결론은 동적이든 정적이든 이러한 것을 조정하기 위해 각 영역의 분리가 필요하다.
#자바는 하이브리드 방식을 채택하고 있다는것
#javac는 컴파일러의 역할이며 자바는 인터프리터 역할을 함


# In[28]:


help(print)


# In[29]:


import math
help(math)


# In[30]:


#plus함수를 만들어 놓은것이 없으므로 당연히 에러1
#help(plus)


# In[34]:


def plus(a,b):
    return a+b


#언더바 1개가 아닌 2개이다

plus.__doc__="a와 b를 더한다"
help(plus)


# In[38]:


def factorial(n):
    """n!울 구하는 함수다
    감마 함수가 적용되지 않아 
    1.1!,1.3! 등은 구할 수 없다
    또한 값은 0보다 크거나 같은 정수여야 한다
    """
    
    
    if x < 0:
        print("에러")
    elif x <=1:    
        return 1
    
    return c*factorial(x-1)

help(factorial)


# In[52]:


#문제1.
#1~100까지 숫자중 2의 배수만 출력해보시오

item=[]
for i in range(2,101):
    if i%2:
        
        continue
    
    item.append(i)
print(item)
   


# In[53]:


#문제1.
#1~100까지 숫자중 2의 배수만 출력해보시오
#자바스타일

for i in range(1,101):
    #not(i%2)
    if not(i%2):
        print("i",i)


# In[54]:


#문제1.
#1~100까지 숫자중 2의 배수만 출력해보시오
#v파이썬스타일 

for i in range(2,101,2):
    print(i)


# In[88]:


# numpy - Numerical Python - 수치해석을 위한 라이브러리
import numpy as np
# matplotlib - 그래프 그리는 라이브러리
import matplotlib.pyplot as plt
# np.linspace - np 라이브러리 내부에 있는 linspace 매서드
# linspace - Linear Space의 약자
# 증가폭이 일정한 값으로 0 ~ 5 사이의 숫자를 1001개 생성해달라
# 파라미터 첫번째 시작값(포함), 두번째 끝값(포함), 세번째 개수
# 그렇기 때문에 각 숫자간의 간격이 0.005

#1001개라는 개수를 샘플개수
#샘플의 개수가 부족하면 그래프가 깨지게 된다
#그래프를 그릴떄는 원하는 형태를 유지할 수 있도록
#최소한의 샘플 수를 유지하도록 한다
t = np.linspace(0, 5, 1001)
#print(t)


# y = 2 cos(10 * t)
# 진폭(amplitude) = 2
# 주기(period) = 주파수와 역수 관계
# 주파수(frequency) = 주기와 역수 관계
# 2 * pi * f * t = w * t
# w = 10
# 2 * pi * f = 10
# f = 10 / 2pi
# T(주기) = 2pi / 10
x1 = 2 * np.cos(10 * t)
# plt.subplots()은 그래프를 폼을 만듬
# figsize = (6, 2.5)의 크기로 만듬
fig, ax = plt.subplots(figsize = (6, 2.5))
# 시간(t)에 따른 cos 함수의 위치(x1)를 찍어보자!
ax.plot(t, x1)
# 그래프 상에서 x의 범위는 0 ~ 5 까지
ax.set_xlim(0, 5)
# x축의 라벨에 t(초)를 표기한다.
ax.set_xlabel('t(sec)')
# 여기는 어떤 수식에 대한 그래프인지 표기해주는 부분
# 앞뒤에 반드시 $를 표시해주도록 한다.
# 또한 x_1 (x 아래첨자 1)
# 숫자와 cos등을 결합할때는 \ 표시를 넣어주도록 한다.
ax.set_title('$x_1(t) = 2\cos(10t)$')
# 화면상에 그래프가 보여진다.
fig.show()


# In[71]:


#y=x를 그려보자
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 1001)
y=x
fig, ax = plt.subplots(figsize = (3,3))
ax.plot(x,y)
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_title('$y = x$')
fig.show()


# In[81]:


#랜덤을 먼저 보자 
import random
help(random,randrange)


# In[82]:


#랜덤값을 생성하기 위해 추가해야하는 라이브러리
#import java.util.scanner
import random

cnt=0

while cnt<5:
    #randrange(시작값 포함 ,끝값 포함 x)
    #위의 값 사이에서 랜덤값을 뽑아 온다
    #1~6사이의 랜덤값
    x=random.randrange(1,7)
    print(x)
    cnt += 1


# In[84]:


#수학 라이브러리 필요
import math
#직각삼각형의 대각선 길이를 구해보자

width=3
height=4

#피타고라스 정리:대각선 길이 =루트 (밑변^2 + 높이^2)
#sqrt=Square Root(제곱근=루트)
diag=math.sqrt(width*width+height*height)
print(diag)
#계산공식이 명확한 경우
diag=math.sqrt(width**2+height**2)
print(diag)
#계산공식이 정해지지않고 와리가리 칠때
diag=math.sqrt(math.pow(width,2)+math.pow(height,2))
print(diag)


# In[101]:


# 현재 우리가 있는 위치를 2D 좌표상 (5, 5) 라고 가정한다.
# (실제 지도에서 3D 좌표로 고려해야겠지만 편의를 위해 2D로 진행한다)
# 랜덤 좌표 7개를 생성한다.
# 해당 랜덤 좌표는 주유소에 해당한다.
# 현재 차량에 기름이 없다.
# 어떻게 하면 가장 빨리 주유소에 도달하여 주유를 할 수 있을까 ?
# (랜덤값은 1 ~ 10)
import math
import random
myloc = [5, 5]   # [x, y]
distance = []
x = []
y = []
def assignRandXY():
    #i = 0
    #while i < 7:
    #    x.append(random.randrange(1, 11))
    #    y.append(random.randrange(1, 11))
    #    i += 1
    for _ in range(7):
        x.append(random.randrange(1, 11))
        y.append(random.randrange(1, 11))
def calculateDistance():
    for idx in range(7):
        distance.append(
            math.sqrt(
                (myloc[0] - x[idx]) ** 2 +
                (myloc[1] - y[idx]) ** 2
            )
        )
def findBetterSolution():
    distance.sort()
    #print("distance =", distance)
    return distance[0]
def prettyPrint(myList):
    #print(len(myList))
    for idx in range(len(myList)):
        print("%.2f" % myList[idx])
assignRandXY()
print("x =", x)
print("y =", y)
calculateDistance()
#print("distance =", distance)
#print("Most Better Solution:", findBetterSolution())]
print("distance =")
prettyPrint(distance)
print("Most Better Solution = %.2f" % findBetterSolution())


    
    
    


# In[103]:


from numpy import linspace,sqrt
import matplotlib.pyplot as plt

x=linspace(-1,5,400)
y=1.0/sqrt(x**2+1)

#subplot(figsize =~~~)같은 부분없이
#단순히 plt.plot()으로도 그래프를 그릴수 있다
#단 그래프 크기 조정이 불가능
plt.plot(x,y)
plt.show()


# In[106]:


from numpy import linspace,sqrt
import matplotlib.pyplot as plt

x=linspace(-1,5,400)
y1=1.0/sqrt(x**2+1)
y2=1.0/sqrt(3*x**2+1)

#아무런 옵션이 없으면 실선
plt.plot(x,y1,label='plot 1')
#아래와 같이 '--'이 있다면 점선
plt.plot(x,y2,'--',label='plot 2')
#plt.legend()면 plot 1과 plot2가 각가 어떤것인지 지표가 붙음
plt.legend()
plt.show()


# In[121]:


from numpy import array
import matplotlib.pyplot as plt
#numpy에 있는 arry기능으로 값들을 쭉 담아 넣는 구조
x=array([0,   1 ,3,  7,  8,10])
y=array([1.1,2.2,3.8,0,-0.6,7])
#numpy.ndarray(수치해석용 배열)
print(type(x))

#(x,y)좌표에 동그라미로 포인트 주기
plt.plot(x,y,'<-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[139]:


import numpy as np
import matplotlib.pyplot as plt
x = linspace(-3, 4, 1000)
y = x ** 2
plt.plot(x, y)
plt.show()
# x^2에 대한 0 ~ 3 까지의 정적분 구현
# 1. 컴퓨터는 limit 개념을 구현할 방법이 없다.
# 2. 그렇기 때문에 0에 근접한 값을 만들 수가 없고
#    대신 아주 작은 미소값 dx의 개념을 활용해야 한다.
# 3. y = x^2 를 구한다 할 때 각각의 0 ~ 3 사이의 x값들을 먼저 산출해야한다.
# 4. dx(고정) * y(고정 x) - 작은 사각형의 넓이
# 5. 구한 작은 사각형들의 넓이를 모두 더했을때
#    9에 근접한 값이 나오는 것을 확인하면 된다.
dx = 0.0000001
y = []
# 면적을 return
# x^2을 0 ~ 3 까지 -> 1/3 x^3 = 9
def integralRange(start, end):
    loopNum = (int)((end - start) / dx + 1)
    #print(loopNum)
    area = 0
    for i in range(loopNum - 1):
        curX = dx * i
        #print(curX)
        #y.append(curX ** 2)
        area += dx * (curX ** 2)
    return area;
area = integralRange(0, 3)
#print(y)
print("x^2의 0 ~ 3까지 정적분 결과 =", area)


# In[ ]:


#아주 작은 사각형들로 위의 도형을 채운다고 생각하고 접근
#그래서 작은 사각형의 넓이를 구하고
#그 사각형들의 넓이를 모두 더한 결과




import numpy as np
import matplotlib.pyplot as plt
x = linspace(-3, 4, 1000)
y = x ** 2
plt.plot(x, y)
plt.show()

dx = 0.0000001#사격형의 밑변값을 0.0000001이라고 가정한것
y = []

def integralRange(start, end):
    loopNum = (int)((end - start) / dx + 1)  #우리가 계산하려는 실제 거리를 구한 =(end - start)   
                                            #다음 반복적으로 사각형을 더해야함 =  / dx+1
    area = 0
    for i in range(loopNum - 1):  # 0~  loopNum -2
        curX = dx * i            # = current X
       
        area += dx * (curX ** 2)
    return area;
area = integralRange(0, 3)

print("x^2의 0 ~ 3까지 정적분 결과 =", area)

