#Q1
print((80+75+55)/3)

#Q2
print(bool(13%2),14%2,13%2)

#Q3
pin = "881120-1068234"
pin_temp = pin.split('-')
num = pin_temp.pop()
yyyymmdd = pin_temp.pop()
print(num)

#Q4
pin = "881120-1068234"
print(pin[-1])

#Q5
a = "a:b:c:d"
b = a.replace(':',"#")
print(b)

#Q6
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#Q7
a = ['life','is','too','short']
print("".join(a))

#Q8
a=(1,2,3)
b=(4,)
print(a+b)

#Q9
a=dict()
print(a)
a['name'] = 'python'
a[('a',)]='python'
#a[[1]]='python'
a[250]='python'
print(a)

#Q10
a={'A':40,"B":80,"C":70}
del a["B"]
result = a
print(result)

#Q11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#Q12
a=b=[1,2,3]
a[1]=4
print(b)