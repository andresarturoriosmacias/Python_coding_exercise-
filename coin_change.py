def coin_change(coin_list, amount):

    coin_dic = {}
    for i in coin_list:
        coin_dic[str(i)] = amount // i
        amount = round(amount%i,2)
        #amount = round(amount-(i*coin_dic[str(i)]),2)
        print(amount)
    return coin_dic

print(coin_change([0.25,0.10,0.05,0.01],0.43))
