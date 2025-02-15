# chala dasturchi kodi 
my_list = [1,2,3,4,5,6,7,8,9,10]
result = []
for num in my_list:
    if num % 2 == 0:
        result.append(num)
print(result)

# opitniy dasturchi kodi 
print([num for num in range(1,11) if num % 2 == 0])
 