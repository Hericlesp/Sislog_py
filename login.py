#     LOGIN

login = []
senha = []
tent = 0
valid= False


#def newlog(a):
while valid == False:
        import os
        os.system('cls')
        print('==' * 30)
        print('     VAMOS LOGAR...  ')
        print('\n')
        print(tent)
        print('==' * 20)
        print(' '*5,'| LOGIN |')
        print('==' * 20)
        logEn=str(input('ACESSE SEU LOGIN:  '))
        print('==' * 20)
        senEn=str(input('ACESSE SUA SENHA:  '))
        print('==' * 20)
        if login == logEn and senha == senEn:
            print('==' * 20)
            print('     ACESSO LIBERADO    ')
            print('==' * 20)
            valid = True
            break
        else:
            tent = tent + 1

    
if tent==4:
        import os
        os.system('cls')
        print('==' * 20)
        print('     ACESSO NEGADO!!    ')
        print('==' * 20)
        if login != logEn:
            print('     LOGIN INCORRETO!!    ')
            print('==' * 20)
        if senha != senEn:
            print('     SENHA INCORRETA!!    ')
            print('==' * 20)


# pagina primaria
import os
os.system('cls')

print('\n' * 6)
print('==' * 20)
print("     PRIMEIRO ACESSO??")
acess=str(input("   ")).lower()
print('==' * 20)
print('\n' * 6)
if acess == "sim":
    import os
    os.system('cls')
    print('==' * 20)
    print('     | REGISTRAR |    ')
    print('==' * 20)
    login=str(input('DEFINA SEU LOGIN:  '))
    print('==' * 20)
    senha=str(input('SENHA:  '))
    print('==' * 20)
else:
#     newlog(acess)
# newlog(acess)

# elif acess==("nao" or "NAO" or "Nao" or "não" or "NÃO" or "Não"):
#     print('\n' * 6)