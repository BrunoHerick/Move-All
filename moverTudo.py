# coding: utf-8
import os as sistema
import time as tempo
import shutil as moverArquivo
import pathlib2 as pastas

meses = [0,"JANEIRO","FEVEREIRO","MARCO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]
caminho = "{}/".format(pastas.Path.cwd())

for i in sistema.listdir(caminho):
    if i == "moverTudo.py": 
        continue
    if i == "moverTudo.exe": 
        continue
    if i == "moverTudo":
        continue
    if sistema.path.isdir("{}{}".format(caminho,i)) == True:
        continue
    dataCriacao = sistema.path.getmtime("{}{}".format(caminho,i))
    dataCriacao = tempo.ctime(dataCriacao)
    dataCriacao = tempo.strptime(dataCriacao)
    mesCriacao = dataCriacao.tm_mon
    anoCriacao = dataCriacao.tm_year
    if sistema.path.exists("{}{}_{}".format(caminho,meses[mesCriacao],anoCriacao)) == False:
        sistema.makedirs("{}{}_{}".format(caminho,meses[mesCriacao],anoCriacao))
        moverArquivo.move("{}{}".format(caminho,i),"{}{}_{}".format(caminho,meses[mesCriacao],anoCriacao))
    else:
        moverArquivo.move("{}{}".format(caminho,i),"{}{}_{}".format(caminho,meses[mesCriacao],anoCriacao))