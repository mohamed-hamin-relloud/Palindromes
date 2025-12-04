def check_password(s):
    """
    Docstring for check_password
    
    :param s: Description

    >>>check_password('ioooedfvkrv')
    pas assez solide
    >>>check_password('ioooedfvkr7875')
    solide
    >>>check_password('IOFusoofjc5756')
    solide
    >>>check_password('IOEIDFFEVCEVCE')
    pas assez solide
    >>>check_password('8522555545685')
    pas assez solide
    """
    if len(s)<10:
        print('pas assez solide')
    elif str.isupper(s) or str.islower(s) or str.isdigit(s):
        print('pas assez solide')
    else:
        print('solide')  

def main():
    print(check_password('Ajdfcv568r7vzEff!'))  

if __name__=="__main__":
    main()
    