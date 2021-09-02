with open("1.txt", encoding="utf-8") as file:
    text1 = file.readlines()
    text1[-1] = text1[-1].strip()

with open("2.txt", encoding="utf-8") as file:
    text2 = file.readlines()
    text2[-1] = text2[-1].strip()

with open("3.txt", encoding="utf-8") as file:
    text3 = file.readlines()
    text3[-1] = text3[-1].strip()

names = ["1.txt", "2.txt", "3.txt"]
text = [text1, text2, text3]
new_text = ''

for i in sorted(text, key=lambda x: len(x)):
    new_text += names[text.index(i)] + "\n"
    new_text += str(len(i)) + "\n"
    for j in i:
        new_text += j
    new_text += "\n"

with open("4.txt", "w",encoding="utf-8") as file:
    file.write(new_text)