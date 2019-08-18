import copy
import time
from tkinter import *

class Life:
	def __init__(self,S,rule,b):
		self.grid=S
		self.ruleone,self.rulezero=rule.split('/')
		self.b=b
		if b==1:
			self.edge=0
		if b==2:
			self.edge=1
		self.M=len(self.grid[0])
		self.N=len(self.grid)
		
	def countone(self,i,j):
		n=0
		for x in range(i-1,i+2):
			for y in range(j-1,j+2):
				#print(x,y)
				if x==i and y==j:
					#print('Nothing')
					pass
				elif x < 0  or y < 0:
					#print('too small')
					n+=self.edge
				elif x >= self.N or y >= self.M:
					#print('too big')
					n+=self.edge
				else:
					#print('inside')
					n+=self.grid[x][y]
		return n
	
	def counttwo(self,i,j):
		n=0
		for x in [i-1,i,i+1]:
			for y in [j-1,j,j+1]:
				if x==i and y==j:
					pass
				elif x!=self.N and y!=self.M:
					n+=self.grid[x][y]
				elif x!=self.N and y==self.M:
					n+=self.grid[x][0]
				elif x==self.N and y!=self.M:
					n+=self.grid[0][y]
				else:
					n+=self.grid[0][0]
		return n
		
	def tick(self):
		newgrid=copy.deepcopy(self.grid)
		for i in range(self.N):
			for j in range(self.M):
				if self.b==3:
					save=self.counttwo(i,j)
				elif self.b in [1,2]:
					save=self.countone(i,j)
				#print(save)
				if self.grid[i][j]==1:
					if str(save) in self.ruleone:
						newgrid[i][j]=1
					else:
						newgrid[i][j]=0
				elif self.grid[i][j]==0:
					if str(save) in self.rulezero:
						newgrid[i][j]=1
					else:
						newgrid[i][j]=0
		self.grid=copy.deepcopy(newgrid)
	
	def __str__(self):
		string=''
		for i in range(self.N):
			if i!=0:
				string+='\n'	
			for j in range(self.M):
				string+=str(self.grid[i][j])
		return string	
	
	def run(self):
		while 1:
			print(self.__str__())
			time.sleep(1)
			self.tick()
			
class startpage:
	def __init__(self,master):
		self.title=('Game of Life')
		self.label1=Label(master,text='Höhe')
		self.label2=Label(master,text='Breite')
		self.label3=Label(master,text='Bitte geben sie Höhe und Breite an')
		self.label1.grid(row=0,column=0)
		self.label2.grid(row=1,column=0)
		self.label3.grid(row=2,column=1)
		self.nentry=Entry(master,bd=5)
		self.mentry=Entry(master,bd=5)
		self.nentry.grid(row=0,column=1)
		self.mentry.grid(row=1,column=1)
		self.createbutton=Button(master,text='Erzeuge Spielfeld',height=1,width=15,command=self.create)
		self.createbutton.grid(row=3,column=1)
	def create(self):
		n=self.nentry.get()
		m=self.mentry.get()
		root.destroy()
		gridtk(n,m)
		
class gridtk:
	def __init__(self,n,m):
		root2=Tk()
		self.n=int(n)
		self.m=int(m)
		self.gridlist=[[0 for j in range(self.m)]for i in range(self.n)]
		self.label1=Label(root2,text='Regel')
		self.label2=Label(root2,text='Rand')
		self.label3=Label(root2,text='Q1')
		self.label4=Label(root2,text='Q0')
		self.label1.grid(row=0,column=1)
		self.label2.grid(row=0,column=2)
		self.label3.grid(row=1,column=0)
		self.label4.grid(row=2,column=0)
		self.q1entry=Entry(root2,bd=5,width=10)
		self.q0entry=Entry(root2,bd=5,width=10)
		self.q1entry.grid(row=1,column=1)
		self.q0entry.grid(row=2,column=1)
		self.v=StringVar(root2)
		self.v.set('1')
		self.randentry=OptionMenu(root2,self.v,'1','2','3')
		self.randentry.grid(row=1,column=2)
		self.buttonlist=[]
		for i in range(self.n):
			self.buttonlist.append([])
			for j in range(self.m):
				x=Button(root2,background='linen')
				self.buttonlist[i].append(x)
				self.buttonlist[i][j].config(command=self.gridpress(i,j))
				self.buttonlist[i][j].grid(row=i+3,column=j)
				
	def gridpress(self,i,j):
		if self.gridlist[i][j]==0:
			self.gridlist[i][j]=1
			self.buttonlist[i][j].config(background='black')
		elif self.gridlist[i][j]==1:
			self.gridlist[i][j]=0
			self.buttonlist[i][j].config(background='linen')

root=Tk()
lifefenster=startpage(root)
root.mainloop()
			
lifefenster.mainloop()	
#seed = [[ 0 ,0 ,0 , 0 ] ,[0 ,1 ,1, 0 ] ,[0 ,0 ,0 , 0 ]]
#T=Life(seed,'23/2',3)	
				
		
