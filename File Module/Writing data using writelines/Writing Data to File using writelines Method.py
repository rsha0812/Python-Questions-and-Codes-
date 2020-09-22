f = open('student1.txt',mode='w')
lst = ['Rahul\n','Sonam\n','Sumit\n','Rani\n','Raj\n']
f.writelines(lst)
f.close()
print('success')