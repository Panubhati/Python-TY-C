a=("One","Two","Three")
b= list(a)
b.remove(b[1])
a=tuple(b)
print(a)