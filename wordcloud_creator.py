import sys
import os
import numpy as np
from PIL import Image
import requests
from wordcloud import WordCloud, STOPWORDS

import html2text
from readability import Document

currdir = os.path.dirname(__file__)


def get_page(url):
    f = requests.get(url)

    doc = Document(f.text).summary()

    h = html2text.HTML2Text()
    h.ignore_links=True

    html_text = h.handle(doc)

    return html_text


def create_wordcloud(text):
    mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))

    stopwords = set(STOPWORDS)

    wc = WordCloud(background_color="white",
                   max_words=200,
                   mask=mask,
                   stopwords=stopwords)

    wc.generate(text)
    wc.to_file(os.path.join(currdir, "output.png"))


if __name__ == "__main__":
    url = sys.argv[1]
    text = get_page(url)

    create_wordcloud(text)