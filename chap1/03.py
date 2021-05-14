s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print(s)

new_s = s.replace(',','').replace('.','')
new_s = new_s.split()
pi= []
for i in new_s:
    pi.append(len(i))

print(pi)