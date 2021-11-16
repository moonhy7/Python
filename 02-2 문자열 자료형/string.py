# 문자열 사용(' ', " ", ''' ''', """ """)
hello = 'Hello, Python!'
print(hello)

hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)

# Python isn't difficult
s = "Python isn't difficult"
print(s)
# He said "Python is easy"
s = 'He said "Python is easy"'
print(s)
print("He said \"Python is easy\"")

# 문자열은 문자 여러개가 연속적으로 이어져 있는 시퀀스 자료형
# 문자열 상수(immutable 자료형) 요솟값을 바꿀 수 없다
s = "Life is too short, You need Python"
print(type(s)) # <class 'str'>
print('0123456789012345678901234567890123456789')
print(s[33]) # n
print(s) # Life is too short, You need Python
print(s[0]) # L
print(len(s)) # 34
print(s[-1]) # n
print(s[-2]) # o
print(s[len(s)-1]) # n
s1 = s[0] + s[1] + s[2] + s[3]
print(s1) # Life
print(s[0:4]) # Life
print(s[:4]) # Life
print(s[-6:]) # Python
print(s[:]) # Life is too short, You need Python
print(s[::-1]) # 역출력 nohtyP deen uoY ,trohs oot si efiL

# 슬라이싱
str = s[0] + s[1] + s[2] + s[3]
print(str) # Life
print(s[0:4]) # Life
print(s[19:]) # You need Python
print(s[:17]) # Life is too short
print(s[:]) # Life is too short, You need Python
print(s[19:-7]) # You need

data = '2021/11/16 11:11:11 Mon'
date = data[:10]
time = data[-12:]
print(date)
print(time)

# 문자열 조작하기(method 사용)
# - 문자열 바꾸기
text = 'Hello, world!'
print(text)
text = text.replace('world', 'python')
print(text)

# - 문자열 분리하기
list = 'apple pear grape pineapple orange'.split()
print(list)
list = 'apple, pear, grape, pineapple, orange'.split(', ')
print(list)

# - 구분자 문자열과 문자열 리스트 연결하기
fruit = '/'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(fruit)
print(type(fruit))

# - 대소문자 바꾸기
print('python'.upper());
print('PYTHON'.lower());

# - 공백삭제하기
txt1 = '     Python   '
print(txt1.lstrip())
print(txt1.rstrip())
print(txt1.strip())
print(len(txt1))
txt2 = txt1.strip()
print(len(txt2))

# - 특정 문자 삭제하기
txt2 = ', python.'
print(txt2.lstrip(',.'))
print(txt2.rstrip(',.'))
print(txt2.strip(',.'))

# (참고)구두점 삭제
import string
print(string)
print(string.punctuation)
print(txt2.strip(string.punctuation + ' '))

txt2 = ', python.'
print(txt2.strip(string.punctuation))
print(txt2.strip(string.punctuation + ' '))


# - 문자열 정렬하기
txt3 = 'Hello'
t =  txt3.rjust(10)
print(t)

# 메서드 체이닝
print('.'.join('python').upper().split('.'))

# - 문자열 왼쪽에 0 채우기
print('3500'.zfill(10))

# - 문자열 위치 찾기
print('apple pineapple'.find('pl'))






