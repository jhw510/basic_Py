#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello python")
print('안녕')


# In[3]:


Num=3.3
num=7
print(Num,num)


# In[6]:


#파이썬은 주석으로 샵을 쓴다 
#파이썬 진영이 데이터 과학자 , 일반 과학자들이 좋아하는 이유가 
#아래와 같은 수식 연산들을 언어 차원에서 지원해주고 있기 때문이다 
#백터,행렬: 선형대수를 공부해야함 ,(통계,미적분  : 각각을 따로 공부해야함  )
#공업수학 (리플리스 변환 푸리에 변환 )

#i를 j로 표현하는 이유가 전류 기호가 i이기 때문이다 
#i가 혼선을 유발할 수 있으므로 복소수 표현시 j를 사용하는 것을 추천한다
z =3+4j

print(type(z))
print ("z.imag =",z.imag)
print('z.imag =' + str(z.imag))
print(z.conjugate())


# In[9]:


z1=3+4j #객체1
z2=2-2j #객체 2

#지금 보는것은 연산자 오버로딩이다 (operator overload)
# 만약 자바로 한다면 z1.sub(z2)
# class Complex{
# float real,imag
# public Conplex sub(complex other)  {
#  complex res = new conplex()
#  res.real = real-other.eral
#  res.imag = imag - other.imag
#    return res
#  }
#}
res=z1-z2
print("res = ",res)


# In[13]:


big=1.2e30  #1.2* 10의 30승 (e가 euler 상수가 아님)
small = 1.57e-20 #1.57*10의 -20승 (같은 식으로는 1.57* 10^-20로도 표현가능 )
test =2**10 #2^10

print (big)
print(small)
print(test)       

print(type(big))
print(type(small))
print(type(test))       


# In[14]:


#파이썬은 데이터 타입이 없다 

num1=3/7  # 데이터 타입이 없다 보니까 소수점이 나오면 자동으로 float처리 
num2=3//7 #나눗셈의 몫만 계산하도록 만들어 준다. 

print(num1)
print(num2)


# In[17]:


# """ 쌍따옴표 3개를 쓰면 문자열의 출력 형식을 작성한 그대로 유지할 수 있다.
fixStr="""
       오늘도 간다 ~
        내일도 간다~
         모레도 간다 ~
"""

print(fixStr)


# In[18]:


testStr = 'test' + 'python'
print(testStr)


# In[19]:


str = "pointer"
print(str)
print(str[0])
print(str[3])


# In[67]:


#앞의 내용과 공유가 된다
str='pointer'
print(str[0:1])   #0부터 1미만 (0을 포함 ,1은 포함하지 않음 )
print(str[1:4])  # 1부터 4 미만 (1,2,3)
print(str[:2])    #생략은 0이므로 (0,1)
print(str[-2:])   #(-2,-1) 음수이므로 거꾸로 
print(str[:])   # 그냥 전부 다 
print(str[::2])   #전부다 뿌리는데 2번째 칸마다 나온다 (2칸씩 건너뜀)
print(str[::3])

print("**********")
print(str[-5:-2])    #-5,-4,-3
print(str[-5:5])    #-5,-4,-3   얘는 문자가 연결되서 출력가능 
print(str[-5:0])    #-5,-4,-3  애는 문자가 연결 안되니까 출력 불가  i다음으로 연결된 문자가 없기때문이다 


#[시작:끝:스탭] --> 스탭 :값을 몇 씩 올릴 것인가 (for문의 증감부 같은거라 생각)


# In[23]:


#파이썬은 자바와 같이 collection 등을 활용하지 않더라도 쉽게 리스트를 만들 수 있다 .
colors=["red","green","blue"]
print(colors)
print(type(colors))


# In[24]:


colors=["red","green","blue"]
colors.append("gold")     # append는 맨 마지막 원소에 값을 배치한다.
print(colors)


# In[29]:


colors=["red","green","blue"]
colors.insert(1,"black")   # insert는 원하는 특정 위치에 값을 배치한다       1번자리에 값을 배치 ,0번부터 시작 배열이라서 
                        # 단 ,기존에 인던 값은 1칸씩 뒤로 밀려난다
print(colors)


# In[27]:


colors=["red","green","blue"]
colors.extend(["yellow","pink"])     # extend 는  리스트에 리스트를  붙일수 있다 .
print(colors)


# In[28]:


colors=["red","green","blue"]
colors+=['purple']                           # sum += account -> sum=sum+account
                                             #colors=colors=['purple']
colors+=['red']
print(colors)


# In[34]:


colors=["red","green","blue"]
colors.append("gold")
colors.insert(1,"black") 
colors.extend(["yellow","pink"])  
colors+=['purple'] 
colors+=['red']

