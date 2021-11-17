# 리스트 생성: [,,,]
print(type([]))

score = [80, 90, 100]
print(score)

person = ['james', 17, 173.5, True]
print(person)

score = []
# score[0] = 98 # IndexError: list assignment index out of range 
score.append(100)
print(score)

# - range()를 사용하여 리스트 생성
r = range(10)
print(type(r))

li = list(range(10))
print(li)
print('li = {0}'.format(li))

li = list(range(5, 12))
print(f'list(range(5, 12)) = {li}')

li = list(range(-4, 10, 2))
print('list(range(-4, 10, 2)) = {0}'.format(li))

li = list(range(10, 0, -1))
print("list(range(10, 0, -1)) = {0}".format(li))

# 시퀀스(sequence) 자료형 : 값이 연속적으로 순서를 가지는 자료형
# 시퀀스 자료형 (list, tuple, str)

# -in 사용
index = list(range(10))
print('index={0}'.format(index))
print(5 in index)
print(11 in index)
print('n' in 'Python')
print('a' in ('a', 'b', 'c'))

# - '+', '*' 연산자 사용
a = ['a', 'b', 'c']
b = ['d', 'e']
print('a + b = {0}'.format(a + b))
print("Hello, " + "world")

li = [1, 2, 3]
print(li * 3)
print(('a', 'b', 'c') * 3)
print("Hello~ " * 5)
print('###############')

# - 인덱스 사용
li = [1, 2, 3]
print(li)
print(li[0])
print(li.__getitem__(2))
print('Hello'[0])
print((10, 20, 30)[-1])


li = [1, 2, 3]
print(li)
li[2] = 5
print(li)

# - 값 삭제
del li[2]
print(li)

orgl = list(range(0, 10)) # orgl = original list 
print(orgl)

del orgl[-4:-1]
print(orgl)
