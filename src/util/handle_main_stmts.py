import ast

from src.d_types import CppInclude
from src.handle_stmt.stmt import handle_stmt
from src.util.handle_lists import handle_stmts


def handle_main_stmts(stmts: list[ast.stmt], ret_imports: set[CppInclude]) -> str:
    main_stmt = stmts[-1]
    if not _is_proper_main(main_stmt):
        raise Exception(
            "Correctly defined main guard as the last stmt in main.py is required"
        )
    before_main = handle_stmts(stmts[:-1], ret_imports, [], handle_stmt)
    assert isinstance(main_stmt, ast.If), "shouldn't happen"
    inside_main = handle_stmts(
        main_stmt.body + [ast.Return(ast.Constant(0))], ret_imports, [], handle_stmt
    )
    return f"{before_main} int main() {{{inside_main}}}"


def _is_proper_main(node: ast.stmt) -> bool:
    if not isinstance(node, ast.If):
        return False
    if len(node.orelse) != 0:
        return False
    if not isinstance(node.test, ast.Compare):
        return False
    if not isinstance(node.test.left, ast.Name):
        return False
    if node.test.left.id != "__name__":
        return False
    if len(node.test.ops) != 1:
        return False
    if not isinstance(node.test.ops[0], ast.Eq):
        return False
    if len(node.test.comparators) != 1:
        return False
    comp = node.test.comparators[0]
    if not isinstance(comp, ast.Constant):
        return False
    if comp.value != "__main__":
        return False
    return True
