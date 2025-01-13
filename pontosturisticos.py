import heapq
import sys
# heappush: Adiciona um elemento à fila com sua prioridade associada.
# heappop: Remove e retorna o elemento com a prioridade mais alta (o elemento com o menor valor).

def dijkstra(pontos, inicio, fim):
    distancias = {no: sys.maxsize for no in pontos}
    distancias[inicio] = 0
    origem =  {no: None for no in pontos}
    rota = []
    visitados = set() #evita a repetição de nós visitados
    prioridade = [(0, inicio)]
    while prioridade:

        distancia_atual, no_atual = heapq.heappop(prioridade)
        if no_atual in visitados:
            continue


        visitados.add(no_atual)
        
        if no_atual == fim:
            break
        for vizinho, peso in pontos[no_atual]:
            nova_distancia = peso + distancia_atual

            if nova_distancia < distancias[vizinho]:
                origem[vizinho] = no_atual
                distancias[vizinho] = nova_distancia
                heapq.heappush(prioridade,(nova_distancia, vizinho))

    no_atual = fim
    while no_atual  is not None:
        rota.append(no_atual)
        no_atual = origem[no_atual]
       

    return rota[::-1]
def verificacao(resultado):
    match resultado:
        case '1':
            return'praia de tambaú'
        case '2':
            return'mercado de artesanato paraibano'
        case '3':
            return'piscinas naturais de picãozinho'
        case '4':
            return'jardim botânico'
        case '5':
            return'parque sólon de lucena'
        case _:
            return False
        

pontos = {
    'praia de tambaú': [('jardim botânico', 6.4), ('piscinas naturais de picãozinho', 0.11), ('mercado de artesanato paraibano', 0.7)],
    'mercado de artesanato paraibano': [('jardim botânico', 7.9), ('praia de tambaú', 0.7)],
    'piscinas naturais de picãozinho': [('praia de tambaú', 0.11)],
    'jardim botânico': [('mercado de artesanato paraibano', 7.9), ('praia de tambaú', 6.4), ('parque sólon de lucena', 3.2)],
    'parque sólon de lucena': [ ('jardim botânico',3.2)],   
    # 'centro cultura de São Francisco': [('parque sólon de lucena', 2), ('jardim botânico', 4.9), ('praia de tambaú', 7.9), ('piscinas naturais de picãozinho', 7.8)],
}

while True:
    print("Digite o número de acordo com as opções:")
    print("1 - Praia de Tambaú \
\n2 - Mercado de Artesanato Paraibano \
\n3 - Piscinas Naturais de Picãozinho \
\n4 - Jardim Botânico \
\n5 - Parque Sólon de Lucena")
    inicio = input("Digite onde iniciará o passeio: ")
    inicio = verificacao(inicio)
    print(f"Você escolheu: {inicio}")
    if not inicio:
        print("Resposta inválida. Tente novamente")
        continue

    fim = input("Digite  onde será o último ponto: ")
    fim = verificacao(fim)
    if not fim: 
        print("Resposta inválida. Tente novamente")
        continue
    origem = dijkstra(pontos, inicio, fim)
    print(f"Sua rota que começa em {inicio} e termina em {fim} segue por: ")

    for n, local in enumerate(origem):
        print(f'{n} => {local}')
    break