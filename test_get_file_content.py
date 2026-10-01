from functions.get_file_content import get_file_content

def run_tests():
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    result = get_file_content("calculator", "main.py")
    print("main.py result:")
    print(f"{result}")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("calculator.py result:")
    print(f"{result}")

    result = get_file_content("calculator", "/bin/cat")
    print(f"/bin/cat result:")
    print(f"{result}")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"does_not_exist.py result:")
    print(f"{result}")

if __name__ == "__main__":
    run_tests()
