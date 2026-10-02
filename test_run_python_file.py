# Import the function from the calculator directory/module
from functions.run_python_file import run_python_file

def run_tests():
    # Test case 1
    result1 = run_python_file("calculator", "main.py")
    print(result1)  

    # Test case 2
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)  

    # Test case 3:
    result3 = run_python_file("calculator", "tests.py")
    print(result3)

    result4 = run_python_file("calculator", "../main.py")
    print(result4)  # Should return an error about being outside the permitted working directory

    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)  # Should return an error about the file not existing

    result6 = run_python_file("calculator", "lorem.txt")
    print(result6)  # Should return an error about the file not being a Python file

if __name__ == "__main__":
    run_tests()
