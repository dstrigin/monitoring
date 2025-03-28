import multiprocessing
import time

def cpu_load():
    while True:
        # Генерация нагрузки на CPU
        [x * x for x in range(10000)]

if __name__ == '__main__':
    # Создаем количество процессов равное количеству ядер CPU
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_load)
        p.start()
        processes.append(p)
    
    print("Нагрузочное тестирование запущено")
    time.sleep(90)  # Запускаем на 1.5 минуты
    
    # Останавливаем процессы
    for p in processes:
        p.terminate() 
