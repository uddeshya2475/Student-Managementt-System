lst = []
while True:
    sum = 0
    choice = int(input())
    if choice == 1:
        lst.append('maagge')
    if choice == 2:
        lst.append('chai')


for i in lst:
    if i == 'maagge':
        sum += 10
    if i == 'chai':
        sum += 5
print("Hello world")
