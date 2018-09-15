"""
Autor: Nicolas Ramos
Data : 14/09/2018
"""
from datetime import datetime
from calendar import monthrange


class Idade:
    """
    Com base na sua data e hora de nascimento calcula sua idade em dias, horas e minutos!
    Calcula Também em anos, meses, e dias.
    """
    def __init__(self, nascimento_data_hora):
        self.__nascimento = nascimento_data_hora

    def dias(self):
        """
        Calcula a idade em dias.
        Retorna um int.
        :return: dias
        """
        hoje = datetime.now()
        return (hoje - self.__nascimento).days

    def dias_horas(self):
        """
        Calcula a idade em dias, horas e minutos.
        Retorna uma lista.
        :return: [dias, horas, minutos]
        """
        hoje = datetime.now()
        vida = (hoje - self.__nascimento)
        dias = vida.days
        minutos = vida.seconds // 60
        horas = minutos // 60
        minutos -= horas * 60
        return [dias, horas, minutos]

    def idade(self):
        """
        Calcula a idade em dias, horas e minutos.
        Retorna uma lista.
        :return: [dias, horas, minutos]
        """
        hoje = datetime.now()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        dias = hoje.day - self.__nascimento.day
        if meses < 0 or dias < 0:
            anos -= 1
            meses += 12
        mes = hoje.month
        ano = hoje.year
        if dias < 0:
            mes -= 1
            meses -= 1
            if mes < 1:
                mes += 12
                ano -= 1
            dias += monthrange(ano, mes)[1]

        return [anos, meses, dias]


