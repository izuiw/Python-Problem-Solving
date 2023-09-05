'''
#변수입력과 연산자
#a=input("숫자 입력 : ")
#print(a)

a, b = map(int, input("숫자입력 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a//b) #몫 연산자

print(a%b) #나머지 연산자

print(a**b) #제곱 연산자
'''

#=============================================

'''
조건문 if (분기, 중접) 


x=15
if x>=10:
    print("Lucky")
    print("!!!!!") #들여쓰기 주의 indentationError
    if x%2==1:
        print(
            "10이상의 홀수"
        )


x=9
if x>0:
    if x<10:
        print("10보다 작은 자연수")


x=7
if x > 0 and x < 10:
    print("10보다 작은 자연수 -and 연산자")

if 0<x<10:
    print("10보다작은 자연수이다")
'''

# 분기

x=10
if x>0:
    print("양수")
else:
    print("음수")


y=50
if y >= 90:
    print('A')
elif y >= 80:
    print('B')
elif y >= 70:
    print('C')
else:
    print("Fail")





