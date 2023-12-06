#Interface gráfica

import PySimpleGUI as psg

import calc2
from calc2 import soma
from calc2 import sub
from calc2 import mult
from calc2 import div
from calc2 import porc

layout = [
              [psg.Text('Informe N1: '), psg.InputText(key= 'Num1')],
              [psg.Text('Informe N2: '), psg.InputText(key= 'Num2')],
              [psg.Text('Adição -'), psg.Text( text= '', key= 'total')],
              [psg.Text('Subtração -'), psg.Text( text= '', key= 'total2'),],
              [psg.Text('Multiplicação - '), psg.Text( text= '', key= 'total3'),],
              [psg.Text('Divisão - '), psg.Text( text= '', key= 'total4'),],
              [psg.Text('Porcentagem - '), psg.Text( text= '', key= 'total5'),],
              [psg.Button('calcular'), psg.Button('limpar')],
        ]

janela = psg.Window('Calculadora Simples', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'limpar':
        janela['Num1'].update('')
        janela['Num2'].update('')
        janela['total'].update('')
        janela['total2'].update('')
        janela['total3'].update('')
        janela['total4'].update('')
        janela['total5'].update('')
        janela['Num1'].set_focus()
    else:
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        janela['total'].update(calc2.soma(num1, num2))
        janela['total2'].update(calc2.sub(num1, num2))
        janela['total3'].update(calc2.mult(num1, num2))
        janela['total4'].update(calc2.div(num1, num2))
        janela['total5'].update(calc2.porc(num1, num2))

janela.close()