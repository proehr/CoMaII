class LinkedList :
	def __init__ ( self ):
		self.head = None
	def isEmpty ( self ):
		return self.head == None
	def insert (self , node ):
		node.setNext ( self.head )
		self.head = node
	def search (self , key ):
		current = self.head
		found = None
		while current != None and found == None :
			if current.getKey () == key :
				found = current
			else:
				current = current.getNext ()
			return found
			
class Node :
	def __init__ (self , key ):
		self.key = key
		self.next = None
	def getKey ( self ):
		return self.key
	def getNext ( self ):
		return self.next
	def setKey (self , key ):
		self.key = key
	def setNext (self , node ):
		self.next = node
		
def merge(L1,L2):				#hier wird das gleiche Prinzip verwendet
	if L1.isEmpty():			#wie bei dem vorher bekannten MergeSort
		return L2
	if L2.isEmpty():
		return L1
	L3=LinkedList()
	dummy=Node(None)
	L3.insert(dummy)
	while not (L1.isEmpty() or L2.isEmpty()):
		if L1.head.getKey()<L2.head.getKey():
			x=L1.head
			L1.head=L1.head.getNext()
		else:
			x=L2.head
			L2.head=L2.head.getNext()
		dummy.setNext(x)
		dummy=dummy.getNext()
	
	if L1.isEmpty():
		dummy.setNext(L2.head)
	if L2.isEmpty():
		dummy.setNext(L1.head)
		
	L3.head=L3.head.getNext()
		
	return L3
		
	

a=Node(1)
b=Node(3)
c=Node(5)
d=Node(6)
e=Node(9)
f=Node(2)
g=Node(4)
h=Node(7)
i=Node(8)
a.setNext(b)
b.setNext(c)
c.setNext(d)
d.setNext(e)

f.setNext(g)
g.setNext(h)
h.setNext(i)
L1=LinkedList()
L2=LinkedList()
L1.head=a
L2.head=f
