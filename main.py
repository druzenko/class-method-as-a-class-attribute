# class method as a class attribute

class MyClass:
    def __init__(self, name: str, func=None):
        self.name = name
        self.func = func
        if self.func is not None:
            self.func(self, 'constructor')

    def class_instance_method(self, source: str):
        print('Class instance method has been called from {} on \'{}\' instance.'.format(source, self.name))


if __name__ == '__main__':
    my_class_instance0 = MyClass('my_class_instance0', MyClass.class_instance_method)
    my_class_instance1 = MyClass('my_class_instance1', MyClass.class_instance_method)

    print('exit')
