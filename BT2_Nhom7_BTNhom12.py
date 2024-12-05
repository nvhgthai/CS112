from itertools import permutations, product

def evaluate_expression(values, operators):
    a, b, c, d = values
    op1, op2, op3 = operators
    results = []
    try:
        results.append(eval(f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"))
        results.append(eval(f"({a} {op1} ({b} {op2} {c})) {op3} {d}"))
        results.append(eval(f"{a} {op1} (({b} {op2} {c}) {op3} {d})"))
        results.append(eval(f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"))
        results.append(eval(f"(({a} {op1} {b}) {op2} ({c} {op3} {d}))"))
    except ZeroDivisionError:
        pass  # Ignore invalid divisions
    return [res for res in results if res == int(res)]  # Only integer results

def solve_24(cards):
    max_value = float('-inf')
    for perm in permutations(cards):
        for ops in product("+-*/", repeat=3):
            for result in evaluate_expression(perm, ops):
                if result <= 24:
                    max_value = max(max_value, result)
    return int(max_value) if max_value != float('-inf') else 0

# Đọc đầu vào
n = int(input())
results = []
for _ in range(n):
    cards = [int(input()) for _ in range(4)]
    results.append(solve_24(cards))

# Xuất kết quả
for res in results:
    print(res)
