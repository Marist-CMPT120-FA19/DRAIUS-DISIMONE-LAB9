##Draius Disimone Lab 9

def main():
    n = int(input("Show prime numbers up to the #: "))
    number = []
    for i in range(2 , n + 1):
        number.append(i)
        
    while len(number) > 0:
        cur = number.pop(0)
        print(cur , "is prime.")
        
        for j in number:
            if j % cur == 0:
                number.remove(j)
main()
