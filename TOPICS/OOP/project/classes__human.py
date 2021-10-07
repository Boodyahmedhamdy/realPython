import datetime


class Human:

    ID = 0

    def __init__(self):

        self.ID = Human.ID

        self.firstName = input('what is your first name: ').strip().capitalize()
        self.middleName = input('what is your middle name: ').strip().capitalize()
        self.lastName = input('what is your last name: ').strip().capitalize()

        self.phoneNumber = input('your phone number: ').strip()
        self.haveCar = input('do you have a car (y/n): ').lower()

        self.haveCar = Human.analize_have_car(self.haveCar)

        self.__nationalID = input('please enter your national id: ').strip()
        self.nationalIdData = Human.analize_nationalID(self.__nationalID)

        # all from national id
        self.gender = self.nationalIdData['gender']
        self.governorate = self.nationalIdData['governorate']
        self.birthday = self.nationalIdData['birthday']
        self.dayOfBirth = self.nationalIdData['dayOfBirth']
        self.monthOfBirth = self.nationalIdData['monthOfBirth']
        self.yearOfBirth = self.nationalIdData['yearOfBirth']
        self.ageInYears = self.nationalIdData['ageInYears']
        self.address = None

        Human.ID += 1
        print(f'created user successfully,welcome {self.firstName} {self.middleName} {self.lastName}')

    # NAMEING CONTROL
    def get_full_name(self):
        return f'{self.firstName} {self.middleName} {self.lastName}'

    def get_nationalid(self):
        return self.__nationalID

    def set_nationalid(self, newNationalID):
        self.__nationalID = newNationalID
        print('your id has been changed successfully')

    # OUTPUT FUNCTION
    def output(self):
        print(f'----------------------------------\n'
              f'ID : {self.ID}\n'
              f'name : {self.firstName} {self.middleName} {self.lastName}\n'
              f'national ID : {self.__nationalID}\n'
              f'address : {self.address}\n'
              f'phone number : {self.phoneNumber}\n'
              f'car : {self.haveCar}\n'
              f'gender : {self.gender}\n'
              f'age : {self.ageInYears}\n'
              f'birthday : {self.birthday}\n'
              f'governorate : {self.governorate}\n'
              f'----------------------------------')

    # STATIC METHOD TO CONTROL THE CONSTRUCTOR AND ANALIZE DATA
    @staticmethod
    def analize_have_car(answer):
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            return None

    @staticmethod
    def analize_nationalID(nationalID):
        if len(nationalID) != 14:
            print('wrong national id')
            raise Exception("write national id correctly .."
                            " there is a messing number or added number")

        birthDay = nationalID[1:7]

        day = birthDay[-2:]
        try:
            if int(day) > 31:
                print('wrong national id')
                raise Exception('write your national id correctly')
        except ValueError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')

        month = birthDay[2:4]
        try:
            if int(month) > 12:
                print('wrong national id')
                raise Exception('write your national id correctly')
        except ValueError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')

        year = birthDay[0:2]
        try:
            if int(year) > 12:
                print('wrong national id')
                raise Exception('write your national id correctly')
        except ValueError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')

        try:
            if nationalID[0] == '3':
                year = int(year) + 2000
            elif nationalID[0] == '2':
                year = int(year) + 1900
            else:
                print('wrong national id')
                raise Exception('write your national id correctly .. starts with 2 or 3')
        except ValueError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')

        age = None
        try:
            birthDay = day + '-' + month + '-' + str(year)
            currentYear = datetime.datetime.now()
            age = currentYear.year - year
        except TypeError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')

        # print(f'birthday: {birthDay}, age: {age}')
        # print(birthDay, day, month, year, age)

        gender = nationalID[-2]
        try:
            if int(gender) % 2 == 0:
                gender = 'female'
            else:
                gender = 'male'
        except TypeError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')
        except ValueError:
            print('national id should contains only numbers')
            raise Exception('national id should contains only numbers')

        # print(gender)

        codeOfGovrenorate = nationalID[7:9]
        if codeOfGovrenorate == '01':
            governorate = 'cairo'

        elif codeOfGovrenorate == '02':
            governorate = 'alexanderia'

        elif codeOfGovrenorate == '03':
            governorate = 'port sead'

        elif codeOfGovrenorate == '04':
            governorate = 'elsouse'

        elif codeOfGovrenorate == '11':
            governorate = 'domyat'

        elif codeOfGovrenorate == '12':
            governorate = 'dacahleya'

        elif codeOfGovrenorate == '13':
            governorate = 'sharkeya'

        elif codeOfGovrenorate == '14':
            governorate = 'qaluopiya'

        elif codeOfGovrenorate == '15':
            governorate = 'kafr elshekh'

        elif codeOfGovrenorate == '16':
            governorate = 'gharpiya'

        elif codeOfGovrenorate == '17':
            governorate = 'monofiya'

        elif codeOfGovrenorate == '18':
            governorate = 'behera'

        elif codeOfGovrenorate == '19':
            governorate = 'esmailiya'

        elif codeOfGovrenorate == '21':
            governorate = 'giza'

        elif codeOfGovrenorate == '22':
            governorate = 'bany souf'

        elif codeOfGovrenorate == '23':
            governorate = 'fayoum'

        elif codeOfGovrenorate == '24':
            governorate = 'menya'

        elif codeOfGovrenorate == '025':
            governorate = 'assuot'

        elif codeOfGovrenorate == '26':
            governorate = 'sohag'

        elif codeOfGovrenorate == '27':
            governorate = 'kenna'

        elif codeOfGovrenorate == '28':
            governorate = 'aswan'

        elif codeOfGovrenorate == '31':
            governorate = 'oxour'

        elif codeOfGovrenorate == '32':
            governorate = 'bahr al ahmer'

        elif codeOfGovrenorate == '33':
            governorate = 'wadi el gedid'

        elif codeOfGovrenorate == '34':
            governorate = 'matrooh'

        elif codeOfGovrenorate == '34':
            governorate = 'shamal senay'

        elif codeOfGovrenorate == '35':
            governorate = 'ganoub senay'

        elif codeOfGovrenorate == '88':
            governorate = 'out side egypt'

        else:
            governorate = 'unknown city'

        # print(f'govenorate : {governorate.capitalize()}')

        governorate = governorate.capitalize()

        allData = {
            "birthday": birthDay,
            'yearOfBirth': str(year),
            'monthOfBirth': month,
            'dayOfBirth': day,
            "ageInYears": age,
            'gender': gender,
            'governorate': governorate
        }
        return allData


# user = Human()
# user.output()
