import time

import random


class PhoneNOGenerator():
    # 随机生成手机号码

    def phoneNORandomGenerator(self):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

    #随机生成6位数
    def six(self):
        # prelist=["1","2",'3','4','5','6','7','8','9']
        list=[random.choice('123456789') for i in range(1)]
        hz=random.randint(0, 99999)
        return random.choice(list)+"".join(str(hz))



if __name__ == '__main__':
    pg = PhoneNOGenerator()
    print(pg.phoneNORandomGenerator())
    print(PhoneNOGenerator().six())

