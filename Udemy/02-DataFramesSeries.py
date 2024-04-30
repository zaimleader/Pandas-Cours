import pandas as pd

animals = {
    "Mammals" : ["Cow", "Cat", "Dog"],
    "Reptiles" : ["Crocodile", "Bird", "Snakes"],
    "Insects" : ["Ant", "Bee", "Spider"],
}

df = pd.DataFrame(animals)

serie = df.iloc[0]

print(serie)

print(type(serie))
