def lychrel(n):
    def est_palindrome(s):
        return s == s[::-1]

    def reverse_number(n):
        return int(str(n)[::-1])

    iteration = 0
    while iteration < 1050:
        n += reverse_number(n)
        if est_palindrome(str(n)):
            iteration +=1
            return iteration
        iteration += 1
    



def main():
    print(lychrel(50))

if __name__=='__main__':
    main()
