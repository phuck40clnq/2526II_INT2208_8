from app.models import TriangleInput


class ValidationError(Exception):
    pass


def validate_triangle(inp: TriangleInput) -> None:
    for name, value in [("a", inp.a), ("b", inp.b), ("c", inp.c)]:
        if not isinstance(value, int):
            raise ValidationError(f"Side {name} must be an integer")
        if not (1 <= value <= 100):
            raise ValidationError(f"Side {name} must be in range [1, 100]")
