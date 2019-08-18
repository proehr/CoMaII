class Node:
	def __init__ ( self ):
		self.outgoing = []
		self.y = float ("inf")
		self.p = None
		
class Edge:
	def __init__ (self , v , w , c ):
		self.start = v
		self.target = w
		self.c = c
		v.outgoing.append (self)

class DirectedGraph:
	def __init__(self, V, E):
		self.vertices=V
		self.edges=E
		self.v=0
		
	def next_edge(self):
		self.v+=1
		if self.v<=(len(self.vertices)-1)*len(self.vertices):
			return self.edges[(self.v-1)%len(self.vertices)]
		else:
			return None
			
		
class DAG:
	def __init__(self, V, E):
		if len(V)==0:
			self.vertices=V
			self.edges=E
		for x in V:
			x.incoming=0
		for x in V:
			for s in x.outgoing:
				s.target.incoming+=1
		zerolist=[]
		for x in V:
			if x.incoming==0:
				zerolist.append(x)
		if zerolist==[]:
			self.vertices=V
			self.edges=E
		else:
			resultV=[]
			resultE=[]
			while len(zerolist)>0:
				for a in zerolist[0].outgoing:
					a.target.incoming-=1
					resultE.append(a)
					if a.target.incoming==0:
						zerolist.append(a.target)
				resultV.append(zerolist.pop(0))
			if len(resultV)!=len(V):
				self.vertices=V
				self.edges=E
			else:
				self.vertices=resultV
				self.edges=resultE
		self.v=0
	def next_edge(self):
		self.v+=1
		if self.v<=len(self.edges):
			return self.edges[self.v-1]
		else:
			return None
			
def ford(G,r):
	for v in G.vertices:
		v.y=float("inf")
		v.p=None
		
	r.y=0
	#if type(G)==DAG:
		#for x in range(len(G.vertices)):
			#e=G.next_edge()
			#if e.target.y>e.start.y + e.c:
				#e.target.y=e.start.y + e.c
				#e.target.p=e.start
	#elif type(G)==DirectedGraph:
		#for x in range(len(G.vertices)-1):
			#for w in range(len(G.vertices)):
				#e=G.next_edge()
				#if e.target.y>e.start.y + e.c:
					#e.target.y=e.start.y + e.c
					#e.target.p=e.start
	e=G.next_edge()			
	while e!=None:
		if e.target.y>e.start.y + e.c:
			e.target.y=e.start.y + e.c
			e.target.p=e.start
		e=G.next_edge()	
	G.v=0

	
		
		
nodes = [Node() for _ in range(4)]
e1 = Edge ( nodes [0] , nodes [1] , 1 )
e2 = Edge ( nodes [0] , nodes [2] , 1 )
e3 = Edge ( nodes [1] , nodes [3] , 3 )
e4 = Edge ( nodes [2] , nodes [3] , 1 )
e1.name = 1
e2.name = 2
e3.name = 3
e4.name = 4
G = DAG(nodes,[e4,e3,e2,e1])
F= DirectedGraph(nodes,[e4,e3,e2,e1])
