Height = float(input("請輸入您的身高(cm): \n"))
Weight = float(input("請輸入您的體重(kg): \n"))
BMI = Weight/(Height/100)**2
if BMI < 18.5:
    print("您的BMI值= ", round(BMI, 1),("體重過輕"))
elif BMI >= 18.5 and BMI < 24:
    print("您的BMI值= ", round(BMI, 1), ("正常體位"))
elif BMI >= 24 and BMI < 27:
    print("您的BMI值= ", round(BMI, 1), ("體重過重"))
elif BMI >= 27 and BMI < 30:
    print("您的BMI值= ", round(BMI, 1), ("輕度肥胖"))
elif BMI >= 30 and BMI < 35:
    print("您的BMI值= ", round(BMI, 1), ("中度肥胖"))
else:
    BMI >= 35
    print("您的BMI值= ", round(BMI, 1), ("重度肥胖"))



