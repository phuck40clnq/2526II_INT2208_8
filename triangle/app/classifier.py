def classify_triangle(a: int, b: int, c: int) -> str:
    if a + b <= c or a + c <= b or b + c <= a:
        return "NOT_TRIANGLE"

    if a == b == c:
        return "EQUILATERAL"

    if a == b or b == c or a == c:
        return "ISOSCELES"

    return "SCALENE"
