class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        full_name = self.first_name + " " + self.family_name
        return full_name

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        fee = self.entry_fee()
        ff_name = self.full_name()
        return ff_name + "," + str(self.age) + "," + str(fee)


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# 省略
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力
