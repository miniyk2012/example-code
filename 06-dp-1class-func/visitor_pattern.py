class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand  # 操作数


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format(type(node).__name__))

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            method = self.generic_visit
        return method(node)


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -self.visit(node.operand)


if __name__ == '__main__':
    # Representation of -(-1 + 2 * (3 - 4) / 5)
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Negate(Number(1))
    t5 = Add(t4, t3)
    t6 = Negate(t5)

    evl = Evaluator()
    ret = evl.visit(t6)
    print(ret)
