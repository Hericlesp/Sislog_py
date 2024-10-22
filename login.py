#     LOGIN

login = []
senha = []
loginM = "ROOT"
senhaM = "ROOT"
tent = 0
validador = 0


def logar():
    tent=1
    validador=0
    while validador < 6:
        tent
        import os
        os.system('cls')
        print('==' * 30)
        print('     VAMOS LOGAR...  ')
        print('\n')
        print(" TENTATIVAS FALHAS: ",tent)
        print('==' * 20)
        print(' '*5,'| LOGIN |')
        print('==' * 20)
        logEn=str(input('ACESSE SEU LOGIN:  '))
        print('==' * 20)
        senEn=str(input('ACESSE SUA SENHA:  '))
        print('==' * 20)

           #  validar
        if login == logEn and senha == senEn: 
            print('==' * 20)
            print('     ACESSO LIBERADO    ')
            print('==' * 20)
            print('\n'*6)
            validador = 7
            break
        if loginM == 'ROOT' and senhaM == 'ROOT':
            print('==' * 20)
            print('     ACESSO LIBERADO    ')
            print('==' * 20)
            print('\n'*6)
            validador = 7
            break
        else:
            tent = tent + 1

        if tent==3:
                import os
                os.system('cls')
                print('==' * 20)
                print('     ACESSO NEGADO!!    ')
                print('==' * 20)
                if login != logEn:
                    print('    MOTIVO (1) LOGIN INCORRETO!!    ')
                    print('==' * 20)
                if senha != senEn:
                    print('    MOTIVO (2) SENHA INCORRETA!!    ')
                    print('==' * 20)
                    print("\n" * 6)
                    print("         TENTAR NOVAMENTE??   ")
                    new=str(input("  ")).lower()
                    if new =="sim":
                        logar()
                    else:
                        print('     !!ERRO AO LOGAR REINICIE O \n      SISTEMA E TENTE NOVAMENTE!!')



# pagina primaria
import os
os.system('cls')

print('\n' * 6)
print('==' * 20)
print("     PRIMEIRO ACESSO??")
acess=str(input("   ")).lower()
print('==' * 20)
print('\n' * 6)

# Registro
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
    logar()
else:
    logar()

 
