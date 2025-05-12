
# Online Python - IDE, Editor, Compiler, Interpreter

n = int(input("numero:"))
primos = []
criba = list(range(2,n+1))
while criba!=[]:
    m = min(criba)
    primos.append(m)
    for i in range(m,n+1,m):
        if i in criba:
            criba.remove(i)
            
print(primos)