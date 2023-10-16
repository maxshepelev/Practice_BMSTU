#данный класс описывает все точки, лежащие на плоскости в декартовой системе координат

class Point_on_the_coordinate_plane:
    
    #единственные атрибуты точки: координата по оси Ox и по оси Oy
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        
    #метод str возвращает координаты заданной точки в виде строки
    
    def __str__(self):
        return '(' + str(self.x_coordinate) + ',' + ' ' + str(self.y_coordinate) + ')'
        
    #данный метод высчитывает расстояния от данной точки до цетра координат
    
    def distance_to_coordinate_center(self):
        return (self.x_coordinate ** 2 + self.y_coordinate ** 2) ** 0.5
    
    #данный метод высчитывает расстояние между двумя выбранными точками
    
    @staticmethod
    def distance_between_two_points(a, b):
        return ((a.x_coordinate - b.x_coordinate) ** 2 + (a.y_coordinate - b.y_coordinate) ** 2) ** 0.5
    
    #данный метод вычисляет уравнение прямой(угловой коэффициет и свободный член), проходящей через 2 заданные точки
    
    @staticmethod
    def equation_of_line(a, b):
        k = (a.y_coordinate - b.y_coordinate) / (a.x_coordinate - b.x_coordinate)
        d = a.y_coordinate - k * a.x_coordinate
        return (k, d)
    
    #данный метод проверяет, лежат ли все 3 заданные точки на одной прямой
    
    @staticmethod
    def check_3points_1line(a, b, c):
        d = Point_on_the_coordinate_plane.equation_of_line(a, b)
        if c.y_coordinate == d[0] * c.x_coordinate + d[1]:
            return 'All 3 points lie on the same line'
        else:
            return 'All 3 points can not lie on the same line'
    
    #данный метод определяет взаимное расположение двух прямых
    
    @staticmethod
    def relativ_pos_of_lines(s1, s2):
        if s1[0] != s2[0]:
            return 'lines intersect'
        elif s1[1] != s2[1]:
            return 'lines are parallel'
        else:
            return 'lines coincide'
        
class Point_in_the_space(Point_on_the_coordinate_plane):
    
    #единственные атрибуты точки: координатЫ по оси Ox, по оси Oy и по оси Oz
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z_coordinate = z
        
    #метод str возвращает координаты заданной точки в виде строки
    
    def __str__(self):
        return '(' + str(self.x_coordinate) + ',' + ' ' + str(self.y_coordinate) + ',' + ' ' + str(self.z_coordinate) + ')'
        
    #данный метод высчитывает расстояния от данной точки до цетра координат в пространстве
    
    def threeD_distance_to_coordinate_center(self):
        return (self.x_coordinate ** 2 + self.y_coordinate ** 2 + self.z_coordinate ** 2) ** 0.5
    
    #данный метод высчитывает расстояние между двумя выбранными точками в пространстве
    
    @staticmethod
    def threeD_distance_between_two_points(a, b):
        return ((a.x_coordinate - b.x_coordinate) ** 2 + (a.y_coordinate - b.y_coordinate) ** 2 + (a.z_coordinate - b.z_coordinate) ** 2) ** 0.5        
        
a = Point_on_the_coordinate_plane(0, 0)
b = Point_on_the_coordinate_plane(1, 1)
c = Point_on_the_coordinate_plane(0, -1)
d = Point_on_the_coordinate_plane(1, 0)
e = Point_in_the_space(3, 4, 5)
f = Point_in_the_space(1, 0, 2)
