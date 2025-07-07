maths = []
physics = []
russian = []
names = []
with open('DataSet.txt', 'r') as in_file:
    for line in in_file:
        current_line = line.strip().split(';')
        names.append(current_line[0])
        maths.append(int(current_line[1]))
        physics.append(int(current_line[2]))
        russian.append(int(current_line[3]))
out_file = open('Statistic.txt', 'w')
for i in range(len(maths)):
    out_file.write(str((maths[i] + physics[i] + russian[i]) / 3) + '\n')
if len(maths) > 0:
    out_file.write(str(sum(maths) / len(maths)) + ' ' +
                   str(sum(physics) / len(physics)) + ' ' +
                   str(sum(russian) / len(russian)))
out_file.close()
print(names)