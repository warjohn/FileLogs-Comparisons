import sys

from file_reader import FileReader
from log_comparator import LogComparator
from utils import print_diff
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

TIMESTAMP = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 myscript.py <file1> <file2> ...")
        sys.exit(1)

    files = sys.argv[1:]
    print(f"Запуск сравнения логов в {TIMESTAMP}")

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(FileReader.read_file, files))

    # Сравниваем все файлы попарно
    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            comparator = LogComparator(results[i], results[j])
            differences = comparator.compare()

            if differences:
                print_diff(files[i], files[j], differences)
            else:
                print("Файлы отличаются только временем и местом сборки")

if __name__ == "__main__":
    main()
