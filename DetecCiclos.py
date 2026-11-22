def criar_grafo():
    return {'vertices': [], 'matriz': []}

def inserir_vertice(grafo, v):
    if v not in grafo['vertices']:
        grafo['vertices'].append(v)
        for linha in grafo['matriz']:
            linha.append(0)
        grafo['matriz'].append([0] * len(grafo['vertices']))
        print(f"Vértice '{v}' inserido com sucesso.")
    else:
        print(f"O vértice '{v}' já existe.")

def inserir_aresta(grafo, origem, destino, nao_direcionado=True):
    if origem not in grafo['vertices'] or destino not in grafo['vertices']:
        print("\nErro: Os vértices devem existir antes de criar uma aresta. Insira-os primeiro!")
        return
    
    i1 = grafo['vertices'].index(origem)
    i2 = grafo['vertices'].index(destino)
    grafo['matriz'][i1][i2] = 1
    if nao_direcionado:
        grafo['matriz'][i2][i1] = 1
    print("Aresta inserida com sucesso.")

def exibir_grafo(grafo):
    if not grafo['vertices']:
        print("\nO grafo está vazio.")
        return
    print("\n Matriz de Adjacência ")
    print("   " + " ".join(grafo['vertices']))
    for i, v in enumerate(grafo['vertices']):
        print(f"{v}:  " + " ".join(str(x) for x in grafo['matriz'][i]))
    print("-")

def detectar_ciclo_dfs(grafo, inicio):
    if inicio not in grafo['vertices']:
        return False

    pilha = [{'vertice': inicio, 'pai': None}]
    visitados = []
    
    while pilha:
        item = pilha.pop()
        atual = item['vertice']
        pai = item['pai']
        
        if atual in visitados:
            continue
            
        visitados.append(atual)
        idx = grafo['vertices'].index(atual)
        
        for j, val in enumerate(grafo['matriz'][idx]):
            if val == 1:
                vizinho = grafo['vertices'][j]
                if vizinho not in visitados:
                    if not any(p['vertice'] == vizinho for p in pilha):
                        pilha.append({'vertice': vizinho, 'pai': atual})
                elif vizinho != pai:
                    return True
                    
    return False

def main():
    grafo = criar_grafo()
    while True:
        print("\n MENU")
        print("1. Inserir Vértice")
        print("2. Inserir Aresta")
        print("3. Exibir Matriz")
        print("4. Detectar Ciclo")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(grafo, v)
        elif opcao == '2':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input != 'n' else False
            inserir_aresta(grafo, origem, destino, nao_direcionado=nd)
        elif opcao == '3':
            exibir_grafo(grafo)
        elif opcao == '4':
            inicio = input("Digite o vértice inicial: ").strip()
            tem_ciclo = detectar_ciclo_dfs(grafo, inicio)
            if tem_ciclo:
                print("-> Ciclo DETECTADO no grafo!")
            else:
                print("-> Nenhum ciclo detectado a partir deste vértice.")
        elif opcao == '0':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()