def biggestst(x):
    MaxKey={}

    MaxKey=max(x, key=x.get)

    return MaxKey

x={"Mon": 3, "Tue": 11, "Wed": 8}

print(biggestst(x))
