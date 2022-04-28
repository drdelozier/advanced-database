import time

def mapper(line):
    for word in line.split():
        print("computing a value")
        yield(word,1)

x = mapper("this is a sentence that is short")
w = next(x)
while w:
    print(w)
    w = next(x)
    time.sleep(1)

