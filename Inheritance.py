class Mobile:
    def call(self):
        print("You Can Call")

    def msg(self):
        print("You Can Msg")

    def photo(self):
        print("You Can take photo")


class Samsung(Mobile):
    def game(self):
        print("You can play games")


s = Samsung()
s.call()
s.msg()
s.photo()
s.game()