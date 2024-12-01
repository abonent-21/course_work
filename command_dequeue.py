from dequeue import Dequeue

class CommandHistory:
    def __init__(self, size=20):
        self.__size__ = size  # Максимальное количество команд
        self.__history__ = Dequeue()  # История команд с ограничением по размеру

    def add_command(self, command):
        if self.__history__.get_size() == self.__size__:
            self.__history__.pop_front()
        self.__history__.add_back(command)

    def set_size(self, new_size):
        if self.__history__.get_size() - new_size > 0:
            self.__size__ = new_size
            for _ in range(self.__history__.get_size() - new_size):
                self.__history__.pop_front()
        elif new_size > 0:
            self.__size__ = new_size
    def get_history(self):
        if self.__history__.is_empty():
                print("Deque is empty!")
                return []
        current = self.__history__.front.prev
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        return elements
    
    def get_size(self):
        return self.__size__
    

if __name__ == "__main__":
    command_history = CommandHistory()
    command_history.add_command('pwd')
    command_history.add_command('cd')
    command_history.add_command('vim main.c')
    command_history.set_size(3)
    command_history.set_size(2)
    print(command_history.get_history())
