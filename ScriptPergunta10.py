from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

#ShowOff: (originalmente as contas eram hNorm = h / (altura*largura), então substitui por uma função pra calcular isso
def prob(caso, casoPossivel):
    return caso / casoPossivel

image = Image.open('imagens/Rosa1024.png')
arr = np.asarray(image)  # Cria um objeto numpy
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.title('Image Original')
plt.show()
print(arr.shape)
print(arr.dtype)

"""
Objetivo: h(L) (histograma de cinzento)

h(L) produz o numero de ocorrencias de cada nível de cinza L,
 0 <= L <= 2^b - 1.
Representa a DISTRIBUICAO da PROBABILIDADE de valores dos pixeis
"""

altura, largura = arr.shape

b = 8  # profundidade da cor (imagem de 8 bits)
niveis = 2**b  # 2^8 = 256 niveis de cinzento (do 0 ao 255)

print(f"A imagem tem altura: {altura} pixeis e largura: {largura} pixeis")

#=====CONTAS MANUAIS (ciclos for)=====#

# Histograma h(L)
h = np.zeros(niveis, dtype=int)  # um array de 0's do tipo inteiro

for y in range(altura):
    for x in range(largura):
        h[arr[y, x]] += 1  # arr[linha, coluna] = arr[y, x]

# h[L] diz quantos pixeis da imagem têm o tom de cinzento L

# Histograma normalizado: nº de pixeis com o tom / nº total de pixeis
hNorm = prob(h, altura * largura)

# Histograma acumulado
ha = np.zeros(niveis, dtype=int)
ha[0] = h[0]  # o primeiro valor é só o nº de pixeis com tom 0

for L in range(1, niveis):
    ha[L] = ha[L - 1] + h[L]  # nº de pixeis com tom L ou inferior

# Probabilidade de, ao escolher um pixel ao acaso, o tom ser <= L
haNorm = prob(ha, altura * largura)

#===== JEITO DA PROFESSORA =====#

# Histograma: depois de transformar a imagem num array 1D,
# conta quantas vezes cada tom de cinza aparece
histo = np.bincount(arr.ravel(), minlength=256)
histoNorm = histo / arr.size  # igual a hNorm

# Histograma acumulado
histoA = np.cumsum(histo)
histoNormA = histoA / arr.size  # igual a haNorm

# Verificação: manual e NumPy devem dar exatamente o mesmo
print("h igual a histo:", np.array_equal(h, histo))
print("ha igual a histoA:", np.array_equal(ha, histoA))
print("Soma de hNorm:", hNorm.sum())  # deve dar 1.0
print("haNorm[-1]:", haNorm[-1])      # deve dar 1.0

#=====PLOTS=====#
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

# Linha 1: contas manuais (ciclos for)
ax[0, 0].bar(range(256), h, width=1, color='blue')
ax[0, 0].set_title("Histograma h(L) (manual)")

ax[0, 1].bar(range(256), hNorm, width=1, color='green')
ax[0, 1].set_title("Histograma normalizado (manual)")

ax[0, 2].plot(haNorm, color='red', linewidth=2)
ax[0, 2].set_title("Histograma acumulado normalizado (manual)")

# Linha 2: funções do NumPy
ax[1, 0].bar(range(256), histo, width=1, color='blue')
ax[1, 0].set_title("Histograma h(L) (NumPy)")

ax[1, 1].bar(range(256), histoNorm, width=1, color='purple')
ax[1, 1].set_title("Histograma normalizado (NumPy)")

ax[1, 2].plot(histoNormA, color='cyan', linewidth=2)
ax[1, 2].set_title("Histograma acumulado normalizado (NumPy)")

# Parte estética
for a in ax.flat:
    a.set_xlabel("Nível de cinzento L")
    a.set_xlim([0, 255])

plt.tight_layout()
plt.show()