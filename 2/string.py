

name="ekramul haque"

upper=name.upper()
lower=name.lower()
capitalize=name.capitalize()

rep_text="sms , Developer"
#rep=rep_text.replace('Developer','Software Developer people loved eating food')

#split=rep.split(' ')
rep_index='Software Developer people loved eating Software food'
split2=rep_index.split(' ')
print(upper)
print(lower)
print(capitalize)
#print(rep)
print(split2[5])

len=len(rep_index)

sp=rep_index.split(' ')
print(rep_index[len-1])
print(sp[4])
qun=rep_index.count('Software')
print(qun)

pref=rep_index.startswith('Software')
pref=rep_index.endswith('food')
print(pref)




