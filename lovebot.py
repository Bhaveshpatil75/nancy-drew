
def love(x,y):
	z=x.strip()+'loves'+y.strip()
	a=''
	b=[]
	for i in z:
		if i not in a:
			a+=i
			b.append(z.count(i))
	while len(b)>2:
		l=[]
		for i in range(len(b)):
			if len(b)%2==0:
				if i<len(b)/2:
					l.append(b[i]+b[-i-1])
			else:
				if i<int(len(b)/2):
					l.append(b[i]+b[-i-1])
				elif i==int(len(b)/2):
					l.append(b[i])
		b=l

	m=str(b[0])+str(b[1])
	n=''
	if len(m)>2:
		if len(m)==3:
			n=str(int(m[0])+int(m[2]))+m[1]
			if int(n)>100:
				n=str(int(n[0])+int(n[2]))+n[1]
			return n+'%'
		else:
			n=str(int(m[0])+int(m[3]))+str(int(m[1])+int(m[2]))
			if int(n)>100:
				n=str(int(n[0])+int(n[2]))+n[1]
			return n+'%'
	else:
		if int(m)>100:
			m=str(int(m[0])+int(m[2]))+m[1]
		return m+'%'