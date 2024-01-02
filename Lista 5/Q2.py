s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- "
pn = s[14] + s[13] + s[-9] + s[10] + s[-12] + s[13] + s[-15] + s[-1]
sn = s[21] + s[-9] + s[12] + s[10] + s[-11]
print(pn + sn)