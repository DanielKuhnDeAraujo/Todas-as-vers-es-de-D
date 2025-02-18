a=input("Digite seu código")
a=a.split()
c=0
out=""
while c<len(a) :
  if a[c] == "mostrar" :
    cau=(int(a[c+1]))
    c+=2
    while cau>0 :
      out+=(a[c])
      out+=(" ")
      c+=1
      cau-=1
    
  if a[c] == "msoma" :
    if a[c+1].isnumeric() == True and a[c+2].isnumeric() == True :
      out+=str((((int(a[c+1]))+(int(a[c+2])))))
    else :
      out+=(a[c+1]+a[c+2])
    c+=2
  
  if a[c] == "msub" :
    if a[c+1].isnumeric() == True and a[c+2].isnumeric() == True :
      out+=str((((int(a[c+1]))-(int(a[c+2])))))
    else :
      out+=(a[c+1]-a[c+2])
    c+=2
    c+=2
  if a[c] == "mmulti" :
    if a[c+1].isnumeric() == True and a[c+2].isnumeric() == True :
      out+=str((((int(a[c+1]))*(int(a[c+2])))))
    else :
      out+=(a[c+1]*a[c+2])
    c+=2
    c+=2
  if a[c] == "mdiv" :
    if a[c+1].isnumeric() == True and a[c+2].isnumeric() == True :
      out+=str((((int(a[c+1]))/(int(a[c+2])))))
    else :
      out+=(a[c+1]/a[c+2])
    c+=2
    c+=2
  if a[c] == "m" :
    print(out)
    out=""
  c+=1
if out!= "":
  print(out)
  
