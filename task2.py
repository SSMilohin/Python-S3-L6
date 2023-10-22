input_file = open('task2_input.txt', 'r')
numbersList = sorted(list(map(int, input_file.read().split())))
input_file.close()

output_file = open('task2_output.txt', 'w')
for i in range(len(numbersList)):
    output_file.write(str(numbersList[i]) + "\n")
output_file.close()