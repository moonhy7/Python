# 리스트 조작하기

# - 요소 추가(append, extend, insert)
a = ['a', 'b', 'c']
b = ['d', 'e']
a.extend(b) # extend : b의 원소들이 들어감
print('a.extend(b) = {0}'.format(a))

a = ['a', 'b', 'c']
b = ['d', 'e']
print('a + b = {0}'.format(a + b))

a = ['a', 'b', 'c']
b = ['d', 'e']
a.append(b) # append : b 자체가 들어감
print('a.append(b) = {0}'.format(a))

a = ['a', 'b', 'c']
b = ['d', 'e']
a.insert(len(a), b) # insert : 들어갈 위치까지 알려줌
print('a.insert(len(a), b) = {0}'.format(a))

a = ['a', 'b', 'c']
b = ['d', 'e']
a.insert(1, b) # 인덱스 1 자리에 들어감
print('a.insert(1, b) = {0}'.format(a))

# - 요소 삭제하기(del 리스트[], pop, remove, clear)
a = ['a', 'b', 'c']
print(a)
a.pop()
print(f'a.pop() = {a}')
a.pop(0)
print(a)

li = ['a', 'b', 'x']
print(f'li = {li}')
li.remove('b')
print(f"li.remove('b') = {li}")
li.clear()
print(f'li.clear = {li}')

# - 리스트가 비어 있는가? 아닌가?
li = []
print("li = {0}".format(li))

print(f'bool(" ") = {bool(" ")}')
print(f'bool("Hello") = {bool("Hello")}')
print(f'bool("False") = {bool("False")}')
print(f'bool([0,1,2]) = {bool([0,1,2])}')
print(f'bool([]) = {bool([])}')
print(f'bool() = {bool()}')

if not li:
    li.append(100) # 들여쓰기 안하면 if문이 소속이 아니게됨
print(li)

# - 리스트의 할당과 복사
a = list(range(3))
print('a = {0}'.format(a))

b = a
print(id(a))
print(id(b))
print(a is b)
b.append(3)
print('a={0}'.format(a))
print('b={0}'.format(b))
print(f'a is b = {a is b}')

a = [0,0,0]
b = a.copy()
b [2] = 99
print(a, b)

# 반복문 (for, while) 사용
li = list(range(10))
print("li = {0}".format(li))

for i in li :
    print(i, end = ' ')

print()

for i in range(3) :
    print(i, end = '*')

print()

for c in 'Hello' :
    print(c, end = '.')

print()

i = 0;
while i < len(li):
    print(li[i], end='/')
    i += 1
print()
print('*********')

# 리스트 표현식 사용하기([식 for 변수 in 리스트])
a = list(range(10))
print('a={0}'.format(a))

a= [34, 52, 92, 14, 13]
print(a)
for idx in range(len(a)):
    a[idx] *= 100 # 모든 원소에 100 곱하기
print(a)

a = list(range(10))
print('a={0}'.format(a)) 

b = [i*100 for i in range(10)]
print('b={0}'.format(b)) # 모든 원소에 100 곱하기

c = [i for i in range(10) if i % 2 == 0] # 짝수 리스트 생성
print('c = {0}'.format(c))

# - 구구단 출력 리스트 만들기
li = []
for i in range(8):
    for j in range(9):
        li.append((i+2)*(j+1))
print(li)

print()
li = []
for i in range(2, 10):
    for j in range(1, 10):
        li.append(i*j)
print(li)

print()
e = [i*j for i in range(2, 10) for j in range(1, 10)]
print('e = {0}'.format(e))
    
