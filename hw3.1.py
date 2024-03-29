import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    try:
        date, time, level, *message = line.split(' ')  # Розділення рядка на компоненти: дату, час, рівень, повідомлення
        return {'date': date, 'time': time, 'level': level, 'message': " ".join(message)}  # Повернення словника з рядком журналу
    except ValueError:
        print(f"Недійсний формат рядка журналу: {line}")  # Виведення повідомлення про недійсний формат рядка
        return None

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r") as logfile:
            lines = list(map(parse_log_line, logfile.readlines()))  # Завантаження і розбір кожного рядка журналу
        return [log for log in lines if log is not None]  # Повернення списку рядків журналу без недійсних
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")  # Виведення повідомлення про відсутність файлу
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x['level'] == level, logs))  # Фільтрація рядків журналу за вказаним рівнем

def count_logs_by_level(logs: list) -> dict:
    count_dict = defaultdict(int)
    for log in logs:
        count_dict[log['level']] += 1  # Підрахунок кількості рядків журналу для кожного рівня
    return dict(count_dict)

def display_log_count(counts: dict):
    print(f"{'Рівень логування':20}| Кількість ")  # Виведення заголовків
    print(f"{'-'*20}|{'-'*10}")  # Роздільник
    print("\n".join(list(map(lambda x: f"{x:20}| {counts[x]}", counts))))  # Виведення кількості рядків для кожного рівня

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Введіть ім'я файлу журналу.")
        sys.exit(1)  # Вихід з програми при відсутності імені файлу

    filename = sys.argv[1]
    logs = load_logs(file_path=filename)

    if not logs:
        print("Не вдалося завантажити журнали. Перевірте правильність шляху до файлу.")
        sys.exit(1)  # Вихід з програми, якщо не вдалося завантажити журнали

    display_log_count(count_logs_by_level(logs))

    if len(sys.argv) == 3:
        level = sys.argv[2]
        logs_filtered = filter_logs_by_level(logs, level)

        print()
        print(f"Деталі логів для рівня {level}: ")
        print(''.join(map(lambda x: f"{x['date']} - {x['time']} - {x['message']}", logs_filtered)))  # Виведення деталей для вказаного рівня

