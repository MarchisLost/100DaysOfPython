def add(*args):
    for i in args:
        print(i)


#add(1, 2, 3, 4, 5)


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print('key=', key, 'value=', value)

    print(n)


calculate(3, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        #!! Get instead of just '[]' makes it so it is optional, so in this case i need to give somethign for the make, but not for the model
        self.make = kw['make']
        self.model = kw.get('model')


myCar = Car(make='Nissan')
print(myCar.make)
