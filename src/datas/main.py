"""
Autor: Nicolas Ramos
Data : 14/09/2018
Nota : Exemplificar o uso da classe Idade.
"""
from datetime import datetime
from src.datas.Idade import Idade


def main():
    """Exemplificar o uso da classe idade."""
    i = Idade(data())
    print('Idade em dia(s) é:', i.dias())
    dhm = i.dias_horas()
    print(f'Sua Idade e de {dhm[0]} dia(s), {dhm[1]} hora(s), e {dhm[2]} minuto(s)')
    idade = i.idade()
    print(f"Você têm {idade[0]} ano(s), {idade[1]} mês(es) e {idade[2]} dia(s).")
    return


def data():
    """Recebe o valor digitado no formato 'datetime'"""
    print('                      Formato: dd/mm/aaaa HH:MM')
    digitado = input('Digite sua data de nascimento: ')
    try:
        return datetime.strptime(digitado, '%d/%m/%Y %H:%M')
    except ValueError:
        print('A data não foi fornecida no formato solicitado')
        print('dd/mm/aaaa HH:MM veja a data de hoje:')
        print(datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M'))
        exit(1)


main()
