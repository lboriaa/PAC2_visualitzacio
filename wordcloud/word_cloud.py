import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

# Descarregar el text
url = "https://www.gutenberg.org/cache/epub/61/pg61.txt"
response = requests.get(url)
response.raise_for_status()
full_text = response.text

# Contingut principal
start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK THE COMMUNIST MANIFESTO ***"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK THE COMMUNIST MANIFESTO ***"

if start_marker in full_text and end_marker in full_text:
    text = full_text.split(start_marker)[1].split(end_marker)[0].strip()
else:
    text = full_text

# Carregar la imatge màscara (en blanc i negre)
mask_image = np.array(Image.open("communism.png").convert("L"))

# Funció per assignar tons de vermell
def rojo_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    r = random.randint(150, 255)  # rojo brillante
    g = random.randint(0, 50)     # poco verde
    b = random.randint(0, 50)     # poco azul
    return f"rgb({r}, {g}, {b})"

# Crear WordCloud amb màscara i color personalitzat
wordcloud = WordCloud(
    width=800,
    height=800,
    max_words=200,
    background_color=None,
    mode="RGBA",
    mask=mask_image,
    color_func=rojo_color_func
).generate(text)

# Mostrar WordCloud
plt.figure(figsize=(8,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('wordcloud.png')
