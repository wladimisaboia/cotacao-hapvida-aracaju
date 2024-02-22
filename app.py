from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cotacao.html')

@app.route('/cotacao', methods=['POST'])
def cotar():
    idades_str = request.form['idade']
    idades = [int(age.strip()) for age in idades_str.split(',')]
    plano = request.form['plano'].strip()

    valores = {}
    total_valor = 0
    desconto_aplicado = False

    for idade in idades:
        valor = 0

        if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'ambulatorial (pessoa física) - Com coparticipação' or plano == 'nosso plano enfermaria (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'nosso plano enfermaria (pessoa física) - Com coparticipação' or plano == 'nosso plano apartamento (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'nosso plano apartamento (pessoa física) - Com coparticipação' or plano == 'mix enfermaria (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'mix apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if len(idades) >= 2 and not desconto_aplicado:
                valor = valor * 0.95
                desconto_aplicado = True

        if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 168.97
            elif idade <= 23:
                valor = 222.41
            elif idade <= 28:
                valor = 253.49
            elif idade <= 33:
                valor = 282.74
            elif idade <= 38:
                valor = 297.54
            elif idade <= 43:
                valor = 334.00
            elif idade <= 48:
                valor = 408.36
            elif idade <= 53:
                valor = 566.24
            elif idade <= 58:
                valor = 763.19
            else:
                valor = 991.09
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 108.62
            elif idade <= 23:
                valor = 142.56
            elif idade <= 28:
                valor = 162.30
            elif idade <= 33:
                valor = 180.88
            elif idade <= 38:
                valor = 190.28
            elif idade <= 43:
                valor = 213.44
            elif idade <= 48:
                valor = 260.67
            elif idade <= 53:
                valor = 360.95
            elif idade <= 58:
                valor = 486.05
            else:
                valor = 630.81
        elif plano == 'nosso plano enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 234.95
            elif idade <= 23:
                valor = 309.00
            elif idade <= 28:
                valor = 354.82
            elif idade <= 33:
                valor = 396.97
            elif idade <= 38:
                valor = 416.64
            elif idade <= 43:
                valor = 470.34
            elif idade <= 48:
                valor = 573.04
            elif idade <= 53:
                valor = 789.45
            elif idade <= 58:
                valor = 1064.52
            else:
                valor = 1382.82
        elif plano == 'nosso plano enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 169.39
            elif idade <= 23:
                valor = 222.47
            elif idade <= 28:
                valor = 255.31
            elif idade <= 33:
                valor = 285.52
            elif idade <= 38:
                valor = 299.62
            elif idade <= 43:
                valor = 338.11
            elif idade <= 48:
                valor = 411.72
            elif idade <= 53:
                valor = 566.83
            elif idade <= 58:
                valor = 763.99
            else:
                valor = 992.13
        elif plano == 'nosso plano apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 350.65
            elif idade <= 23:
                valor = 461.73
            elif idade <= 28:
                valor = 530.46
            elif idade <= 33:
                valor = 593.69
            elif idade <= 38:
                valor = 623.20
            elif idade <= 43:
                valor = 703.76
            elif idade <= 48:
                valor = 857.81
            elif idade <= 53:
                valor = 1182.44
            elif idade <= 58:
                valor = 1595.06
            else:
                valor = 2072.52
        elif plano == 'nosso plano apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 252.32
            elif idade <= 23:
                valor = 331.93
            elif idade <= 28:
                valor = 381.19
            elif idade <= 33:
                valor = 426.51
            elif idade <= 38:
                valor = 447.66
            elif idade <= 43:
                valor = 505.40
            elif idade <= 48:
                valor = 615.81
            elif idade <= 53:
                valor = 848.48
            elif idade <= 58:
                valor = 1144.21
            else:
                valor = 1486.41
        elif plano == 'mix enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 386.83
            elif idade <= 23:
                valor = 509.49
            elif idade <= 28:
                valor = 585.38
            elif idade <= 33:
                valor = 655.20
            elif idade <= 38:
                valor = 687.78
            elif idade <= 43:
                valor = 776.73
            elif idade <= 48:
                valor = 946.83
            elif idade <= 53:
                valor = 1305.28
            elif idade <= 58:
                valor = 1760.89
            else:
                valor = 2288.10
        elif plano == 'mix apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 578.44
            elif idade <= 23:
                valor = 762.41
            elif idade <= 28:
                valor = 876.24
            elif idade <= 33:
                valor = 980.97
            elif idade <= 38:
                valor = 1029.84
            elif idade <= 43:
                valor = 1163.26
            elif idade <= 48:
                valor = 1418.40
            elif idade <= 53:
                valor = 1956.05
            elif idade <= 58:
                valor = 2639.43
            else:
                valor = 3430.20
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 210.77
            elif idade <= 23:
                valor = 236.06
            elif idade <= 28:
                valor = 264.39
            elif idade <= 33:
                valor = 304.05
            elif idade <= 38:
                valor = 349.66
            elif idade <= 43:
                valor = 416.10
            elif idade <= 48:
                valor = 520.13
            elif idade <= 53:
                valor = 650.16
            elif idade <= 58:
                valor = 1105.27
            else:
                valor = 1237.90
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 118.04
            elif idade <= 23:
                valor = 132.20
            elif idade <= 28:
                valor = 148.06
            elif idade <= 33:
                valor = 170.27
            elif idade <= 38:
                valor = 195.81
            elif idade <= 43:
                valor = 233.01
            elif idade <= 48:
                valor = 291.26
            elif idade <= 53:
                valor = 364.08
            elif idade <= 58:
                valor = 618.94
            else:
                valor = 693.21
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 284.01
            elif idade <= 23:
                valor = 318.09
            elif idade <= 28:
                valor = 356.26
            elif idade <= 33:
                valor = 409.70
            elif idade <= 38:
                valor = 471.16
            elif idade <= 43:
                valor = 560.68
            elif idade <= 48:
                valor = 700.85
            elif idade <= 53:
                valor = 876.06
            elif idade <= 58:
                valor = 1489.30
            else:
                valor = 1668.02
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 158.84
            elif idade <= 23:
                valor = 177.90
            elif idade <= 28:
                valor = 199.25
            elif idade <= 33:
                valor = 229.14
            elif idade <= 38:
                valor = 263.51
            elif idade <= 43:
                valor = 313.58
            elif idade <= 48:
                valor = 391.98
            elif idade <= 53:
                valor = 489.98
            elif idade <= 58:
                valor = 832.97
            else:
                valor = 932.93
        else:
            return 'Plano inválido'

        if idade not in valores:
            valores[idade] = {'plano': [], 'qtd': 0}

        valores[idade]['plano'].append(valor)
        total_valor += valor
        valores[idade]['qtd'] += 1

    if desconto_aplicado:
        total_valor = total_valor * 0.95

    total_valor = '{:.2f}'.format(total_valor)

    return render_template('resposta.html', valores=valores, total_valor=total_valor, desconto_aplicado=desconto_aplicado, plano_selecionado=plano)

if __name__ == '__main__':
    app.run(debug=True)
