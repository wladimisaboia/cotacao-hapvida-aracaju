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
                valor = 189.95
            elif idade <= 23:
                valor = 250.11
            elif idade <= 28:
                valor = 285.10
            elif idade <= 33:
                valor = 318.02
            elif idade <= 38:
                valor = 334.68
            elif idade <= 43:
                valor = 375.72
            elif idade <= 48:
                valor = 459.42
            elif idade <= 53:
                valor = 637.15
            elif idade <= 58:
                valor = 858.85
            else:
                valor = 1115.39
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 122.02
            elif idade <= 23:
                valor = 160.23
            elif idade <= 28:
                valor = 182.46
            elif idade <= 33:
                valor = 203.37
            elif idade <= 38:
                valor = 213.95
            elif idade <= 43:
                valor = 240.02
            elif idade <= 48:
                valor = 293.19
            elif idade <= 53:
                valor = 406.09
            elif idade <= 58:
                valor = 546.92
            else:
                valor = 709.88
        elif plano == 'nosso plano enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 264.23
            elif idade <= 23:
                valor = 347.60
            elif idade <= 28:
                valor = 399.18
            elif idade <= 33:
                valor = 446.64
            elif idade <= 38:
                valor = 468.79
            elif idade <= 43:
                valor = 529.25
            elif idade <= 48:
                valor = 644.87
            elif idade <= 53:
                valor = 888.51
            elif idade <= 58:
                valor = 1198.19
            else:
                valor = 1556.53
        elif plano == 'nosso plano enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 190.42
            elif idade <= 23:
                valor = 250.17
            elif idade <= 28:
                valor = 287.14
            elif idade <= 33:
                valor = 321.15
            elif idade <= 38:
                valor = 337.02
            elif idade <= 43:
                valor = 380.35
            elif idade <= 48:
                valor = 463.21
            elif idade <= 53:
                valor = 637.82
            elif idade <= 58:
                valor = 859.76
            else:
                valor = 1116.58
        elif plano == 'nosso plano apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 394.47
            elif idade <= 23:
                valor = 519.51
            elif idade <= 28:
                valor = 596.88
            elif idade <= 33:
                valor = 668.06
            elif idade <= 38:
                valor = 701.28
            elif idade <= 43:
                valor = 791.96
            elif idade <= 48:
                valor = 965.38
            elif idade <= 53:
                valor = 1330.81
            elif idade <= 58:
                valor = 1795.30
            else:
                valor = 2332.78
        elif plano == 'nosso plano apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 283.77
            elif idade <= 23:
                valor = 373.39
            elif idade <= 28:
                valor = 428.84
            elif idade <= 33:
                valor = 479.86
            elif idade <= 38:
                valor = 503.67
            elif idade <= 43:
                valor = 568.66
            elif idade <= 48:
                valor = 692.95
            elif idade <= 53:
                valor = 954.86
            elif idade <= 58:
                valor = 1287.76
            else:
                valor = 1672.98
        elif plano == 'mix enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 435.19
            elif idade <= 23:
                valor = 573.26
            elif idade <= 28:
                valor = 658.69
            elif idade <= 33:
                valor = 737.29
            elif idade <= 38:
                valor = 773.97
            elif idade <= 43:
                valor = 874.10
            elif idade <= 48:
                valor = 1065.59
            elif idade <= 53:
                valor = 1469.10
            elif idade <= 58:
                valor = 1981.99
            else:
                valor = 2575.47
        elif plano == 'mix apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 650.89
            elif idade <= 23:
                valor = 857.99
            elif idade <= 28:
                valor = 986.13
            elif idade <= 33:
                valor = 1104.02
            elif idade <= 38:
                valor = 1159.04
            elif idade <= 43:
                valor = 1309.23
            elif idade <= 48:
                valor = 1596.44
            elif idade <= 53:
                valor = 2201.68
            elif idade <= 58:
                valor = 2970.97
            else:
                valor = 3861.15
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 237.09
            elif idade <= 23:
                valor = 265.54
            elif idade <= 28:
                valor = 297.40
            elif idade <= 33:
                valor = 342.01
            elif idade <= 38:
                valor = 393.31
            elif idade <= 43:
                valor = 468.04
            elif idade <= 48:
                valor = 585.05
            elif idade <= 53:
                valor = 731.31
            elif idade <= 58:
                valor = 1243.23
            else:
                valor = 1392.42
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 132.71
            elif idade <= 23:
                valor = 148.64
            elif idade <= 28:
                valor = 166.48
            elif idade <= 33:
                valor = 191.45
            elif idade <= 38:
                valor = 220.17
            elif idade <= 43:
                valor = 262.00
            elif idade <= 48:
                valor = 327.50
            elif idade <= 53:
                valor = 409.38
            elif idade <= 58:
                valor = 695.95
            else:
                valor = 779.46
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 319.53
            elif idade <= 23:
                valor = 357.87
            elif idade <= 28:
                valor = 400.81
            elif idade <= 33:
                valor = 460.93
            elif idade <= 38:
                valor = 530.07
            elif idade <= 43:
                valor = 630.78
            elif idade <= 48:
                valor = 788.48
            elif idade <= 53:
                valor = 985.60
            elif idade <= 58:
                valor = 1675.52
            else:
                valor = 1876.58
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 178.63
            elif idade <= 23:
                valor = 200.07
            elif idade <= 28:
                valor = 224.08
            elif idade <= 33:
                valor = 257.69
            elif idade <= 38:
                valor = 296.34
            elif idade <= 43:
                valor = 352.64
            elif idade <= 48:
                valor = 440.80
            elif idade <= 53:
                valor = 551.00
            elif idade <= 58:
                valor = 936.70
            else:
                valor = 1049.10
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
