import random   #引用随机数
import time   #引用时间间隔

answer = random.randint(1,10)  #取1到10中的随机整数，并赋值给answer


def guess_game(): #定义一个guess_game的函数
    
    print ('游戏开始：') 
    time.sleep(0.5)   #时间间隔1秒
    
    for n in range(4):   #允许猜(循环)4次
        print( 'round'+ str(n+1))
        guess = int(input('1到10 猜猜我心里想的是几 ？'))  # guess的值变为int 整数
        time.sleep(0.5)
        if guess > answer and n <3:
             print('太大了，请继续猜 ')
             print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
             time.sleep(0.3)

        elif guess < answer and n<3:
            print('太小了，请继续猜 ')
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<')
            time.sleep(0.3)

        elif guess != answer and n==3:
            print('答案是'+str(answer)+',游戏结束，你输了')
            print('--------------------------')
            time.sleep(1.2)
            break
        
        else:
            print('好聪明，猜对了！')
            print('★☆★☆★☆★☆★☆★☆★☆★☆★☆')
            time.sleep(1.2)
            break
        
while True:
    answer = random.randint(1,10)
    guess_game()
    goon = input('是否要继续游戏，退出请按n，按其他键再来一盘 ')
    time.sleep(0.5)
    if goon == 'n':
        print ('游戏结束啦')
        break

