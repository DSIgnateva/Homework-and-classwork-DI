import time


class Tamagotchi:  # допилила Тамагочи
    kill_flag = False
    KILL = 10

    def __init__(self, name):
        self.name = name
        self.satiety = 100
        self.health = 100
        self.time = time.time()

    def feed(self):
        if not Tamagotchi.kill_flag:
            self.satiety = 100
            print(f"{self.name} сыт")
        else:
            print(f'{self.name} труп, зачем ему твоя еда?')

    def check_satiety_and_helth(self):
        hunger = (int(time.time()) - int(self.time)) * Tamagotchi.KILL
        self.time = time.time()
        if not Tamagotchi.kill_flag:
            self.satiety -= hunger
            if self.satiety < 0:
                self.health += self.satiety
                self.satiety = 0
                if self.health <= 0:
                    Tamagotchi.kill_flag = True
                    print(f'Ну молодец, {self.name} погиб смертью храбрых перед страшным лицом голода')
                else:
                    print(f'Ох, {self.name} умирает от голода, его здоровье: {self.health}/100')
            else:
                print(f'Похоже {self.name} голоден, его сытость: {self.satiety}/100')


# pet = Tamagotchi('Толик')
# time.sleep(3)
# pet.check_satiety_and_helth()
# time.sleep(8)
# pet.check_satiety_and_helth()
# pet.feed()
# time.sleep(14)
# pet.check_satiety_and_helth()
# time.sleep(6)
# pet.check_satiety_and_helth()
# pet.feed()


class Card:  # задача про карты
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Arm:
    fingers = 0
    cipher_rank = {'двойка': 2, 'тройка': 3, 'четвёрка': 4, 'пятёрка': 5, 'шестёрка': 6, 'семёрка': 7,
                   'восьмёрка': 8, 'девятка': 9, 'десятка': 10, 'валет': 11, 'дама': 12, 'король': 13, 'туз': 14}
    one_suit = True

    def __init__(self):
        self.cards = []

    def take_a_card(self, suit, rank):
        if Arm.fingers < 6:
            cards = Card(suit, rank)
            self.cards.append(cards)
            Arm.fingers += 1
            print(f'Тебе пришла карта: {cards.rank}, {cards.suit}')
        else:
            print('В руку больше не помещаются карты :с')

    def subsequence(self, sps):  # побочная функция для выявления, есть последовательность карт или нет
        sps = sorted(sps)
        for i in range(1, len(sps)):
            if sps[i] - sps[i - 1] > 1:
                return False
        return True

    def check_combination(self):
        deck = []
        suit = self.cards[0].suit
        for card in self.cards:
            deck.append(Arm.cipher_rank[card.rank])
            if card.suit != suit:
                Arm.one_suit = False
        if [10, 11, 12, 13, 14] == sorted(deck) and Arm.one_suit:
            print('Флеш Рояль')
        elif self.subsequence(deck) and Arm.one_suit:
            print('Стрит Флеш!')
        elif 4 in [deck.count(i) for i in deck]:
            print('Вау, Каре!')
        elif 3 in [deck.count(i) for i in deck] and 2 in [deck.count(i) for i in deck]:
            print('Это Фулл-хауз')
        elif Arm.one_suit:
            print('Уау, Флеш!')
        elif self.subsequence(deck):
            print('Стрит тоже неплох')
        elif 3 in [deck.count(i) for i in deck]:
            print('Ну, это Тройка')
        elif len([a for a in [deck.count(a) for a in deck] if a == 2]) == 4:
            print('Что ж, Две Пары тоже неплохо')
        elif len([a for a in [deck.count(a) for a in deck] if a == 2]) == 2:
            print('Пара!')
        else:
            print('Эх, всего лишь Старшая Карта')

# arm = Arm()
# arm.take_a_card('черви', 'восьмёрка')
# arm.take_a_card('черви', 'семёрка')
# arm.take_a_card('черви', 'шестёрка')
# arm.take_a_card('черви', 'девятка')
# arm.take_a_card('черви', 'десятка')
# arm.check_combination()
