def remove_vowels_rec(s):
    chaine = ''
    for c in s:
        if c in 'aeiuoy':
            c=''
            chaine+=c
        chaine+=c
    return chaine


def main():
    remove_vowels_rec(s)

if __name__=='__main__':
    main()
