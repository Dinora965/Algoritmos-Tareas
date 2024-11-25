class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def combine(self, operator, left_tree, right_tree):
        self.value = operator
        self.left = left_tree
        self.right = right_tree

    def preOrder(self):
        """Recorrido preorden"""
        result = [self.value]
        if self.left:
            result += self.left.preOrder()
        if self.right:
            result += self.right.preOrder()
        return result

    def inOrder(self):
        """Recorrido inorden con paréntesis para claridad"""
        result = []
        if self.left:
            result.append("(")
            result += self.left.inOrder()
        result.append(self.value)
        if self.right:
            result += self.right.inOrder()
            result.append(")")
        return result

    def postOrder(self):
        """Recorrido postorden"""
        result = []
        if self.left:
            result += self.left.postOrder()
        if self.right:
            result += self.right.postOrder()
        result.append(self.value)
        return result


def buildExpressionTree(expression):
    """Construye un árbol binario a partir de una expresión en notación posfija"""
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isalnum():  # Operandos
            stack.append(BinaryTree(token))
        elif token in "+-*/":
            if len(stack) < 2:
                raise ValueError("Expresión inválida: insuficientes operandos para el operador.")
            right_tree = stack.pop()
            left_tree = stack.pop()
            new_tree = BinaryTree()
            new_tree.combine(token, left_tree, right_tree)
            stack.append(new_tree)
        else:
            raise ValueError(f"Expresión inválida: token no reconocido '{token}'.")

    if len(stack) != 1:
        raise ValueError("Expresión inválida: más operandos u operadores de los necesarios.")
    
    return stack[0]


def evaluateExpression(expression):
    try:
        tree = buildExpressionTree(expression)
        print(f"\nExpresión: {expression}")
        print("Preorden :", " ".join(tree.preOrder()))
        print("Inorden  :", " ".join(tree.inOrder()))
        print("Postorden:", " ".join(tree.postOrder()))
    except ValueError as e:
        print(f"\nExpresión: {expression}")
        print("Error:", e)


# Pruebas
expressions = [
    "91 95 + 15 + 19 + 4 *",
    "B B * A C 4 * * - ",
    "42",
    "A 57",
    "+ /"
]

for expr in expressions:
    evaluateExpression(expr)