#    0      1       2       3      4     5        6     7         8
# ["red","black","green","blue","gold","yellow","pink","purple","red"]
print(colors.index('purple'))    #인자로 들어온 원소의 인덱스를 찾아라
print(colors.index('red')) 
print(colors.index('red',1))  # 두번째 인자는 시작위치 
 #print(colors.index('purple',0,3))   # 일부러 오류 나게함 , 세번째 인자는 끝 위치 
print(colors.index('purple',4,8))


# In[38]:


colors = ["red","black","green","blue","gold","yellow","pink","purple","red"]
print(colors.count('red'))                      # 같은 인자의 갯수를 알려줌 


# In[65]:


colors = ["red1","black","green","blue","gold","yellow","pink","purple","red2"]
#현재 만든 리스트 (스택,디폴트는 스택)        
print(colors.pop())   # pop는 맨뒤에것부터 빠지고 저장됌
print(colors.pop(0))   # 숫자를 지정하면 그 해당 순번의 것이 빠지고 저장됌 
print(colors.pop())
print(colors)


# In[39]:


colors = ["red","black","green","blue","gold","yellow","pink","purple","red"]
colors.remove("green")           #원하는 원소를 제거한다 
print(colors)


# In[40]:


colors = ["red","black","green","blue","gold","yellow","pink","purple","red"]
colors.sort()                     # 값을 알파벳순으로 정렬 = a와 가까운 순서대로 정렬
print(colors)


# In[42]:


colors = ["red","black","green","blue","gold","yellow","pink","purple","red"]
colors.reverse()                    # 값을 뒤집기 ,(거꾸로 정렬과는 다름 )
print(colors)


# In[44]:


colors = ["red","black","green","blue","gold","yellow","pink","purple","red"]
colors.sort(reverse=True)                     # 값을 거꾸로 정렬 =z와 가까운 순서대로 정렬
print(colors)


# In[56]:


def mysort(x):
    return x[-1]           
#   red   [r=0,e=1,d=2] 순차 인데 -1이니까 d 
# 값의 가장 마지막 스펠링 ex)re'd', yello'w'  를 X[-1]번째의 스펠링을 a와 가까운 순으로 정렬
# 낱장으로 보다보니 글자 하나만 봐서 
#앞뒤의 전후 사정을 알 수가 없다 
#그러므로 동일한 

colors = ["1red","black","green","blue","gold","yellow","pink","purple","2red","blue"]
colors.sort(key=mysort)                         
print(colors)


# In[66]:



def mysort(x):
    return x[-2]       #맨마지막 글자 하나 

colors = ["1red","black","green","blue","gold","yellow","pink","purple","2red","blue"]
colors.sort(key=mysort)                         
print(colors)


# In[68]:


#중괄호에 넣은 값들은 집합으로 분류된다 
a={1,2,3}
b= {2,3,4,5}

print(a)

print(b)

print(type(a),type(b))


# In[70]:


a={1,2,3}
b= {2,3,4,5}

print(a.union(b))  # 합집합
print(a.intersection(b))  #교집합
print(a-b)                        # 차집합
print(b-a)              # 차집합의 특징 :빼는 순서에 따라 결과가 바뀐다 
print("****************")
print(a|b)        # OR(합집합)
print(a&b)      #and(교집합)
print(a^b)     #xor(여집합) = 차집합들의 합집합이다 


# In[71]:


#파이썬은 True 혹은 False 로 표기한다!
isTrue = False 
print(isTrue)
print(type(isTrue)) 


# In[74]:


print(1<2)          
print(1!=2)              # '같지않다'가 아니라 '같지않냐? '고 물어보는것 
print(1 == 2)           #같은 거냐? 고 물어보는것 
print("************")
print(True and False)          # and 특징 -양쪽 모두 참인 경우에만 참 
print(True  & False)           # and 의 기호의 표현식       =  &
print(True or False)          # or의 특징 -한쪽이라도 참이면 참 
print(False | False)           # or 의 기호식 표현      =  |
print(False | True)         
print(not False)               #not 의 특징 -무조건 반전


# In[75]:


print('bool(0)=',bool(0))           # 0은 거짓                 
print('bool(-1)=',bool(-1))                # -1은 참 (값이 있으면 참 )
print("bool(None)=",bool(None))              # None은 아무것도 없다는 것이므로 거짓
print("bool('test')=",bool('test'))                #문자열이 있으므로 참 
print("bool('')=",bool(''))                          #텅 비어있으로 거짓

# 숫자에선 0이 안값들은 참이고 String 에서는 None아닌 것들이 참이다 


# In[84]:


val = 10
# 자바에서 한다고하면 if(val>5); 인데 파이썬은 중괄호 없이 :(콜론)으로 스코핑을 한다 
#해당 if나 함수(메서드)나 반복문등의 내부 코드는 들여쓰기로 구분한다 

