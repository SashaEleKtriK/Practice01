string1 = " this is a string. "
string2 = " This is another string."
string3 = string1 + string2
print(string3)
print(len(string3))
print(len(string2))
print(len(string1))
print(string3.title())
print(string3.lower())
print(string1.upper())
print(string1.rstrip())
print(string2.lstrip())
print(string3.strip())
print(string3.strip('.'))
d = "qwerty"
ch = d[2]
print(ch)
chm = d[1:3]
print(chm)
chm = d[:3]
print(chm)
chm = d[1:]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)
# d[2] = "2"
first_int = 5
second_int = 9
divide = second_int / first_int
print(divide)
divide_reminder = second_int % first_int
print(divide_reminder)
exponentiation = second_int ** first_int
print(exponentiation)
param = "string" + str(15)
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", "{:7.3f}".format(n3))
a = 1 / 3
print("{:7.3f}".format(a))
a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
list1[0] = 55
list1[len(list1) - 1] = 1703
list1.append(1812)
list1.insert(5, 1991)
list1.pop(0)
print(list1)
list1.sort(reverse=True)
print(list1)
list2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2)
print(list2)
print(lis)
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(type(listseq))
print(listseq)
listseq.sort()
print(listseq)
D = {
    'food': 'Apple',
    'quantity': 4,
    'color': 'Red'
}
print(D['food'])
D['quantity'] += 10
print(D['quantity'])
dp = {}
name = input('Enter ur name: ')
age = input('Enter ur age: ')
sex = input('Enter ur sex (male/female): ')
dp['name'] = name
dp['age'] = age
dp['sex'] = sex
print(dp)
rec = {
    'name': {'firstname': 'Bob',
             'lastname': 'Smith'},
    'job': ['dev', 'mgr'],
    'age': 25}
print(f'{rec["name"]["firstname"]} {rec["name"]["lastname"]}')
print(rec["name"]["firstname"])
print(rec['job'])
rec['job'].append('janitor')
print(rec)
