def discount(price,rate):
	finalprice=price*rate
	print("折扣过的价格为：",finalprice)

oldprice=float(input("请输入原价格："))

rate=float(input("请输入折扣率："))
finalprice=discount(oldprice,rate)

