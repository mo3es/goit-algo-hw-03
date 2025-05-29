import sys
import shutil
from pathlib import Path

def file_sort_by_type(source: Path, dest: Path):

    try:
        dest.mkdir(parents=True, exist_ok=True)
        print(f'Розпочато роботу в директорії {source}')
        for item in source.iterdir():
            try:
                if item.is_dir():
                    print(f'Вхід в піддиректорію {item}')
                    file_sort_by_type(item, dest)
                elif item.is_file():
                    print(f'Копіювання файлу {item}')
                    file_copy(item, dest)
                else:
                    print(f"Об'єкт {item} знайдено у файловій системі, але, не ідентифіковано як файл чи директорію. Об'єкт пропущено без обробки.")
            except PermissionError as e:
                print(f"Помилка доступу до об'єкту {item}: {e}; об'єкт {item} пропущено.")
            except OSError as e:
                print(f"Помилка файлової системи при обробці {item}: {e}.")
    except PermissionError as e:
        print(f"Помилка доступу до вихідної директорії/директорії призначення: {e}")
    except OSError as e:
        print(f"Помилка файлової системи при обробці директорії/директорії призначення: {e}.")

def file_copy(item, dest):
    extension = item.suffix.strip('.').lower()
    if len(extension) == 0 or extension is None:
        extension = 'without_extension'
    current_dest = dest / extension
    try:
        current_dest.mkdir(parents=True, exist_ok=True)
        file_path = current_dest / item.name
        shutil.copy2(item, file_path)
        print(f"Файл {item} скопійовано до {file_path}")
    except shutil.SameFileError:
        print(f"Файл {item} вже існує у {file_path}")
    except FileNotFoundError:
        print(f"Файл {item} був знайдений в процесі обробки але не був знайдений під час копіювання")
    except PermissionError as e:
        print(f"Відсутній дозвіл на копіювання: {e}")
    except OSError as e:
        print(f"Помилка файлової системи при копіюванні: {e}.")


if __name__ == '__main__':
    _dest_path_string = None
    if len(sys.argv) > 1:
        _source_path_string = sys.argv[1]
        if len(sys.argv) > 2:
            _dest_path_string = sys.argv[2]
        file_sort_by_type(_source_path_string, _dest_path_string)
    else:
        exit_item = 0
        while not exit_item:
            _source_path_string = input('Введіть шлях до вихідної директорії:   ')
            if Path(_source_path_string).exists() and Path(_source_path_string).is_dir():
                exit_item = 1
                _dest_path_string = input('Введіть директорію призначення (Директорія /dest в поточній директорії - за замовчуванням):   ')
                if len(_dest_path_string) == 0 or _dest_path_string.isspace():
                    _dest_path_string = 'dest'
        file_sort_by_type(Path(_source_path_string), Path(_dest_path_string))
