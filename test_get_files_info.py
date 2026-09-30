# Import the function from the calculator directory/module
from functions.get_files_info import get_files_info

def run_tests():
    print('get_files_info("calculator", "."):')
    print("\nResult for current directory:")
    print(get_files_info("calculator", "."))
    print("\n" + "="*40 + "\n")

    print('get_files_info("calculator", "pkg"):')
    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print("\n" + "="*40 + "\n")

    print('get_files_info("calculator", "/bin"):')
    print("\nResult for '/bin' directory:")
    print(f"    {get_files_info('calculator', '/bin')}")
    print("\n" + "="*40 + "\n")

    print('get_files_info("calculator", "../"):')
    print("\nResult for '../' directory:")
    print(f"    {get_files_info('calculator', '../')}")

if __name__ == "__main__":
    run_tests()
