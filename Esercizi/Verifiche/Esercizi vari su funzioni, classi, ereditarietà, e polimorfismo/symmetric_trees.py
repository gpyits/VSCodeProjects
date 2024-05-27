# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.
# La lista di interi è formata così:
#     L'elemento in posizione 0 corrisponde alla radice
#     Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#     Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#     Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.
#Potete utilizzare la classe TreeNode per crearvi prima l'albero - anziché usare la lista tree - e poi visitare l'albero sfruttando gli oggetti di tipo TreeNode.
def symmetric(tree: list[int]) -> bool:
    nodes=[tree[0]]
    for i in range(len(tree)):
        try:
            nodes.append(tree[2*i + 1])
            nodes.append(tree[2*(i+1)])
        except IndexError: break
    result=[]
    i=1
    while nodes!=[]:
        result.append(nodes[:i])
        nodes=nodes[i:]
        i*=2
    return True if result==[i[::-1] for i in result] else False

print(symmetric([1,2,2,3,4,4,3])) #True
print(symmetric([1,2,2,None,3,None,3])) #False