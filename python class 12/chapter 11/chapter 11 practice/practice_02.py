class Animals:
    location='anywhere'
    owner=False


class Pets(Animals):
    location='Home'
    owner=True

class Dogs(Pets):
    @staticmethod
    def bark():
        print('Woff!!')

tom=Dogs()
tom.bark()