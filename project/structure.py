chain=['A']
a={'A': 'HHHHHLQISITLAAALEHYKFFEQMQNQGRILSKMQQNGYENPTVEVDAAVTPEERHLKKKQYTSIHHGVVVIATVIVITLVMSNKGAIIGLMVGGHHQKLVFFAEDVGMDAEFRHDSGYEV'}
h={'A': ['687','695','700','708','708','724']}
p={'A': 'HHHHHLQISITLA'}
c=''
s=''
print(len(a.get('A')))
for i in chain:
    c+=p.get(i).replace(p.get(i),'-'*len(p.get(i)))#.replace(p.get(i)[2:6],'|'*4))
    s+=a.get(i).replace(a.get(i)[2:6],'|'*4).replace(a.get(i)[8:11],'|'*3).replace('A-Z','-')
    # c=''
print(s)