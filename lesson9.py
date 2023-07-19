class Human:
    def __init__(self, name: str, age: int, work: str, height: int):
        self.name = name
        self.age = age
        self.work = work
        self.height = height

    def hello(self):
        print(f'{self.name} hello for you!')

    def poly(self, a, s, d):
        return f"{self.name}, {a}, {s}, {d}"

    def __add__(self, other):
        return Human(self.name+other.name, self.age + other.age, self.work+other.work, self.height+other.height)

    def __str__(self):
        return f'{self.name}, {self.age}, {self.work}, {self.height}'

    def __len__(self):
        return self.height


dioneer = Human('Elena', 34, "GB", 156)
zaur = Human('Zaur', 18, "Home", 178)
print(dioneer)
print(zaur)
print(dioneer.poly(1, 2, 3))
print(len(zaur))
print(dioneer+zaur)
