print("""
      .    _.----~~~~~~~7
          /          ~-..-~~--..--.
     .'.'.'                      `.
      .~                        \
    .'                           `.
  . (                             \
'.   )                              `.
   ' (                                 ~-.
      \                                  ~-~~7
       `.  __.._                      .'
         ~-.--~~  ~--.              /
                  ;            .-~
                  (          .~
                   `.       .'
                    ;       ;
                    `.      `      _
                     )      )    / )
                   (      _.-'  .-' .'
                   `.    (      )  /
                     7    _;    < _/
                      \  /      ~
                       \  /
                        `. __..-'
                          ~

""")

início = input("Bem Vindo a ilha do tesouro. Para que lado você quer ir? ")

if início == "esquerda":
    estágio_2 = input("Você achou dois caminhos, um para a direita, outro para a esquerda. Qual lado você escolhe agora? ")
    
    if estágio_2 == "esquerda":
        estágio_3 = input("Boa escolha. Agora você vê dois baús. Qual deles você quer abrir? O verde ou o vermelho? ")
        
        if estágio_3 == "vermelho":
            print("Você achou o tesouro!")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")