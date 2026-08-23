birth = int(input("Enter your birth year: "))

if birth < 1900:
    print("Year it shouldn't be earlier than 1900")

def zodiac_sign(a):
    zodiac = {
        1: "Rat (鼠 / Shǔ)",
        2: "Ox (牛 / Niú)",
        3: "Tiger (虎 / Hǔ)",
        4: "Rabbit (兔 / Tù)",
        5: "Dragon (龙 / Lóng)",
        6: "Snake (蛇 / Shé)",
        7: "Horse (马 / Mǎ)",
        8: "Goat (羊 / Yáng)",
        9: "Monkey (猴 / Hóu)",
        10: "Rooster (鸡 / Jī)",
        11: "Dog (狗 / Gǒu)",
        12: "Pig (猪 / Zhū)"
    }

    sign = (birth - 4)% 12+ 1
    print(f"Your Chinese Zodiac sign is: {zodiac[sign]}")

zodiac_sign(birth)