for _ in range(int(input())) :
    toPay = int(input())
    coins = [50000, 10000, 5000, 1000, 500, 100]
    coinCnt = 0
    
    for coin in coins :
        coinCnt += toPay // coin
        toPay %= coin
    print(coinCnt)