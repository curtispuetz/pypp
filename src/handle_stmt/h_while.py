import ast

from src.util.handle_lists import handle_stmts
from src.util.ret_imports import RetImports


def handle_while(
    node: ast.While,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    assert len(node.orelse) == 0, "While loop else not supported"
    body_str = handle_stmts(node.body, ret_imports, ret_h_file, handle_stmt)
    test_str = handle_expr(node.test, ret_imports)
    return f"while ({test_str})" + "{" + body_str + "}"
