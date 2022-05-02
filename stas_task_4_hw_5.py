from pydoc import locate

object_name = input('Please enter your object \n')
method_name = locate(object_name) # Определяем объект
list_1 = list(dir(method_name))

i = 0

while list_1[i][0] == '_':
    list_1.remove(list_1[i])
    continue

print(list_1)