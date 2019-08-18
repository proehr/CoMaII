class UnionFind:
	def __init__(self):
		self.p=[]
	def make_set(self):
		self.p.append(-1)
	def find_set(self,i):
		if self.p[i]<0:
			return i
		else:
			x=i
			xlist=[]
			while self.p[x]>=0:
				xlist.append(x)
				x=self.p[x]
			for v in xlist:
				self.p[v]=x
			return x
	def union(self,i,j):
		y=self.find_set(i)
		z=self.find_set(j)
		if self.p[y]<=self.p[z]:
				self.p[y]=self.p[y]+self.p[z]
				self.p[z]=y
		else:
				self.p[z]=self.p[y]+self.p[z]
				self.p[y]=z
		
			
class Edge:
	__slots__=["incident","w"]
	def __init__(self, v1, v2, w):
		self.incident={v1,v2}
		self.w=w
		
def kruskal(I):
	elist=[]
	X=UnionFind()
	for v in I:
		X.make_set()
		for e in v:
			elist.append(e)
	elist.sort(key=lambda x:x.w)
	result=[]
	for e in elist:
		v1=e.incident.pop()
		v2=e.incident.pop()
		e.incident={v1,v2}
		if X.find_set(v1)!=X.find_set(v2):
			X.union(v1,v2)
			result.append(e)
	return result
	
e1=Edge(0,2,4)
e2=Edge(2,1,3)
e3=Edge(0,1,2)
I = [[ e1 , e3 ] ,[ e2 , e3 ] ,[ e1 , e2 ]]
		
		
		
		
		
