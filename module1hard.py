grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sum1 = sum(grades[0])/len(grades[0])
sum2 = sum(grades[1])/len(grades[1])
sum3 = sum(grades[2])/len(grades[2])
sum4 = sum(grades[3])/len(grades[3])
sum5 = sum(grades[4])/len(grades[4])

sum6 = [sum1, sum2, sum3, sum4, sum5]
print(sum6)

students1 =sorted(list(students))
print(students1)

result = dict(zip(students1, sum6))
print(result)