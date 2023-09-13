import abc
import math

class Figure(abc.ABC):
    
    def __init__(self) -> None:
        pass
    
    @property
    @abc.abstractmethod
    def area() -> float:
        """Area of a figure."""
        pass

class Circle(Figure):
    __slots__ = ['r']
    
    def __init__(self, r : float) -> None:
        super().__init__()
        if(r is None or math.isnan(r)):
            raise ValueError("Radius must be a valid number")
        if(r <= 0):
            raise ValueError("Radius must be a valid number greater then 0.")
        self.r = r
    
    @property
    def area(self) -> float:
        """Area of a circle."""
        return math.pi * self.r * self.r

class Triangle(Figure):
    __slots__ = ['a', 'b', 'c']
    
    def __init__(self, a : float, b : float, c : float) -> None:
        super().__init__()
        if (a is None or b is None or c is None or
            math.isnan(a) or math.isnan(b) or math.isnan(c)):
            raise ValueError("Side size must be a valid number")
        if (a <= 0 or b <= 0 or c <= 0):
            raise ValueError("Side size must be a valid number greater then 0.")
        if (a + b <= c or
            a + c <= b or
            b + c <= a):
            raise ValueError("Triangle is not possible.")
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def area(self) -> float:
        """Area of a triangle."""
        lenghts = (self.a, self.b, self.c)
        #Check if triangle is right
        maxidx = lenghts.index(max(lenghts))
        previdx = maxidx - 1
        nextidx = 0 if maxidx + 1 >= 3 else maxidx + 1
        if math.isclose(lenghts[previdx] ** 2 + lenghts[nextidx] ** 2, lenghts[maxidx] ** 2):
            #If triangle is right
            return lenghts[previdx] * lenghts[nextidx] / 2
        else:
            #If triangle is not right
            s = sum(lenghts) / 2
            return math.sqrt(s * (s - lenghts[0]) * (s - lenghts[1]) * (s - lenghts[2]))
        

def getarea(figure: str, *args: float) -> float:
    """Get an area of a given figure.

    Keyword arguments:
    figure -- figure type ("circle", "triangle")
    args -- figure sizes (radius for circle; a, b, c sizes of a triangle)
    """
    if figure.lower() == "circle":
        if len(args) != 1:
            raise ValueError("Number of additional arguments must be 1 in order to find a circle area.")
        fig = Circle(*args)
        return fig.area
    elif figure.lower() == "triangle":
        if len(args) != 3:
            raise ValueError("Number of additional arguments must be 3 in order to find a triangle area.")
        fig = Triangle(*args)
        return fig.area
    else:
        raise ValueError("Unimplemented figure.")