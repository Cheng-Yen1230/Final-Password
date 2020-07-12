from random import randint
from time import sleep
from terminaltables import AsciiTable
Head = ["回合", "   範圍", "猜謎數字"]
Min, Max, Round = 1, 100, 1
isBingo, Judy = True, True
data = []
#選擇模式
def mode():
    body = """電腦隨機生成終極密碼(1) & 手動設定終極密碼(2) & 退出當前操作(3): """
    while Judy:
        print("------------------------終極密碼 1 ~ 100 ---------------------------")
        choose = input(body)
        if choose.isdigit() and 0 < int(choose) < 4:
            if choose == "1":
                generate_num()
            if choose == "2":
                Manual_setting()
            if choose == "3":
                break
        else:
            print("輸入指令錯誤")
            body = "重新輸入指令"

#計算機隨機產生密碼
def generate_num():
    global Min, Max, Judy, Round
    #初始化範圍
    Min, Max, Round = 1, 100, Round
    #不包含 1 和 100
    rd = randint(2, 100)
    print("正在產生密碼...")
    sleep(3)
    print("終極密碼產生完畢 ! ! !")
    while True:
        result = input("輸入終極密碼，密碼介於 {} ~ {} : \n".format(Min, Max))
        data.append([Round, "%3d ~ %3d" % (Min, Max), result])
        Round += 1
        if result.isdigit() and Min < int(result) < Max:
            result = int(result)
            if result > rd:
                Max = result
            elif result < rd:
                Min = result
            else:
                print("Bingo，答對了 ! ! ! ")
                table = AsciiTable([Head, *data])
                print(table.table)
                if input("還要繼續玩嗎 [y / n] ?: ") == "y":
                    break
                else:
                    print("遊戲結束 ! ! !")
                    Judy = False
                    break
        else:
            print("密碼並非數字 & 終極密碼範圍超出 ! ! !\n重新輸入終極密碼...")

#手動設定密碼
def Manual_setting():
    global Min, Max, isBingo, Judy, Round
    #初始化範圍
    Min, Max, Round = 1, 100, 1
    #初始化 isBingo
    isBingo = True
    while isBingo:
        num = int(input("設定終極密碼: "))
        if isinstance(num, int) and Min < num < Max :
            print("設定完成")
            while True:
                result = input("輸入終極密碼，密碼介於 {} ~ {} : \n".format(Min, Max))
                data.append([Round, "%3d ~ %3d" % (Min, Max), result])
                Round += 1
                if result.isdigit() and Min < int(result) < Max:
                    result = int(result)
                    if result > num:
                        Max = result
                    elif result < num:
                        Min = result
                    else:
                        print("Bingo，答對了 ! ! ! ")
                        table = AsciiTable([Head, *data])
                        print(table.table)
                        if input("還要繼續玩嗎 [y / n] ?: ") == "y":
                            isBingo = False
                            break
                        else:
                            isBingo = False
                            Judy = False
                            print("遊戲結束 ! ! !")
                            break
                else:
                    print("密碼並非數字 & 終極密碼範圍超出 ! ! !\n重新設定終極密碼...")
        else:
            print("重新設定 ! 密碼並非數字 & 範圍超出")
    
mode()
        

