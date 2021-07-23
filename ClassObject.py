class Object:

    def __init__(self, name='', type='portal', x=0, y=0, z=0, xx=0, yy=0, zz=0):
        self._name = name
        self._type = type
        self._x = x
        self._y = y
        self._z = z
        self._xx = xx
        self._yy = yy
        self._zz = zz

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_coordinates(self):
        coordinates = [self._x, self._y, self._z, self._xx, self._yy, self._zz]
        return coordinates

    def set_name(self, name):
        self._name = name

    def set_type(self, type):
        self._type = type

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value

    def set_z(self, value):
        self._z = value

    def set_xx(self, value):
        self._xx = value

    def set_yy(self, value):
        self._yy = value

    def set_zz(self, value):
        self._zz = value

    def change_value(self, attr, value):
        if attr == 'Name':
            self.set_name(value)
        if attr == 'Type':
            self.set_type(value)
        if attr == 'x':
            self.set_x(value)
        if attr == 'y':
            self.set_y(value)
        if attr == 'z':
            self.set_z(value)
        if attr == 'xx':
            self.set_xx(value)
        if attr == 'yy':
            self.set_yy(value)
        if attr == 'zz':
            self.set_zz(value)