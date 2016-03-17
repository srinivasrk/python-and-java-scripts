file1 = file("c:\\Input1.txt","r");
file2 = file("c:\\Input2.txt","r");
cfgname=raw_input("Enter the Zone config name : ");
hostname=[];
hostwwn=[];
vnxname=[];
vnxwwn=[];
zonenames=[];
i=0;
temp=[];
for line in file1:
    temp=line.split(" ");
    hostname.append(temp[0]);
    hostwwn.append(temp[1].strip());


for l1 in range(0,len(hostname)):
    print "alicreate \""+hostname[l1]+"\" \""+hostwwn[l1]+"\"";
        
for line in file2:
    temp=line.split(" ");
    vnxname.append(temp[0]);
    vnxwwn.append(temp[1].strip());

for l1 in range(0,len(vnxname)):
    print "alicreate \""+vnxname[l1]+"\" \""+vnxwwn[l1]+"\"";
k=0;
z=len(vnxname)/2
for l1 in range(0,len(hostname)):
    for l2 in range(k,len(vnxname)/2):
        print "zonecreate \""+ hostname[l1]+"_"+vnxname[l2]+"\""+"," +hostname[l1]+";"+vnxname[l2]+"\"";
        print "zonecreate \""+ hostname[l1]+"_"+vnxname[l2+z]+"\""+"," +hostname[l1]+";"+vnxname[l2+z]+"\"";
        zonenames.append( hostname[l1]+"_"+vnxname[l2]);
        k=k+1;
        if(k == len(vnxname)/2):
            k=0;
        break;

temp1="";
for l1 in range(0,len(zonenames)):
    temp1 += zonenames[l1]+";"
    if(l1+1 == len(zonenames)):
         temp += zonenames[l1];

print"cfgcreate \""+cfgname+"\""+","+"\""+temp1+"\"";
print "cfgsave "+cfgname;
print "cfgenable "+cfgname;

raw_input("press any key to exit");
