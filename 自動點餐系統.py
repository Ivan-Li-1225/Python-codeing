print("歡迎使用拉麵點餐機~")
print("(1)","鹽味拉麵","$220")
print("(2)","醬油拉麵","$240")
print("(3)","豚骨拉麵","$280")

Noddles_1 = 220
Noddles_2 = 240
Noddles_3 = 280

taste = input("請選擇拉麵口味(1 or or 3:) \n")

AddSize = str(input("是否加大, 豚骨口味+$50, 其他口味+$30 (輸入:Y or N):"))

AddSizePrice_1 = 30
AddSizePrice_2 = 30
AddSizePrice_3 = 50

if taste == 1 and AddSize == "Y" :
    AddSizePrice = Noodles_1 + AddSizePrice_1
elif taste == 2 and AddSize == "Y" :
    AddSizePrice = Noodles_2 + AddSizePrice_2
elif taste == 3 and AddSize == "Y" :
    AddSizePrice = Noddles_3 + AddSizePrice_3
else:
    AddSizePrice = Noddles_1
    AddSizePrice = Noddles_2
    AddSizePrice = Noddles_3

AddEgg = str(input("是否加溏心蛋+$30 (輸入:Y or N):"))
AddEggPrice = 30

if taste == 1 and AddEgg == ""

AddItem = str(input("是否加叉燒+$60 (輸入:Y or N):"))
AddItemPrice_ = 60

TotalPrice = AddSize+



print("總金額= ", , 謝謝您的光臨)