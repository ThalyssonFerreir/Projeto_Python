def menu():
    print('-------------------------------------- MENU --------------------------------------')
    print("\nDigite 1 para saber o que e uma vida saudavel",
    "\nDigite 2 Para saber se voce esta saudavel",
    "\nDigite 3 Para criar uma rotina de exercicios fisicos",
    "\nDigite 4 Para entender a como fazer uma dieta",
    "\nDigite 5 Para aprender a como ter animo para fazer uma dieta e exercicios fisicos",
    "\nDigite 6 Para desligar o programa")
    
print("Este programa e um menu onde pode fazer interacoes para saber, aprender, e como comecar uma vida mais saudavel")
while True:
    menu()
    
    opcao = int(input("\nDigite uma das opcoes acima: "))
    
    while opcao not in [1, 2, 3, 4, 5, 6]:
            opcao = int(input("Inválido, digite uma das opções válidas: "))

    if opcao == 6:
        print("Tchauuu")
        break

    if opcao == 1:
        print("\nVIDA SAUDAVEL:"
        "\nvida saudável é aquela em que se adota hábitos que promovem o"
        "\nbem estar físico, mental e social. Isso inclui manter uma alimentação"
        "\nbalanceada, praticar atividades físicas regularmente, dormir o suficiente,"
        "\ngerenciar o estresse, evitar comportamentos prejudiciaiscomo o uso excessivo"
        "\nde substâncias como álcool e tabaco e cuidar da saúde emocional e psicológica.")

        print("\nDigite 1 para voltar ao menu."
              "\nDigite 2 para desligar o programa.\n")
        opcao = int(input("Digite uma das opcoes acima: "))

        while opcao not in [1, 2]:
            opcao = int(input("Inválido, digite uma das opções válidas: "))

            if opcao == 1:
                break
        
            if opcao == 2:
                print("Tchauuu!")
                exit()

    if opcao == 2:
        print("\nVOCE ESTA SAUDAVEL?\n"
              "\nvou fazer 5 perguntas para voce e voce deve responder com Sim ou Nao")
        pergunta1 = str(input("\nVoce bebe pelomenos 2 litros de agua por dia? ")).lower()
        pergunta2 = str(input("\nVocê pratica exercícios físicos pelo menos 2 vezes por semana? ")).lower()
        pergunta3 = str(input("\nvocê tem uma alimentação equilibrada, evitando excesso de açúcar e alimentos ultraprocessados? ")).lower()
        pergunta4 = str(input("\nVocê dorme entre 7 e 9 horas por noite regularmente? ")).lower()
        pergunta5 = str(input("\nVocê cuida da sua saúde mental, evitando estresse excessivo e tirando tempo para lazer? ")).lower()
        numero_perguntas = 0

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
       
        for pergunta in perguntas:
            if pergunta == "sim":
                numero_perguntas += 1

        if numero_perguntas < 2:
            print("\nSua vida nao esta muito saudavel e melhor dar uma cuidada")

        if numero_perguntas >= 2 and numero_perguntas < 4:   
            print("\nVoce esta saudavel mas da para melhorar")

        if numero_perguntas >= 4:
            print("\nVoce esta muito saudavel parabenss")
            
        print("\nDigite 1 para voltar ao menu."
              "\nDigite 2 para desligar o programa.\n")
        opcao = int(input("Digite uma das opcoes acima: "))

        while opcao not in[1, 2]:
            opcao = int(input("Invalido, digite uma das opções validas: "))

            if opcao == 1:
                break

            if opcao == 2:
                print("Tchauuu")
                exit()

    if opcao == 3:
        print("\nCRIANDO UMA ROTINA DE EXERCÍCIOS FÍSICOS")

        print("\nQual é o seu objetivo principal?")
        print("\nDigite 1 para ganhar massa muscular")
        print("Digite 2 para perder peso")
        print("Digite 3 para melhorar o condicionamento físico")
        print("Digite 4 para bem-estar geral")

        opcao = int(input("\nDigite o numero do tipo de treino que voce quiser criar: "))
        
        while opcao not in [1, 2, 3, 4]: 
            opcao = int(input("Invalido, digite uma das opções validas: "))
            
        dias = int(input("\nquantos dia da semana você pode treinar? "))
        while dias > 7 or dias < 0:  
            print("\nEscolha um número entre 0 e 7.")
            dias = int(input("Quantos dias da semana você pode treinar? "))

        print("\nAqui está sua sugestão de rotina:")

        if dias > 1 and dias <8:
            dias = [dias,"dias por semana,"]

        elif dias == 1:
            dias = [dias,"dia por semana,"]
            
        else:
            dias = str
            dias = ["quando der,"]

        if opcao == 1:
            print("\nTreine pelo menos", *dias,"focando em exercícios de força como musculação."
            "\nExemplo de divisão de treino:"
            "\n- Segunda: Peitos e tríceps"
            "\n- Terça: Costas e bíceps"
            "\n- Quarta: Pernas e abdômen"
            "\n- Quinta: Descanso ou cardio leve"
            "\n- Sexta: Ombros e braços")

        if opcao == 2:  
            print("\nPara perder peso, faça exercícios aeróbicos pelo menos", *dias,"combinados com musculação."
            "\nSugestão:"
            "\n- Terça: HIIT ou ciclismo + treino de braços"
            "\n- Quarta: Yoga ou alongamento ativo"
            "\n- Quinta: Pular corda ou natação + treino de abdômen"
            "\n- Sexta: Subida de escada ou dança + treino funcional")

        if opcao == 3: 
            print("\nPara melhorar o condicionamento, pratique atividades variadas", *dias,""
            "\nSugestão:"
            "\n- Segunda: Corrida ou bicicleta"
            "\n- Terça: Treino funcional ou musculação"
            "\n- Quarta: Natação ou yoga"
            "\n- Quinta: HIIT ou esportes coletivos"
            "\n- Sexta: Exercícios de resistência, como escadas ou circuitos")

        if opcao == 4:
            print("\nPara bem-estar, o ideal é manter-se ativo ao menos", *dias ,"dias por semana com atividades leves e prazerosas."
            "\nSugestão:"
            "\n- Caminhada ou dança"
            "\n- Yoga ou pilates"
            "\n- Exercícios de alongamento"
            "\n- Passeios ao ar livre")

        print("\nDigite 1 para voltar ao menu."
              "\nDigite 2 para desligar o programa.\n")
        opcao = int(input("Digite uma das opcoes acima: "))
        
        while opcao not in [1, 2]:
            opcao = int(input("Inválido, digite uma das opções válidas: "))

            if opcao == 1:
                break
        
            if opcao == 2:
                print("Tchauuu!")
                exit()
    
    if opcao == 4:
        print("\nENTENDENDO E CRIANDO UMA DIETA")
        
        print("Uma dieta é o conjunto de alimentos e bebidas que uma pessoa consome regularmente."
              "\nO termo pode ser usado de forma ampla, referindo-se a qualquer tipo de padrão" 
              "\nalimentar, mas também é comumente associado a um"
              "\nplano específico de alimentação com o objetivo de atingir metas como perda de peso, ganho de massa muscular, melhora da saúde, ou até para manter um peso saudável."
              "\nDieta não é só sobre o que você come, mas também sobre como você come." 
              "\nPode envolver controle das porções, qualidade nutricional dos alimentos"
              "\ncomo proteínas, carboidratos, gorduras e fibras, além de regular a ingestão calórica para atender a "
              "\nobjetivos específicos.")
        
        print("\nAgora que voce sabe o que e uma dieta hora de voce criar o seu tipo de dieta")
        
        print("\nDigite 1 para criar uma dieta sobre melhora do sistema digestivo"
              "\nDigite 2 para criar uma dieta sobre controle de diabetes"
              "\nDigite 3 para criar uma dieta sobre aumento de massa muscular"
              "\nDigite 4 para criar uma dieta sobre controle de colesterol"
              "\nDigite 5 para criar uma dieta sobre saude mental e bem-star"
              "\nDigite 6 para criar uma dieta sobre perda de peso")
        
        opcao = int(input("\nDigite uma das opcoes acima: "))
        
        while opcao not in [1, 2, 3, 4, 5, 6]:
            opcao = int(input("Invalido, Digite uma das opcoes validas: "))
        
        print("\nAqui está sua sugestão de cardápio semanal:")

        if opcao == 1:
            print("\nSegunda:" 
            "\nMerenda: Mamão com aveia, chá de hortelã"
            "\nAlmoço: Arroz integral com frango grelhado, legumes cozidos"
            "\nJantar: Peixe grelhado com batata-doce, salada de folhas verdes\n"
          
            "\nTerça:" 
            "\nMerenda: Iogurte natural com chia"
            "\nAlmoço: Quinoa com salada de folhas e filé de tilápia grelhado"
            "\nJantar: Sopa de legumes com peito de frango desfiado\n"
          
            "\nQuarta:" 
            "\nMerenda: Suco de laranja natural, amêndoas"
            "\nAlmoço: Feijão preto com carne magra e arroz integral"
            "\nJantar: Peixe assado com purê de abóbora e vegetais assados\n"
          
            "\nQuinta:" 
            "\nMerenda: Mingau de aveia com banana, chá de erva-doce"
            "\nAlmoço: Arroz integral com frango grelhado e legumes no vapor"
            "\nJantar: Omelete de espinafre com queijo branco, salada de pepino\n"
          
            "\nSexta:" 
            "\nMerenda: Panqueca de banana com mel"
            "\nAlmoço: Peixe grelhado com arroz integral e brócolis"
            "\nJantar: Sopa de legumes com carne magra\n"
          
            "\nSábado:" 
            "\nMerenda: Vitamina de frutas com linhaça"
            "\nAlmoço: Carne magra com batata-doce, vegetais cozidos"
            "\nJantar: Frango grelhado com arroz integral, legumes sauté\n"
          
            "\nDomingo:" 
            "\nMerenda: Pão integral com requeijão light"
            "\nAlmoço: Peixe grelhado com quinoa, salada de rúcula"
            "\nJantar: Omelete com cogumelos e abobrinha assada\n")
          
        if opcao == 2:
            print("\nSegunda:" 
            "\nMerenda: Pão integral com queijo cottage"
            "\nAlmoço: Filé de frango grelhado com arroz integral, salada de pepino"
            "\nJantar: Sopa de abóbora com peito de frango desfiado\n"
          
            "\nTerça:" 
            "\nMerenda: Omelete com tomate e cebola"
            "\nAlmoço: Arroz integral com peixe grelhado e legumes no vapor"
            "\nJantar: Frango desfiado com quinoa, salada de folhas verdes\n"
          
            "\nQuarta:" 
            "\nMerenda: Iogurte natural com granola"
            "\nAlmoço: Feijão preto com carne magra e arroz integral"
            "\nJantar: Peixe assado com batata-doce, salada de rúcula\n"
          
            "\nQuinta:" 
            "\nMerenda: Vitamina de abacate"
            "\nAlmoço: Arroz integral com frango grelhado, vegetais assados"
            "\nJantar: Sopa de legumes com carne magra\n"
          
            "\nSexta:" 
            "\nMerenda: Mingau de aveia com frutas vermelhas"
            "\nAlmoço: Peixe grelhado com quinoa, legumes cozidos"
            "\nJantar: Omelete de espinafre com queijo branco\n"
          
            "\nSábado:" 
            "\nMerenda: Panqueca de aveia"
            "\nAlmoço: Carne magra com arroz integral, legumes no vapor"
            "\nJantar: Frango grelhado com salada de folhas e pepino\n"
          
            "\nDomingo:" 
            "\nMerenda: Iogurte com granola"
            "\nAlmoço: Peixe grelhado com arroz integral, brócolis"
            "\nJantar: Omelete de cogumelos e espinafre\n")

        if opcao == 3:
            print("\nSegunda:"
            "\nMerenda: Mamão com aveia"
            "\nAlmoço: Arroz integral com frango"
            "\nJantar: Chá de hortelã\n"
          
            "\nTerça:"
            "\nMerenda: Iogurte natural com chia"
            "\nAlmoço: Peixe grelhado com batata-doce"
            "\nJantar: Salada de folhas verdes\n"
          
            "\nQuarta:"
            "\nMerenda: Suco de laranja natural"
            "\nAlmoço: Omelete com queijo branco"
            "\nJantar: Chá de camomila\n"
          
            "\nQuinta:"
            "\nMerenda: Mingau de aveia com banana"
            "\nAlmoço: Quinoa com legumes"
            "\nJantar: Chá de erva-doce\n"
          
            "\nSexta:"
            "\nMerenda: Panqueca de banana"
            "\nAlmoço: Frango grelhado com arroz integral"
            "\nJantar: Iogurte probiótico\n"
          
            "\nSábado:"
            "\nMerenda: Vitamina de frutas com linhaça"
            "\nAlmoço: Carne magra com legumes"
            "\nJantar: Chá digestivo\n"
          
            "\nDomingo:"
            "\nMerenda: Pão integral com requeijão light"
            "\nAlmoço: Peixe grelhado com arroz integral"
            "\nJantar: Salada de folhas\n")

        if opcao == 4:
            print("\nSegunda:"
            "\nMerenda: Mingau de aveia com chia"
            "\nAlmoço: Peixe grelhado com arroz integral, castanhas"
            "\nJantar: Peito de frango com quinoa e salada de pepino\n"
          
            "\nTerça:"
            "\nMerenda: Iogurte com linhaça"
            "\nAlmoço: Filé de tilápia com batata-doce"
            "\nJantar: Salada de folhas verdes\n"
          
            "\nQuarta:"
            "\nMerenda: Vitamina de abacate"
            "\nAlmoço: Peixe assado com batata-doce"
            "\nJantar: Salada de folhas\n"
          
            "\nQuinta:"
            "\nMerenda: Pão integral com azeite de oliva"
            "\nAlmoço: Filé de frango com purê de abóbora"
            "\nJantar: Chá de hortelã, sopa de abóbora com filé de frango\n"
          
            "\nSexta:"
            "\nMerenda: Omelete com espinafre"
            "\nAlmoço: Carne magra com legumes, arroz integral"
            "\nJantar: Peixe grelhado com arroz integral\n"
          
            "\nSábado:"
            "\nMerenda: Panqueca de aveia"
            "\nAlmoço: Carne magra com batata-doce, arroz integral"
            "\nJantar: Sopa de legumes com carne magra\n"
          
            "\nDomingo:"
            "\nMerenda: Iogurte com granola"
            "\nAlmoço: Frango grelhado com arroz integral e legumes"
            "\nJantar: Salada de folhas verdes com filé de tilápia grelhado\n")

        if opcao == 5:
            print("\nSegunda:"
            "\nMerenda: Panqueca de banana com mel"
            "\nAlmoço: Peixe grelhado com batata-doce"
            "\nJantar: Chocolate amargo, salmão com legumes, chá de camomila\n"
          
            "\nTerça:"
            "\nMerenda: Vitamina de abacate"
            "\nAlmoço: Frango grelhado com arroz integral"
            "\nJantar: Sopa de legumes com peito de frango desfiado\n"
          
            "\nQuarta:"
            "\nMerenda: Mingau de aveia com canela"
            "\nAlmoço: Salmão com legumes"
            "\nJantar: Nozes e amêndoas, omelete de cogumelos\n"
          
            "\nQuinta:"
            "\nMerenda: Omelete de cogumelos"
            "\nAlmoço: Filé de frango com purê de batata"
            "\nJantar: Chá de erva-cidreira, iogurte com granola, carne magra com arroz integral\n"
          
            "\nSexta:"
            "\nMerenda: Iogurte com granola"
            "\nAlmoço: Carne magra com arroz integral e legumes"
            "\nJantar: Chocolate 70 porcento cacau, peixe grelhado com arroz integral\n"
          
            "\nSábado:"
            "\nMerenda: Tapioca com queijo branco"
            "\nAlmoço: Peixe grelhado com arroz integral e salada"
            "\nJantar: Chá relaxante, omelete de cogumelos e espinafre\n"
          
            "\nDomingo:"
            "\nMerenda: Mingau de aveia com frutas vermelhas"
            "\nAlmoço: Frango grelhado com legumes e quinoa"
            "\nJantar: Mix de castanhas, salada de folhas verdes com filé de tilápia\n")

        if opcao == 6:
            print("\nSegunda:"
            "\nMerenda: Omelete com espinafre"
            "\nAlmoço: Peito de frango com salada de folhas"
            "\nJantar: Chá verde, peixe grelhado com batata-doce e legumes no vapor\n"
          
            "\nTerça:"
            "\nMerenda: Iogurte natural com chia"
            "\nAlmoço: Filé de peixe com purê de abóbora"
            "\nJantar: Água com limão, panqueca de banana com aveia, salmão grelhado com legumes\n"
          
            "\nQuarta:"
            "\nMerenda: Panqueca de banana com aveia"
            "\nAlmoço: Peixe grelhado com legumes e arroz integral"
            "\nJantar: Omelete de espinafre, peito de frango com brócolis\n"
          
            "\nQuinta:"
            "\nMerenda: Mingau de aveia com frutas vermelhas"
            "\nAlmoço: Filé de frango com quinoa"
            "\nJantar: Chá sem açúcar, ovos mexidos com pão integral, salada de rúcula\n"
          
            "\nSexta:"
            "\nMerenda: Omelete de claras"
            "\nAlmoço: Frango desfiado com brócolis, arroz integral"
            "\nJantar: Chá de gengibre, peixe grelhado com arroz integral\n"
          
            "\nSábado:"
            "\nMerenda: Pão integral com queijo cottage"
            "\nAlmoço: Salmão grelhado com arroz integral"
            "\nJantar: Chá de hortelã, panqueca de aveia com frutas, peito de frango com quinoa\n"
          
            "\nDomingo:"
            "\nMerenda: Panqueca de aveia com frutas"
            "\nAlmoço: Frango grelhado com quinoa"
            "\nJantar: Chá verde, peixe grelhado com arroz integral e legumes assados\n")

        print("\nDigite 1 para voltar ao menu."
              "\nDigite 2 para desligar o programa.\n")

        opcao = int(input("Digite uma das opções acima: "))

        while opcao not in [1, 2]:
            opcao = int(input("Inválido, digite uma das opções válidas: "))

            if opcao == 1:
                break
        
            if opcao == 2:
                print("Tchauuu!")
                exit()
            
            
    if opcao == 5:
        print("\n--- COMO TER ÂNIMO PARA FAZER DIETA E EXERCÍCIOS ---")

        print("Qual seu maior desafio para se manter motivado?"
        "\nDigite 1 para Falta de tempo"
        "\nDigite 2 para Falta de disciplina"
        "\nDigite 3 para Não gosto de exercícios"
        "\nDigite 4 para Não consigo seguir uma alimentação saudável"
        "\nDigite 5 para Não vejo resultados rápidos e desanimo"
        "\nDigite 6 para Falta de apoio de amigos e família"
        "\nDigite 7 para Sinto preguiça ou cansaço constante")

        desafio = int(input("\nDigite o número correspondente ao seu desafio: "))

        while desafio not in [1, 2, 3, 4, 5, 6, 7]:
            desafio = int(input("Opção inválida! Escolha um número de 1 a 7: "))

        if desafio == 1:
            print("\nDicas para quem tem pouco tempo:"
                  "\nTente encaixar treinos rápidos, de 15 a 30 minutos, no seu dia."
                  "\nFaça pequenas escolhas saudáveis, como subir escadas ao invés do elevador."
                  "\nPlaneje suas refeições com antecedência para evitar escolhas ruins.")

        if desafio == 2:
            print("\nDicas para melhorar a disciplina:"
                  "\nCrie uma rotina e siga horários fixos para exercícios e alimentação."
                  "\nUse lembretes e aplicativos para acompanhar seu progresso."
                  "\nNão desista nos primeiros dias! A disciplina vem com a repetição.")

        if desafio == 3:
            print("\nDicas para quem não gosta de exercícios:"
                  "\nExperimente diferentes atividades até encontrar uma que goste."
                  "\nTente esportes, dança, ou até mesmo caminhadas ao ar livre."
                  "\nFaça exercícios ouvindo música ou assistindo algo para se distrair.")

        if desafio == 4:
            print("\nDicas para seguir uma alimentação saudável:"
                  "\nFaça substituições aos poucos, como trocar frituras por assados."
                  "\nExperimente novas receitas saudáveis que sejam saborosas."
                  "\nPermita-se comer algo que gosta de vez em quando para não desistir.")

        if desafio == 5:
            print("\nDicas para quem desanima por não ver resultados rápidos:"
                  "\nLembre-se de que mudanças levam tempo, seja paciente!"
                  "\nTire fotos e anote seu progresso para acompanhar as pequenas melhorias."
                  "\nFoque em como você se sente, e não apenas na balança.")

        if desafio == 6:
            print("\nDicas para quem não tem apoio de amigos e família:"
                  "\nProcure comunidades online ou grupos de apoio para compartilhar sua jornada."
                  "\nConverse com amigos sobre seus objetivos e tente encontrar um parceiro de treino."
                  "\nLembre-se de que essa mudança é para você e pelo seu bem-estar!")

        if desafio == 7:
            print("\nDicas para quem sente preguiça ou cansaço constante:"
                  "\nVerifique se está dormindo bem e hidratando-se adequadamente."
                  "\nComece devagar e aumente a intensidade aos poucos para evitar exaustão."
                  "\nTente criar uma playlist animada para se motivar a se mexer.")

        print("\nLembre-se: cada pequeno passo conta! O importante é continuar.")
        
        print("\nDigite 1 para voltar ao menu."
              "\nDigite 2 para desligar o programa.\n")

        opcao = int(input("Digite uma das opções acima: "))

        while opcao not in [1, 2]:
            opcao = int(input("Inválido, digite uma das opções válidas: "))

            if opcao == 1:
                break
        
            if opcao == 2:
                print("Tchauuu!")
                exit()

            