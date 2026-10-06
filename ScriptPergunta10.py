from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

#ShowOff (originalmente as contas eram hNorm = h / (altura*largura), então substitui por uma função pra calcular isso
def prob(caso, casoPossivel):
    return caso/casoPossivel

image = Image.open('imagens/Rosa1024.png')
arr = np.asarray(image) #Cria um objeto numpy
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.title('Image Original')
plt.show()
print(arr.shape)
print(arr.dtype)

"""

Objetivo: h(L) (historiograma de cinzento)

h(L) produz o numero de ocorrencias de cada nível de cinza L,
 0 <= L <= 2^b - 1.
Representa a DISTRIBUICAO da PROPABILIDADE de valores dos pixeis 
 

"""

altura, largura = arr.shape

b = 8 #Para definir a profundidade da cor (imagem de 8 bits)
niveis = 2**b # 2^8 = 256 niveis de cinzento (do 0 ao 255)

print(f"A imagem tem altura: {altura} pixes e largura: {largura} pixeis")

h = np.zeros(niveis, dtype=int) #um array de 0's do tipo inteiro

for y in range(altura):
    for x in range(largura):
        h[arr[x, y]] += 1

#Aqui guardas cada tom de cinzento na imagem (arr[x,y])
#Depois conta que pixeis é que tem cada tom de cinzento,
# o array h[] diz quantos pixeis da imagem tem cada tom desse cinzento em específico

hNorm = prob(h, altura*largura) #numero de tons / numeros de casos possíveis, assim se monta a probabilidade

#==========================#

#Hist acumulado
ha = np.zeros(niveis, dtype=int)

for L in range(1, niveis):
    ha[L] = ha[L - 1] + h[L] ##isso da nos quantos pixeis tem o tom L ou inferior
    # (soma a ha[L-1] quantos pixeis tem esse tom ou inferior)

#A probabilidade de ao selecionar ao acaso um pixel o tom de cinza ser <= L
haNorm = prob(ha, altura*largura)

#=====PLOTS=====#
#Histograma das contas manuais

fig, bx = plt.subplots(1, 3, figsize=(15, 4))

bx[0].bar(range(256), h, width=1, color='blue')
bx[0].set_title("Histograma h(L)")

bx[1].bar(range(256), hNorm, width=1, color='green')
bx[1].set_title("Histograma normalizado")

bx[2].plot(ha, color='red', linewidth=2)
bx[2].set_title("Histograma acumulado (normalizado)")

#Essa parte é estética e eu adicionei depois
for b in bx:
    b.set_xlabel("Nível de cinzento L")
    b.set_xlim([0, 255])

plt.tight_layout()
plt.show()

"""

'
When I wrote this code, 
only god and I knew how it worked.
Now, only god knows it
'

nos ciclos for eu calculei manualmente cada histograma
aqui, eu pesquisei no site do numpy e encontrei funções que calculavam diretamente

"""

# histograma
histo = np.bincount(arr.ravel(), minlength=256) #depois de transformar a imagem num array de 1 dimensão,
# contamos quantas vezes cada tom de cinza aparece
histoNorm = histo / arr.size #é a mesma coisa de "hNorm = h / (altura * largura)" (linha 41)

# histograma acumulado
histoA = np.cumsum(histo)
histoNormA = histoA / arr.size #mais uma vez, "haNorm = ha / (altura * largura)" (linha 53)

#Organizei os plots em uma janela só
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
ax[0].bar(range(256), h, width=1, label='Histograma')
ax[0].set_title("Histograma")
ax[1].bar(range(256), histoNorm, width=1, label='Histograma Normalizado', color='purple')
ax[1].set_title('Histograma Normalizado')
ax[2].plot(histoNormA, label='Histograma Acumulado Normalizado', color='cyan')
ax[2].set_title('Histograma Acumulado Normalizado')

for a in ax:
    a.set_xlabel("Nível de cinzento L")
    a.set_xlim([0, 255])

plt.tight_layout()
plt.show()