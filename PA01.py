def topologische_sortierung(G):
	if len(G)==0:
		return []
	for x in G:
		x.predecessors=0
	for x in G:
		for s in x.successors:
			s.predecessors+=1
	zerolist=[]
	for x in G:
		if x.predecessors==0:
			zerolist.append(x)
	if zerolist==[]:
		return [-1]
	result=[]
	while len(zerolist)>0:
		for a in zerolist[0].successors:
			a.predecessors-=1
			if a.predecessors==0:
				zerolist.append(a)
		result.append(zerolist.pop(0))
	if len(result)!=len(G):
		return [-1]
	else:
		result2=[]
		for x in result:
			result2.append(x.name)
		return result2
		
#class Node:
	#pass
	
#A=Node()
#B=Node()
#C=Node()
#D=Node()
#E=Node()
#A.name="A"
#B.name="B"
#C.name="C"
#D.name="D"
#E.name="E"
#A.successors=[B]
#B.successors=[C,E]
#C.successors=[A]
#D.successors=[B]
#E.successors=[]
#G=[A,B,C,D,E]
