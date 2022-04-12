from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
cf = Image.open("andhy.jpg")
lbr, tgl = (cf.size)
plt.imshow(cf, cmap='gray', vmin=0, vmax=255)
cf.show(cf)

hiskul = cf.histogram()
L = 256
n = lbr*tgl
alpha = float(L-1)/n

cdf1 = []
c1 = 0
for i in range(L):
    c1 += hiskul(i)
    cdf1.append(c1)

cdf_eq1=[]
for i in range(L):
    ak = round(float(L-1)*(cdf1[i]/float(n)))
    cdf_eq1.append(ak)

cdf_eq2 = np.array(cdf_eq1)
cg = cdf_eq2[cf]

hiskul = np.histogram(cg,L,[0,L])[0]





