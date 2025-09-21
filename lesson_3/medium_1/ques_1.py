sentence = "The Flintstones Rock!"
counter = 0

# while counter < 10:
#     sentence = "-" + sentence
#     print(sentence)
#     counter += 1

for padding in range(1,11):
    print(f'{"-" * padding}{sentence}')