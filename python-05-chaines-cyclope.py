def is_cyclope(n):
    a = str(n)
    if len(a)%2!=0 and a[len(a)//2]=='0':
        print(f'{n} est un nombre cyclope')
    else:
        print(f"{n} n'est pas un nombre cyclope")

def main():
    print(is_cyclope(6))

if __name__=="__main__":
    main()

