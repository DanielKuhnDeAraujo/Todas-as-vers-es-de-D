a=input("Digite seu código")
a=a.split()
c=1
out=""
while c<(int(a[0])) :
  if a[c] == "mostrar" :
    cau=(int(a[c+1]))
    c+=2
    while cau>0 :
      out+=(a[c])
      out+=(" ")
      c+=1
      cau-=1
    
  if a[c] == "msoma" :
    out+=str((((int(a[c+1]))+(int(a[c+2])))))
    c+=2
  
  if a[c] == "msub" :
    out+=str((((int(a[c+1]))-(int(a[c+2])))))
    c+=2
  if a[c] == "mmulti" :
    out+=str((((int(a[c+1]))*(int(a[c+2])))))
    c+=2
  if a[c] == "mdiv" :
    out+=str((((int(a[c+1]))/(int(a[c+2])))))
    c+=2
  if a[c] == "m" :
    print(out)
    out=""
  c+=1
if out!= "":
  print(out)
  
