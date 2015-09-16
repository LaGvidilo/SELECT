# -*- coding: utf-8 -*-
import mmap

def deter_l(fichier):
	f=open(fichier,'r')
	tmp,l=" ",0
	while tmp!="":
		l=l+1
		tmp=f.readline()
	f.close()
	return l-1

def suppr_acc(ligne):
	out = ligne.replace("\xe9","e").replace("\xe8","e").replace("\xea","e").replace("\xe0","a").replace("\xeb","e").replace("\xeb","a").replace("\xf8","#").replace("\xe2","a").replace("\xf4","o").replace("\xe7","c").replace("\xee","i")
	out = out.replace("À","A").replace("Á","A").replace("Â","A").replace("Ã","A").replace("Ä","A").replace("Å","A").replace("à","a").replace("á","a").replace("â","a").replace("ã","a").replace("ä","a").replace("å","a").replace("Ò","o").replace("Ó","o").replace("Ô","o").replace("Õ","o").replace("Ö","o").replace("Ø","#").replace("ò","o").replace("ó","o").replace("ô","o").replace("õ","o").replace("ö","o").replace("ø","#").replace("È","E").replace("É","E").replace("Ê","E").replace("Ë","E").replace("è","e").replace("é","e").replace("ê","e").replace("ë","e").replace("Ç","c").replace("ç","c").replace("Ì","I").replace("Í","I").replace("Î","I").replace("Ï","I").replace("ì","i").replace("í","i").replace("î","i").replace("ï","i").replace("Ù","u").replace("Ú","u").replace("Û","u").replace("Ü","u").replace("ù","u").replace("ú","u").replace("û","u").replace("ü","u").replace("ÿ","y").replace("Ñ","n").replace("ñ","n")
	return out


def load_asc(fichier,l):
	lat,lon,name=[],[],[]
	with open(fichier, 'r+b') as f:
		mm = mmap.mmap(f.fileno(), 0)
	
		a=mm.tell()
	
		n=0
		while n<l:

			b=mm.find(",",a)
			lat.append(mm.read(b-a).replace(',',''))
			a=b

			b=mm.find(",",a+1)
			mm.seek(a+1)
			lon.append(mm.read(b-a-1).replace(' ','').replace(',',''))
			a=b

			b=mm.find('"',a+1)
			c=mm.find('"',b+1)
			mm.seek(b+1)
			name.append(suppr_acc(mm.read(c-b-1)))
			a=c

			b=mm.find("\n",a)
			z=mm.read(b+1-a)
			a=b	

			n=n+1
	return lat,lon,name



def main(f):
	lat,lon,name=[],[],[]
	l=deter_l(f)
	lat,lon,name=load_asc(f,l)
	return lat,lon,name



