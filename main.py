'''
1. 1부터 n까지 홀수 출력하기
2. 1부터 n까지 의 합 구하기
3. n의 약수출력하기

n=int(input())

for i in range(1, n+1):
    print(i)
'''

#n=int(input())
n=10

for i in range(1, n+1):
    if i%2==1:
        print(i)
print("=====================")
sum=0
for i in range(1, n+1): 
    sum=sum+i
    if i==n:
        print(sum)

print("=====================")

for i in range(1, n+1):
    if n%i==0:
        print(i, end='  ')


print("\n=====================")

'''
중첩 반복문 (2중 for문)



for i in range(5):
    print('i : ', i , sep='', end='  ')
    for j in range(5):
        print('j : ', j, sep='', end="  ")
    print()
'''

for num in range(5):
    for star in range(5-num):
        print("*", end= ' ')
    print()

'''
문자열과 내장함수
'''

msg= "It is Time"

#upper() : 출력값을 대문자로 변경 / 기존 데이터를 변경하는 것은 아님
#lower() : 소문자로 변경

print(msg.upper())
print(msg)
print(msg.lower())

#find() : 인덱스 번호 리턴 (-1 : 없으면 -1 리턴값 오는 듯)
#count() : 갯수 리턴

tmp=msg.lower()
print()
print(tmp.find('t'))
print(tmp.count('t'))

print(msg)
print(msg[:2]) #[:n] 0~n번째 까지의 값 출력
print(msg[3:5]) #[n:j] n~j번쨰 까지의 값 출력

#len() : 공백포함/ 문자길이 출력
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    if x.isupper(): #isupper() -> 대문자일 때 참
        print(x, "X: ",end=' ')
    if x.islower():
        print(x, end=' ')
print("\n\n\n")

for x in msg:
    if x.isalpha(): #isalpha -> 알파벳 출력 / 공백제거
        print (x, end=' ')

print()


#아스키넘버
tmp="AZ"
for x in tmp:
    print(ord(x)) #ord >> 아스키 넘버 출력 A==65 / Z==90


tmp="az"
for x in tmp:
    print(ord(x)) #a==97 / z== 122

tmp=65
print(chr(tmp)) #아스키넘버 -> 알파벳