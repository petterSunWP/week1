large_number = 100_000_000
print(large_number)

x,_,y = (0,'ignore',1)
print(x,y,_)

names = ['Alice','Bob','cathy']
ages = [12,13,14]
paired = zip(names,ages)

print(type(paired),paired)

ids = [1,2,3]
names = ['Alice','Bod','Cathy','Mike']
grades = ['A','B','A+','A']
zipped = zip(ids,names,grades)
unzipped = list(zip(*zipped))
print(unzipped)
keys = ['ids', 'names', 'grades']
unzipped_dict = dict(zip(keys, unzipped))
print(unzipped_dict)

data = []
a = 2
for i in range(5):
    data.append(lambda a,i=i*2: i*a)
print(type(data))
print(data[4](3))

for x in data:
    print(x(a))