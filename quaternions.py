import math
class Quaternions:
    def __init__(self,a0=0, a1=0, a2=0, a3=0):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __str__(self):
        return f"{self.a0} {self.a1:+}i {self.a2:+}j {self.a3:+}k"

    def __eq__(self, other):
        if not isinstance(other, Quaternions):
            return False

        if (self.a0 == other.a0 and
                self.a1 == other.a1 and
                self.a2 == other.a2 and
                self.a3 == other.a3):
            return True

        else:
            return False

    def __add__(self, other):
        if not isinstance(other, Quaternions):
            return NotImplemented
        sum = Quaternions()
        sum.a0 = self.a0 + other.a0
        sum.a1 = self.a1 + other.a1
        sum.a2 = self.a2 + other.a2
        sum.a3 = self.a3 + other.a3
        return sum

    def __sub__(self, other):
        if not isinstance(other, Quaternions):
            return NotImplemented
        diff = Quaternions()
        diff.a0 = self.a0 - other.a0
        diff.a1 = self.a1 - other.a1
        diff.a2 = self.a2 - other.a2
        diff.a3 = self.a3 - other.a3
        return diff

    def __mul__(self, other):
        if not isinstance(other, Quaternions):
            return NotImplemented

        product = Quaternions()

        a0, a1, a2, a3 = self.a0, self.a1, self.a2, self.a3
        b0, b1, b2, b3 = other.a0, other.a1, other.a2, other.a3

        product.a0 = a0*b0 - a1*b1 - a2*b2 - a3*b3
        product.a1 = a0*b1 + a1*b0 + a2*b3 - a3*b2
        product.a2 = a0*b2 - a1*b3 + a2*b0 + a3*b1
        product.a3 = a0*b3 + a1*b2 - a2*b1 + a3*b0

        return product

    def __abs__(self):
        magnitude = math.sqrt(self.a0**2 + self.a1**2 + self.a2**2 + self.a3**2)
        return magnitude

    def conjugate(self):
        return Quaternions(self.a0, -self.a1, -self.a2, - self.a3)

    def inverse(self):
      mag_squared = self.a0**2 + self.a1**2 + self.a2**2 + self.a3**2

      if mag_squared == 0:
          raise ValueError("Magnitude is zero")

      conj = self.conjugate()

      inverse = Quaternions()
      inverse.a0 = conj.a0 / mag_squared
      inverse.a1 = conj.a1 / mag_squared
      inverse.a2 = conj.a2 / mag_squared
      inverse.a3 = conj.a3 / mag_squared

      return inverse

    def __truediv__(self, other):
        if not isinstance(other,Quaternions):
            return NotImplemented

        return self * other.inverse()

