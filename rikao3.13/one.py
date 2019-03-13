#1. 设计一个电商商品价格数据统计程序，
# 先从“product.txt”中读取出全部10种待考察商品的名称，
# 接下来循环输入每个商品在京东、天猫、1号店的网售价格。
# 最后将全部统计结果写入“stat.txt”文档。
list_name = []
dict = {}
with open("D://stat.txt", "w") as f2:
    with open("D://product.txt","r") as f:
       lines = f.readlines()
       for i in lines:
           newi = i.strip('\n')
           list_name.append(newi)
       for i in range(10):
            print("请分别输入%s的价格" %list_name[i])
            price1 = input("在京东的价格：")
            price2 = input("在天猫的价格：")
            price3 = input("在1号店的价格：")
            s  = list_name[i] + '\t'+price1 + '\t'+ price2+ '\t' + price3+'\n'
            f2.write(s)


