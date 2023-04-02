import json

data = {}

class User:
    def __init__(self, user_name, password=None, full_name=None, phone_number=None):
        self.user_name = user_name
        self.password = ""
        self.full_name = ""
        self.phone_number = ""

        if password is not None:
            self.password = password
        if full_name is not None:
            self.password = full_name
        if phone_number is not None:
            self.password = phone_number

    def __del__(self):
        print("önce kayıt işlemleri yapabilirsin.")
        print("Nesne Yok Oldu")

    def verify(self, password):
        if self.password == password:
            return True
        return False

    def save(self):
        data[self.user_name] = {"password": self.password,
                                "full_name": self.full_name,
                                "phone_number": self.phone_number}
        with open("data.json", "w", ) as file_object:
            file_object.write(json.dumps(data, indent=2))


def main():
    user = User("Gokhan")
    user.save()
    print(data)
    print(user.user_name, "şifre dogrulama sonucu", user.verify("1234"))


main()
