import os
import shutil

pwd = os.getcwd()
files = os.listdir()
organized = 'organized'
if not os.path.exists(organized):
    os.mkdir(organized)

def mkdir():
    for c in files:
        if os.path.isfile(c):
            nome, ex = os.path.splitext(c)
            try:
                os.mkdir(fr'{organized}\{ex.strip('.')}')
            except:
                pass
    movefiles()
    rename()
    
def movefiles():
    for dirs in os.listdir(organized):
        for files in os.listdir():
            if os.path.isfile(files):
                if files == 'faxineiro.py':
                    continue
                
                if dirs in files:
                    try:
                        pwd_files = rf"{pwd}\{files}"
                        destin_files = rf'{pwd}\{organized}\{dirs}'
                        shutil.move(pwd_files,destin_files)
                    except:
                        pass
def rename():
    arquivos_conhecidos = {
        'arquivos python' : ['py'],
        'arquivos de texto' : ['txt'],
        'arquivos de imagem' : ['png','jpeg'],
        'arquivos markdown' : ['md'],
        'arquivos pdf' : ['pdf'],
        'arquivos zipados' : ['zip','rar'],
        'arquivos de planilhas' : ['xlsx','xlsm'],
        'arquivos json' : ['json']
    }
    for dirs in os.listdir(organized):
        for chave, valor in arquivos_conhecidos.items():
            if dirs in valor:
                new_name = chave
                my_source = fr'{pwd}\{organized}\{dirs}'
                my_new_source = fr'{pwd}\{organized}\{new_name}'
                os.rename(my_source,my_new_source)
    
if __name__ == '__main__':    
    mkdir()