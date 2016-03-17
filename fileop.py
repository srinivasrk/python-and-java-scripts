import re
import xlwt
def find_word(text, search):
   b = r'(\s|^|$)'
   result = re.findall(b+search+b, text, flags=re.IGNORECASE)
   if len(result)>0:
      return True
   else:
      return False


def find_match(text, search):
   result = re.findall(search, text, flags=re.IGNORECASE)
   if len(result)>0:
      return True
   else:
      return False

f  = open("C:\\Users\\kulkas24\\Desktop\\fcns data - test.txt",'r')
irofile = iter(f)

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet',cell_overwrite_ok=True)
i=0
j=0
flag = 0
for line in irofile:
   
   if(j==0):
        if find_match(line,"VSAN:"):
             ws.write(i,j,line)
             j=j+1
   if(j==1):
          if find_word(line,"port-wwn"):
             ws.write(i,j,line)
             j=j+1
   if(j==2):
        if "[" in line:
             ws.write(i,j,line)
             j=j+1
        elif find_word(line,"node-wwn"):
             j=j+1
             ws.write(i,j,line)
             j=j+1
   if(j==3):
          if find_word(line,"node-wwn"):
              ws.write(i,j,line)
              j=j+1
   if(j==4):
         if find_word(line,"connected interface"):
             ws.write(i,j,line)
             j=j+1
   if(j==5):
         if find_word(line,"switch name"):
             ws.write(i,j,line)
             j=j+1  
   if(j%6==0):
         i=i+1
         j=0
    
wb.save("c:\\Test1.xls")      
f.close()
