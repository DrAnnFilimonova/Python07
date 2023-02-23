def GetVowelsCount(text):
    count = 0
    for letter in text:
        if letter in vowels:
            count = count + 1
    return count
vowels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
poem = input().lower()
phrases = poem.split()
vowelsCount = GetVowelsCount(phrases[0])
rhyme = True
for phrase in phrases:
    rhyme &= GetVowelsCount(phrase) == vowelsCount
if rhyme:
    print("Парам пам-пам")
else:
    print("Пам парам")