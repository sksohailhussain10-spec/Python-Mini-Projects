import string
import secrets


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True

    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False


def generate_password(length: int, symbols: bool,uppercase=bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
    print("____Password Generator____")

    ab=int(input("Enter the Length of your password  : "))
    df=int(input("How many passwords do you want to generate  : "))

    for i in range(1,df+1):

      new_pass: str = generate_password(length=ab, symbols=True, uppercase=True)
      specs: str = f'Uppercase:{contains_upper(new_pass)},Symbols:{contains_symbols(new_pass)}'
      print(f'{i}. Result -> {new_pass}  ')



