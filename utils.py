from termcolor import colored


def print_diff(file1_path, file2_path, differences):
    """
    :param
        file1_path - путь до файла 1
        file2_path - путь до файла 2
        differences - разнциа в файлах
    Печатает различия между файлами в стиле diff.
    """
    for index, line1, line2 in differences:
        # Форматируем строку diff
        print(f"--- {file1_path} line {index + 1}")
        print(f"+++ {file2_path} line {index + 1}")
        print(colored(f"- {line1}", "red"))
        print(colored(f"+ {line2}", "green"))
        print()
