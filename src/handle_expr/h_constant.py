import ast

from src.d_types import CppInclude, QInc


def handle_constant(node: ast.Constant, ret_imports: set[CppInclude]) -> str:
    if isinstance(node.value, str):
        ret_imports.add(QInc("py_str.h"))
        return f'PyStr("{node.value}")'
    if isinstance(node.value, bool):
        bool_str = str(node.value)
        first_letter = bool_str[0].lower()
        return first_letter + bool_str[1:]
    if isinstance(node.value, int) or isinstance(node.value, float):
        return str(node.value)
    raise Exception(f"constant type {node.value} not handled")
