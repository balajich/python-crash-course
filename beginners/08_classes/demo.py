class A:
    pass


class B:
    pass


class C(A, B):
    def hello(self):
        print('Class C')


if __name__ == "__main__":
    r = Rect()
    print(r.get_name())
