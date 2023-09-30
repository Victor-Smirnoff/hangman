import random


class Hangman:
    """Класс для описания игры 'Виселица'"""
    word_list = ("СОЛНЦЕ", "РУЧКА", "МАШИНА", "КОМПЬЮТЕР", "СТОЛ", "ДОМ", "ЦВЕТОК", "КНИГА", "СОБАКА", "ГОРОД")
    acceptable_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def init(self):
        """инициализация основных параметров игры"""
        self.tries = 0                                  # количество попыток
        self.word = self.get_word()                     # случайно выбранное слово
        self.word_completion = "_" * len(self.word)     # строка, содержащая символы _ на каждую букву задуманного слова
        self.guessed = False                            # сигнальная метка, угадано слово - True или нет - False
        self.guessed_letters = []                       # список уже названных букв
        self.guessed_words = []                         # список уже названных слов

    def find_target_char(self, letter):
        self.tries += 1
        self.guessed_letters.append(letter)
        res = list(self.word_completion)
        if letter in self.word:
            for indx, value in enumerate(self.word):
                if letter == value:
                    res[indx] = letter
        self.word_completion = "".join(res)
        if self.word_completion == self.word:
            self.guessed = True

    def show_display(self):
        print(self.display_hangman(self.tries))
        print("Слово: " + self.word_completion)
        print(f"Попытки ({len(self.guessed_letters) + len(self.guessed_words)}) из (6): " + ", ".join(self.guessed_letters + self.guessed_words))

    def play(self):
        while not self.guessed and self.tries < 6:
            self.show_display()

            letter_or_word = input(f"Введите букву [а-я] или слово из {len(self.word)} букв целиком: ").upper()

            if len(letter_or_word) == 1 and letter_or_word not in self.acceptable_letters:
                print(f"Вы ввели символ <{letter_or_word}> не букву, попробуйте ввести ещё раз")
                continue
            elif len(letter_or_word) > 1 and len(letter_or_word) != len(self.word):
                print(f"Вы ввели слово <{letter_or_word}>, длина которого не равна {len(self.word)}, попробуйте ввести ещё раз")
                continue
            elif len(letter_or_word) == len(self.word) and letter_or_word not in self.guessed_words:
                if not all([char in self.acceptable_letters for char in letter_or_word]):
                    print(f"Вы ввели слово <{letter_or_word}>, содержащее символ <{''.join([x for x in letter_or_word if x not in self.acceptable_letters])}> не буквы, попробуйте ввести ещё раз")
                    continue
                else:
                    if letter_or_word == self.word:
                        self.guessed_words.append(letter_or_word)
                        self.word_completion = letter_or_word
                        self.guessed = True
                    else:
                        self.tries += 1
                        self.guessed_words.append(letter_or_word)
            elif len(letter_or_word) == len(self.word) and letter_or_word in self.guessed_words:
                print(f"Вы ввели слово <{letter_or_word}>, которое уже вводили ранее, попробуйте ввести ещё раз")
                continue
            elif len(letter_or_word) == 1 and letter_or_word in self.acceptable_letters and letter_or_word in self.guessed_letters:
                print(f"Вы ввели букву <{letter_or_word}>, которую уже вводили ранее, попробуйте ввести ещё раз")
                continue
            elif len(letter_or_word) == 1 and letter_or_word in self.acceptable_letters and letter_or_word not in self.guessed_letters:
                self.find_target_char(letter_or_word)

        if self.guessed:
            self.show_display()
            print(f"Поздравляем, вы угадали слово <{self.word}>! Вы победили!")
        else:
            self.show_display()
            print(f"Вы исчерпали попытки угадать слово <{self.word}>! В следующий раз обязательно получится!")

    def get_word(self):
        return random.choice(self.word_list)

    def display_hangman(self, tries):
        stages = {6: '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''',
                  5: '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            ''',
                  4: '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            ''',
                  3: '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            ''',
                  2: '''
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            ''',
                  1: '''
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            ''',
                  0: '''
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            '''
                  }

        return stages[tries]


game = Hangman()
print("Давайте начнём новую игру!")
answer = input("Нажмите любую букву для начала игры или пробел для выхода из игры: ")

while True:
    if answer != " ":
        game.init()
        game.play()
        print("Желаете поиграть в игру ещё раз?")
        answer = input("Нажмите любую букву для начала игры или пробел для выхода из игры: ")
    else:
        break

print()
print("Спасибо за игру! До новых встреч!")