import re

class LogComparator:
    """
        попарно сравнивает файла и возвращает различия игнорирую время созданяи и путь до файла
    """
    def __init__(self, file1_lines, file2_lines):
        self.file1_lines = file1_lines
        self.file2_lines = file2_lines

    @staticmethod
    def normalize_line(line):
        """
        Нормализует строку, чтобы игнорировать время и пути.
        """
        # Удаляем пути и время из строки
        line = re.sub(r'(/\S+)|(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})', '', line)
        return line.strip()

    def compare(self):
        """
        Сравнивает два файла и возвращает различия.
        """
        normalized_file1 = [self.normalize_line(line) for line in self.file1_lines]
        normalized_file2 = [self.normalize_line(line) for line in self.file2_lines]

        differences = []
        max_lines = max(len(normalized_file1), len(normalized_file2))

        for i in range(max_lines):
            line1 = normalized_file1[i] if i < len(normalized_file1) else ""
            line2 = normalized_file2[i] if i < len(normalized_file2) else ""

            if line1 != line2:
                differences.append((i, line1, line2))

        return differences