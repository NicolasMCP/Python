"""
Autor: Nicolas Ramos
Data : 20/09/2018
Nota : Exemplificar o uso da classe Monitor.
"""
from src.files.monitor import Monitor


def main():
    m = Monitor()
    print('Caminho :', m.get_path())
    print('Arq.mais Recente:', m.get_file_recent())
    print('Arq.mais Recente + path:', m.get_path_file_recent())
    print('Arquivos:', m.get_files())
    return


main()
