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


pet = Tamagotchi('Толик')
time.sleep(3)
pet.check_satiety_and_helth()
time.sleep(8)
pet.check_satiety_and_helth()
pet.feed()
time.sleep(14)
pet.check_satiety_and_helth()
time.sleep(6)
pet.check_satiety_and_helth()
pet.feed()
