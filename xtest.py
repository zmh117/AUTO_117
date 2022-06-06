


class s(object):
    sl="s的sl"
    def __init__(self):
        self.p="sss"

    def a(self):
        print("a")

    @classmethod
    def b(cls):
        print("b")
        print(cls,cls())
        cls().a()
        print(cls.sl)
        print(cls().p[1])
s.b()
ss=s()
ss.a()

ss.b()