if val >5:
        print("%d is bigger than 5"%val)
        
print("들여쓰기가 안돼있으므로 이건 if문에 해당안됌 ")        
        
        #%d 는 decimal의 약자로 정수 타입의 숫자를 출력 
        #%f 는 float 으로 소수점 타입의 숫자를 출력 
        #%s 는 String 으로 문자열을 출력 
        
        #문자열 내부에 %d ,%s,%f 등을 표현한다 
        #문자열으 ㄹ끝내고 뒤에 %를 붙이고 대응 시킬 변수들을 넣으면 됌


# In[83]:


val1=3
val2=7
fval=3.3
sval="test"
print("%d이(가) 나오고, %d도 나오고 %f %s"%(val1,val2,fval,sval))


# In[91]:


val = 1
if val>3:
    print("크다")
else:
    print("작다")


# In[90]:


val = 1
if val>3:
    print("크다")
elif val <3:
    print("작다")
else :
    print("같다")


# In[93]:


fruits = {"apple":"red","banana":"yellow"}
#파이썬에서 해쉬는 dict 라고 불리며 kye값:value값으로 구성된다 
print(fruits)
print(type(fruits))


# In[94]:


fruits = {"apple":"red","banana":"yellow"}
#key값으로 value값을 얻는 모습
print(fruits["apple"])


# In[98]:


#dict 추가는 +기호가 필요없다
#dict형태[키값]="벨류값"
fruits ['cherry']='red'
print(fruits)


# In[99]:


#해쉬가 키값을 기반으로 값을 찾는 방식이므로
#키값으로 검색을 하고 삽입하면 벨류값이 변경된다 
#키값으로 검색 ==fruits['apple']  ->True
fruits['apple']='green'
print(fruits)


# In[101]:


#fruits.items()은 fruits 딕셔너리 (dict)에 들어있는 요소들을 가져온다 
#('apple', 'green') - 첫번째요소 
#('banana', 'yellow')-두번째 요소
#('cherry', 'red') -세번째 요소        이때 키값과 벨류값으로 갖고온다 

cnt =0
# 각각의 키 &벨류에 해당하는 요소를 c에 가져온다 .
for c in fruits.items():
    print(c)
    # 파이썬은 c++같은 형식이 안된다
    cnt +=1
    
print(cnt)    


# In[102]:


#k는 key에 대응하며,v는 value에 대응한다 .
for k,v in fruits.items():
    print("k=",k)
    print("v=",v)


# In[104]:


for k,v in fruits.items():
      print(k,v)
#k에 key v에value값
#1번째 k가apple,v가 green
print('****************************')       


for v,k in fruits.items():
      print(k,v)
#1번째 k가 green,v가 apple          


# In[105]:


# del을 통해 dict를 지울 수 있다.
del fruits['cherry']
print(fruits)


# In[106]:


#dict  형태의 객체를 clear()하면 전부 제거된다.
fruits.clear()
print(fruits)


# In[107]:



#파이썬은 아래와 같은 혼성 데이터도 언어 차원에서 지원한다

test = {'age':37,'job':[1,2,3],'name':{'kim':2,'cho':1}}
print(test)
print(type(test))


# In[147]:


I=[3,4,33,77,333,777,3333]

#iter는 리스트의 반복할 값을 만들어주는 폼 (From)
iterator=iter(I)

print(type(iterator))
print(type(I))

for i in iterator:
    print(i)


# In[109]:


# 순차적인 값을 뽑고 싶을때는 range가 더 좋다 .
# 반면 순차적인 값이 아니라 무작위 데이터 
#혹은 입력을 통해 쵝득한 값이라면 iter()을 사용하는 것이 좋다
for i in range(10):
    print(i)


# In[119]:


numList = [1,2,3,4,5,6,7]

for i in numList:
    if i>3:
        break;                   #현재 돌고 있는 루프 1개를 빠져나간다.
            # {0},{1} 요런식으로 적는 것들은 첫번째 인자 ,두번째 인자를 의미한다 .
            #현재 예에서는 {0} 이므로 첫번째 인자가 i임을 의미한다 .
    print("item:{0}".format(i))


# In[145]:


for i in range(5):
    for j in range(5):
        if j>2:
            break
        # {0}, {1}을 활용하는 방법 예제
        print("item: {0}, {1}".format(i, j))
        #print("item: {0}, {1}, {2}".format(i,j, result)) 이런식으로 사용한다.


# In[155]:


