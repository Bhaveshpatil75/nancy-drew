
s="q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"

st=s.split()
t=[]
for i in st:
    t.append(i.capitalize())

res=""
k=0
for i in s:
    if i==" ":
        res+=i
    else:
        res+=t[k]
        k+=1

print(res)