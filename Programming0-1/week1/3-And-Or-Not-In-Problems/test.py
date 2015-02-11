__author__ = 'Боян'

s = input("Enter Your test score !")
score = int(s)

if 0 <= score <= 50:
    print("Слаб 2")
elif 51 <= score <= 60:
    print("Среден 3")
elif 61 <= score <= 70:
    print("Добър 4")
elif 71 <= score <= 80:
    print("Много Добър 5")
elif 81 <= score < 100:
    print("Отличен 6")
elif score == 100:
    print("Много Отличен 7")
else:
    print("You have wealthy parents, they will buy You diploma")