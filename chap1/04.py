s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
print(s)

new_s = s.replace(',','').replace('.','')
new_s = new_s.split()
elements= {}
for i in range(len(new_s)):
    idx = i + 1
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 \
       or i == 14 or i == 15 or i == 18:
        elements[new_s[i][0:1]] = idx
    else:
        elements[new_s[i][0:2]] = idx

print(elements)