import os
import shutil

def main():
    volume=32*1024*1024

    print("Создаётся папка для нагрузочных файлов.")

    try:
        os.makedirs('payload',exist_ok=True)

    except Exception as e:
        print("Не удалось создать папку для нагрузочных файлов. Скрипт будет остановлен")
        print(f"Ошибка: {Exception}")
        exit(1)

    while True:
        print(f"Начато заполнение файлами по {volume} байт.")
        volume_filler(volume)
        if volume == 1:
            break
        volume //= 2

    try:
        shutil.rmtree('payload')

    except:
        pass

    print('Готово.')


def volume_filler(file_size: int):
    number = 1
    for attempt in range(5):
        try:
            while True:
                with open(f"payload/dumb_file{file_size}_{number}.bin", "wb") as file:
                    file.write(b'\xFF'*file_size)
                    file.close()
                number += 1
        except:
            pass

confirm = False
assert confirm

if __name__ == '__main__':
    main()