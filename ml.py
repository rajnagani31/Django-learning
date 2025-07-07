a=[0,1,2,3,4,5]
b=a
a=b
print("a=b",a)
print(f"a:{a}")
print(f"b:{b}")
b[3]=100
a[3]=1000

print(b)
print(a)


# pshallow
import copy

original=[[1,2],[3,4]]
shallow=copy.copy(original)
print(f"original:{original}")

print(f"Shallow:{shallow}")

original[0][0]=10
shallow[0][1]=20
print(f"{original}")
print(f"{shallow}")

x=[1,2,3,4,5,6]
y=copy.deepcopy(x)

print(f"x:{x}")
print(f"y:{y}")
y[3]=50

x[3]=10

print(f"x:{x}")
print(f"y:{y}")
