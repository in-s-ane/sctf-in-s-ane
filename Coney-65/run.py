hidden = "xU2FsdGVkX1/seMYknjQGW971EboRgFcx+jfczzdSrWMjt1xwRrPnQBbEsz+Mt7dA4xxsOVB88e8VGl70PK"
output = ""
for char in hidden:
    if char == '/' or char == '+':
        output += char
    else:
        output += str(ord(char))
print output
n = eval(output) #1061029912289326634121429830731764918786386758167948780724603197
n = str(n)
print n

temp = ""
answer = ""
for char in n:
    temp += char
    if int(temp) >= 30:
        answer += chr(int(temp))
        temp = ""

print answer