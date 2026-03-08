cadastros = []
continuar = True
# A lista "cadastros" vai armazenar todas as pessoas cadastradas
# O uso do "True" faz com que esse laço fique em loop até que a variável "continuar" se torne "False"


while continuar:
    acao = int(input(
        "\n=== SISTEMA DE CADASTRO ===\n"
        "1 - Cadastrar pessoa\n"
        "2 - Listar cadastros\n"
        "3 - Buscar pessoa pelo nome\n"
        "4 - Remover cadastro\n"
        "5 - Encerrar programa\n"
        "Sua escolha: "
    ))
# Definimos a variável "acao" para que a escolha do usuário determine qual operação será realizada
# O comando "input" permite a interação com o usuário, enquanto o "int" limita a resposta a números inteiros


    if acao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cidade = input("Digite a cidade: ")

        pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }
# As variáveis "nome", "idade" e "cidade" armazenam os dados digitados pelo usuário
# O dicionário "pessoa" organiza essas informações de forma mais clara

        cadastros.append(pessoa)
        print("Pessoa cadastrada com sucesso!")
# O comando ".append()" adiciona o dicionário "pessoa" dentro da lista "cadastros"
# Assim, cada novo cadastro fica salvo no sistema


    elif acao == 2:
        if len(cadastros) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("\n=== LISTA DE CADASTROS ===")
            for i in range(len(cadastros)):
                print(
                    f"{i + 1}. Nome: {cadastros[i]['nome']} | "
                    f"Idade: {cadastros[i]['idade']} | "
                    f"Cidade: {cadastros[i]['cidade']}"
                )
# O comando "len()" verifica quantos itens existem na lista
# Se não houver nenhum cadastro, o programa avisa isso ao usuário
# Caso existam pessoas cadastradas, o "for" percorre toda a lista e mostra os dados de cada pessoa


    elif acao == 3:
        nome_busca = input("Digite o nome da pessoa que deseja buscar: ").lower()
        encontrado = False
# A variável "nome_busca" armazena o nome que o usuário quer procurar
# O ".lower()" transforma tudo em minúsculo para facilitar a comparação
# A variável "encontrado" serve para verificar se a pessoa foi localizada ou não

        for pessoa in cadastros:
            if pessoa["nome"].lower() == nome_busca:
                print(
                    f"Pessoa encontrada: Nome: {pessoa['nome']} | "
                    f"Idade: {pessoa['idade']} | "
                    f"Cidade: {pessoa['cidade']}"
                )
                encontrado = True
# O comando "for" percorre cada cadastro dentro da lista
# Se o nome digitado for igual ao nome armazenado, os dados da pessoa são exibidos
# Quando a pessoa é encontrada, a variável "encontrado" se torna "True"

        if encontrado == False:
            print("Pessoa não encontrada.")
# Esse bloco funciona como tratamento caso nenhum cadastro com esse nome exista


    elif acao == 4:
        nome_remover = input("Digite o nome da pessoa que deseja remover: ").lower()
        removido = False
# A variável "nome_remover" armazena o nome da pessoa que o usuário quer excluir
# A variável "removido" verifica se algum cadastro foi apagado

        for pessoa in cadastros:
            if pessoa["nome"].lower() == nome_remover:
                cadastros.remove(pessoa)
                print("Cadastro removido com sucesso!")
                removido = True
                break
# O comando ".remove()" remove a pessoa encontrada da lista
# O comando "break" encerra o loop assim que o cadastro é removido

        if removido == False:
            print("Pessoa não encontrada.")
# Esse bloco informa ao usuário caso o nome digitado não exista na lista


    elif acao == 5:
        continuar = False
# Caso o usuário escolha a opção 5, a variável "continuar" se torna "False"
# Isso encerra o loop e finaliza o programa


    else:
        print("Opção inválida! Tente novamente.")
# O comando "else" nesse caso funciona como tratamento de erro
# Se o usuário digitar uma opção que não existe no menu, o programa avisa

print("\nPrograma encerrado.")
# Quando o loop termina, essa mensagem final é exibida

# Projeto simples de sistema de cadastro em Python
# Feito por Arthur Costa