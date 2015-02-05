from __future__ import division # for python 2
def get_at_content(dna): # define function get_at_content for variable 'dna'
    length = len(dna) # define length as length of dna
    a_count = dna.upper('A') # define a_count as occurances of A
    t_count = dna.upper('T') # define t_count as occurances of T
    #convert sequence to upper case before counting
    at_content = (a_count + t_count) / length #calculate at content by (A+T)/2
    return round (at_content, 2)  # return with 2 sig figs

#example for 3 function calls
my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content)) 
print(get_at_content("ATGCATGCAACTGTAGC")) 
print(get_at_content("aactgtagctagctagcagcgta")) 
