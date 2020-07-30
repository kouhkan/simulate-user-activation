import json
from tasks import set_active_code, check_code
from time import sleep


class User:
    def __init__(self, phone, full_name):
        self.user = {
            'phone': phone,
            'full_name': full_name,
            'is_active': False,
        }

    def __repr__(self):
        return json.dumps(self.__dict__)

    def set_active_user(self):
        result = set_active_code(self.user['phone'])

        if result:
            return True
        else:
            return False

    def check_active_code(self, code):
        result = check_code(self.user['phone'], code)
        if result:
            return True
        else:
            return False


user1 = User('09120001122', 'Amir Kouhkan')

if user1.set_active_user():
    print("Active code was sent for {}".format(user1.user['full_name']))
    while True:
        code = input("Enter code: ")
        if user1.check_active_code(code):
            user1.user['is_active'] = True
            print('-'*50)
            print("User is active:{}".format(user1.user))
            sleep(3)
            print("byeee")
            break
        else:
            print("Wrong code")
else:
    print("Something went wrong ...")

