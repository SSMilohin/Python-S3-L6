index_min = 0
index_max = 0
input_file = open('task3_input.txt', 'r', encoding='utf-8')
children = input_file.read().split("\n")
input_file.close()

for i in range(len(children)):
    data = children[i].split()
    children[i] = {'surname': data[0], 'name': data[1], 'age': float(data[2])}

    if children[i]['age'] > children[index_max]['age']:
        index_max = i
    if children[i]['age'] < children[index_min]['age']:
        index_min = i

output_file_min = open('task3_output_minimal.txt', 'w', encoding='utf-8')
print(children[index_min]['surname'], children[index_min]['name'], children[index_min]['age'], file=output_file_min)
output_file_min.close()

output_file_max = open('task3_output_maximal.txt', 'w', encoding='utf-8')
print(children[index_max]['surname'], children[index_max]['name'], children[index_max]['age'], file=output_file_max)
output_file_max.close()