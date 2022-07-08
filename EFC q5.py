def main():
    estados = list(input("Insira os estados possiveis, separados por espaco: ").split())
    
    elementos = list(input("Insira os elementos presentes no alfabeto da fita: ").split())

    transicoes = []
    l1 = [" "]
    
    for i in elementos: l1.append(i)

    transicoes.append(l1)

    for i in range(len(estados)):
        l = [""]*(len(elementos) + 1)
        l[0] = estados[i]
        transicoes.append(l)
    
    print("Insira, progressivamente, as transicoes de acordo com as solicitacoes. Deixe vazio caso nao haja transicao\n")

    for i in range(1, len(transicoes)):
        for j in range(1, len(transicoes[0])):
            print("No estado " + transicoes[i][0] + " lendo " + transicoes[0][j])
            transicoes[i][j] = list(input("Estado destino, elemento de gravacao e movimento, separados por espaco: ").split())

    qFitas = int(input("\nInsira o numero de fitas que a MT possui: "))

    if qFitas == 1:
        fita = input("Insira a configuracao que deseja rodar na fita: ")
        fita = [fita]
        finais = list(input("Insira os estados pertencentes ao conjunto dos finais, separados por espaco: ").split())

        maquinaDeTuring(estados, transicoes, fita, finais)
    #elif qFitas == 2:
    
    else:
        print("O algoritmo não suporta máquinas com 3 ou mais fitas.")


def maquinaDeTuring(estados, transicoes, fitas, qf):
    if len(fitas) == 1:
        monoFita(estados, transicoes, fitas[0], qf)
    
    #elif len(fitas) == 2:
    #    multiFita(estados, transicoes, fitas, qf)

def monoFita(estados, transicoes, fita, qf):
    #assumindo que a fita sempre comeca a ser lida em q0
    p = 0
    ativa = True
    estado = "q0"
    fita += "B"

    #primeira computacao invariavel
    print("q0",end="")
    for i in fita:
        print(i,end="")
    print()

    while ativa and p < len(fita):
        elementoLido = fita[p]

        transicao = acharTransicaoMono(transicoes, elementoLido, estado)

        #caso "transicao" tenha tamanho 1, significa que encontrou um erro. interromper computacao
        if len(transicao) == 1:
            ativa = False
            print(transicao[0])
        
        else:
            estado, fita, p = executarTransicaoMono(transicao, p, fita)

            if p == "erro":
                ativa = False
                print("Movimentacao invalida de fita, encerrando a computacao")
            
            if estado not in estados:
                ativa = False
                print("Movimentacao para estado invalido, encerrando a computacao")

            if p > len(fita):
                ativa = False
                print("Erro na movimentacao da cabeca de leitura e gravaao, encerrando a computacao")
            
            else: printarComputacao(fita, p, estado)

            if estado in qf:
                print("\nComputacoes concluidas, entrada aceita por estado final!")
                ativa = False

#imprime a computacao da iteracao    
def printarComputacao(f, p, e):
    computacao = ""

    for i in range(p):
        computacao += f[i]

    computacao += e
    
    for i in range(p, len(f)):
        computacao += f[i]
    
    print(computacao,end="\n")

#achar a transicao na matriz para uma maquina monofita
def acharTransicaoMono(mt, el, es):
    acheiEstado = False
    i = 0
    while i < len(mt) and not acheiEstado:
        if mt[i][0] == es:
            acheiEstado = True
            ped = i
        i += 1
    
    if acheiEstado:
        acheiElemento = False
        i = 1
        while i < len(mt[0]) and not acheiElemento:
            if mt[0][i] == el:
                c = i
                acheiElemento = True
            i += 1

        t = mt[ped][c]

        if not acheiElemento: return ["Elemento fora do alfabeto, encerrando a computacao"]       
        if t == []: return ["Transicao nao encontrada, encerrando a computacao"]
        
        return t
    
    else:
        return ["Estado nao encontrado, encerrando a computacao"]

#executar a transicao da iteracao numa maquina monofita
def executarTransicaoMono(t, p, f):
    e = t[0] #estado destino
    
    #troca do elemento original pelo elemento da transicao
    novaf = ""
    for i in range(len(f)):
        if p != i: novaf += f[i]
        else: novaf += t[1]

    if t[2] == "L": p -= 1 #andando para a esquerda
    elif t[2] == "R": p += 1 #andando para a direita
    elif t[2] != "S": p = "erro"

    return e, novaf, p


#def multiFita(estados, transicoes, fitas, qf):

main()