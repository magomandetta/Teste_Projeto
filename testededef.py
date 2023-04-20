def validar_a_medida_do_lado(mensagem):

    print("Programa para calcular a area de um quadrado")
    while True:
        try:
            lado = float(input(mensagem))

            if lado <= 0:
                print("A medida de um dos lados não pode ser menor ou igual a zero! Tente novamente.")
                continue
            return lado
        except ValueError:
            print("O lado desejado deve ser descrito de forma numérica! Tente Novamente")

fecharPrograma = True 
while fecharPrograma:
#while fecharPrograma == False: erro que eu nao entendi
    try:
        ladoQuadrado = validar_a_medida_do_lado("Digite aqui um dos lados do Quadrado: ")

        print("A area do quadrado descrito equivale a", ladoQuadrado*ladoQuadrado,"m2")
        fecharPrograma = False
    
    except ValueError:
        print("\nOpção Inválida! Tente Novamente")

    repeticaoPrograma = True
    while repeticaoPrograma:
            
        try:
            repProgr=input("\nDeseja realizar uma nova pesquisa?\n"
                            "1-Sim"
                            "2-Não")
        

            if repProgr == "1":
                repeticaoPrograma = False
                fecharPrograma = True


            elif repProgr == "2":
                print("Obrigado por usar esse programa :D")
                repProgr = False
                fecharPrograma = False
                break

        except ValueError:
            print("Opção Inválida! Tente novamente.")



