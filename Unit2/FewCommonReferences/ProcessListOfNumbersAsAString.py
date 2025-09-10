#expecting int values separated by spaces 10 20 30
input_str = input()

#convert each str value into list element
strList = input_str.split()
# pieces will be ['10', '20', '30']


#convert string element to integer and create a list
int_list = list(map(int,strList ))


print(int_list)

print(sum(int_list))