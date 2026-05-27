from app.models import TriangleInput
from app.service import process_triangle
from app.validator import ValidationError


def main():

    application = TriangleInput(a=3, b=4, c=5)

    try:
        result = process_triangle(application)

        print("=== Triangle Classification Result ===")
        print(f"Input:          {application}")
        print(f"Classification: {result}")

    except ValidationError as error:
        print("=== Validation Error ===")
        print(error)


if __name__ == "__main__":
    main()