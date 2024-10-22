#     LOGIN

login = []
senha = []
tent = 0
valid = False
# tlog=True

def log(acess):
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
    
else:
 while valid == False:
    tent
    if acess != "sim":
        # acessar
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
            valid = True
            break
        else:
            tent = tent + 1


            # ERRO

    if tent==3:
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
                    print("\n" * 6)
                    print("         TENTAR NOVAMENTE??   ")
                    new=str(input("  ")).lower()
                    if new =="sim":
                        tent=0
                    else:
                        break
                    
