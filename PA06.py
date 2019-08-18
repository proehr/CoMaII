class Node:
	def __init__(self,key,data):
		self.key=key
		self.left=None
		self.right=None
		self.p=None
		self.data=data
		self.balance=0
		self.s=1
	
		
class SplayTree:
	def __init__(self,key,data):
		self.root=Node(key,data)
		self.nodes=[self.root]
		self.R=0
		
		
	def rotateleft(self,x):
		y=x.right
		if x.p==None:
			self.root=y
		elif x.p.left==x:
			x.p.left=y
		else:
			x.p.right=y
		y.p=x.p
		x.right=y.left
		if x.right!=None:
			x.right.p=x
		y.left=x
		x.p=y
		y.s=x.s
		if x.left!=None and x.right!=None:
			x.s=1+x.left.s+x.right.s
		elif x.left==None and x.right!=None:
			x.s=1+x.right.s
		elif x.left!=None and x.right==None:
			x.s=1+x.left.s
		else:
			x.s=1
		
	def rotateright(self,x):
		y=x.left
		if x.p==None:
			self.root=y
		elif x.p.right==x:
			x.p.right=y
		else:
			x.p.left=y
		y.p=x.p
		x.left=y.right
		if x.left!=None:
			x.left.p=x
		y.right=x
		x.p=y
		y.s=x.s
		if x.left!=None and x.right!=None:
			x.s=1+x.left.s+x.right.s
		elif x.left==None and x.right!=None:
			x.s=1+x.right.s
		elif x.left!=None and x.right==None:
			x.s=1+x.left.s
		else:
			x.s=1
		
			
	def splayingstep(self,x):
		if x.p==None:
			pass
		elif x.p.p==None and x==x.p.left:
			self.rotateright(x.p)
			self.R+=1
		elif x.p.p==None and x==x.p.right:
			self.rotateleft(x.p)
			self.R+=1
		elif x==x.p.left and x.p==x.p.p.left:
			self.rotateright(x.p.p)
			self.rotateright(x.p)
			self.R+=2
		elif x == x.p.right and x.p == x.p.p.right:
			self.rotateleft(x.p.p)
			self.rotateleft(x.p)
			self.R+=2
		elif x == x.p.left and x.p == x.p.p.right:
			self.rotateright(x.p)
			self.rotateleft(x.p)
			self.R+=2
		else: 
			self.rotateleft(x.p)
			self.rotateright(x.p)
			self.R+=2
	def Splay(self, x):
		self.R=0
		xbefore=x.s
		potentialbefore=1
		for n in self.nodes:
			potentialbefore*=n.s
		while x.p!=None:
			self.splayingstep(x)
		potentialafter=1
		for n in self.nodes:
			potentialafter*=n.s
		print('Splay an Knoten: ' + str(x.key))
		print('2^Rotationen: ' + str(2**self.R))
		print('2^Potential vorher: ' + str(potentialbefore))
		print('2^Potential nachher: ' + str(potentialafter))
		print('2^armortisierte Rotationen: ' + str(2**(self.R)*potentialafter) + '/' + str(potentialbefore))
		print('2^obere Schranke: ' + str(2*self.root.s**3)+'/'+str(xbefore**3))
		
	def insert(self,key,data):
		z=Node(key,data)
		self.nodes.append(z)
		y=None
		x=self.root
		while x!=None:
			y=x
			y.s+=1
			if z.key<x.key:
				x=x.left
			else:
				x=x.right
		z.p=y
		if y==None:
			self.root=z
		elif z.key<y.key:
			y.left=z
		else:
			y.right=z
		self.Splay(z)
	def search(self,key):
		y=None
		x=self.root
		found=0
		while x!=None:
			y=x
			if key<x.key:
				x=x.left
			elif key>x.key:
				x=x.right
			else:
				y=x
				found=1
				break
		self.Splay(y)
		if found==1:
			return y
		else:
			return None
	def transplant(self,u,v):
		if u.p==None:
			self.root=v
		elif u==u.p.left:
			u.p.left=v
		else:
			u.p.right=v
		if v!=None:
			v.p=u.p
	def delete(self,key):
		xdel=self.search(key)
		if len(self.nodes)<=1:
			pass
		else:
			if xdel!=None:
				self.nodes.remove(xdel)		
				if xdel.left==None:
					self.transplant(xdel,xdel.right)
				elif xdel.right==None:
					self.transplant(xdel,xdel.left)
				else:
					x=xdel.right
					while x.left!=None:
						x=x.left
					if x.p!=xdel:
						z=x
						while z!=None:
							z.s-=1
							z=z.p
						self.transplant(x,x.right)
						x.right=xdel.right
						x.right.p=x
					self.transplant(xdel,x)
					x.left=xdel.left
					x.left.p=x
					x.s=len(self.nodes)
	
	
	
		
	
T = SplayTree ( 10 , 10 )
#for i in range ( 9,4, - 1 ):
T.insert (8 , 8 )	



		
	
		
			
			
