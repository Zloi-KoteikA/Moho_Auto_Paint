import os 

from PIL import ImageColor
def hex_to_rgb(hex_color):
    return ImageColor.getcolor(hex_color, "RGB")
#^^^ Convert HEX to RGB


file=[]
while True:
	x=input("Move the files (press ENTER to continue): ")
	if x == '':
		break
	else:
		file.append(x)
num1=[]
while True:
	x=input("The color is replaceable (press ENTER to continue): ")
	if x == '':
		break
	else:
		num1.append(x)
num2=[]
while True:
	x=input("The color is replaced (press ENTER to continue): ")
	if x == '':
		break
	else:
		num2.append(x)		
#^^^ Write data					
		
		
		
for i in file:
	x=file.index(i)
	i=str(i)
	i=(i.replace("'",""))
	i=(i.replace(" ","",1))
	file[x]=i
for i in file:
	
	rp=(i.replace(".","_(back)."))
	os.system(f'cp -i "{i}" "{rp}"')
#^^^ backup copy



for i in num1:
	x=num1.index(i)
	i=i.replace('#', '')
	i=(f'#{i}')
	i=hex_to_rgb(i)
	i=str(i)
	i=i.replace(',', '')
	i=i.replace('(', '')
	i=i.replace(')', '')
	a,b,c=i.split()
	a=int(a)
	a=a/255
	a=round(a,6)
	if a == 1.0:
		a=1
	b=int(b)
	b=b/255
	b=round(b,6)
	if b == 1.0:
		b=1
	c=int(c)
	c=c/255
	c=round(c,6)
	if c == 1.0:
		c=1
	i= f"{a} {b} {c}"
	num1[x]=i
for i in num2:
	x=num2.index(i)
	i=i.replace('#', '')
	i=(f'#{i}')
	i=hex_to_rgb(i)
	i=str(i)
	i=i.replace(',', '')
	i=i.replace('(', '')
	i=i.replace(')', '')
	a,b,c=i.split()
	a=int(a)
	a=a/255
	a=round(a,6)
	if a == 1.0:
		a=1
	b=int(b)
	b=b/255
	b=round(b,6)
	if b == 1.0:
		b=1
	c=int(c)
	c=c/255
	c=round(c,6)
	if c == 1.0:
		c=1
	i= f"{a} {b} {c}"
	num2[x]=i	
#^^^ Color replace



for i in file:
	for p in num1:
		x=num1.index(p)
		os.system(f'sed -i "s/{num1[x]}/{num2[x]}/g" {i}')
#^^^ file rewrite
