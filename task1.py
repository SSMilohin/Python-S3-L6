input_file = open('task1_input.txt', 'r')
numbersList = list(map(int, input_file.read().split()))
print(numbersList)
input_file.close()

output_file = open('task1_output.txt', 'w')
product = 1
for i in range(len(numbersList)):
    product *= numbersList[i]
output_file.write(str(product))
output_file.close()