# This program demonstrates various set operations.
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# display members of the baseball set
print("the following students are on the baseball team: ")
for name in baseball:
    print(name)

# display members of the basketball set
print()
print("the following students are on the basktball team: ")
for name in basketball:
    print(name)

# demonstrate intersection
print()
print("The following students play both basebll and basketball")
for name in baseball.intersection(basketball):
    print(name)

# demonstrate union
print()
print("the following students play either baseball or basketball")
for name in baseball.union(basketball):
    print(name)

# Demonstrate difference of baseball and basketball
print()
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)
# Demonstrate difference of basketball and baseball
print()
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)
# Demonstrate symmetric difference
print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)
    