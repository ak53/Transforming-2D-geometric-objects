#Name-AMANDEEP KAUR

from math import *
import matplotlib.pyplot as plt
import matplotlib
plt.ion()                                       #interactive mode

shape=input()                                    #choose disc or poly
if shape in ['disc','Disc','DISC']:
	p,q,r=map(float,input().split())                #for disc
	x=[];y=[]
	a=b=r
	s=p                                          #x-coordinates
	t=q                                         #y-coordinates
	maj=mino=r 
	points=[]       
	for i in range(361):
		points.append(radians(i))
	for i in points:
		x.append(p+(a*cos(i)))                        #all x-co of the circle
		y.append(q+(b*sin(i)))                           #all y-co of the circle
else:
	x=list(map(int,input().split()))   
	x.append(x[0])                                   #to draw the last line
	y=list(map(int,input().split()))
	y.append(y[0])                                  #to draw the last line

def view():
	plt.clf()
	plt.axis('equal')
	plt.plot(x,y)
view()

def change(no,m,n=None):              
	global shape ; global x ; global y ; global s ; global t ; global maj ; global mino
	new_x=[]
	new_y=[]
	if no==1:
		for i in range(len(x)):
			new_x.append(m*x[i])
			new_y.append(n*y[i])
	elif no==2:
		for i in range(len(x)):
			new_x.append((cos(m)*x[i])-(sin(m)*y[i]))
			new_y.append((sin(m)*x[i])+(cos(m)*y[i]))
	elif no==3:
		for i in range(len(x)):
			new_x.append((1*x[i])+(m*1))
			new_y.append((1*y[i])+(n*1))
	x=new_x
	y=new_y
	if shape not in ['disc','Disc','DISC']:        #FOR POLYGON
		ans_x='';ans_y=''
		for i in x[:-1]:
			ans_x=ans_x+str(round(i,2))+str(" , ")
		for j in y[:-1]:
			ans_y= ans_y+str(round(j,2))+str(" , ")
		print("The new x-coordinates are: \n",ans_x[:-2])
		print("The new y-coordinates are: \n",ans_y[:-2])
	else:                                              #FOR DISC
		if no==1:
			s=m*s
			t=n*t
			maj=m*maj*2
			mino=n*mino*2
		elif no==2:
			S=(cos(m)*s)-(sin(m)*t)
			T=(sin(m)*s)+(cos(m)*t)
			s=S
			t=T
		elif no==3:
			s+=m
			t+=n
		print("x-coordinate of center:",round(s,2))
		print("y-coordinate of centre:",round(t,2))
		print("major axis of ellipse:",maj)
		print("minar axis of ellipse:",mino)
	view()

r=True        
while r==True:                             #choosing,based on user's                                         
	inp=input()                            #input what tranformation
	if inp[0]=='s' or inp[0]=='S':         #to implement
		p,q=map(float,inp[2:].split())
		change(1,p,q)
	elif inp[0]=='r' or inp[0]=='R':
		p=float(inp[2:])
		change(2,radians(p))
	elif inp[0]=='t' or inp[0]=='T':
		p,q=map(float,inp[2:].split())
		change(3,p,q)
	else:
		r=False
