a = "harry"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#  a[3] = "d"  # does not work (only access do not change)
print(a[0:3])
print(a[0:4])  # string slicing
print(a[1:4])

print(a[:5])  # is same as 0 to 5
print(a[0:])  # as same as 0 to 5

print(a[-5])  # 0 - h
print(a[-4])  # 1 - a
print(a[-3])  # 2 - r
print(a[-2])  # 3 - r
print(a[-1])  # 4 - y
print(a[-0])  # 0 - h

print(a[-4:-1])  # is same as a[1:4]
