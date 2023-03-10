class Student:

    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.Brand = self.Laptop()
        self.Cpu = self.Laptop()
        self.Ram = self.Laptop()

    def show(self):
        """Вывести информацию о студенте и его ноутбуке"""
        print(self.name, self.stud_id)
        print(self.Brand.brand, self.Cpu.cpu, self.Ram.ram)

    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = 8
# Создаем двух студентов
s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)

# Выводим данные по студенту и его нотбуку
s1.show()
# Ivan 2
# Hp i5 8

# Увеличиваем память у ноутбука студента s1
s1.Ram.ram = 16
s1.show()
# Ivan 2
# Hp i5 16

# У каждого студента отдельный ноутбук (уникальный объект)
lap1 = s1.Cpu
lap2 = s2.Cpu
print(id(lap1))
print(id(lap2))
# 2065309131248
# 2065309348096