from app.models import TriangleInput
from app.validator import validate_triangle
from app.classifier import classify_triangle


def process_triangle(inp: TriangleInput) -> str:
    validate_triangle(inp)
    return classify_triangle(inp.a, inp.b, inp.c)
