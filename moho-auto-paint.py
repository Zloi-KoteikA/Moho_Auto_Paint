''' Полезный мусор
lis=[]
while True:
	p=input("Введи заменяемые цвета или Enter для продолжения: ")
	if p == '':
		break
	else:
		lis.append(p)
lis2=[]
while True:
	p=input("Введи цвета на замену или Enter для продолжения: ")
	if p == '':
		break
	else:
		lis2.append(p)

for el in lis:
	x=lis.index(el)
	lis[x]=(hex_to_rgb(el))
for el in lis:
	x=lis.index(el)
	p=str(el)
	p=p.replace(',', '')
	p=p.replace('(', '')
	p=p.replace(')', '')
	lis[x]=p
titl=[]

for el in lis:
	x=lis.index(el)
	p=str(el)
	titl.append(p.split())
	for i in titl:
		e=titl.index(i)
		titl[e]=(i)/255
		titl[e]=(round(i, 6))
		lis[x]=titl[e]
for el in lis:	
	print(el)

for el in lis2:
	x=lis2.index(el)
	lis2[x]=(hex_to_rgb(el))
for el in lis2:	
	p=str(el)
	p=p.replace(',', '')
	p=p.replace('(', '')
	p=p.replace(')', '')
	lis2[x]=p
'''


''' Quick input
#wl="'/home/morevna/test/Untitled.anme'"
p="#9DA369"
p2="#1A5727"
#'''

import os 

from PIL import ImageColor
def hex_to_rgb(hex_color):
    return ImageColor.getcolor(hex_color, "RGB")
#^^^ Convert HEX to RGB


p=input("The color is replaceable: ")
p2=input("The color is replaced: ")

file=[]
while True:
	x=input("Move the files (press ENTER to continue): ")
	if x == '':
		break
	else:
		file.append(x)

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




p=hex_to_rgb(p)
p=str(p)
p=p.replace(',', '')
p=p.replace('(', '')
p=p.replace(')', '')
a,b,c=p.split()
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
p= f"{a} {b} {c}"



p2=hex_to_rgb(p2)
p2=str(p2)
p2=p2.replace(',', '')
p2=p2.replace('(', '')
p2=p2.replace(')', '')
a2,b2,c2=p2.split()
a2=int(a2)
a2=a2/255
a2=round(a2,6)
if a2 == 1.0:
	a2=1
b2=int(b2)
b2=b2/255
b2=round(b2,6)
if b2 == 1.0:
	b2=1
c2=int(c2)
c2=c2/255
c2=round(c2,6)
if c2 == 1.0:
	c2=1
p2= f"{a2} {b2} {c2}"


for i in file:
	os.system(f'sed -i "s/{p}/{p2}/g" {i}')
#^^^ file rewrite

