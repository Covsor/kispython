class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def crack(self):
        if self.state == 'E':
            self.state = 'A'
            return 7
        raise MealyError('crack')

    def paint(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'F':
            self.state = 'A'
            return 8
        raise MealyError('paint')

    def tread(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'E':
            self.state = 'B'
            return 6
        raise MealyError('tread')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.tread() == 0
    assert o.paint() == 1
    assert o.paint() == 3
    assert o.tread() == 2
    assert o.paint() == 4
    assert o.paint() == 5
    assert o.paint() == 8
    assert o.tread() == 0
    assert o.paint() == 1
    assert o.tread() == 2
    assert o.paint() == 4
    assert o.crack() == 7
    assert o.tread() == 0
    assert o.paint() == 1
    assert o.tread() == 2
    assert o.paint() == 4
    assert o.tread() == 6
    raises(lambda: o.tread(), MealyError)
    raises(lambda: o.crack(), MealyError)
    assert o.paint() == 1
    assert o.tread() == 2
    assert o.paint() == 4
    assert o.crack() == 7
    raises(lambda: o.paint(), MealyError)