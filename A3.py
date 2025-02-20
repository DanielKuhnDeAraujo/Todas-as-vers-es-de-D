var=[]
def erro() :
  print("Erro")
def eot(a) :
  print("Você não pode fazer ", a," usando texto")
a=input("Digite seu código")
a=a.split()
c=0
out=""
while c<len(a) :
  if a[c] == "mostrar" :
    cau=(int(a[c+1]))
    c+=1
    while cau>0 :
      c+=1
      out+=(a[c])
      out+=(" ")
      
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
      eot("subtrações")
    c+=2
    c+=2
  if a[c] == "mmulti" :
    if a[c+1].isnumeric() == True and a[c+2].isnumeric() == True :
      out+=str((((int(a[c+1]))*(int(a[c+2])))))
    elif a[c+2].isnumeric() :
      out+=(a[c+1]*a[c+2])
    else :
      eot("multiplicações")
    c+=2
  if a[c] == "mdiv" :
    if a[c+1].isnumeric() == True and a[c+2].isnumeric() == True :
      out+=str((((int(a[c+1]))/(int(a[c+2])))))
    else :
      eot("dvisões")
    c+=2
  if a[c] == "m" :
    print(out)
    out=""
#novos códigos
  if a[c] =="nvar" :
    c+=1
    var.append(a[c])
  if a[c] == "mvar" :
    c+=1
    print(var[int(a[c])-1])
  
  if a[c] == "msomavar" :
    if (var[int(a[c+1])-1]).isnumeric() == True and (var[int(a[c+2])-1]).isnumeric() == True :
      out+=str(((int((var[int(a[c+1])-1]))+(int(var[int(a[c+2])-1])))))
    else :
      out+=((var[int(a[c+1])])+a(var[int(a[c+2])]))
    c+=2
  if a[c] == "msubvar" :
    if (var[int(a[c+1])-1]).isnumeric() == True and (var[int(a[c+2])-1]).isnumeric() == True :
      out+=str(((int((var[int(a[c+1])-1]))-(int(var[int(a[c+2])-1])))))
    else :
      eot("subtrações")
  if a[c] == "mmultivar" :
    if (var[int(a[c+1])-1]).isnumeric() == True and (var[int(a[c+2])-1]).isnumeric() == True :
      out+=str(((int((var[int(a[c+1])-1]))*(int(var[int(a[c+2])-1])))))
    else :
      eot("multiplicações")
  if a[c] == "mdivvar" :
    if (var[int(a[c+1])-1]).isnumeric() == True and (var[int(a[c+2])-1]).isnumeric() == True :
      out+=str(((int((var[int(a[c+1])-1]))/(int(var[int(a[c+2])-1])))))
    else :
      eot("divisão")
  if a[c] == "nvar_rec_m" :
    cau=(int(a[c+1]))
    c+=1
    while cau>0 :
      c+=1
      out+=(a[c])
      out+=(" ")
      cau-=1
    print(out)
    out=""
    aux=input("")
    var.append(aux)
    
  c+=1
if out!= "":
  print(out)
