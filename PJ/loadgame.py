"""
no load teremos que mecher no save pastatext
o dir de destino será a pasta original que será sobreescritra
pegar do backup e remover dir
"""


import shutil

import os

#source
src_folder = '\\Zomboid\\Saves\\Sandbox\\backup\\savegame'

#destination
dst_folder = '\\Zomboid\\Saves\\Sandbox\\savegame'

os.chdir('Zomboid\\Saves\\Sandbox\\backup')
for file in os.listdir():
    #vamos testar se tem arquivo salvo
    if file == 'savegame' and os.listdir()!=[] :
        #muda-se para a pasta que quer salvar
        os.chdir('Zomboid\\Saves\\Sandbox')
        #remove a original
        shutil.rmtree('savegame')
        shutil.copytree(src_folder,dst_folder)
    else:
        print("sem arquivo de backup")
