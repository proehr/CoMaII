import copy
import time
from tkinter import *
import math

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
		
	def countone(self,i,j):												###counts surrounding 1's for rule 1 and 2, self.edge predefined
		n=0
		for x in range(i-1,i+2):
			for y in range(j-1,j+2):
				#print(x,y)
				if x==i and y==j:										##dont count self
					#print('Nothing')
					pass
				elif x < 0  or y < 0:									##edge above or left
					#print('too small')
					n+=self.edge
				elif x >= self.N or y >= self.M:						##edge under or right
					#print('too big')
					n+=self.edge
				else:													##(x,y) inside the grid
					#print('inside')
					n+=self.grid[x][y]
		return n
	
	def counttwo(self,i,j):												###counts surrounding 1's for rule 3
		n=0
		for x in [i-1,i,i+1]:
			for y in [j-1,j,j+1]:
				if x==i and y==j:										##dont count self
					pass
				elif x!=self.N and y!=self.M:							##(x,y) inside grid or above,left
					n+=self.grid[x][y]
				elif x!=self.N and y==self.M:							##(x,y) right 
					n+=self.grid[x][0]
				elif x==self.N and y!=self.M:							##(x,y) under grid
					n+=self.grid[0][y]
				else:													##(x,y)=(N,M)
					n+=self.grid[0][0]
		return n
		
	def tick(self):
		newgrid=copy.deepcopy(self.grid)								##deepcopy to copy all lists inside list
		for i in range(self.N):
			for j in range(self.M):
				if self.b==3:
					save=self.counttwo(i,j) 							##count 1's for all grid elements in old grid
				elif self.b in [1,2]:
					save=self.countone(i,j)
				#print(save)
				if self.grid[i][j]==1:									##apply rule for 1's into new grid
					if str(save) in self.ruleone:
						newgrid[i][j]=1
					else:
						newgrid[i][j]=0
				elif self.grid[i][j]==0:								##apply rule for 0's into new grid
					if str(save) in self.rulezero:
						newgrid[i][j]=1
					else:
						newgrid[i][j]=0
		self.grid=copy.deepcopy(newgrid)								##apply new grid as self.grid
	
	def __str__(self):
		string=''
		for i in range(self.N):				
			if i!=0:													##\n after each line
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
		gridtk(n,m)														##open up a new window
		
class gridtk:
	def __init__(self,n,m,size=30):
		root2=Tk()
		self.master=root2
		self.n=int(n)
		self.m=int(m)
		self.size=size
		rootsize=str(self.size*(self.m+1))+'x'+str(size*(self.n+1)+60)
		root2.wm_geometry(rootsize)
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
		var=IntVar()
		self.c_width=self.size*self.m+10
		self.c_height=self.size*self.n+10
		self.c=Canvas(root2,width=self.c_width,height=self.size*self.c_height)
		self.c.place(x=10,y=75)
		for i in range(self.n+1):
			self.c.create_line(5, self.size*i+5, self.c_width-5, self.size*i+5)
		for i in range(self.m+1):
			self.c.create_line(self.size*i+5, 5, self.size*i+5, self.c_height-5)
		for x in range(self.m):
			for y in range (self.n):
				self.c.create_rectangle(5+x*self.size, 5+y*self.size,5+(x+1)*self.size, 5+(y+1)*self.size, fill='white')
		self.c.bind("<Button-1>",self.positioncalc)						##bind canvas to button, calculate position in grid 
		self.startbutton=Button(root2,text='Start',height=1,width=10,command=self.prerun)
		self.startbutton.grid(row=2,column=2)

	def prerun(self):													##gathers all important data to start a game of life
		b=int(self.v.get())
		rule1=self.q1entry.get()
		rule0=self.q0entry.get()
		rule=str(rule1)+'/'+str(rule0)
		game=Life(self.gridlist,rule,b)
		self.master.update_idletasks()
		self.run(game)
		
	def run(self,game):													##creates new rectangles above old rectangles
		game.tick()
		self.gridlist=game.grid
		for y in range(game.N):
			for x in range(game.M):
				if self.gridlist[y][x]==0:
					self.c.create_rectangle(5+x*self.size, 5+y*self.size,5+(x+1)*self.size, 5+(y+1)*self.size, fill='white')
				elif self.gridlist[y][x]==1:	
					self.c.create_rectangle(5+x*self.size, 5+y*self.size,5+(x+1)*self.size, 5+(y+1)*self.size, fill='dark gray')
		self.master.update_idletasks()
		time.sleep(1)
		self.run(game)
		
	
	def positioncalc(self,event):										
		x=int(math.floor(int(event.x)-5)/self.size)
		y=int(math.floor(int(event.y)-5)/self.size)
		print(x,y)
		if x<=self.m and y<=self.n:
			if self.gridlist[y][x]==0:
				self.gridlist[y][x]=1
				self.c.create_rectangle(5+x*self.size, 5+y*self.size,5+(x+1)*self.size, 5+(y+1)*self.size, fill='dark gray')
			elif self.gridlist[y][x]==1:
				self.gridlist[y][x]=0	
				self.c.create_rectangle(5+x*self.size, 5+y*self.size,5+(x+1)*self.size, 5+(y+1)*self.size, fill='white')

root=Tk()																##create master
lifefenster=startpage(root)												##get information about master
root.mainloop()															##mainloopmaster
			
lifefenster.mainloop()	
#seed = [[ 0 ,0 ,0 , 0 ] ,[0 ,1 ,1, 0 ] ,[0 ,0 ,0 , 0 ]]
#T=Life(seed,'23/2',3)	
				
		
