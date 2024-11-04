print("Prev coder")
try:
    input()
    print(10 / 0)
    print(value)
except KeyboardInterrupt:
    print("Помилка роботи з клавиатурою")
except ZeroDivisionError:
    print("Не можне дiлити на нуль")
except (NameError, KeyError) as error:
    print(error)


print("Next code")