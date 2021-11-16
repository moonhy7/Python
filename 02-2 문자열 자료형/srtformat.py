# 문자열 서식 지정자(%)와 포캐팅(format 메서드) 사용하기

# -%s
country = 'korean'
print('I am %s' % country)

# -%d
age = 28
st = 'I am %d years old' % age
print(st)

# -%f
print("Error is %f%%" % 99.99)
print('%.3f' % 3.0)
print('%10.2f' % 3.141592)

# - 서식지정(%)로 문자열 안에 여러 값 넣기
st = "Today is %d %s" % (16, 'November')
print(st)

# ========================================================

#format 메서드 사용: '{인덱스}'.format(값)
st = 'Hello, {0}'.format('world!')
print(st)

language = 'Python'
version = '3.10.0'
st = f'Hello, {language} {version}'
print(st)

# - 천단위 콤마(,) 넣기 : format(숫자, ',')
st = format(10000000, ',')
print(st)

# - 서식지정자 + format함수
st = '%08d' % 300000
print(st)
print('**************************')

# ========================================================

# Q) path = 'C:\\Users\\AppData\\Local\\Programs\\Python3\\python.exe'
#   ---------------------------------------
#   print(filename) 실행결과
#   python.exe' 이렇게 나오도록 할 것

# A)
path = 'C:\\Users\\AppData\\Local\\Programs\\Python3\\python.exe'
filename = path.split('\\')[-1]
print(filename)

