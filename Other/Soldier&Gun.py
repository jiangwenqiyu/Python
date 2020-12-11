class bulletLimit(object):
    def __init__(self, model):
        if model == "ak47":
            self.limit = 30
        elif model == "awm":
            self.limit = 10
        else:
            print("不存在这把枪！")

class Gun(bulletLimit):
    def __init__(self, model):
        self.model = model
        self.count = 0
        super().__init__(model)

    def shoot(self):
        if self.count > 0:
            self.count -= 1
            print('剩余子弹：%d/%d' % (self.count, self.limit))
        else:
            self.addBullet()

    def addBullet(self):
        self.count = self.limit
        print('装弹完成，当前子弹数%d' % self.count)

class Soldier(object):
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if not self.gun == None:
            if self.gun.count > 0:
                print('射击！')
                self.gun.shoot()
            else:
                print('没子弹了，准备装弹')
                self.add_bullet()
        else:
            print('没枪')

    def add_bullet(self):
        self.gun.addBullet()


sol_obj = Soldier(input("输入人名："))
isquit = True
while isquit:
    gun_obj = Gun(input("输入枪名："))
    sol_obj.gun = gun_obj
    while True:
        c = input('1.射击  2.装弹  3.换枪  4.退出:')
        if c=="1":
            sol_obj.fire()
        elif c == "2":
            sol_obj.add_bullet()
        elif c == "3":
            break
        elif c == "4":
            isquit = False
            break



