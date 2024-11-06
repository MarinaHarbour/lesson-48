import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        for line in name:
            if not line:
                break
        all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time.time()
for name in filenames:
    read_info(name)
end = time.time()
print(f"Время выполнения Линейного вызова {end - start}")


if __name__ == '__main__':
    start_2 = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_2 = time.time()
    print(f"Время выполнения Многопроцессного вызова {end_2 - start_2}")
