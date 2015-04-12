#max.py

def main():
    n = eval(input("How many numbers are there? "))
    # Set max to be the first value
    max = eval(input("Enter a number >> "))
    #now compare the n-1 successive values
    for i in range(n-1):
        x = eval(input("Enter a number >>" ))
        if x > max:
            max = x
    print("The largest value is", max)
if __name__ == '__main__':
    main()