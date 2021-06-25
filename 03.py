class Shaxs:
    def __init__(self, ismi, familiya, passport, tyil):
        self.ismi = ismi
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_fulname(self):
        return f"{self.ismi} {self.familiya}"

    def get_age(self, yil):
        return yil - self.tyil


class Talaba(Shaxs):
    def __init__(self, ismi, familiya, passport, tyil, id):
        super().__init__(ismi, familiya, passport, tyil)
        self.id = id
        self.bosqich = 1

    def get_id(self):
        return self.id

    def get_bosqich(self):
        return self.bosqich

class Abituriyent(Talaba):
    def __init__(self, ismi, familiya, passport, tyil, id, hobby, manzil):
        super().__init__(ismi, familiya, passport, tyil, id)
        self.hobby = hobby
        self.manzil = manzil

    # def __str__(self):
        # return f"{self.ismi} {self.familiya} {self.tyil} da tug'ilgan. Passport :{self.passport}, ID : {self.id} ,  {self.manzil}"

    def get_hobby(self):
        return self.hobby


class Manzil:
    def __init__(self, viloyat, tuman, kocha, uy ):
        self.viloyat = viloyat
        self.tuman = tuman
        self.kocha = kocha
        self.uy = uy

    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati {self.tuman} tumani {self.kocha} kocahsi {self.uy}-uy"
        return manzil

    # def __str__(self):
    #     return f"{self.ismi} {self.familiya} {self.tyil} da tug'ilgan. Passport :{self.passport}, ID : {self.id} ,  {self.manzil}"

# talaba1 = Talaba('ali', 'vali', 'ac4621', 2005, 321321321)
# print(talaba1.get_fulname())
# print(talaba1)

abit1_manzil = Manzil('Andijon', 'Baliqchi', 'sharafli', 18)
abit1 = Abituriyent('alisher', 'valijon', 'SC2353', 1995, 53, 'futboll', abit1_manzil)
print(abit1_manzil.get_manzil())    