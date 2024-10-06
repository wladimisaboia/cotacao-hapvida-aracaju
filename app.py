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
                valor = 179.30
            elif idade <= 23:
                valor = 236.05
            elif idade <= 28:
                valor = 269.06
            elif idade <= 33:
                valor = 300.12
            elif idade <= 38:
                valor = 315.84
            elif idade <= 43:
                valor = 354.56
            elif idade <= 48:
                valor = 433.53
            elif idade <= 53:
                valor = 601.20
            elif idade <= 58:
                valor = 810.36
            else:
                valor = 1052.38
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 115.21
            elif idade <= 23:
                valor = 151.26
            elif idade <= 28:
                valor = 172.23
            elif idade <= 33:
                valor = 191.96
            elif idade <= 38:
                valor = 201.94
            elif idade <= 43:
                valor = 226.53
            elif idade <= 48:
                valor = 276.69
            elif idade <= 53:
                valor = 383.20
            elif idade <= 58:
                valor = 516.06
            else:
                valor = 669.80
        elif plano == 'nosso plano enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 249.37
            elif idade <= 23:
                valor = 328.02
            elif idade <= 28:
                valor = 376.68
            elif idade <= 33:
                valor = 421.45
            elif idade <= 38:
                valor = 442.34
            elif idade <= 43:
                valor = 499.38
            elif idade <= 48:
                valor = 608.45
            elif idade <= 53:
                valor = 838.29
            elif idade <= 58:
                valor = 1130.43
            else:
                valor = 1468.48
        elif plano == 'nosso plano enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 179.74
            elif idade <= 23:
                valor = 236.10
            elif idade <= 28:
                valor = 270.98
            elif idade <= 33:
                valor = 303.07
            elif idade <= 38:
                valor = 318.04
            elif idade <= 43:
                valor = 358.92
            elif idade <= 48:
                valor = 437.09
            elif idade <= 53:
                valor = 601.82
            elif idade <= 58:
                valor = 811.20
            else:
                valor = 1053.48
        elif plano == 'nosso plano apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 372.24
            elif idade <= 23:
                valor = 490.20
            elif idade <= 28:
                valor = 563.19
            elif idade <= 33:
                valor = 630.34
            elif idade <= 38:
                valor = 661.68
            elif idade <= 43:
                valor = 747.23
            elif idade <= 48:
                valor = 910.83
            elif idade <= 53:
                valor = 1255.58
            elif idade <= 58:
                valor = 1693.77
            else:
                valor = 2200.82
        elif plano == 'nosso plano apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 267.81
            elif idade <= 23:
                valor = 352.36
            elif idade <= 28:
                valor = 404.67
            elif idade <= 33:
                valor = 452.80
            elif idade <= 38:
                valor = 475.26
            elif idade <= 43:
                valor = 536.58
            elif idade <= 48:
                valor = 653.84
            elif idade <= 53:
                valor = 900.93
            elif idade <= 58:
                valor = 1215.00
            else:
                valor = 1578.42
        elif plano == 'mix enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 410.66
            elif idade <= 23:
                valor = 540.92
            elif idade <= 28:
                valor = 621.52
            elif idade <= 33:
                valor = 695.67
            elif idade <= 38:
                valor = 730.27
            elif idade <= 43:
                valor = 824.74
            elif idade <= 48:
                valor = 1005.39
            elif idade <= 53:
                valor = 1386.07
            elif idade <= 58:
                valor = 1869.93
            else:
                valor = 2429.83
        elif plano == 'mix apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 614.15
            elif idade <= 23:
                valor = 809.53
            elif idade <= 28:
                valor = 930.42
            elif idade <= 33:
                valor = 1041.64
            elif idade <= 38:
                valor = 1093.54
            elif idade <= 43:
                valor = 1235.23
            elif idade <= 48:
                valor = 1506.19
            elif idade <= 53:
                valor = 2077.17
            elif idade <= 58:
                valor = 2802.92
            else:
                valor = 3642.72
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 223.75
            elif idade <= 23:
                valor = 250.60
            elif idade <= 28:
                valor = 280.67
            elif idade <= 33:
                valor = 322.77
            elif idade <= 38:
                valor = 371.19
            elif idade <= 43:
                valor = 441.72
            elif idade <= 48:
                valor = 552.15
            elif idade <= 53:
                valor = 690.19
            elif idade <= 58:
                valor = 1173.32
            else:
                valor = 1314.12
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 125.27
            elif idade <= 23:
                valor = 140.30
            elif idade <= 28:
                valor = 157.14
            elif idade <= 33:
                valor = 180.71
            elif idade <= 38:
                valor = 207.82
            elif idade <= 43:
                valor = 247.31
            elif idade <= 48:
                valor = 309.14
            elif idade <= 53:
                valor = 386.43
            elif idade <= 58:
                valor = 656.93
            else:
                valor = 735.76
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 301.52
            elif idade <= 23:
                valor = 337.70
            elif idade <= 28:
                valor = 378.22
            elif idade <= 33:
                valor = 434.95
            elif idade <= 38:
                valor = 500.19
            elif idade <= 43:
                valor = 595.23
            elif idade <= 48:
                valor = 744.04
            elif idade <= 53:
                valor = 930.05
            elif idade <= 58:
                valor = 1581.09
            else:
                valor = 1770.82
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 168.59
            elif idade <= 23:
                valor = 188.82
            elif idade <= 28:
                valor = 211.48
            elif idade <= 33:
                valor = 243.20
            elif idade <= 38:
                valor = 279.68
            elif idade <= 43:
                valor = 332.82
            elif idade <= 48:
                valor = 416.03
            elif idade <= 53:
                valor = 520.04
            elif idade <= 58:
                valor = 884.07
            else:
                valor = 990.16
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
