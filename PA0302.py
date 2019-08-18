def toposort(G):				#angepasster Algorithmus zur topologischen Sortierung
	resultV=[]
	for r in G.vertices:
		r.color="white"
	for r in G.vertices:
		if r.color == "white":
			r.color="red"
			Q=[r]
			while not len(Q) == 0:
				v=Q[-1]
				i=0
				while len(v.outgoing) > i and v.outgoing[i].target.color == "orange":
					i += 1
				if len(v.outgoing) > i:
					if v.outgoing[i].target.color == "white":
						w = v.outgoing[i].target
						w.color="red"
						Q.append(w)
					else:
						return [-1]
				else:
					resultV.append(v)
					v.color="orange"
					Q.pop()
	resultV.reverse()
	return resultV

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
		
class AbstractGraph:
	def __init__ (self ,V , E ):
		self.vertices = V
		self.edges = E
	def next_edge ( self ):
		pass

class DirectedGraph(AbstractGraph):					
	def __init__(self, V, E):
		AbstractGraph.__init__(self,V,E)
		self.v=0									#Zählvariable, kann bei bedarf zurückgesetzt werden
		self.elist=[]								#erstelle Liste, in der die ursprüngliche Kantenreihenfolge beibehalten wird
		for i in range(len(self.vertices)-1):		#und n mal wiederholt wird
			self.elist+=self.edges
			
	def next_edge(self):
		self.v+=1
		if self.v<=len(self.elist):					#gebe nächstes Element aus, Zähler größer als Länge der Liste ist
			return self.elist[self.v-1]
		else:
			return None
			
		
class DAG(AbstractGraph):
	def __init__(self, V, E):
		AbstractGraph.__init__(self,V,E)
		self.topvertices=toposort(self)				#Knoten werden topologisch sortiert
		self.topedges=[]
		for x in self.topvertices:
			self.topedges+=x.outgoing				#Kanten werden anhand der Knotenliste topologisch sortiert
		self.v=0
	def next_edge(self):
		self.v+=1									#gleiches Prinzip wie DirectedGraph
		if self.v<=len(self.topedges):
			return self.topedges[self.v-1]
		else:
			return None
			
def ford(G,r):										#normaler Ford-Algorithmus
	for v in G.vertices:
		v.y=float("inf")
		v.p=None
		
	r.y=0

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
