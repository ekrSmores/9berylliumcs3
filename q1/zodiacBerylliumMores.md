a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

Example:
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1900

d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.

i. Rat (鼠 / Shǔ)
ii. Ox (牛 / Niú)
iii. Tiger (虎 / Hǔ)
iv. Rabbit (兔 / Tù)
v. Dragon (龙 / Lóng)
vi. Snake (蛇 / Shé)
vii. Horse (马 / Mǎ)
viii. Goat (羊 / Yáng)
ix. Monkey (猴 / Hóu)
x. Rooster (鸡 / Jī)
xi. Dog (狗 / Gǒu)
xii. Pig (猪 / Zhū)

e. CONSIDER only the year of birth.

Example input and output:
Enter your birth year: 2000
Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)


Code:

birth = int(input("Enter your birth year: "))

if birth < 1900:
    print("Year it shouldn't be earlier than 1900")
else:
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

        sign = (birth - 4) % 12 + 1
        print(f"Your Chinese Zodiac sign is: {zodiac[sign]}")

    zodiac_sign(birth)

