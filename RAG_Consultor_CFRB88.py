# -*- coding: utf-8 -*-
"""IAsmim_jur.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eYOJ0TK6xUpUgWrDZvWLky_LiGAgry9z
"""



"""Mini Projeo RAG - IAsmim_Jur.

Resgate data base - Constituição
"""

#MRPT - fast nearest neighbor search with random projection
!pip install git+https://github.com/vioshyvo/mrpt/

!pip install vectordb2

"""#Atualizar a dependência entre as versões de tf-keras e tensorflow. A mensagem de erro indica que tf-keras requer uma versão do TensorFlow inferior a 2.16, enquanto você tem a versão 2.16.1 do TensorFlow instalada."""

pip install --upgrade tf-keras

!pip install langchain

"""Quebra de Texto - Constituição Federal

Embedding chunks - Quebra de texto
"""

import requests
bruto_text = requests.get('https://raw.githubusercontent.com/abjur/constituicao/main/CONSTITUICAO.md').text
bruto_text

import re

padrao_capitulo = r'^##\s+(.*)$'
sections = re.split(padrao_capitulo, bruto_text, flags=re.MULTILINE)
sections = [section.strip() for section in sections [ 1:]]

#Import - Langchain
from langchain.text_splitter import MarkdownHeaderTextSplitter

padrao_capitulo = [
      ("##", "Capitulo"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=padrao_capitulo)
sections = markdown_splitter.split_text(bruto_text)

#Validando Chunks e database --> Teste de Constituição
sections[:11]

#Testando os Chunk Size e o Overlap - funcionando!!!

from langchain.text_splitter import RecursiveCharacterTextSplitter

# Defina o tamanho do chunk e a sobreposição
chunk_size = 20  # Defina o tamanho do chunk conforme necessário
chunk_overlap = 3  # Defina a sobreposição conforme necessário

splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

chunks = splitter.split_text(text)


text = "A República Federativa do Brasil, formaulda pela união indissolúvel dos Estados e Municípios e do Distrito Federal"

splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)

from vectordb import Memory

memory = Memory(chunking_strategy={"mode":"sliding_window", "window_size": 128, "overlap": 8})

for i in range(0, len(sections)):
    capitulo = sections[i].metadata
    texto = sections[i].page_content

    metadata = {'capitulo': capitulo, 'origem': 'constituicao federal'}

    memory.save(texto, metadata)

memory.search ('direito da seguridade social', top_n=5)
