# exercicio de autenticaçao basico e simples em python usando if
user = input("ingrese seu usuario ")
senha = input("ingrese sua senha ")
# condicional if para fazer a autenticação do usuario
if user == "autorizado" and senha == "senha-user":
    print(f"o usuario esta autorizado \n bem-vindo {user}")
else:
    print("por favor verifique o seus dados")
