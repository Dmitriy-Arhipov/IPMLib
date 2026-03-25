import datetime

log_file = "log.txt"

with open(log_file, 'a') as file:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"Программа запущена: {current_time}\n")

print("Запуск программы зафиксирован в журнале.")
