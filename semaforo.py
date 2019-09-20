class Tree(object):
	def __init__(self, r, iz, der):
		self.left = iz
		self.right = der
		self.label = r

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

    if f.right == None:
        return f.label
    elif f.label == '~':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"


def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['~', 'v', '&', '>']
    pila = []
    for c in A:
        if c not in conectivos and c in letrasProposicionales:
            pila.append(Tree(c,None,None))
        else :
            if c == '~':
                formulaAux = Tree(c, None, pila[-1])
                del pila[-1]
                pila.append(formulaAux)
            elif c in conectivos and c != '~':
                formulaAux = Tree(c, pila[-1], pila[-2])
                del pila[-1]
                del pila[-1]
                pila.append(formulaAux)
    return pila[-1]

regla = ""
letras = ["R","A","V"]

count = True #es la primera regla que creo
for i in letras:
    regla_aux = i #EMpiezo a crear la subregla con la letra que es verdadera
    aux = [x+"~" for x in letras if x != i] #Creo la lista de las letras propocicionales que tienen que ser negadas
    for j in aux:
        regla_aux = regla_aux+j+"&" #uno las letras negadas con un Y
    if (count):
        regla = regla_aux #Si es la primera regla que creo, inicializo mi regla
    else:
        regla = regla+regla_aux+"v" #Si no es la primera regla que creo, la uno con un O
    count = False #Ya no es la primera regla que creo

print(Inorder(StringtoTree(regla,letras)))