for i in range(10):
    # if(i%2 == 0) 이건 자바스타일
    # 값이 없거나 비어있는 값은 False
    # 그러나 값이 있는 경우에도 0 에 한해서는 False
    #1은 참 0은 거짓 
    
    if i % 2:      # 2로나눴을때 나머지가 0이면 false , 0으로 나오면 무조건 false 니까 컨티뉴로안가고 print되는것 , %는 나머지 연산 
        continue # 더이상 진행하지않고 최상위 루프로 돌아감(증감진행)
        print("I can't do Anyting")
 
    print("item: {0}".format(i))


# In[159]:



for i in range(10):
    # if(i%2 == 0) 이건 자바스타일
    # 값이 없거나 비어있는 값은 False
    # 그러나 값이 있는 경우에도 0 에 한해서는 False
    #1은 참 0은 거짓 
    
    if i % 2:     
        pass #pass는 할 일이 없다 ,일반적인 상황에서는 쓸 일이 없다.
        print("There's nothing what i do!")   # 홀수인 경우에만 찍힌다 
   
    print("item: {0}".format(i))


# In[160]:


#0~9까지 총 10개
# 숫자 10전까지 (10을 포함하지 않음)
print(list(range(10)))
#첫번째인자 = 시작값 ,두번째 인자 =끝값(포함하진않음)
#5~9
print(list(range(5,10)))
#첫번째 =시작 ,두번째 끝 (포함x),세번째 증감
print(list(range(10,0,-1)))

#증감이 2 이므로 2칸씩 건너뜀 
print(list(range(10,20,2)))


# In[164]:


strList=['apple','banana','Orange','cherry']
print(strList)
#len은 요소의 개수를 구하는 부분에 활용이 가능 
print(len(strList))
print(range(len(strList)))
#0~3총 4번 루프를 돈다 ,.
for i in range(len(strList)):
    print("idx:{0},val:{1}".format(i,strList[i]))


# In[169]:


# 람다를 쓰는 이유는 직관적으로 볼수있기 때문에 ,계산식에 활용하기 위해 


#인자가 1개인 GetBiggerThan20() 함수 (메서드)
#def를 적으면 함수를 선언하는 작업 
def GetBiggerThan20(i):
    return i>20
print(type(GetBiggerThan20))

numList = [10,25,30]
#람다식,람다스타일 ,함수형 프로그래밍
#filter라는 것은 일반적으로 조건식에 사용함
#함수포인터 - c,c++개념 
# 클래스를 new를 하면 객체 
#이 안에는 클래스의 변수들과 메서드가 존재
#여기서 메서드만 따로 뽑아서 객체화 한다고 생각하면 그것이 바로 람다
# 이스타일은 사실 c ,c++스타일에 해당함 
iterList=filter(GetBiggerThan20,numList)#GetBiggerThan20 이거 자체를 메서드화 했기때문에 객체처럼 사용가능한것 
for i in iterList:
    print("item:{0}".format(i))

print(type(filter))    #filter는 뭔가 조건이 있을때 사용


# In[170]:


numList = [10,25,30]

# 여기서 보이는 스타일은 순수한 람다 스타일 
iterList=filter(lambda i:i>20,numList)   #이름이 없는 순수한 람다 형식 
for i in iterList:
    print("item:{0}".format(i))

 


# In[173]:


numList = [1,2,3]

def Add10(i):
    return i+10
#map는 주로 순수한 계산식들에 활용됨
for i in map(Add10,numList):
    print("item:{0}".format(i))


# In[174]:


retList=list(map((lambda i: i+10),numList))    # i자리에 numList 가 들어간다 ,...map때문에
print(retList)


# In[1]:


import time

l=range(400000)
# 현재 시간을 구해옵니다.
t=time.mktime(time.localtime())

#40만개를 뿌립니다
for i in l:
    print(i,)
    
#현재 시간을 구해서 이전에 구한 시간을 뺀다
#즉 for문 40만개를 도는데 걸린 시간을 측정할수 있다 ,
t1=time.mktime(time.localtime())-t

# 현재 시간 을 구해옵니다 
t=time.mktime(time.localtime())
# ㅣ(list)에 있는 값들을 for 를 돌면서 가져올것이다.
#각각을 str(i)에 지정해줄것인데
#join을 통해 각각을 병렬화 하고 고속화 할 수 있다 .
print(",".join(str(i)for i in l ))   #람다를 지원하는 것은 join

t2=time.mktime(time.localtime())-t

print("Take{0} seconds".format(t1))
print("Take{0} seconds".format(t2))


# In[ ]:


#메모리 계층 구조   (Memory )
#1.레지스터 Register
#2.캐시 Cache : sram
#3.메모리 memory :oram
#4.I/o(대표적인 장치는 디스크 ,모니터,키보드 등등)
#숫자가 작을수록 속도가 압도적으로 빠르다 


# In[ ]:





# In[ ]:





# In[ ]:




