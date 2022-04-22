from sympy.solvers import solve
from sympy import Symbol, symbols
from sympy import Array 
from sympy import summation



def printList(argumentsList):
    """Receives a list of arguments and prints them with the the list format"""
    for value in argumentsList:
        print(value, end='')
    print()

def getMissingValue(valueDict):
    """Gets the dictionary that we use and returns the missing valuye to use as symbol and solve for the equation"""
    #Find the missing value
    nameToSave = ""
    hasUnique = 0
    for key in valueDict:
        if valueDict[key] == '' :
            valueToSolve = Symbol(valueDict[key])
            valueDict[key] = valueToSolve
            nameToSave = key
            hasUnique = 1
        else:
            valueDict[key] = float(valueDict[key])
    
    if hasUnique == 0:
        #Quer dizer que eu meti numeros para tudo
        print("   Es burro, ja deste a resposta")
    return nameToSave


#Valores recebidos: 
#   ->   o valorAtual inicial ou o valorAtual de um ano
#   ->   taxa de atualizacao
#   ->   ano inicial em questão
#   ->   ano final
#   ->   valor Atual
#   ->   capital inicial
# Quero saber o meu valorAtual final depois de x anos
# M/Z
def JuroSimples():
    """
    Valores Recebidos:
           ->   o valorAtual inicial ou o valorAtual de um ano
           ->   taxa de atualizacao
           ->   ano inicial em questão
           ->   ano final
           ->   valor Atual
           ->   capital inicial
    
    Explicacao:
        Quanto dinheiro tenho depois de x anos a receber com juros de valor y
    """    
    print("----Juros Simples 3----\n")

    anoInicial = input("    Tempo inicial: ")
    anoFinal = input("    Tempo final: ")
    capital = input("    Capital inicial: ")
    valorAtual = input("    ValorAtual: ")
    taxaJuros = input("    Taxa de juros (decimal): ")
    
    valueDict = {"anoInicial": anoInicial, "anoFinal":anoFinal, "capital": capital, "valorAtual":valorAtual, "taxaJuros":taxaJuros}
    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    #Might be juro composto
    # print(solve(valueDict["capital"]/(1+valueDict["taxaJuros"])**(valueDict["anoFinal"] - valueDict["anoInicial"]) - valueDict["valorAtual"], valueToSolve))
    solution = solve(valueDict["capital"] + ((valueDict["capital"] * valueDict["taxaJuros"]) * (valueDict["anoFinal"] - valueDict["anoInicial"])   - valueDict["valorAtual"]), valueDict[nameToSave])[0]
    print("\n")
    print(f"    {nameToSave}: {solution}")    
    
    valueDict[nameToSave] = solution
    myList = ["capital", "capital", "taxaJuros", "anoFinal", "anoInicial", "valorAtual"]
    printList(myList)
    print(f'{valueDict["capital"]} + (({valueDict["capital"]} * {valueDict["taxaJuros"]}) * ({valueDict["anoFinal"]} - {valueDict["anoInicial"]}) - {valueDict["valorAtual"]}) = 0')



# Fazer a lista de argumentos por ordem da formula
# Salvar a solution para o valueDict apropriado
# Passar lista para a funcao
# Imprimir a formula


#Valores recebidos: 
#   ->   o valorAtual inicial ou o valorAtual de um ano
#   ->   taxa de atualizacao
#   ->   ano inicial em questão
#   ->   ano final
#   ->   valor Atual
#   ->   capital inicial
# Quero saber o meu valorAtual final depois de x anos (composto)
# Capitalizacao
# M/Z
def JuroComposto():
    """
    Valores recebidos: 
           ->   o valorAtual inicial ou o valorAtual de um ano
           ->   taxa de atualizacao
           ->   ano inicial em questão
           ->   ano final
           ->   valor Atual
           ->   capital inicial
    
    Explicacao:
        Quanto dinheiro tenho depois de x anos a receber com juros composto de valor y
            (Juros sobre juros)
        A cada atualizacao eu recebo uma percentagem do valor atual e nao do valor inicial
    
    """
    print("----Juro Composto 3----\n")
    
    anoInicial = input("    Tempo inicial: ")
    anoFinal = input("    Tempo final: ")
    capitalInicial = input("    Capital inicial: ")
    valorAtual = input("    Valor atual: ")
    taxaJuros = input("   Taxa de juros (decimal) : ")
    
    valueDict = {"anoInicial": anoInicial, "anoFinal":anoFinal, "capitalInicial": capitalInicial, "valorAtual":valorAtual, "taxaJuros":taxaJuros}
    #Find the missing value
    for key in valueDict:
        if valueDict[key] == '':
            valueToSolve = Symbol(valueDict[key])
            valueDict[key] = valueToSolve
            nameToSave = key
        else:
            valueDict[key] = float(valueDict[key])

    solution = solve(valueDict["capitalInicial"]*(1+valueDict["taxaJuros"])**(valueDict["anoFinal"] - valueDict["anoInicial"]) - valueDict["valorAtual"], valueDict[nameToSave])[0] 
        
    print("\n")
    print(f"    {nameToSave}: {solution}")    

    valueDict[nameToSave] = solution
    myList = ["capitalInicial", "taxaJuros", "anoFinal", "anoInicial", "valorAtual"]
    printList(myList)
    print(f'{valueDict["capitalInicial"]}*(1+{valueDict["taxaJuros"]})**({valueDict["anoFinal"]} - {valueDict["anoInicial"]}) - {valueDict["valorAtual"]}) = 0')


#Valores recebidos: 
#   -> inflação
#   -> juro nominal
#   -> juro nominal
# juro aplicavél a projetos a preço corrente
# taxa de juro considerando inflacao, aplicado a preços correntes

# M/Z
def JuroReal():
    """
    Valores recebidos: 
           ->   Inflação
           ->   Juro real
           ->   Juro nominal

    Explicacao:
        Quanto e que realmente vou receber dos meus juros considerando taxa inflacao (taxa de atualizacao)
    
    """
    print("----Juro Real 3----\n")
    taxaInflacao = input("    Inflação (decimal): ")
    taxaReal = input("    Juro Real (decimal): ")
    taxaNominal = input("    Juro nominal (decimal): ")

    valueDict = {"taxaInflacao": taxaInflacao, "taxaReal": taxaReal, "taxaNominal": taxaNominal} 
    #Find the missing value
    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve( (1 + valueDict["taxaReal"]) * (1 + valueDict["taxaInflacao"]) - (1 + valueDict["taxaNominal"]), valueDict[nameToSave])[0]
    
    print("\n")
    print(f"    {nameToSave}: {solution}")
    
    valueDict[nameToSave] = solution
    myList = ["taxaReal", "taxaInflacao", "taxaNominal"]
    printList(myList)
    print(f'1 + {valueDict["taxaReal"]}) * (1 + {valueDict["taxaInflacao"]}) - (1 + {valueDict["taxaNominal"]}) = 0')


    

