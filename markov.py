import markovify

with open("rick.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(10):
    print(text_model.make_short_sentence(140))
