nome_de_usuário= input("digite um nome de usuário:")
senha = input("digite uma senha:")
while nome_de_usuário == senha or nome_de_usuário in senha:
   senha= input("não insira seu nome de usuário em sua senha. tente outra combinação")