import random
dish=['西红柿炒鸡蛋','烧茄子','糖醋里脊','青椒肉丝炒面','醋溜土豆丝','鱼香肉丝','宫保鸡丁','粉蒸排骨','锅挞鸡蛋']
fanguan=['肯德基','麦当劳','吉野家','晋面香','重庆小面','大懒龙','711','酱骨头','烤串店','羊汤馆']
goes='True'
mode=int(input('请输入1选吃的，2选馆子，其他结束'))
while True:
    if mode==1:
        dishchoice=random.choice(dish)
        print('今天你就吃%s吧 '% dishchoice)
        chizhexingma=input('吃这个可以吗，不行输入n，其他结束')
        if chizhexingma =='n':
            continue
        else:
            print('这道%s不错呦'% dishchoice)
            break

            

    elif mode==2:
        fanguanchoice=random.choice(fanguan)
        print('今天你就吃%s这家吧 '% fanguanchoice)
        chizhexingma=input('吃这个可以吗，不行输入n，其他结束')
        if chizhexingma =='n':
            continue
        else:
            print('这家%s不错呦'% fanguanchoice)
            break
    else:
        break
print('好好享用！')
