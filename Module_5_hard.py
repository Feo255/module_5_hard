

import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:

    def __init__(self):
        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user = None

    def add(self, *args):
        self.videos = list(args)

    def register(self, nickname, password, age):

        user_reg = User(nickname, password, age)
        if user_reg.nickname not in [user.nickname for user in self.users]:
            self.users.append(user_reg)
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):

        for user in self.users:
            if user.password == hash(password) and user.nickname == nickname:
                self.current_user = user

    def logout(self):
        self.current_user = None

    def add(self, *videos):
        list_title = []
        for video in self.videos:
            list_title.append(video.title)
        for video in videos:
            if video.title not in list_title:
                self.videos.append(video)

    def get_videos(self, key_word):
        list_videos = []
        for video in self.videos:
            if key_word.lower() in video.title.lower():
                list_videos.append(video.title)

        return list_videos

    def watch_video(self, title):
        for video in self.videos:
            if title == video.title:
                if self.current_user is not None:
                    if video.adult_mode is True and self.current_user.age >= 18:
                        for i in range(1, video.duration + 1):
                            print(i, end=' ')
                            video.time_now += 1
                            time.sleep(1)
                        print("Конец видео")
                    elif video.adult_mode is False:
                        for i in range(1, video.duration + 1):
                            print(i, end=' ')
                            video.time_now += 1
                            time.sleep(1)
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
