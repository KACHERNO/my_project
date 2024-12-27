import os
import b

print('Hello GIT !!!')
print("Indexing - it is important !!!")


ind = 0
sum = 0

while ind <= 9:
        sum += ind
        print(sum)
        ind += 1

print(b.any_func(2, sum))

print(os.getcwd())

s = 'Version Control System'
print(f'{s} - length is {len(s)} characters')
