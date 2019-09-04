import random

guess = ''
punk= ['正面','反面']

while guess not in ['正面','反面']:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')

# 随机抛硬币，0代表反面，1代表正面
    toss = random.choice(punk)


    if toss == guess:
        print('猜对了！你真棒')
        break
    else:
        print('没猜对，你还有一次机会。')
        guess = input('再输一次“正面”或“反面”：')
        if toss == guess:
            print('你终于猜对了！')
            break
        else:
            print('败得一塌糊涂！')
            break
