class Node:
	def __init__(self,key):
		self.key=key
		self.left=None
		self.right=None
		self.p=None
		self.balance=0
		self.depth=0
	def calcbal(self):													##balance berechnen
		if self.left==None and self.right==None:
			self.balance=0
		elif self.left!=None and self.right==None:
			self.balance=-self.left.depth-1
		elif self.left==None and self.right!=None:
			self.balance=self.right.depth+1
		elif self.left!=None and self.right!=None:
			self.balance=self.right.depth-self.left.depth
	def calcdepth(self):												##tiefe berechnen
		if self.right!=None and self.left!=None:
			self.depth=max(self.left.depth,self.right.depth)+1
		elif self.right==None and self.left!=None:
			self.depth=self.left.depth+1
		elif self.left==None and self.right!=None:
			self.depth=self.right.depth+1
		elif self.left==None and self.right==None:
			self.depth=0
		
		
		
class AVLTree:
	def __init__(self,key):
		self.root=Node(key)
		self.nodestyle='circle,draw'
		self.edgestyle='blue, very thick'
		self.nodes=[self.root]											##alle Knoten werden abgespeichert
	def insert(self,key):
		insertnode=Node(key)
		self.nodes.append(insertnode)
		testnode=self.root
		trail=[testnode]
		while testnode.left!=None or testnode.right!=None:
			if insertnode.key<testnode.key and testnode.left!=None:
				testnode=testnode.left
				trail.append(testnode)
			elif insertnode.key>testnode.key and testnode.right!=None:
				testnode=testnode.right
				trail.append(testnode)
			else:
				break
		if insertnode.key<testnode.key:									##neuer Knoten wird unten angefügt
			testnode.left=insertnode
			insertnode.p=testnode		
		if insertnode.key>testnode.key:
			testnode.right=insertnode
			insertnode.p=testnode
			
		
		for k in range (len(trail)):									##für alle durchlaufenen Knoten wird die Tiefe um 1 erhöht
			if len(trail)-k > trail[k].depth:
				trail[k].depth+=1
				
				
		change=0
		for n in trail:
			n.calcbal()													##für alle durchlaufenen Knoten wird die Balance berechnet
			if n.balance not in [-1,0,1]:								##der letzte Knoten, der unbalanciert ist, wird abgespeicher
				nsave=n
				change=1		
		if change==1:													##falls es unbalancierte Knoten gab wird entsprechend rotiert
			n=nsave
			if n.balance==-2 and n.left.balance<=0:
				
				rotateright(self,n)
			elif n.balance==2 and n.right.balance>=0:
				
				rotateleft(self,n)
			elif n.balance==2 and n.right.balance==-1:
				
				rotateright(self,n.right)
				rotateleft(self,n)
			elif n.balance==-2 and n.left.balance==1:
				
				rotateleft(self,n.left)
				rotateright(self,n)
		
	def __str__(self):
		nodecoords=[]
		for n in self.nodes:
			nodecoords.append(str(coordcalc(n)))																				#koordinaten für visualisierung
		part1='\\documentclass[tikz]{standalone} \n\n \\begin{document} \n \\begin{tikzpicture}[every node/.style={'			##tikz dokument eröffnen und def
		part2=self.nodestyle																									##Text größtenteils aus Vorgabe übernommen
		part3='}, every edge/.style={draw,'																						##Probleme mit /n
		part4=self.edgestyle
		part5='}] \n\n % Hier stehen die Zeichen-Befehle. \n'
		part6=''
		for k in range (len(nodecoords)):	
			part6+='\coordinate (x' + str(self.nodes[k].key) + ') at ' + nodecoords[k] + '; \n'
		part7=''
		for n in self.nodes:
			part7+='\\node (n' + str(n.key) + ') at (x' + str(n.key) + ') {$' + str(n.key) + '$}; \n'
		part8=''
		for n in self.nodes:
			if n.p!=None:
				part8+='\draw (n' + str(n.p.key) + ') edge (n' + str(n.key) + '); \n'
		part9='\\end{tikzpicture} \n \\end{document}'
		
		return part1+part2+part3+part4+part5+part6+part7+part8+part9
		
	def visualize(self):
		import subprocess
		content=str(self)
		with open('avl.tex','w') as f:									##probleme mit mac-->unix, testen war schwierig, befehle über google gefunden
			f.write(content)											##.tex datei wird geschrieben
		commandline = subprocess.call(['pdflatex', 'avl.tex'])			
		commandline = subprocess.call(['evince','avl.pdf'])				##pdf datei wird geöffnet
		
	
				
				
def rotateright(T,n):													##Problem/Fehler: Rotationen außerhalb der Klasse definiert(weniger effizient)
		subroot=n.left
		n.left=subroot.right
		if subroot.right!=None:
			subroot.right.p=n
		subroot.p=n.p
		if n==T.root:
			T.root=subroot
		else:
			if n.p.left==n:
				n.p.left=subroot
			elif n.p.right==n:
				n.p.right=subroot
		subroot.right=n
		n.p=subroot
		if subroot.balance==-1:
			n.balance=0
			subroot.balance=0
		elif subroot.balance==0:
			n.balance=-1
			subroot.balance=1
		n.calcdepth()													##da keine Sorge um Laufzeit: Tiefe und Balance der veränderten Knoten einzeln berechnet
		subroot.calcdepth()
		x=subroot
		while x.p!=None:	
			x.p.calcdepth()
			x.p.calcbal()
			x=x.p
			
			

def rotateleft(T,n):
		subroot=n.right
		n.right=subroot.left
		if subroot.left!=None:
			subroot.left.p=n
		subroot.p=n.p
		if n==T.root:
			T.root=subroot
		else:
			if n.p.right==n:
				n.p.right=subroot
			if n.p.left==n:
				n.p.left=subroot
		subroot.left=n
		n.p=subroot
		if subroot.balance==1:
			n.balance=0
			subroot.balance=0
		elif subroot.balance==0:
			n.balance=1
			subroot.balance=-1
		n.calcdepth()
		subroot.calcdepth()
		x=subroot
		while x.p!=None:
			x.p.calcdepth()
			x.p.calcbal()
			x=x.p
		
def coordcalc(n):														##rekursive Berechnung der Koordinaten, da keine Sorge um Laufzeit
	if n.p==None:
		return (0,0)
	else:
		if n.p.left==n:
			return (coordcalc(n.p)[0]-(2**(n.depth)),coordcalc(n.p)[1]-1)
		if n.p.right==n:
			return (coordcalc(n.p)[0]+(2**(n.depth)),coordcalc(n.p)[1]-1)
		
		
			
		
T=AVLTree(12)
import random
l = [random.randint(1,1000) for i in range(100)]
l = list(set(l))
for x in l:
	T.insert(x)

#T.insert(2)
#T.insert(1)
#T.insert(9)
#T.insert(1000)
#T.insert(6)
#T.insert(-1000)
T.visualize()
		
		
			
			
