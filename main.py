from email.mime import image
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

image = Image.open('imagens/Rosa1024.png')
arr = np.asarray(image) #Cria um objeto numpy
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.title('Image Original')
plt.show()
print(arr.shape)
print(arr.dtype)

#Ficha 3 - ex 1

print("Débito da Monarch.ppm: ", 512*768*24, 'bits')
print("Débito de Monarch.ppm (em Bytes):", 512*768*24/8, 'Bytes')
print("Débito de Monarch.ppm (em KB):", 512*768*24/8/1024, 'KB')

"""
#Ficha 3 - ex3
espelharV = arr[ : : -1, : : ] #Mostramos as LINHAS ao contrário primeiro, da primeira a última
plt.title('Image Espelhada Verticalmente')
plt.imshow(espelharV, cmap='gray', vmin=0, vmax=255)
plt.show()
"""


"""
#Ficha 3 - ex3
espelharH = arr[ : : , : : -1] #Mostramos as COLUNAS ao contrário primeiro, da primeira a última
plt.title('Image Espelhada Horizontalmente')
plt.imshow(espelharH, cmap='gray', vmin=0, vmax=255)
plt.show()
"""


#Ficha 3 - ex4
metade = arr[::2 , ::2]
plt.imshow(metade, cmap='gray', vmin=0, vmax=255)
plt.title('Metade da Imagem')
plt.show()
print(metade.shape)
print(metade.dtype)


"""
#Ficha 3 - ex5
L, C = np.shape(arr)
arrDobro = np.zeros_like(arr, shape=(2*L,2*C))
arrDobro[::2,::2]=arr
arrDobro[1::2,::2]=arr
arrDobro[::2,1::2]=arr
arrDobro[1::2,1::2]=arr
plt.imshow(arrDobro, cmap='gray', vmin=0, vmax=255)
plt.title('Dobro da Imagem')
plt.show()
print(arrDobro.shape)
"""

#Ficha 3 - ex6
corte = arr [400: 600: , 400: 600: ]
plt.imshow(corte, cmap='gray', vmin=0, vmax=255)
plt.title('Corte da Imagem')
plt.show()
plt.show()
print(corte.shape)

#Ficha 3 - ex7
novaImg = arr.copy()
novaImg[:200: , :200:] = corte
plt.title('Inserção do Corte')
plt.imshow(novaImg, cmap='gray', vmin=0, vmax=255)
plt.show()
print(novaImg.shape)


#Ficha 3 - ex8
negativo = 1 - arr
plt.title('Imagem negativo')
plt.imshow(negativo, cmap='gray', vmin=0, vmax=255)
plt.show()
print(negativo.shape)


"""
rodada = np.rot90(arr)
plt.title('Imagem rodada')
plt.imshow(rodada, cmap='gray', vmin=0, vmax=255)
plt.show()
"""


"""
#Ficha 3 - ex 10
altura, largura = arr.shape
b = 8
niveis = 2**b                      # 256

# Histograma h(L): nº de ocorrências de cada nível
h = np.zeros(niveis, dtype=int)
for y in range(altura):
    for x in range(largura):
        h[arr[y, x]] += 1

# Histograma normalizado em [0, 1]
h_norm = h / (altura * largura)

# Histograma acumulado ha(L): nº de pixels com nível <= L
ha = np.zeros(niveis, dtype=int)
ha[0] = h[0]
for L in range(1, niveis):
    ha[L] = ha[L - 1] + h[L]

# Acumulado normalizado (termina em 1)
ha_norm = ha / (altura * largura)

print(h.sum() == altura * largura)   # verificação: deve dar True
print(ha[-1])                        # deve ser N x M

h = np.bincount(arr.ravel(), minlength=256)
h_norm = h / arr.size
ha = np.cumsum(h)
ha_norm = ha / arr.size

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

ax[0].bar(range(256), h, width=1)
ax[0].set_title("Histograma h(L)")

ax[1].bar(range(256), h_norm, width=1)
ax[1].set_title("Histograma normalizado")

ax[2].plot(ha_norm)
ax[2].set_title("Histograma acumulado (normalizado)")

for a in ax:
    a.set_xlabel("Nível de cinzento L")
plt.tight_layout()
plt.show()
"""

"""
plt.figure(figsize=(7,7))
plt.title("Histograma h(L)")
vals = arr.flatten()
hist, bins, patches = plt.hist(vals, 256)
plt.xlim([0, 255])
plt.show()

#hist acumulado
plt.figure(figsize=(7, 7))
plt.title("Histograma acumulado ha(L)")
vals = arr.flatten()
plt.hist(vals, 256, range=(0, 256), cumulative=True, histtype='step')
plt.xlim([0, 255])
plt.grid(True)
plt.show()

plt.figure(figsize=(7, 7))
plt.title("Histograma normalizado")
plt.hist(arr.flatten(), 256, range=(0, 256),
         weights=np.ones(arr.size) / arr.size)
plt.xlim([0, 255])
plt.show()

"""

#Ficha 3 - ex11

h = np.bincount(arr.ravel(), minlength=256)         # Histograma
h_norm = h / arr.size                               # Normalizado
ha = np.cumsum(h)                                   # Acumulado
ha_norm = ha / arr.size                             # Acumulado normalizado

t = 127
seg = np.where(arr <= t, 0, 255)                    # Limiarização

# Imagens
fig, ax = plt.subplots(1, 3, figsize=(14, 5))
for a, (img, tit) in zip(ax, [(negativo, "Negativo"), (rodada, "Rotação 90°"),
                              (seg, f"Limiar t={t}")]):
    a.imshow(img, cmap='gray', vmin=0, vmax=255); a.set_title(tit)
plt.show()

# Histogramas
fig, ax = plt.subplots(1, 4, figsize=(18, 4))
for a, (y, tit) in zip(ax, [(h, "h(L)"), (h_norm, "Normalizado"),
                            (ha, "Acumulado"), (ha_norm, "Acumulado normalizado")]):
    a.plot(y); a.set_title(tit); a.set_xlim(0, 255)
plt.show()