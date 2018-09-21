"""
Autor: Nicolas Ramos
Data : 20/09/2018
"""
import glob
import os


class Monitor:
    """
    A classe Monitor tem por objetivo monitorar um diretório fornecido como parámetro (path_absoluto)
    devolvendo os seguintes
    get_path: o caminho monitorado
    get_files: uma lista dos arquivos em get_path
    get_file_recent: o nome do arquivo mais recente em get_path
    get_path_file_recent: igual a get_file_recent, mas entrega o arquivo com o caminho completo
    """
    def __init__(self, path_absoluto=os.path.join(os.environ['HOME'], 'Downloads', 'test')):
        self.__path_absoluto = path_absoluto
        if not os.path.exists(self.__path_absoluto):
            os.mkdir(self.__path_absoluto)
        if not os.path.isdir(self.__path_absoluto):
            print(f'ERROR: o caminho {self.__path_absoluto} não é um diretório!')

    def get_path(self):
        """
        :return: o path_absoluto
        """
        return self.__path_absoluto

    def get_files(self):
        """
        :return: uma lista dos arquivos no path_absoluto
        """
        lista = os.listdir(self.__path_absoluto)
        lista.sort()
        return lista

    def get_path_file_recent(self):
        """
        :return: igual a get_file_recent, mas entrega o arquivo com o caminho completo
        """
        files = glob.glob(os.path.join(self.__path_absoluto, '*'))
        if len(files) > 0:
            files.sort(key=os.path.getmtime)
            file = files[-1]
        else:
            file = ''
        return file

    def get_file_recent(self):
        """
        :return: o nome do arquivo mais recente no path_absoluto
        """
        file = self.get_path_file_recent()
        if not file == '':
            size = len(self.__path_absoluto) + 1
            file = file[size:]
        return file

