f = open('test3.txt','r')
body = f.read()
f.close
##print(body)
body = body.replace('java','python')
##print(body)
f = open('test3.txt','w')
f.write(body)
f.close