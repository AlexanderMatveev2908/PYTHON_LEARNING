import attr


@attr.s(auto_attribs=True)
class Person:
    name: str
    age: int
    city: str
    _income: int = attr.ib(repr=False)
    # def __init__(self, name: str, age: int, city: str, income: int) -> None:
    #     self.name = name
    #     self.age = age
    #     self.city = city
    #     self.__income = income

    def greet(self) -> None:
        print(f"hi I am {self.name}")

    def safe_income(self) -> None:
        print(
            f"I earn between {self._income - 1000} "
            f"and {self._income + 1000}"
        )

    def __get_count(self) -> None:
        print(f"i earn {self._income} for month")


p = Person("John", 30, "Maryland", 3000)

p.greet()
# p._Person__get_count()
# print(p._Person__income)
p.safe_income()


# class Lawyer(Person):
#     def __init__(
#         self, name: str, age: int, city: str, income: int, car: str
#     ) -> None:
#         super().__init__(name, age, city, income)
#         self.car = car

#     def speach(self):
#         print(f"I'm a lawyer and my dream car is {self.car}")


# lw = Lawyer("Saul", 35, "Albequrqe", 100000, "Some fancy car")


# lw.greet()
# lw.speach()


@attr.s(auto_attribs=True)
class Lawyer(Person):
    car: str

    def speach(self):
        print(f"I'm a lawyer and my dream car is {self.car}")


lw = Lawyer("Saul", 35, "Albequrqe", 100000, "Some fancy car")


lw.greet()
lw.speach()
