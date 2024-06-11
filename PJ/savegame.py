import shutil

import os
# pasta é do tipo c:\\usuáruo\\Jogo ... etc

#source
src_folder = 'pasta do save game'

#destination
dst_folder = 'pasta de destino'

#backup_folder ='pasta de backup'

os.chdir('pasta de backup')

#se estiver vazio copia direto, mas nem sempre ta vazio
if os.listdir() == []:
    shutil.copytree(src_folder, dst_folder)
#tem que passar arquivo por arquivo e remover pra depois add
else:
    for file in os.listdir():
        '''
        aqui ele vai tentar remover aquivo por arquivo
        tentar os.remove
        caso falhe por existencia de DIR então ele vai fazer 
        recursive pra apagar um de cada vez rmtree
        '''
        try:
            os.remove(file)
        except:
            #rmtree apaga recursivamente a pasta mesmo estando cheia
            shutil.rmtree(file)
            # os.rmdir(file)
            # não funciona pois a pasta pode não estar vazia
    shutil.copytree(src_folder, dst_folder)

#shutil.copytree(src_folder, dst_folder) 
