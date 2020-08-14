from Driver.handle_excle import handle
import random

for i in range(8000):
    print('第{}条'.format(i+1))
    user = random.choice(['AA', 'BB', 'CC', 'DD', 'EE', 'HH', 'HW']) + "".join(
        random.choice("0123456789") for i in range(5))
    pwd = "姬存希yuan{0}".format(random.randint(6, 999999))
    array = [user, pwd]
    handle.write_cell_content(array)
    print("授权码: " + str(user))
    print("姓名：" + str(pwd))