import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()

with open("input.txt", "r") as file:
    text = file.read().lower()

words = {}

print(re.findall(r"\bquick\b", text))

for searched_word in searched_words:
    pattern = re.compile(r"\b{searched_word}\b")
    result = re.findall(pattern, text)
    words[searched_word] = len(result)

with open("output.txt", "w") as file:
    for key, value in sorted(words.items(), key=lambda kvp: -kvp[1]):
        file.write(f"{key} - {value}\n")