#Valores recebidos: 
#   -> juro
#   -> valor do dinheiro
# valor do dinheiro apos aplicação da taxa de inflação (preços constantes)

# M
def ValorDoDinheiro():
    """
    Valores recebidos: 
           ->   Taxa de juros
           ->   Valor atual
           ->   Valor real

    Explicacao:
           Quanto vai valer o meu dinheiro aplicando a taxa de inflacao
           Apenas de um ano para o seguinte
    
    """

    print("----Valor do Dinheiro 3----\n")

    taxaJuros = input("    Taxa de juros (decimal): ")
    valorAtual = input("    Valor Atual: ")
    valorReal = input("    Valor real: ")

    valueDict = {"taxaJuros": taxaJuros, "valorAtual": valorAtual, "valorReal": valorReal} 
    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    
    solution = solve(valueDict["valorAtual"]/(1+valueDict["taxaJuros"]) - valueDict["valorReal"], valueDict[nameToSave])[0]

    print("\n")
    print(f"    {nameToSave}: {solution}")

    
    valueDict[nameToSave] = solution
    myList = ["valorAtual", "taxaJuros", "valorReal"]
    printList(myList)
    print(f'{valueDict["valorAtual"]}/(1+{valueDict["taxaJuros"]}) - {valueDict["valorReal"]} = 0')

    


# Valores recebidos
#   -> Juros anual
#   -> numero de subperiodos do ano
#   -> taxa efetiva para o subperiodo
# Relaciona taxas de juros com periodos diferentes
# M
def TaxasEquivalentes():
    """
    Valores recebidos
            ->   Juros anual
            ->   Numero de subperiodos do ano
            ->   taxa efetiva para o subperiodo

    Explicacao:
        Usado quando trabalhamos com periodos infra anuais
        Uma taxa efitiva que aplicada ao mesmo capital inciial conduz ao mesmo capital final
    """

    print("--Taxas Equivalentes 3--")
    
    juroAnual = input("    Taxa de juros anual (decimal): ")
    numeroSub = input("    Numero de subperiodos no ano (n de meses): ")
    taxaEfetiva = input("    Taxa efetiva para subperiodo: ")
    
    valueDict = {"juroAnual": juroAnual, "numeroSub": numeroSub, "taxaEfetiva": taxaEfetiva} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == None:
        return
        
    
    solution = solve( (1 + valueDict["taxaEfetiva"])**valueDict["numeroSub"] - 1 - valueDict["juroAnual"], valueDict[nameToSave])[0] 

    print("\n")
    print(f"    {nameToSave}: {solution}")
    

    valueDict[nameToSave] = solution
    myList = ["taxaEfetiva", "numeroSub", "juroAnual"]
    printList(myList)
    print(f'(1 + {valueDict["taxaEfetiva"]})**{valueDict["numeroSub"]} - 1 - {valueDict["juroAnual"]} = 0')


# valores a introduzir
#   -> periodo de tempos correspondente a um ano
#   -> TAN
#   -> Juro Correspondente
# retorna a equivalencia da TAN (Taxa anual nominal) no periodo desejado

