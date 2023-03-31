def solution(price, money, count):
    summ = (price + price*count)*(count/2)
    if(summ<money):
        return 0
    else:
        return summ - money
