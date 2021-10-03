class Human:

    def __init__(self):
        self.__nationalID = input('please enter your national id: ').strip()
        self.firstName = input('what is your first name: ').strip().capitalize()
        self.lastName = input('what is your last name: ').strip().capitalize()
        self.phoneNumber = input('your phone number: ').strip()
        self.haveCar = input('do you have a car (y/n): ').lower()

        if self.haveCar == 'y':
            self.haveCar = True
        elif self.haveCar == 'n':
            self.haveCar = False
        else:
            self.haveCar = None
        print(f'created user successfully,welcome {self.firstName} {self.lastName}')

    def get_nationalid(self):
        return self.__nationalID

    def set_nationalid(self, newNationalID):
        self.__nationalID = newNationalID
        print('your id has been changed successfully')

    def output(self):
        print(f'first name : {self.firstName}\n'
              f'last name : {self.lastName}'
              f'national id : {self.__nationalID}'
              f'phone number : {self.phoneNumber}'
              f'have a car: {self.haveCar}')

    def analize_phone_number(self):
        phoneNumber = self.phoneNumber
    def analize_national_id(self):
        pass


class Car:

    def __init__(self):
        self.model = 'car model'
        self.yearOfManifacture = 2222
        self.engine = Engine()

    def create_driver(self):
        print(self.engine.)


class Engine:

    def __init__(self):
        self.name = 'engine'
        self.numberOfCelenders = 0
        self.power = 0
        self.powerByHorse = self.power * 3.3

    def check_all(self):
        if self.power == 0 and self.powerByHorse == self.power * 3.3 and self.numberOfCelenders == 0:
            print(f"user {self.name}")
