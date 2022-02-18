import re
chain=['A']
a={'A': 'HHHHHLQISITLAAALEHYKFFEQMQNQGRILSKMQQNGYENPTVEVDAAVTPEERHLKKKQYTSIHHGVVVIATVIVITLVMSNKGAIIGLMVGGHHQKLVFFAEDVGMDAEFRHDSGYEV'}
h={'A': ['687','695','700','708','708','724']}
p={'A': 'HHHHHLQISITLA'}
c=''
s=''
print(len(a.get('A')))
for i in chain:
    c+=p.get(i).replace(p.get(i)[2:6],'|'*4).replace(p.get(i)[7:10],'|'*3)#.replace('R','-').replace('H','-').replace('K','-').replace('D','-').replace('E','-').replace('S','-').replace('T','-').replace('N','-').replace('Q','-').replace('C','-').replace('U','-').replace('G','-').replace('P','-').replace('A','-').replace('V','-').replace('I','-').replace('L','-').replace('M','-').replace('F','-').replace('Y','-').replace('W','-')

    # c+=p.get(i).replace(p.get(i),'-'*len(p.get(i))).replace('R','-').replace('H','-').replace('K','-').replace('D','-').replace('E','-').replace('S','-').replace('T','-').replace('N','-').replace('Q','-').replace('C','-').replace('U','-').replace('G','-').replace('P','-').replace('A','-').replace('V','-').replace('I','-').replace('L','-').replace('M','-').replace('F','-').replace('Y','-').replace('W','-')
    s+=a.get(i).replace(a.get(i)[2:6],'|'*4).replace(a.get(i)[8:11],'|'*3).replace(a.get(i)[20:41],'|'*21).replace(a.get(i)[15:18],'/'*3).replace(a.get(i)[90:105],'|'*15)
    # c=''
# print(s)
print(c)
y=c.replace('R','-').replace('H','-').replace('K','-').replace('D','-').replace('E','-').replace('S','-').replace('T','-').replace('N','-').replace('Q','-').replace('C','-').replace('U','-').replace('G','-').replace('P','-').replace('A','-').replace('V','-').replace('I','-').replace('L','-').replace('M','-').replace('F','-').replace('Y','-').replace('W','-')
print(y)
print(p.get('A'))
print(len(s))
f=''
p=''
for j in chain:
    for i in range(0,len(a.get(j))):
        # p+=a.get(j).replace(a.get(j)[2:6],'|'*4).replace(a.get(j)[8:11],'|'*3).replace(a.get(j)[20:41],'|'*21).replace(a.get(j)[15:18],'/'*3).replace(a.get(j)[90:105],'|'*15)

        
        if a.get(j)[i] in "'a','q','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'".upper():
            f+=a.get(j)[i].replace(a.get(j)[i],'-')
        # p=f.replace(f[2:6],'|'*4).replace(f[8:11],'|'*3).replace(f[20:41],'|'*21).replace(f[15:18],'/'*3).replace(f[90:105],'|'*15)
# print(s.replace(str(re.findall(r'[A-z]*',s)),'-'))
# print(p)
y= "'a','q','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'".upper()
   #                                                j='RHKDESTNQCUGPAVILMFYW'
d=''
d=s.replace('R','-').replace('H','-').replace('K','-').replace('D','-').replace('E','-').replace('S','-').replace('T','-').replace('N','-').replace('Q','-').replace('C','-').replace('U','-').replace('G','-').replace('P','-').replace('A','-').replace('V','-').replace('I','-').replace('L','-').replace('M','-').replace('F','-').replace('Y','-').replace('W','-')
# d=s.replace('H','-')
# for i in j.upper():
#     print(i)
#     d=s.replace(i,'-')
#     # d=''
print(len(d))
print(d)