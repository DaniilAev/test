def main():
    volume=32
    print(f"Начато заполнение файлами по {volume} Мб.")
    while True:
        volume_filler(volume)
        if volume == 1:
            break
        volume //= 2

def volume_filler(file_size: int):
    number = 1
    for attempt in range(5):
        try:
            while True:
                with open(f"dumb_file{file_size}_{number}.bin", "wb") as file:
                    file.write(b'\xFF'*file_size)
                    file.close()
                number += 1
        except:
            pass


confirm = False
assert confirm

if __name__ == '__main__':
    main()