# M
def TAN():
    """
    Valores recebidos
            -> Periodo
            -> TAN  (Taxa anual nominal)
            -> Juros correspondente
            
    Explicacao:
        Taxa anual utilizada em operações que envolvam o pagamento de juros, expressando assim os juros do empréstimo.

        TAN não inclui impostos nem outros encargos com o crédito, pelo que não deverá servir de termo de comparação entre empréstimos.
    """
    print("--TAN 3--")

    periodo = input("    Periodo a ser dividido: ")
    tan = input("    TAN (decimal): ")
    juroCorrespondente = input("    Juro Correspondente (decimal): ")

    valueDict = {"periodo": periodo, "tan": tan, "juroCorrespondente": juroCorrespondente} 
    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(valueDict["periodo"]/valueDict["tan"]/100 - valueDict["juroCorrespondente"], valueDict[nameToSave])[0]

    print("\n")
    print(f"    {nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["periodo", "tan", "jurosCorrespondente"]
    printList(myList)
    print(f'{valueDict["periodo"]}/{valueDict["tan"]}/100 - {valueDict["juroCorrespondente"]} = 0')


# valores a introduzir
#   -> periodo de tempos correspondente a um ano
#   -> TAE
#   -> Juros Correspondentes
#  retorna a equivalencia da TAE (taxa anual efetiva) no periodo desejado

# M
def TAE():
    """
    Valores recebidos
            -> Periodo
            -> TAE  (Taxa anual nominal)
            -> Juros correspondente
            
    Explicacao:
        Mede todos os custos associados a um determinado emprestimo
            Juros, comissoes bancarias, premeios dos seguros exigidos
        Nao incluid impostos como o do selo
        Igual a TAEG menos impostos
    """
    print("--TAE 3--")
    
    periodo = input("    Periodo a ser dividido: ")
    tae = input("    TAN (decimal): ")
    juroCorrespondente = input("    Juro Correspondente (decimal): ")

    valueDict = {"periodo": periodo, "tae": tae, "juroCorrespondente": juroCorrespondente} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve( ( (1 + valueDict["tae"]) ** (1/valueDict["periodo"]) - 1) - valueDict["juroCorrespondente"], valueDict[nameToSave])[0]
    
    print("\n")
    print(f"    {nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["tae", "periodo", "jurosCorrespondente"]
    printList(myList)
    print(f'(1 + {valueDict["tae"]}) ** (1/{valueDict["periodo"]}) - 1) - {valueDict["juroCorrespondente"]} = 0')


# valores a introduzir
#   -> cashFlow Atual
#   -> taxa de Atualização
#   -> periodo de Atualização
#   -> cashFlowAtualizado
# Pagina 10 da api
# M
def CashFlowAtualizado():
    """
    Valores recebidos
            -> Anuidade
            -> Taxa de Atualizacao
            -> Periodo atual
            -> Cash flow atualizado
            
    Explicacao:
        Quanto e que o meu cash flow vai valer daqui a x anos
    """
    print("--Cash Flow Atualizado 4--")

    anuidade = input("    Anuidade: ")
    taxaDeAtualizacao = input("    Taxa de Atualização: ")
    periodoAtual = input("    Periodo de Atualização: ")
    cashFlowAtualizado = input("    CashFlow Atualizado: ")
    
    valueDict = {"anuidade": anuidade, "taxaDeAtualizacao": taxaDeAtualizacao, "periodoAtual": periodoAtual, "cashFlowAtualizado": cashFlowAtualizado} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(valueDict["anuidade"] / ((1 + valueDict["taxaDeAtualizacao"])**(valueDict["periodoAtual"])) - valueDict["cashFlowAtualizado"], valueDict[nameToSave])[0]
    
    print("\n")
    print(f"    {nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["anuidade", "taxaDeAtualizacao", "periodoAtual", "cashFlowAtualizado"]
    printList(myList)
    print(f'{valueDict["anuidade"]} / ((1 + {valueDict["taxaDeAtualizacao"]})**({valueDict["periodoAtual"]})) - {valueDict["cashFlowAtualizado"]} = 0')

    
# valores a introduzir
#   -> Anuidade - A
#   -> taxa de Atualização - r
#   -> periodo de Atualização - n
#   -> valor da anuidade  - VA
#   G
def VaAnuidadeSemCrescimento(): 
    """
    Valores recebidos
            -> Anuidade
            -> Taxa de atualizacao
            -> Periodo Atual
            -> Valor Atual
            
    Explicacao:
        A soma ao fim de x anos que o meu investimento vai me dar
        Assumindo que nao tem crescimento e que o investimento tem uma data de vencimento

        Substituindo o tempo por infitno nesta formaula vou ter VaPerpetualidadeSemCrescimento

        Para calcular quantia prestacoes, retirar pagamento inicial
            Retirar pagamento final (cash flow atualizado)
        Depois dividir por fator anuidade 

    """
    print("--Valor Atual Anuidade Sem Crescimento 4--")

    anuidade = input("    Anuidade: ")
    taxaDeAtualizacao = input("    Taxa de Atualização: ")
    periodoAtual = input("    Periodo de Atualização: ")
    valorAtual = input("    Valor Atual: ")
    
    valueDict = {"anuidade": anuidade, "taxaDeAtualizacao": taxaDeAtualizacao, "periodoAtual": periodoAtual, "valorAtual": valorAtual} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve((valueDict["anuidade"]*((((1 + valueDict["taxaDeAtualizacao"]) ** valueDict["periodoAtual"]) - 1)/(((1 + valueDict["taxaDeAtualizacao"]) ** valueDict["periodoAtual"]) * valueDict["taxaDeAtualizacao"]))) - valueDict["valorAtual"], valueDict[nameToSave])[0]
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["capital", "capital", "taxaJuros", "anoFinal", "anoInicial", "valorAtual"]
    printList(myList)
    print(f'({valueDict["anuidade"]}*((((1 + {valueDict["taxaDeAtualizacao"]}) ** {valueDict["periodoAtual"]}) - 1)/(((1 + {valueDict["taxaDeAtualizacao"]}) ** {valueDict["periodoAtual"]}) * {valueDict["taxaDeAtualizacao"]}))) - {valueDict["valorAtual"]} = 0')



# valores a introduzir
#   -> Anuidade - A
#   -> Taxa de Atualização - r
#   -> Valor da Perpetualidade Sem Crescimento - VA

# M
def VaPerpetualidadeSemCrescimento(): 
    """
    Valores recebidos
            -> Taxa de atualizacao
            -> Anuidade
            -> Valor Atual Perpetualidade sem crescimento
            
    Explicacao:
        A soma ao fim de x anos que o meu investimento vai me dar
        Assumindo que o investimento nao tem crescimento e que o investimento nao tem data de vencimento

        Exemplos seria reformas, manutencao de pontes e barragens...
    """
    print("--Valor Atual Perpetualidade Sem Crescimento 3--")
    
    taxaDeAtualizacao = input("    Taxa de Atualização: ")
    Anuidade = input("    Anuidade: ")
    valorAtualPerpetualidadeSemCrescimento = input("    Valor atual perpetualidade sem crescimento: ")
    
    valueDict = {"taxaDeAtualizacao": taxaDeAtualizacao, "Anuidade": Anuidade, "valorAtualPerpetualidadeSemCrescimento": valorAtualPerpetualidadeSemCrescimento} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(valueDict["Anuidade"] * (1/valueDict["taxaDeAtualizacao"]) - valueDict["valorAtualPerpetualidadeSemCrescimento"] , valueDict[nameToSave])[0]
    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["Anuidade", "taxaDeAtualizacao", "valorAtualPerpetualidadeSemCrescimento"]
    printList(myList)
    print(f'valueDict["Anuidade"] * (1/valueDict["taxaDeAtualizacao"]) - valueDict["valorAtualPerpetualidadeSemCrescimento"] = 0')


# valores a introduzir
#   -> Anuidade
#   -> Taxa de Atualização
#   -> Taxa de crescimento
#   -> Valor atual Perpetuidade com crescimento

# M 
def VaPerpetualidadeComCrescimento():
    """
    Valores recebidos
            -> Anuidade
            -> Taxa de atualizacao
            -> Taxa de crescimento
            -> Valor Atual Perpetualidade sem crescimento
            
    Explicacao:
        A soma que o meu investimento vai me dar
        Assumindo que o investimento tem crescimento e que o investimento nao tem data de vencimento

        Exemplos seria reformas, manutencao de pontes e barragens...
    """
    print("--Valor Atual Perpetualidade Com Crescimento 4--")
    
    anuidade = input("  Anuidade: ") 
    taxaDeAtualizacao = input("    Taxa de Atualização: ")
    taxaCrescimento = input("    Taxa de Crescimento: ")
    valorAtualPerpetualidadeComCrescimento = input("    Valor Atual: ")
    
    valueDict = {"taxaDeAtualizacao": taxaDeAtualizacao, "taxaCrescimento": taxaCrescimento, "valorAtualPerpetualidadeComCrescimento": valorAtualPerpetualidadeComCrescimento, "anuidade": anuidade} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(valueDict["anuidade"] * (1/(valueDict["taxaDeAtualizacao"] - valueDict["taxaCrescimento"])) - valueDict["valorAtualPerpetualidadeComCrescimento"], valueDict[nameToSave])[0]
    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["anuidade", "taxaDeAtualizacao", "taxaCrescimento", "valorAtualPerpetualidadeComCrescimento"]
    printList(myList)
    print(f'{valueDict["anuidade"]} * (1/({valueDict["taxaDeAtualizacao"]} - {valueDict["taxaCrescimento"]})) - {valueDict["valorAtualPerpetualidadeComCrescimento"]}) = 0')


# valores a introduzir
#   -> Anuidade - A
#   -> taxa de Atualização - r
#   -> periodo de Atualização - n
#   -> taxa de crescimento - g
#   -> Valor Atual - VA

# Gui
# UNTESTED ON CURRENT VERSION
def VaAnuidadeComCrescimento(): 
    """
    Valores recebidos
            -> Anuidade
            -> Taxa de atualizacao
            -> Periodo Atual
            -> Taxa de atualizacao 
            -> Valor Atual
            
    Explicacao:
        A soma ao fim de x anos que o meu investimento vai me dar
        Assumindo que o investimento tem crescimento e que o investimento tem uma data de vencimento

        Substituindo o tempo por infitno nesta formaula vou ter VaPerpetualidadeComCrescimento
    """
    print("--Valor Atual Anuidade Com Crescimento-- 4")

    anuidade = input("    Anuidade: ")
    taxaDeAtualizacao = input("    Taxa de Atualização: ")
    periodoDeAtualizacao = input("    Periodo de Atualização: ")
    taxaDeCrescimento = input("    Taxa de crescimento: ")
    valorAtual = input("    Valor Atual: ")
    
    valueDict = {"anuidade": anuidade, "taxaDeAtualizacao": taxaDeAtualizacao, "periodoDeAtualizacao": periodoDeAtualizacao, "taxaDeCrescimento": taxaDeCrescimento, "valorAtual": valorAtual} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve((valueDict["anuidade"]*((1/(valueDict["taxaDeAtualizacao"]-valueDict["taxaDeCrescimento"]))-(((1 + valueDict["taxaDeCrescimento"])**valueDict["periodoDeAtualizacao"])/(((1+valueDict["taxaDeAtualizacao"])**valueDict["periodoDeAtualizacao"])*(valueDict["taxaDeAtualizacao"]-valueDict["taxaDeCrescimento"]))))) - valueDict["valorAtual"], valueDict[nameToSave])[0]
    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["anuidade", "taxaDeAtualizacao", "taxaDeCrescimento", "taxaDeCrescimento", "periodoDeAtualizacao", "taxaDeAtualizacao", "periodoDeAtualizacao", "taxaDeAtualizacao", "taxaDeCrescimento", "valorAtual"]
    printList(myList)
    print(f'({valueDict["anuidade"]}*((1/({valueDict["taxaDeAtualizacao"]}-{valueDict["taxaDeCrescimento"]}))-(((1 + {valueDict["taxaDeCrescimento"]})**{valueDict["periodoDeAtualizacao"]})/(((1+{valueDict["taxaDeAtualizacao"]})**{valueDict["periodoDeAtualizacao"]})*({valueDict["taxaDeAtualizacao"]}-{valueDict["taxaDeCrescimento"]}))))) - {valueDict["valorAtual"]} = 0')

# valores a introduzir 
#   -> taxa de Atualização 
#   -> fator de perpetualidade
# Slide 9 do capitulo 5
# fator pelo qual se multiplica uma anuidade para obter o valor atual de uma anuidade
# M
def FatorPerpetualidade():
    """
    Valores recebidos
            -> Taxa de Atualizacao
            -> Fator de Prepetualidade

    Explicacao:
        fator de crescimento do investimento perpetuo
    """
    print("--Fator Perpetualidade 2--")
    
    taxaDeAtual = input("   Taxa de atualizazação: ")
    fatorPerp = input("    Factor de Prepetualidade: ")

    valueDict = {"taxaDeAtual": taxaDeAtual, "fatorPerp": fatorPerp} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(1/valueDict["taxaDeAtualizacao"] - valueDict["fatorPerp"] , valueDict[nameToSave])[0]
    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["taxaDeAtualizacao", "fatorPerp"]
    printList(myList)
    print(f'1/{valueDict["taxaDeAtualizacao"]} - {valueDict["fatorPerp"]} = 0')


# valores a introduzir 
#   -> taxa de Atualização - r
#   -> periodo de atualizacao - n
#   -> fator de anuidade
# Slide 9 do capitulo 5
# fator pelo qual se multiplica uma anuidade para obter o valor atual de uma anuidade
# G
def FatorAnuidade():
    """
    Valores recebidos
            -> Taxa de Atualizacao
            -> Periodo Atual
            -> Fator de Anuidade

    Explicacao:
        fator de crescimento do investimento
    """
    print("--Fator Anuidade 2--")
    
    taxaDeAtualizacao = input("   Taxa de atualização: ")
    periodoAtual = input("    Periodo de atualização: ")
    fatorAnual = input("    Fator de Anuidade: ")

    valueDict = {"taxaDeAtualizacao": taxaDeAtualizacao, "fatorAnual": fatorAnual, "periodoAtual": periodoAtual} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(((((1 + valueDict["taxaDeAtualizacao"]) ** valueDict["periodoAtual"]) - 1)/(((1 + valueDict["taxaDeAtualizacao"]) ** valueDict["periodoAtual"]) * valueDict["taxaDeAtualizacao"])) - valueDict["fatorAnual"] , valueDict[nameToSave])[0]
    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["taxaDeAtualizacao", "periodoAtual", "taxaDeAtualizacao", "periodoAtual", "taxaDeAtualizacao", "periodoAtual", "taxaDeAtualizacao", "fatorAnual"]
    printList(myList)
    print(f'((((1 + valueDict["taxaDeAtualizacao"]) ** valueDict["periodoAtual"]) - 1)/(((1 + valueDict["taxaDeAtualizacao"]) ** valueDict["periodoAtual"]) * valueDict["taxaDeAtualizacao"])) - valueDict["fatorAnual"] = 0')



# valores a introduzir
#   -> valor de Mercado - Valor	esperado	de	venda	do	ativo	no	ano	n
#   -> valor contabilistico - Valor	de	compra	– Amortizações	Acumuladas no ano n.
#   -> taxa de Imposto
#   -> valor Residual 
# Slide 11 dos slides do capitulo 5, 
# Pagina 15 da API
# CashFlow positivo no final do investimento
# M
def ValorResidualInvestimento():
    """
    Valores recebidos
            -> Valor Mercado -> Valor esperado de venda do ativo no ano N
            -> Valor Contabilistico -> Valor de compra - amortizacoes acumuladas
            -> Taxa Imposto
            -> Valor Residual

    Explicacao:
        Mostrar se no fim de vida do projeto, foi um projeto lucrativo ou nao
        A venda no fim do teempo de vida de um projeto (ano n) de ymn dado ativo fixo origina geralmente um ganho ou perda extraordianria
        Se a emprea for lucrativa, este valor vai ter impacto fiscal
            Sobre a diferenca entre o valor de venda e o valor contabilistico
            Pagamentoi adicional ou reducao do valor de imposto a pagar
    """
    print("--Valor Residual do Investimento 4--")

    valorMercado = input("     Valor de mercado: ")
    valorContabilistico = input( "     Valor Contabilistico: ")
    taxaImposto = input("     taxa de Imposto: ")
    valorResidual = input("     Valor Residual: ")

    valueDict = {"valorMercado": valorMercado, "valorContabilistico": valorContabilistico, "taxaImposto": taxaImposto, "valorResidual": valorResidual} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return


    solution = solve(valueDict["valorMercado"] - (valueDict["valorMercado"] - valueDict["valorContabilistico"])*valueDict["taxaImposto"] - valueDict["valorResidual"], valueDict[nameToSave])[0]
    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["valorMercado", "valorMercado", "valorContabilistico", "taxaImposto", "valorResidual"]
    printList(myList)
    print(f'{valueDict["valorMercado"]} - ({valueDict["valorMercado"]} - {valueDict["valorContabilistico"]})*{valueDict["taxaImposto"]} - {valueDict["valorResidual"]} = 0')


# valores a introduzir
#   -> EBIT - resultanto antes de juros e impostos
#   -> Taxa imposto
#   -> Amortizações  
#   -> CashFlow de Exploração
# Slide 11 do capitulo 5 
# pagina 15 da api
# fundos provenientes da exploração da empresa
# M
def CashFlowExploracao():
    """
    Valores recebidos
            -> EBIT (earning before interest and tax)
            -> Amortizacoes
            -> Taxa de imposto
            -> Cash Flow de Exploracao
            -> Em dividas (true or false)

    Explicacao:
        Quando cash flow vai ser possivel explorar a partir de um investimento
        Ter atencao a ebit negativa
    """
    print("--Valor cashFlow Exploracao 5--")

    EBIT = input("     EBIT: ")
    amortizações = input( "     Montante Amortizações (valor negativo): ")
    taxaImposto = input("   Taxa de Imposto: ")
    cashFlowExpl = input("    CashFlowExploração: ")
    emDividas = input("    Em dividas (true/false): ")

    valueDict = {"EBIT": EBIT, "amortizações": amortizações, "taxaImposto": taxaImposto, "cashFlowExpl": cashFlowExpl} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return
    if(not emDividas):
        solution = solve(valueDict["EBIT"] * (1 -valueDict["taxaImposto"]) + valueDict["amortizações"] - valueDict["cashFlowExpl"], valueDict[nameToSave])[0]
    else:
        solution = solve(valueDict["EBIT"] + valueDict["amortizações"] - valueDict["cashFlowExpl"], valueDict[nameToSave])[0]        
    print(f"")
    print(f"{nameToSave}: {solution}")
    
    valueDict[nameToSave] = solution
    if(not emDividas):
        myList = ["EBIT", "taxaImposto", "amortizações", "cashFlowExpl"]
        printList(myList)
        print(f'{valueDict["EBIT"]} * (1 - {valueDict["taxaImposto"]}) + {valueDict["amortizações"]} - {valueDict["cashFlowExpl"]} = 0')
    else:
        myList = ["EBIT", "amortizações", "cashFlowExpl"]
        printList(myList)
        print(f'{valueDict["EBIT"]} + {valueDict["amortizações"]} - {valueDict["cashFlowExpl"]} = 0')
   


# valores a introduzir
#   -> custo médio ponderado do capital
#   -> custo do capital próprio
#   -> percentagem de capital próprio
#   -> custo do capital alheio líquido de impostos - (taxa de juro dos empréstimos)
#   -> percentagem de capital alheio
#   -> taxa de imposto
#   -> taxa de atualização com financiamento misto (Capital Próprio e dívida)
# pagina 21 api
# indica qual o custo em média do capital envolvido num investimento, isto é, o valor do "juro" mais relevante
# M 
def TaxaAtualizacaoComFinanciamentoMistoCMPC():    
    """
    Valores recebidos
            ->   Custo do capital propiro
            ->   Percentagem do capital proprio
            ->   Custo do capital alheio liquido de impostos
            ->   Percentagem capital alheio
            ->   Taxa de imposto
            ->   Taxa de atualizacao com financiamento misto
            
    Explicacao:
        Adaptacao do risco quando existe dinheiro de vairas fontes
    """
    print("--Taxa Atualizacao Com Financiamneto Misto (CMPC) 6--")

    custCapProp = input("   Custo do Capital Próprio (Percentagem): ")
    percCapProp = input("    Capital Próprio (decimal): ")
    custCapAlheio = input("    Custo do Capital Alheio (Percentagem): ")
    percCapAlheio = input("    Capital Alheio (decimal): ")
    taxaImposto = input("    Taxa de imposto (decimal): ")
    taxaAtualFinMisto = input("    Taxa de Atualização com Financiamento Misto: ")
    
    valueDict = {"custCapProp": custCapProp, "percCapProp": percCapProp, "custCapAlheio": custCapAlheio, "percCapAlheio": percCapAlheio, "taxaImposto": taxaImposto, "taxaAtualFinMisto": taxaAtualFinMisto}
    nameToSave = getMissingValue(valueDict)

    solution = solve(valueDict["custCapProp"] * valueDict["percCapProp"] + valueDict["custCapAlheio"] * valueDict["percCapAlheio"] * (1 - valueDict["taxaImposto"])- valueDict["taxaAtualFinMisto"], valueDict[nameToSave])[0]        

    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["custCapProp", "percCapProp", "custCapAlheio", "percCapAlheio", "taxaImposto", "taxaAtualFinMisto"]
    printList(myList)
    print(f'{valueDict["custCapProp"]} * {valueDict["percCapProp"]} + {valueDict["custCapAlheio"]} * {valueDict["percCapAlheio"]} * (1 - {valueDict["taxaImposto"]})- {valueDict["taxaAtualFinMisto"]} = 0')


# valores a introduzir 
#   -> cashFlow atualizado
#   -> numero de periodos
#   -> taxa de atualização
#   -> valor Atual Líquido

# consiste na soma de todos os cashflows de um projeto, indica se o projeto é rentável, quando maior que 0, ou não
# quando maior o val mais rentável é o projeto

# Z
def VAL():
    """
    Valores recebidos
            ->   Tabela de cash flow representado por numeros divididos por espacos
            ->   Numero de periodos que eu quero
            ->   Taxa de atualizacao -> inflacao

    Explicacao:
        Analisando um so projeto se VAL > 0 -> Projeto rentavel
            Exploracao atualizadas excedem os Cash FLow
            Tem uma rentabilidade maior que o custo do capital
        Dois ou mais projetos se VAL(A) > VAL(B) -> A preferivel em relacao a B
            Menos se houver condicoes especiais em cada um, como duracao ou diferenca em capital necessario
    """

    print("--Valor Atual Líquido 4--")

    tabelaCashFlow = input("    Tabela de cashflow (numeros com espacos): ")
    numeroPeriodos = input("    Numero de Períodos: ")
    taxaAtualizacao = input("   Taxa de Atualização: ")
    val = input("   Valor Atual Líquido: ")

    tabelaCashFlow = [float(x) for x in tabelaCashFlow.split(" ")]
    
    valueDict = {"numeroPeriodos": numeroPeriodos, "taxaAtualizacao":taxaAtualizacao, "val": val}
    nameToSave = getMissingValue(valueDict)

    k = symbols("k")

    listaCashFlow = Array(tabelaCashFlow)  
    eq = summation(listaCashFlow[k]/((1+valueDict["taxaAtualizacao"])**k), (k,0,int(valueDict["numeroPeriodos"])-1))
    
    solution = solve(eq-valueDict["val"], valueDict[nameToSave])[0]
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["capital", "capital", "taxaJuros", "anoFinal", "anoInicial", "valorAtual"]
    printList(myList)
    print(f'{valueDict["capital"]} + (({valueDict["capital"]} * {valueDict["taxaJuros"]}) * ({valueDict["anoFinal"]} - {valueDict["anoInicial"]}) - {valueDict["valorAtual"]}) = 0')


# M 
def TIR():    
    print("--Taxa de Rentibilidade interna --")

    print(" Explicação: \n Taxa de atualização para a qual o VAL é zero \n \
         Problemas: \n \
             1º pode existir mais do que uma TIR quando existem cashFlows negativos finais ou intermédios\n\
                 2º pode não existir sequer TIR \n\
                     3º É inadquada para projetos mutualmente exclusivos \n \
                         Para calcular introduza no calculo do VAL o valor deste a zero")

# valores a inserir 
#   -> periodo de tempo que demorámos a reaver o nosso dinheiro
#   -> numero do ultimo periodo negativo a contar do periodo 0
#   -> valor no cash flow acumulado até o ultimo periodo negativo
#   -> montante do primeiro cashFlow positivo (acumulado) 

# indica o periodo de tempo necessário para o montante investido ser recuperado
# M
def PeriodoDeRecuperacaoInvestimento():
    """
    Valores recebidos
        -> periodo de tempo que demorámos a reaver o nosso investimento
        -> numero do ultimo periodo negativo a contar do periodo 0
        -> valor no cash flow acumulado até o ultimo periodo negativo
        -> montante do primeiro cashFlow positivo (acumulado) 

    Explicacao:
        Tempo necessário para que os cash flows atualizados gerados pelo
    projeto igualem (recuperem) o capital investido inicialmente.
        
    """
    
    # slide 19

    print("--Periodo de Recuperação do Investimento 4--")

    periodoDeRecuperacao = input("    Periodo de Recuperação: ")
    periodoNegativo = input("     Número do último Periodo Negativo: ")
    cashflowPeriodonegativo = input("     Montante do ultimo cashFlow acumulado Negativo (valor positivo): ")
    cashflowPositivo = input("    Montante do primeiro cashFlow atualizado positivo: ")
        
    valueDict = {"periodoDeRecuperacao": periodoDeRecuperacao, "periodoNegativo": periodoNegativo, "cashflowPeriodonegativo": cashflowPeriodonegativo, "cashflowPositivo": cashflowPositivo} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return

    solution = solve(valueDict["periodoNegativo"] + valueDict["cashflowPeriodonegativo"]/valueDict["cashflowPositivo"] - valueDict["periodoDeRecuperacao"], valueDict[nameToSave])[0]     

    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["periodoNegativo", "cashflowPeriodonegativo", "cashflowPositivo", "periodoDeRecuperacao"]
    printList(myList)
    print(f'{valueDict["periodoNegativo"]} + {valueDict["cashflowPeriodonegativo"]}/{valueDict["cashflowPositivo"]} - {valueDict["periodoDeRecuperacao"]} = 0')




# valores a introduzir
#   -> taxa de renumeração de um ativo
#   -> prémio de risco
#   -> taxa de atualização do investimento financiado

def TaxaAtualizacaoInvestimentoFinanciado():
    """
    Valores recebidos
        -> Taxa de renumeracao
        -> Premio de risco
        -> Taxa de atualizacao financiado 
    
    Explicacao:
        CMPC  -> Weighted Average Cost of Capital
            Custo medio ponderado do capital

    """
    print("--Taxa de Atualização para um Investimento Financiado (CMPC) 3--")

    taxaRenumeracao = input("     Taxa de Renumeração do Ativo: ")
    premRisco = input( "     Prémio de Risco: ")
    taxaAtualInvFin = input("    Taxa de Atualização de Investimento Financiado: ")

    valueDict = {"taxaRenumeracao": taxaRenumeracao, "premRisco": premRisco, "taxaAtualInvFin": taxaAtualInvFin} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return
    
    solution = solve(valueDict["taxaRenumeracao"] + valueDict["premRisco"] - valueDict["taxaAtualInvFin"], valueDict[nameToSave])[0]        

    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["taxaRenumeracao", "premRisco", "taxaAtualInvFin"]
    printList(myList)
    print(f'{valueDict["taxaRenumeracao"]} + {valueDict["premRisco"]} - {valueDict["taxaAtualInvFin"]} = 0')


# valores a introduzir
#   -> Índice de rentabilidade 
#   -> VAL
#   -> Investimento Inicial
# Slide 5 do capitulo 5
# M
def IndiceRentabilidadeVAL():
    """
    Valores recebidos
        -> Indice de rentabilidade
        -> VAL (valor atual liquido)
        -> Investimneto Inicial 

    Explicacao:
        Indica o quão rentável é um projeto tendo em conta o seu valor atual líquido
        Critério de aceitação > 1

    """

    # slide 20
    
    print("--Indice de Rentabilidade através do VAL 3--")

    indiceRent = input("    Indice Rentabilidade: ")
    VAL = input("   Valor Atual Líquido: ")
    investimentoIni = input("   Investimento Inicial: ")

    valueDict = {"indiceRent": indiceRent, "VAL": VAL, "investimentoIni": investimentoIni} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return
    
    solution = solve((valueDict["VAL"] + valueDict["investimentoIni"])/valueDict["investimentoIni"] - valueDict["indiceRent"], valueDict[nameToSave])[0]        

    print(f"{nameToSave}: {solution}") 

    valueDict[nameToSave] = solution
    myList = ["VAL", "investimentoIni", "investimentoIni", "indiceRent"]
    printList(myList)
    print(f'({valueDict["VAL"]} + {valueDict["investimentoIni"]})/{valueDict["investimentoIni"]} - {valueDict["indiceRent"]} = 0')

# valores a introduzir
#   -> Índice de rentabilidade 
#   -> VA
#   -> Investimento Inicial

# M
def IndiceRentabilidadeVA():
    """
    Valores recebidos
        -> Índice de rentabilidade 
        -> VA
        -> Investimento Inicial

    Explicacao:
        Indica o quão rentável é um projeto tendo em conta o seu índice de rentabilidade
        Critério de aceitação > 1

    """

    # slide 20

    print("--Indice de Rentabilidade através do VA (Rácio Beneficio-Custo) 3--")

    indiceRent = input("    Indice Rentabilidade: ")
    racioBeneficioCusto = input("  Rácio Beneficio-Custo: ")
    investimentoIni = input("   Investimento Inicial: ")

    valueDict = {"indiceRent": indiceRent, "racioBeneficioCusto": racioBeneficioCusto, "investimentoIni": investimentoIni} 

    nameToSave = getMissingValue(valueDict)
    if nameToSave == "":
        return
    
    solution = solve(valueDict["racioBeneficioCusto"]/valueDict["investimentoIni"] - valueDict["indiceRent"], valueDict[nameToSave])[0]        

    
    print(f"{nameToSave}: {solution}")

    valueDict[nameToSave] = solution
    myList = ["racioBeneficioCusto", "investimentoIni", "indiceRent"]
    printList(myList)
    print(f'{valueDict["racioBeneficioCusto"]}/{valueDict["investimentoIni"]} - {valueDict["indiceRent"]} = 0')



# valores a inserir
#   -> numero de periodos
#   -> despezas de investimento de cada periodo
#   -> periodo de desvalorização de cada item desvaloralizável
#   -> numero de items desvalorarizáveis - consideramos que é sempre 1 ou 0
#   -> vendas
#   -> custos operacionais
#   -> periodo de depreciação
#   -> montante a depreciar
#   -> Resultado operacional (EBIT)
#   -> cashFlow Exploração
#   -> cashFlow Total
#   -> taxa de imposto

# M
def MapaDeCashFlow():
    numerodeperiodos = int(input("    Insira o numero de Periodos do projeto ano 0 incluido: "))
    numItensDesval = int(input("    Insira o numero de Itens Desvaloralizáveis: "))
    valorDepreciavel = [[0 for y in range(3) ]for x in range(numItensDesval)]
    print("    Insira o com maior periodo de depreciação primeiro ")
    for x in range(numItensDesval):
        print(f"    Insira valores para o objeto depreciavel numero {x+1}")
        valorDepreciavel[x][0] = int(input("    Insira o numero de Periodos em que se deprecia: ")) #numPeriodosDepreciacao
        valorDepreciavel[x][1] = int(input("    Insira o montante Inicial a ser Depreciado (positivo): ")) #montInicialADepreciar
        valorDepreciavel[x][2] =  valorDepreciavel[x][1] / valorDepreciavel[x][0] #montPorPeriodo
    taxaImposto = float(input("    Taxa de imposto (decimal): "))
    taxaAtualizacao = float(input("   Taxa de Atualização (decimal): "))
    cashflowAtualizado = 0
    amortizacoes = 0

    #Matriz dos valores
    Matrix = [[0 for x in range(numerodeperiodos+1)]for y in range(16)] 
    Aux = [[" " for x in range(numerodeperiodos+1)]for y in range(16)]

    Aux[0][0] = " Rubrica/Periodo--------------------------------------------------"
    Aux[1][0] = " (-) Despesas de Investimento-------------------------------------"
    Aux[2][0] = " (+) Valor Residual do Investimento-------------------------------" 
    Aux[3][0] = " CashFLow do Investimento(=1+2)-----------------------------------"
    Aux[4][0] = " Vendas-----------------------------------------------------------"
    Aux[5][0] = " Custos fixos - Gastos Pessoal------------------------------------"
    Aux[6][0] = " Custos fixos - Manutenção, Seguro e Energia----------------------"
    Aux[7][0] = " Custos Variavéis - Fabrico---------------------------------------"
    Aux[8][0] = " Custos Variáveis - Administração---------------------------------"
    Aux[9][0] = " Depreciações + Amortizações--------------------------------------"
    Aux[10][0] = " Resultado Operacional(EBIT)--------------------------------------"
    Aux[11][0] = " Resultado Líquido[EBIT x (1-t)]----------------------------------"
    Aux[12][0] = " CFExploração = (Depreciações + Amortizações) + Resultado Líquido-"
    Aux[13][0] = " CFTotal  = CFInvestimento + CFExploração-------------------------"
    Aux[14][0] = " CFAtualizado  = CFTotal * Fator Atualização[1/(1+r)**n]----------"
    Aux[15][0] = " CFAcumulado------------------------------------------------------"

    for i in range(1, numerodeperiodos+1):
        Aux[0][i] = f"{i-1}"
    for numColuna in range(1, numerodeperiodos+1): 
        print(f"Valores para o Período: {numColuna-1}\n")
            
        # Depreciações e Amortizações
        if(numColuna >= 2):
            amortizacoes = int(input(f"    Amortizações do Periodo {numColuna-1}: "))
            if(numItensDesval >= 1):
                if(numColuna <= valorDepreciavel[0][0] + 1):
                    Matrix[9][numColuna] = - valorDepreciavel[0][2] + amortizacoes
                    Aux[9][numColuna] = f" - {valorDepreciavel[0][2]} + {amortizacoes}"
                    valorDepreciavel[0][1] -= valorDepreciavel[0][2]     
                    aux = 1
                    if(numItensDesval > 1):
                        while(aux < numItensDesval):
                            if(numColuna <= valorDepreciavel[aux][0] + 1):   
                                Matrix[9][numColuna] -= valorDepreciavel[aux][2]
                                Aux[9][numColuna] += f" - {valorDepreciavel[aux][2]}"
                                valorDepreciavel[aux][1] -= valorDepreciavel[aux][2]
                            aux += 1
                    Aux[9][numColuna] += f" = {Matrix[9][numColuna]}"
                
        # Despesas do Investimento
        Matrix[1][numColuna] = int(input(f"   Insira despesas de investimento do periodo {numColuna-1}: "))
        Aux[1][numColuna] = f"{Matrix[1][numColuna]}"

        # Valor Residual do investimento 
        if(numColuna == numerodeperiodos):
            for x in range(numItensDesval):
                valorMercado = int(input(f"     Valor Comercial da Mercadoria Comprada {x+1}: "))
                if(x == 0):
                    Matrix[2][numerodeperiodos] = valorMercado - (valorMercado - valorDepreciavel[x][1]) * taxaImposto
                    Aux[2][numerodeperiodos] = f"{valorMercado}-({valorMercado}-{valorDepreciavel[x][1]})*{taxaImposto}={Matrix[2][numerodeperiodos]}"
                else:
                    Aux[2][numerodeperiodos] = f"{Matrix[2][numerodeperiodos]}+{valorMercado}-({valorMercado}-{valorDepreciavel[x][1]})*{taxaImposto}"
                    Matrix[2][numerodeperiodos] += valorMercado - (valorMercado - valorDepreciavel[x][1]) * taxaImposto
                    Aux[2][numerodeperiodos] += f"={Matrix[2][numerodeperiodos]}"

        # Cashflow do Investimento
        if(numColuna == numerodeperiodos):            
            Matrix[3][numColuna] = Matrix[1][numColuna] + Matrix[2][numColuna]
            Aux[3][numColuna] = f"{Matrix[1][numColuna]}+{Matrix[2][numColuna]}"
            
        else:
            Matrix[3][numColuna] = Matrix[1][numColuna]
            Aux[3][numColuna] = f"{Matrix[1][numColuna]}"


        # Vendas
        valVendas = int(input(f"    Vendas do Periodo {numColuna-1}: "))
        Matrix[4][numColuna] = valVendas
        Aux[4][numColuna] = f"{valVendas}"

        # Custos fixos - Gastos Pessoal
        if(numColuna > 2 and (int(input("  Custos fixos - Gastos Pessoal estão iguais? (0 ou 1): ")) == True)):    
            Matrix[5][numColuna] = valCustosFixPess
            Aux[5][numColuna] = f"{valCustosFixPess}"
            
        elif(numColuna >= 2):
            valCustosFixPess = int(input(f" Custos Fixos em Gastos de Pessoal {numColuna-1}: "))
            Matrix[5][numColuna] = valCustosFixPess
            Aux[5][numColuna] = f"{valCustosFixPess}"


        # Custos fixos - Manutenção, Seguro e Energia
        if(numColuna > 2 and (int(input("  Custos fixos - Manutenção, Seguro e Energia estão iguais? (0 ou 1): ")) == True)): 
            Matrix[6][numColuna] = valCustosFixMan
            Aux[6][numColuna] = f"{valCustosFixMan}"

        elif (numColuna >= 2):
            valCustosFixMan = int(input(f" Custos fixos - Manutenção, Seguro e Energia {numColuna-1}: "))
            Matrix[6][numColuna] = valCustosFixMan
            Aux[6][numColuna] = f"{valCustosFixMan}"

        # Custos Variavéis - Fabrico
        if(numColuna >= 2):
            valCustosVarFab = int(input(f" Custos Variavéis - Fabrico {numColuna-1}: "))
            Matrix[7][numColuna] = valCustosVarFab
            Aux[7][numColuna] = f"{valCustosVarFab}"

        # Custos Variáveis - Administração
        if(numColuna >= 2):
            valCustosVarAdmin = int(input(f" Custos Variáveis - Administração {numColuna-1}: "))
            Matrix[8][numColuna] = valCustosVarAdmin
            Aux[8][numColuna] = f"{valCustosVarAdmin}"
            
        # Resultado Operacional
        Matrix[10][numColuna] = Matrix[4][numColuna] + Matrix[5][numColuna] + Matrix[6][numColuna] + Matrix[7][numColuna] + Matrix[8][numColuna] + Matrix[9][numColuna]
        Aux[10][numColuna] = f"{Aux[4][numColuna]} {Aux[5][numColuna]} {Aux[6][numColuna]} {Aux[7][numColuna]} {Aux[8][numColuna]}+{Aux[9][numColuna]}={Matrix[10][numColuna]}"

        # Resultado Líquido 
        aplicavel = int(input("    imposto é aplicável? (1 ou 0): "))
        if(Matrix[10][numColuna] < 0):    
            if(aplicavel == True):
                Matrix[11][numColuna] = Matrix[10][numColuna] * (1 - taxaImposto)
                Aux[11][numColuna] = f"{Matrix[10][numColuna]}(= /\)*(1 - {taxaImposto})"

            else: 
                Matrix[11][numColuna] = Matrix[10][numColuna]
                Aux[11][numColuna] = f"{Matrix[10][numColuna]}"
        else:
            Matrix[11][numColuna] = Matrix[10][numColuna] * (1 - taxaImposto)
            Aux[11][numColuna] = f"{Matrix[10][numColuna]}(= /\)*(1 - {taxaImposto})"

        # CashFlow de Exploração
        Matrix[12][numColuna] = Matrix[11][numColuna] - Matrix[9][numColuna]
        Aux[12][numColuna] = f"{Matrix[11][numColuna]}-{Matrix[9][numColuna]}={Matrix[12][numColuna]}"

        # Cashflow Total
        Matrix[13][numColuna] = Matrix[12][numColuna] + Matrix[3][numColuna]
        Aux[13][numColuna] = f"{Matrix[12][numColuna]}+{Matrix[3][numColuna]}={Matrix[13][numColuna]}"


        # CashFlow actualizado
        Matrix[14][numColuna] = Matrix[13][numColuna]/((1+taxaAtualizacao)**(numColuna - 1))
        Aux[14][numColuna] = f"{Matrix[13][numColuna]}/((1+{taxaAtualizacao})**({numColuna} - 1))={Matrix[14][numColuna]}"


        # Cashflow Acumulado
        if(numColuna != 1):
            Matrix[15][numColuna] = Matrix[15][numColuna-1] + Matrix[14][numColuna]
            Aux[15][numColuna] = "{:.2f}".format(Matrix[15][numColuna-1]) + " + " + "{:.2f}".format(Matrix[14][numColuna]) + f"= {Matrix[15][numColuna]}"

        else:
            Matrix[15][numColuna] = Matrix[14][numColuna]
            Aux[15][numColuna] = f"{Matrix[14][numColuna]}"
    
    #isto "{:.2f}".format(13.949999999999999)
    espacoColuna = [0 for x in range(numerodeperiodos+1)]

    for x in range(16):
        for y in range(0, numerodeperiodos+1):
            if(y == 0):
                espacoColuna[y] = len(Aux[x][y])  
            elif(espacoColuna[y] < len(Aux[x][y])):
                espacoColuna[y] = len(Aux[x][y])
    
    for x in range(16):
        for y in range(0, numerodeperiodos+1):
            if(y == 0):
                print("| " + Aux[x][y][0:30], end=" ")
            else:
                print(" | ", end="")
                for i in range(0, espacoColuna[y]-len(Aux[x][y])):
                    print(" ", end="")
                print(Aux[x][y] + " | ", end=" ")
        print("\n", end="")
    print("\n")
    



    
            

# ----------------8<-------------[ cut here ]-------------------------------------------------------------------
# ----------------8<-------------[ cut here ]-------------------------------------------------------------------
# ----------------8<-------------[ cut here ]-------------------------------------------------------------------
# ----------------8<-------------[ cut here ]-------------------------------------------------------------------
# ----------------8<-------------[ cut here ]-------------------------------------------------------------------


def Visao():
    print("--Visão--")
    print("    Preocupa-se com futuro e fornece direção a longo prazo (“where we are going”): \n \
         que mercados perseguir, quais os produtos, tecnologia e clientes onde nos iremos focar, e o tipo de organização que pretendemos criar. \n \
             A visão é elaborada pela gestão de topo de uma organização. \n \
                  Usa linguagem distinta e específica de modo a distinguir uma organização dos seus concorrentes.")

def Missao():
    print("--Missão--")
    print("     Centra-se no presente, no negócio atual (“who we are and what we do”): \n \
        nos produtos e serviços oferecidos atualmente, na área geográfica onde a empresa atua, \
            nas necessidades dos clientes que estão a ser servidas e nas capacidades que a empresa possui.")

def Objetivos():
    print("--Objetivos--")
    print("    Convertem a “visão” em alvos de desempenho específicos e permitem monitorar o desempenho da organização. \n \
         Objetivos são necessários a todos os níveis da organização (para toda a organização, para cada unidade de negócio, \
             departamentos funcionais e unidades operacionais); \n\
                 Devem ser definidos através de um processo “top-down”, com colaboração entre níveis, de modo a \
                     garantir que os objetivos estabelecidos para níveis inferiores apoiam os objetivos dos níveis superiores. \n \
                          Objetivos bem definidos são: \n \
                              – quantificáveis, \n\
                                  – mensuráveis e \n\
                                      – incluem um prazo para serem atingidos. \n\
                                          Tipos de objetivos: \n\
                                              – curto prazo e longo prazo \n\
                                                  – financeiros e estratégicos.")

def Analise():
    print("--Análise--")
    print("    O objectivo da análise, externa e interna, é obter informação que \
        permita ajudar a organização a elaborar a sua estratégia.")
    print("--Análise Interna--\n")
    print("     tem como finalidade identificar os principais desenvolvimentos que existem no\
         exterior da organização e que a afectam na forma de oportunidades ou ameaças.")
    print("--Análise Externa--\n")
    print("    Estuda o ambiente interno da organização de modo a identificar as forças/pontos \
        fortes e fraquezas/pontos fracos que aí existem.")