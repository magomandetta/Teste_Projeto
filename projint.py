inicio = float(input("Escolha uma das opções abaixo: \n" + 
                "1 - Avaliar qualidade do ar\n" +
                "2 - Fechar o programa\n"))

while inicio == 1:
    mp10 = float(input("Digite a concentração medida de MP₁₀(µg/m³)" +
    "coletada nas últimas 24 horas: \n"))
    indiceInicial = 0
    indiceFinal = 0
    concentracaoInicial = 0
    concentracaoFinal = 0
    indiceTotal = 0
    
    if mp10 >= 0 and mp10 <= 50:
        indiceInicial = 0
        indiceFinal = 50
        concentracaoInicial = 0
        concentracaoFinal = 50
        
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp10 > 50 and mp10 <= 150:
        indiceInicial = 51
        indiceFinal = 100
        concentracaoInicial = 50
        concentracaoFinal = 150
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp10 > 150 and mp10 <= 200:
        indiceInicial = 101
        indiceFinal = 150
        concentracaoInicial = 150
        concentracaoFinal = 200
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp10 > 200 and mp10 < 250:
        indiceInicial = 151
        indiceFinal = 199
        concentracaoInicial = 200
        concentracaoFinal = 250
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp10 >= 250 and mp10 <= 350:
        indiceInicial = 200
        indiceFinal = 250
        concentracaoInicial = 250
        concentracaoFinal = 350
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    

    
    mp2e5 = float(input("Digite a concentração medida de MP₂,₅(µg/m³)" +
    "coletada nas últimas 24 horas: \n"))
    
    if mp2e5 >= 0 and mp2e5 <= 40:
        indiceInicial = 0
        indiceFinal = 40
        concentracaoInicial = 0 
        concentracaoFinal = 25
            
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp2e5 > 40 and mp2e5 <= 80:
        indiceInicial = 41
        indiceFinal = 80
        concentracaoInicial = 26
        concentracaoFinal = 50
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp2e5 > 80 and mp2e5 <= 120:
        indiceInicial = 81
        indiceFinal = 120
        concentracaoInicial = 51
        concentracaoFinal = 75
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp2e5 > 120 and mp2e5 < 200:
        indiceInicial = 121
        indiceFinal = 200
        concentracaoInicial = 76
        concentracaoFinal = 125
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif mp2e5 > 200:
        indiceInicial = 251
        #indiceFinal = ?
        concentracaoInicial = 126
        #concentracaoFinal = ?
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    
    o3 = float(input("Digite a concentração medida de O₃(µg/m³)" +
    "coletada nas últimas 8 horas: \n"))
    
    if o3 >= 0 and o3 <= 40:
        indiceInicial = 0
        indiceFinal = 40
        concentracaoInicial = 0 
        concentracaoFinal = 100
        
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif o3 > 40 and o3 <= 80:
        indiceInicial = 41
        indiceFinal = 80
        concentracaoInicial = 101
        concentracaoFinal = 130
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif o3 > 80 and o3 <= 120:
        indiceInicial = 81
        indiceFinal = 120
        concentracaoInicial = 131
        concentracaoFinal = 160
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif o3 > 120 and o3 < 200:
        indiceInicial = 121
        indiceFinal = 200
        concentracaoInicial = 161
        concentracaoFinal = 200
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif o3 >200:
        indiceInicial = 251
        #indiceFinal = ?
        concentracaoInicial = 201
        #concentracaoFinal = ?
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    co = float(input("Digite a concentração medida de CO(µg/m³)" +
    "coletada nas últimas 8 horas: \n"))
    
    if co >= 0 and co <= 40:
        indiceInicial = 0
        indiceFinal = 40
        concentracaoInicial = 0 
        concentracaoFinal = 9
        
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif co > 40 and co <= 80:
        indiceInicial = 41
        indiceFinal = 80
        concentracaoInicial = 10
        concentracaoFinal = 11
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif co > 80 and co <= 120:
        indiceInicial = 81
        indiceFinal = 120
        concentracaoInicial = 12
        concentracaoFinal = 13
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif co > 120 and co < 200:
        indiceInicial = 121
        indiceFinal = 200
        concentracaoInicial = 14
        concentracaoFinal = 15
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif co >200:
        indiceInicial = 251
        #indiceFinal = ?
        concentracaoInicial = 16
        #concentracaoFinal = ?
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    no2 = float(input("Digite a concentração medida de NO₂(µg/m³)" +
    "coletada na última 1 hora: \n"))
    
    if no2 >= 0 and no2 <= 40:
        indiceInicial = 0
        indiceFinal = 40
        concentracaoInicial = 0 
        concentracaoFinal = 200
        
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif no2 > 40 and no2 <= 80:
        indiceInicial = 41
        indiceFinal = 80
        concentracaoInicial = 201
        concentracaoFinal = 240
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif no2 > 80 and no2 <= 120:
        indiceInicial = 81
        indiceFinal = 120
        concentracaoInicial = 241
        concentracaoFinal = 320
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif no2 > 120 and no2 < 200:
        indiceInicial = 121
        indiceFinal = 200
        concentracaoInicial = 321
        concentracaoFinal = 1130
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif no2 > 200:
        indiceInicial = 251
        #indiceFinal = ?
        concentracaoInicial = 1131
        #concentracaoFinal = ?
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    so2 = float(input("Digite a concentração medida de SO₂(µg/m³)" +
    "coletada nas últimas 24 horas: \n"))
    
    if so2 >= 0 and so2 <= 40:
        indiceInicial = 0
        indiceFinal = 40
        concentracaoInicial = 0 
        concentracaoFinal = 20
        
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif so2 > 40 and so2 <= 80:
        indiceInicial = 41
        indiceFinal = 80
        concentracaoInicial = 21
        concentracaoFinal = 40
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif so2 > 80 and so2 <= 120:
        indiceInicial = 81
        indiceFinal = 120
        concentracaoInicial = 41
        concentracaoFinal = 365
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif so2 > 120 and so2 < 200:
        indiceInicial = 121
        indiceFinal = 200
        concentracaoInicial = 366
        concentracaoFinal = 800
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
    
    elif so2 > 200:
        indiceInicial = 251
        #indiceFinal = ?
        concentracaoInicial = 801
        #concentracaoFinal = ?
    
        indiceTotal = indiceInicial + ((indiceFinal - indiceInicial) /
        (concentracaoFinal - concentracaoInicial)) * (mp10 - concentracaoInicial)
    
        
        print("Índice total do mp10: ", indiceTotal)
        
    inicio = float(input("Deseja continuar avaliando a qualidade do ar? \n" + 
                "1 - Sim\n" +
                "2 - Não\n"))

print("Obrigado por usar nosso avaliador de qualidade do ar!")