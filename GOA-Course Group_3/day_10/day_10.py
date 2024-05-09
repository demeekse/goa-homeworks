# #######  part 1   ########    
x = [2, 4, 6, 2, 4, 7, 2, 9]
a=[]
for num in x:
    if num !=(4):
        a.append(num)
print(a)

# ######## part 2 #############
names=["deme", "petre", "Nia", "nanuka"]
ages=[14, 38 , 13, 40]

wlovanebebi_da_saxelebi="me var {} wlis da chemi saxelia  {}, chemi da aris {} wlis da qvia {}, mamachemi aris {} wlis da qvia {} , dedachemi aris {} wlis da qvia {}".format(ages[0], names[0],  ages[2], names[2], ages[1], names[1],  ages[3], names[3] )
print (wlovanebebi_da_saxelebi)

names=["deme", "petre", "Nia", "nanuka"]
ages=[14+10, 38+10 , 13+10, 40+10]

wlovanebebi_da_saxelebi="10 years later: ""me var {} wlis da chemi saxelia  {}, chemi da aris {} wlis da qvia {}, mamachemi aris {} wlis da qvia {} , dedachemi aris {} wlis da qvia {}".format(ages[0], names[0],  ages[2], names[2], ages[1], names[1],  ages[3], names[3] )
print (wlovanebebi_da_saxelebi)
