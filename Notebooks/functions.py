#function for transcribing
def transcribe(dna_string):
    rna_dic = {'A': 'U', 'T':'A', 'C':'G', 'G':'C'}
    rna = ''
    for nuc in dna_string:
        rna = rna_dic[nuc] + rna
    return(rna)    

#Reading frames
def reading_frame(i=0,mrna='None'):
    """generate reading frame from mrna"""
    codon_frame=[]
    for i in range(i,len(mrna),3):
        codon_frame.append(mrna[i:i+3])
    if (len(codon_frame)-1) !=3:
        codon_frame.pop()
    return(codon_frame)

#translate reading frames
def translate(mrna):
    """Translate mrna reading frame to amino acids"""
    a=''
    for i in mrna:
        #print (i)
        for key in codon.keys():
            if i ==key:
                a +=codon[key]
    return(a) 