# class method as a class attribute

from enum import Enum

class MyClass:
    def __init__(self, name: str, func=None):
        self.name = name
        self.func = func
        if self.func is not None:
            self.func(self, 'constructor')

    def class_instance_method(self, source: str):
        print('Class instance method has been called from {} on \'{}\' instance.'.format(source, self.name))


class MyClass2:
    class MyClass1State(Enum):
        Invalid = 0
        State1 = 1
        State2 = 2
        State3 = 3

    def __init__(self, initial_state=MyClass1State.State1):
        self.current_state = MyClass2.MyClass1State.Invalid
        self.f = None
        self.set_state(initial_state)

    def set_state(self, state):
        if self.current_state != state:
            self.current_state = state
            if self.current_state == MyClass2.MyClass1State.State1:
                self.f = MyClass2.function1
            elif self.current_state == MyClass2.MyClass1State.State2:
                self.f = MyClass2.function2
            elif self.current_state == MyClass2.MyClass1State.State3:
                self.f = MyClass2.function3
            else:
                print('Error. Not handled enum value.')

    def function1(self):
        print('function1')

    def function2(self):
        print('function2')

    def function3(self):
        print('function3')

    def run(self):
        self.f(self)



if __name__ == '__main__':
    my_class2_instance = MyClass2()
    my_class2_instance.run()

    my_class2_instance.set_state(MyClass2.MyClass1State.State2)
    my_class2_instance.run()

    my_class2_instance.set_state(MyClass2.MyClass1State.State3)
    my_class2_instance.run()

    print('exit')
