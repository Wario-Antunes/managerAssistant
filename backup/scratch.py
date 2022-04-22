from sympy.solvers import solve
from sympy import Symbol, symbols
from sympy import Array 
from sympy import summation
from sympy import init_printing


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
    # equation = f"{valueDict["capital"]} + ((valueDict["capital"] * valueDict["taxaJuros"]) * (valueDict["anoFinal"] - valueDict["anoInicial"]) - valueDict["valorAtual"])
    # solution = solve(equation)
    
    solution = solve(valueDict["capital"] + ((valueDict["capital"] * valueDict["taxaJuros"]) * (valueDict["anoFinal"] - valueDict["anoInicial"])   - valueDict["valorAtual"]), valueDict[nameToSave])[0]
    # Resposta
    print("\n")
    print(f"    {nameToSave}: {solution}")

    # Valores
    valueDict[nameToSave] = solution
    myList = ["capital", "capital", "taxaJuros", "anoFinal", "anoInicial", "valorAtual"]

    print(f'{valueDict["capital"]} + (({valueDict["capital"]} * {valueDict["taxaJuros"]}) * ({valueDict["anoFinal"]} - {valueDict["anoInicial"]}) - {valueDict["valorAtual"]}) = 0')


init_printing() 
JuroSimples()

