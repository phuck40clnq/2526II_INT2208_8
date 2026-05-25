from app.models import TriangleInput
from app.service import process_triangle
from app.validator import ValidationError


def main():
    inp = TriangleInput(a=3, b=4, c=5)

    try:
        result = process_triangle(inp)
        print("=== Triangle Classification ===")
        print(f"Input: {inp}")
        print(f"Result: {result}")
    except ValidationError as error:
        print("=== Validation Error ===")
        print(error)


if __name__ == "__main__":
    main()
