# try:
#     file = open('Day30_Json/a_file.txt')
#     a_dictionary = {'key':'value'}
#     # print(a_dictionary['aa'])
# except FileNotFoundError as err:
#     print('there was an error', err)
#     file = open('Day30_Json/a_file.txt', 'w')
#     file.write('something')
# except KeyError as err:
#     print('that key does not exist', err)
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError
#     file.close()
#     print('File was closed')

height = float(input('Height: '))
weight = int(input("Weight: "))

# We can raise our own exception, for example in this case the height should never be over 3m
if height > 3:
    raise ValueError('Human height should not be over 3 meters')

bmi = weight / height ** 2
print(bmi)
