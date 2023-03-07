import matplotlib


class Form:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers

    def print_students(self):
        pass


form1 = Form(students=['Ioan', 'Petre', 'Anca', 'Bogdan', 'Tamas'], teachers=['Ioan', 'Petre'])
students = form1.students
# form1.print_students()

form2 = Form(students=[], teachers=[])
print(form2.students)


class Curves:
    def __init__(self, colors, counter=None):
        self._own_color = colors[counter]
        self._curves = ["curve_1", "curve_2", "curve_3", "curve_4"]
        self._x_values = [0, 2, 4, 6]
        self._y_values = [3.5, -2, 5, 8]
        self._colors = ['red', 'blue', 'green', 'red']
        self._mapped_colors_with_curves = {}
    
    @classmethod
    def func(cls):
        for value in cls._x_values:
            print(value)

    def our_own_color(self):
        return self._own_color

    @property
    def curves(self):
        return self._curves

    def get_curves(self):
        return self.__curves

    @property
    def colors(self):
        return self._colors

    @curves.setter
    def curves(self, value):
        self._curves = value

    @colors.setter
    def colors(self, value):
        self._colors = value

    def map_curve_and_color(self):
        for idx in range(len(self._curves)):
            self._mapped_colors_with_curves[self._curves[idx]] = self._colors[idx]


class CurveSelection(Curves):
    def __init(self):
        super().init()

    def print_colors(self):
        print(self.get_curves())


curve = Curves(colors=['1', '2', '3'], counter=1)
curve.map_curve_and_color()

# curve_selection = CurveSelection()
# curve_selection.print_colors()


class RedCurves(Curves):
    def __init__(self):
        super().__init__(['1', '2', '3'], counter=1)
        self._red_curves = {}

    def map_curve_and_color(self):
        super().map_curve_and_color()
        for key, value in self._mapped_colors_with_curves.items():
            if value == "red":
                self._red_curves[key] = value
        print(self._red_curves)


curve = Curves(['1', '2', '3'], counter=1)
curve.map_curve_and_color()
print(curve._mapped_colors_with_curves)

red_curves = RedCurves()
red_curves.map_curve_and_color()
