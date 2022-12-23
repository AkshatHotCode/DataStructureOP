#Numeric Progression can the best exampled of INHERITANCE, because we develop a hierarchy of classes for iterating numeric progressions.

#Numeric Progression is sequence of numbers, where each numbers depends on one or more of the previous numbers.
# --> Arithmetic Progression - determines the next number by adding a foxed constant to the previous value. (a1 + n-1)d
# --> Geometric Progression determines the next number by multiplying the previous valur by a fixed constant.

#An Generic Numeric Progression Class
class Progression:
    """Iterator producing a generic progression.
    Default iterator produces an whole number. 0,1,2,3,...."""

    def __init__(self, start=0):
        """Starting the current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update start value with the new value."""
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise the StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        """Print next n in the progression."""
        print(' '. join(str(next(self)) for j in range(n)))

#Arithmetic Progression -->Inheriting from the above Generic Progression Class
class ArithmeticProgression(Progression): #inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, inccrement, start=0):
        """Create a new arithmetic progression."""
        super().__init__(start)
        self._increment = inccrement

    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment

