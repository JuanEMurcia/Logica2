#Clase para representar arboles binarios sin ningun dato
class Tree(object):
	#constructor de la clase
	def __init__(self, left, right):
		self.left = left
		self.right = right

#Funcion recursiva que cuenta el numero de nodos en un arbol binario
def num_nodos(tree):
	if tree == None:
		return 0
	else:
		return 1+num_nodos(tree.left)+num_nodos(tree.right)

#Ejemplo con un arbol
leaf = Tree(None, None)
r1 = Tree(leaf, leaf)
r2 = Tree(r1, r1)
r3 = Tree(r1, r2)

print num_nodos(r3)