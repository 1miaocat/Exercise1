classA, classB, classC = 32, 45, 51
class1_student, class1_left = divmod(classA,5)
class2_student, class2_left = divmod(classB,7)
class3_student, class3_left = divmod(classC,6)

print('Number of students in each group: ')
print('Class1: ', class1_student)
print('Class2: ', class2_student)
print('Class3: ', class3_student)

print('Number of students leftover: ')
print('Class1: ', class1_left)
print('Class2: ', class2_left)
print('Class3: ', class3_left)
