import pytest
import areapy
import math

class TestCircle():
    
    def test_r_negative(self):
        with pytest.raises(ValueError):
            areapy.Circle(-3)
        with pytest.raises(ValueError):
            areapy.Circle(-5.11)
        with pytest.raises(ValueError):
            areapy.Circle(-661.13)
            
    def test_r_None_or_nan(self):
        with pytest.raises(ValueError):
            areapy.Circle(None)
        with pytest.raises(ValueError):
            areapy.Circle(float("nan"))
    
    def test_r_zero(self):
        with pytest.raises(ValueError):
            areapy.Circle(0)
            
    def test_r_positive(self):
        areapy.Circle(3)
        areapy.Circle(5.23)
        areapy.Circle(777.77)
        
    def test_area(self):
        c1 = areapy.Circle(2)
        c2 = areapy.Circle(4.23)
        c3 = areapy.Circle(32.77)
        assert math.isclose(math.pi * 2 ** 2, c1.area)
        assert math.isclose(math.pi * 4.23 ** 2, c2.area)
        assert math.isclose(math.pi * 32.77 ** 2, c3.area)

class TestTriangle():
    
    def test_abc_negative(self):
        with pytest.raises(ValueError):
            areapy.Triangle(-3, 5, 1)
        with pytest.raises(ValueError):
            areapy.Triangle(5.11, -1.3, 8)
        with pytest.raises(ValueError):
            areapy.Triangle(-33, -2.1, 2)
        with pytest.raises(ValueError):
            areapy.Triangle(33, 2.13, -11)
            
    def test_abc_None_or_nan(self):
        with pytest.raises(ValueError):
            areapy.Triangle(None, 1, 2)
        with pytest.raises(ValueError):
            areapy.Triangle(1, 2, float("nan"))
        with pytest.raises(ValueError):
            areapy.Triangle(None, 2, float("nan"))
    
    def test_abc_zero(self):
        with pytest.raises(ValueError):
            areapy.Triangle(0, 1, 2)
        with pytest.raises(ValueError):
            areapy.Triangle(1, 0, 2)
        with pytest.raises(ValueError):
            areapy.Triangle(0, 0, 2)
        with pytest.raises(ValueError):
            areapy.Triangle(2, 1, 0)
            
    def test_abc_positive_valid(self):
        areapy.Triangle(3, 5, 7)
        areapy.Triangle(5.23, 4.3, 3)
        areapy.Triangle(1, 1, 1)
    
    def test_abc_positive_nonvalid(self):
        with pytest.raises(ValueError):
            areapy.Triangle(1, 10, 2)
        with pytest.raises(ValueError):
            areapy.Triangle(77, 2.311, 1)
        with pytest.raises(ValueError):
            areapy.Triangle(13, 12, 100)
        
    def test_area(self):
        t1 = areapy.Triangle(7, 24, 25)
        t2 = areapy.Triangle(3.23, 2, 2)
        t3 = areapy.Triangle(5, 7, 10)
        t4 = areapy.Triangle(25, 24, 7)
        assert math.isclose(7 * 24 / 2, t1.area)
        s = (3.23 + 2 + 2) / 2
        assert math.isclose(math.sqrt(s * (s - 3.23) * (s - 2) * (s - 2)), t2.area)
        s = (5 + 7 + 10) / 2
        assert math.isclose(math.sqrt(s * (s - 5) * (s - 7) * (s - 10)), t3.area)
        assert math.isclose(7 * 24 / 2, t4.area)
        
class TestGetarea():
    circletxt = "circle"
    triangletxt = "triangle"
    
    def test_wrong_figure(self):
        with pytest.raises(ValueError):
            areapy.getarea("Pentagram", 3, 2, 2, 3, 2)
        with pytest.raises(ValueError):
            areapy.getarea("norway", 100)
    
    def test_circle_wrong_args(self):
        with pytest.raises(ValueError):
            areapy.getarea(self.circletxt)
        with pytest.raises(ValueError):
            areapy.getarea(self.circletxt, 3, 3, 3)
    
    def test_circle_area(self):
        c1 = areapy.getarea(self.circletxt, 3)
        c2 = areapy.getarea(self.circletxt, 5.23)
        c3 = areapy.getarea(self.circletxt, 33.77)
        assert math.isclose(math.pi * 3 ** 2, c1)
        assert math.isclose(math.pi * 5.23 ** 2, c2)
        assert math.isclose(math.pi * 33.77 ** 2, c3)
    
    def test_triangle_wrong_args(self):
        with pytest.raises(ValueError):
            areapy.getarea(self.triangletxt)
        with pytest.raises(ValueError):
            areapy.getarea(self.triangletxt, 5)
    
    def test_triangle_area(self):
        t1 = areapy.getarea(self.triangletxt, 7, 24, 25)
        t2 = areapy.getarea(self.triangletxt, 3.33, 2, 2)
        t3 = areapy.getarea(self.triangletxt, 5, 8, 10)
        t4 = areapy.getarea(self.triangletxt, 25, 24, 7)
        assert math.isclose(7 * 24 / 2, t1)
        s = (3.33 + 2 + 2) / 2
        assert math.isclose(math.sqrt(s * (s - 3.33) * (s - 2) * (s - 2)), t2)
        s = (5 + 8 + 10) / 2
        assert math.isclose(math.sqrt(s * (s - 5) * (s - 8) * (s - 10)), t3)
        assert math.isclose(7 * 24 / 2, t4)
        
    def test_upper_case(self):
        areapy.getarea("Circle", 2)
        areapy.getarea("Triangle", 5, 5, 5)
