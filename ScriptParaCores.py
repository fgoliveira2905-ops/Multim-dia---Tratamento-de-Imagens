from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('imagens/monarch.ppm').convert('RGB'))

cores = ["red","green","blue"]
nomes = ['R','G','B']

plt.figure(figsize=(10,10))
for c in range(3):
    h = np.bincount(img[:,:,c].ravel(), minlength=256)
    plt.plot(h, color=cores[c], label=nomes[c])

plt.title("Histograma")
plt.xlabel('Nível')
plt.ylabel('Frequência')
plt.xlim(0,256)
plt.legend()
plt.show()