"""
Calculating the % GC and % AT content in the trna sequence
"""



danSEQ= 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAG'

def GC_AT_Content(sequence):
    "takes a dna sequence and retuns (GC,AT) percentage content rounded off to 2 decimal places "
    len_seq = len(sequence)
    seq_upper = sequence.upper()
    GT_content = seq_upper.count('G') + seq_upper.count('C')
    AT_content = seq_upper.count('T') + seq_upper.count('A') 
    return  round((GT_content/len_seq)*100, 2),round((AT_content/len_seq)*100, 2)

# print(GC_AT_Content(danSEQ))

"""
find the first, last and the 5th amino acids in the sequence
"""

def find_aa(aa_seq):
    """
    takes ammino acid sequence and returns amino acids in the first, last and the 5th positions
    in that order
    """
    
    first_aa = aa_seq[0]
    last_aa = aa_seq[-1]
    fifyth_aa = aa_seq[4]

    return first_aa, last_aa, fifyth_aa

amino='MNKMDLVADVAEKTDLSKAKATEVIDAVFA'
# print(find_aa(amino))

"""
The above amino acid is a bacterial restriction enzyme that recognizes "TCCGGA".
Find the first restriction site in the following sequence: AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
"""
def restriction(seq,site):
    """
    takes a sequence and restriction site and returns it postion of the first occurance in the sequence
    """
    x = seq.find(site)
    return x

dna='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATTCCGGAAT'
r="TCCGGA"
# print(restriction(dna,r))



"""
Using strings, lists, tuples and dictionaries concepts, find the reverse complement of AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
"""

def complement_seq(seq):
    """
    converting a dna sequence to its reverse complement
    """
    seq_upper =seq.upper()
    compl = seq_upper.replace('A','t').replace('T','a').replace('G',"c").replace('C','g')
    complement =compl.upper()
    return(complement)

# print(complement_seq(dna))

def reverse_seq(rev):
    """
    takes a sequence and return a reverse of the sequence
    """
    rev_upper= rev.upper()
    reverse_sequence=rev_upper[::-1]
    return reverse_sequence
# print(reverse_seq(complement_seq(dna)))

"""
using Dictionary
"""
def reverse_complement(seq):
    """
    use a dictionary to create a reverse complemment of a dna sequence
    """
    dict_seq ={"A":"T",'G':'C','T':'A','C':'G'}
    reverse_comp =''
    for nuc in seq.upper():
        reverse_comp= dict_seq[nuc] + reverse_comp
    return reverse_comp

# print(reverse_complement(dna))

"""
using list
"""
def reverse_comp_list(list_seq):
    """
    takes a a dna sequence and retuns it reverse complement
    """
    comp_reverse=''
    comp=[]
    for nuc in list_seq.upper():
        if nuc=='A':
            comp.append('T')
        elif nuc =='T':
            comp.append('A')
        elif nuc =='G':
            comp.append('C')
        elif nuc =='C':
            comp.append('G')
        else:
            comp.append(nuc)
    for i in comp:
        comp_reverse= i + comp_reverse
    return  comp_reverse

# print(reverse_comp_list(dna))

"""
Create a while loop that starts with x = 0 and increments x until x is equal to 5.
 Each iteration should print to the console.
"""
def while_loop():
    """
    while loop that starts with x = 0,increments x until x is equal to 5.
 Each iteration should print to the console.
    
    """
    y=0
    while y<=5:
        y+=1
        print(y)
    
# while_loop()

"""
Create a for loop that prints values from 4 to 10 to the console.
"""
def for_loop():
    """
    a for loop that prints values from 4 to 10 to the console
    """
    for i in range(4,11):
        print(i)

# for_loop()









"""
This should be checked by a different function,
"""
def validate_dna(dna_seq):
    
    """
    returns True if DNA sequence is valid and false if not
    """
    flag=True




    for i in dna_seq:
        
        if i not in 'ACGT':
            flag=False
    return flag
            


print(validate_dna("CAGTGATGATGACGAT"))

print(validate_dna("ATFRACGATTGHAHYAK"))





def gene_file(file1,file2):
    """
    Reads the file (humchr.txt) 
    Writes to another file (gene_names.txt) a clean list of gene names.
    """
    with open(file1,'r') as file:
        with open(file2,'w')as myfile:
            count=0
            flag=False      
            for line in file:
            # print(line)
                if line.startswith('_____'):
                    flag=True
                    count+=1
                    continue
                elif line.startswith('-'):
                    flag=False
                elif flag and count==2:
                    myfile.writelines(line.split()[0]+'\n')

                
gene_file('../Data/humchrx.txt','../Data/gene_name.txt')




"""
 Using a DNA sequence read from file, answer the following questions:
"""
def dna_four(dna_seq):
    """
    Shows that the DNA string contains only four letters(reterns 4)
    """
    try:
        with open(dna_seq) as myfile:
            read_file= myfile.read()
            sub_header= read_file.split('\n' ,1)[1]
            lis_file =list(sub_header)
            sub_header1= ''.join(lis_file).split('\n' )
            single_line = ''.join(sub_header1)
            dna_four_letter = set(single_line)
            print(dna_four_letter)
        return(len(dna_four_letter))
    except FileNotFoundError as no_file:
            print('enter valid file or parth')

    
# print(dna_four(dna))

dna_four('../Data/example.fasta')
"""
In the DNA string there are regions that have a repeating letter.
What is the letter and length of the longest repeating region?
"""
import itertools

print(sorted([list(g) for k,g in itertools.groupby(dna)], key=len)[-1])

# s=sorted(s, key=len[-1 ])

"""
 In the DNA string there are regions that have a repeating letter. 
 What is the letter and length of the longest repeating region?
"""



def dna_repeat_letter(file):
    """
    takes a dna file and returns the longest repeating region
    """


    try:
        with open(file) as myfile:
            read_file= myfile.read()
            sub_header= read_file.split('\n' ,1)[1]
            lis_file =list(sub_header)
            sub_header1= ''.join(lis_file).split('\n' )
            single_line = ''.join(sub_header1)
            repeat=sorted([list(g) for k,g in itertools.groupby(dna)], key=len)[-1]
        return(repeat)
    except FileNotFoundError as no_file:
            print('enter valid file or parth')

print(dna_repeat_letter(dna))

print(dna_repeat_letter('../Data/example.fasta'))

""""
How many ’ATG’s are in the DNA string?

"""
def dna_string_3(dna_sequence,string):
    """
    takes a dna sequence and a substring of three's and
    returns the frequence of the substring
    """
    try:
        with open(dna_sequence) as myfile:
            read_file= myfile.read()
            sub_header= read_file.split('\n' ,1)[1]
            lis_file =list(sub_header)
            sub_header1= ''.join(lis_file).split('\n' )
            single_line = ''.join(sub_header1)
            count =0
            i=0
            upper_dna = single_line.upper()
            for i in range(i,len(upper_dna), 3):
                # print(single_line[i:i+3])
                if upper_dna[i:i+3]==string.upper():
                    # print(single_line[i:i+3])

                    count= count +1
                

          
        return(count)
    except FileNotFoundError as no_file:
        print('invalid parth')

print(dna_string_3('../Data/example.fasta', 'AtG'))



