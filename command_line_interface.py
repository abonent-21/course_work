import pygame
import sys
import random
from command_dequeue import CommandHistory

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Terminal")


ORANGE = (255, 165, 0)  # Оранжевый цвет для текста и курсора
DARK_ORANGE = (139, 69, 19)  # Темно-оранжевый для сканирующих линий

# Шрифт для текста
font = pygame.font.Font("clacon2.ttf", 26)

# Переменные
input_text = ""  # Текст, который вводит пользователь
history = []    # введенные команды
storage_of_command = CommandHistory(20)
cursor_visible = True  # Флаг для мигающего курсора
last_cursor_time = pygame.time.get_ticks()  # Время последнего мигания курсора
cursor_interval = 500  # Интервал мигания курсора (в миллисекундах)

sound_button = pygame.mixer.Sound("sound1.wav")
sound_button.set_volume(1.0)

# Загрузка и воспроизведение музыки
pygame.mixer.music.load("monitor_sound.wav") 
pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость (от 0.0 до 1.0)
pygame.mixer.music.play(loops=-1, start=0.0)  # Воспроизведение музыки в цикле

# Функция для отрисовки текста
def draw_text(text, y_offset=0):
    # Рендерим текст и отображаем его на экране
    text_surface = font.render(text, True, ORANGE)
    screen.blit(text_surface, (20, y_offset))

def draw_storage_of_command(storage: CommandHistory) -> None:
    commands = storage.get_history()
    y_offset = 20
    num = 1
    for line in commands: 
        history.append(f"{num}) {line}")
        num += 1
        y_offset += 40  # Интервал между строками


# Функция для обработки ввода
def process_input():
    global input_text, history
    if input_text.strip():  # Если введен текст
        history.append(f"$ {input_text}")  # Добавляем команду в историю с $ в начале
        print(input_text)
        input_text = input_text.strip()
        # Простейшая обработка команд
        if input_text.lower() == "hello":
            storage_of_command.add_command(input_text)
            history.append("Hello, user!")
        elif "history" == input_text.lower().split()[0]:
            print(storage_of_command.get_history())
            comm = input_text.split()[1:]
            if comm:
                flag = comm[0]
                if flag == '-s':
                    new_size = comm[-1]
                    try:
                        print(storage_of_command.get_history())
                        new_size = int(new_size)
                        assert new_size > 0
                        storage_of_command.set_size(new_size)
                        print(storage_of_command.get_history())
                    except:
                        history.append(f"Command '{input_text}' not found.")
                elif flag == '-p':
                    history.append(f"Size of command stack - {storage_of_command.get_size()}")
            else:
                draw_storage_of_command(storage_of_command)
        elif input_text.lower() == "pwd":
            storage_of_command.add_command(input_text)
            history.append("/home/home_pc_user/course_work")
        elif input_text.lower() == "cd":
            storage_of_command.add_command(input_text)
            history.append("/home/home_pc_user/course_work")
        elif input_text.lower() == "exit":
            pygame.quit()
            sys.exit()
        else:
            history.append(f"Command '{input_text}' not found.")
            storage_of_command.add_command(input_text)
    input_text = ""  # Очистить текущий ввод

# Главный цикл программы
running = True
while running:
    screen.fill(DARK_ORANGE)  # Заполняем экран черным цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            sound_button.play(loops=0, maxtime=0, fade_ms=200)
            # Если нажата клавиша "Enter"
            if event.key == pygame.K_RETURN:
                process_input()  # Обработать введенную команду
            # Если нажата клавиша "Backspace"
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]  # Удалить последний символ
            # Все остальные клавиши добавляют символ в строку ввода
            else:
                input_text += event.unicode

    # Обновление мигающего курсора
    current_time = pygame.time.get_ticks()
    if current_time - last_cursor_time >= cursor_interval:
        cursor_visible = not cursor_visible  # Переключаем видимость курсора
        last_cursor_time = current_time

    # Отображение  команд
    y_offset = 20
    for line in history[-10:]:  # Ограничим вывод последних 10 команд
        draw_text(line, y_offset)
        y_offset += 40  # Интервал между строками

    # Отображение текущего ввода с символом $
    draw_text(f"$ {input_text}", y_offset)

    # Отображение мигающего курсора как прямоугольник
    if cursor_visible:
        cursor_width = 10  # Ширина прямоугольника
        cursor_height = font.get_height()  # Высота прямоугольника (равна высоте строки)
        cursor_rect = pygame.Rect(20 + font.size(f"$ {input_text}")[0], y_offset, cursor_width, cursor_height)
        pygame.draw.rect(screen, ORANGE, cursor_rect)

    # Обновляем экран
    pygame.display.flip()

    # Задержка на 10 миллисекунд для обработки событий
    pygame.time.delay(10)

# Закрытие Pygame
pygame.quit()
sys.exit()
