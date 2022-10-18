import requests
import json
import re
import datetime
import sys

#Recebe argumentos e valida se precisa de 3 ou de apenas 2
try:
    argv = sys.argv
    args_data_completa = argv[2]
    args_mes = argv[3]
    args_caminho = argv[1]
except:
    argv = sys.argv
    args_data_completa = argv[2]
    args_caminho = argv[1]

#busca informações do arquivo .json
with open(args_caminho, 'r', encoding='utf-8') as itf:
    json_objeto = json.load(itf)
    url = json_objeto['url']
    destino = json_objeto['destino']
    nome = json_objeto['nome_arquivo']


#valida a quantidade de dadtas que vai trabalhar na url
if (len(comparcao := re.findall("\*dt", url)) > 0) and (len(comparcao := re.findall("\*dt", url)) < 2):
    url2 = re.sub("\*dt",args_data_completa, url)
    name2 = re.sub("\*dt", args_data_completa, nome)
    #url_arquivo = url2
    r = requests.get(url2)
    with open(destino+name2, 'wb') as f:
        f.write(r.content)

if len(comparcao := re.findall("\*dt", url)) > 1:
    url2 = url.replace('*dty',args_data_completa)
    url3 = url2.replace('*dtm',args_mes)

    name2 = re.sub("\*dty",args_data_completa, nome)
    name3 = re.sub("\*dtm", args_mes, name2)
    r = requests.get(url3)
    with open(destino+name3, 'wb') as f:
        f.write(r.content) 