import version

# fare gitignore e togliere pycache


def add(a: int, b: int) -> int:
    return a+b



def main() -> None:

    print("Script prova per CI / CD con github")
    print(f"Current version is: {version.__version__}")


    print("Added in the devel branch")
    print("1")

    add(2, 5)

    return



if __name__ == "__main__":
    main()