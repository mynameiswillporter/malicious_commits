def main():
    a = 1       # 'a' followed by a space
    b = 1
    aﾠ= 2       # 'aﾠ' is the variable using an 'a' and a halfwidth hangul filler
    c = aﾠ+ b
    print(c)    # prints 3
    c = a + b
    print(c)    # prints 2

if __name__ == "__main__":
    main()
