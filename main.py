def cadastro_de_alunos():

    alunos = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno.")
        print("2. Buscar aluno.")
        print("3. Atualizar aluno.")
        print("4. Remover aluno:")
        print("5. Lista de todos os alunos.")
        print("6. Sair.")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            matricula = input("Digite a matrícula do aluno: ")
            if matricula in alunos:
                print("Número de matrícula já cadastrado.")
            else:
                nome = input("Digite o nome do aluno: ")
                idade = input("Digite a idade do aluno: ")
                curso = input("Digite o curso: ")
                alunos[matricula] = {"nome": nome, "idade": idade, "curso": curso}
                print(f"Aluno {nome} cadastrado com sucesso!")

        elif opcao == "2":
            matricula = input("Digite o número de matrícula do aluno que deseja buscar: ")
            if matricula in alunos:
                print(f"Dados do Aluno - Matrícula: {matricula}")
                print(f"Nome: {alunos[matricula]['nome']}")
                print(f"Idade: {alunos[matricula]['idade']}")
                print(f"Curso: {alunos[matricula]['curso']}")
            else:
                print("Aluno não encontrado!")

        elif opcao == "3":
            matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")
            if matricula in alunos:
                print("O que você deseja atualizar?")
                print("1. Nome")
                print("2. Idade")
                print("3. Curso")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    novo_nome = input("Digite o novo nome: ")
                    alunos[matricula]['nome'] = novo_nome
                elif escolha == "2":
                    nova_idade = int(input("Digite a nova idade: "))
                    alunos[matricula]['idade'] = nova_idade
                elif escolha == "3":
                    novo_curso = input("Digite o novo curso: ")
                    alunos[matricula]['curso'] = novo_curso
                else:
                    print("Opção inválida.")
                print("Dados do aluno atualizados com sucesso!")
            else:
                print("Aluno não encontrado!")

        elif opcao == "4":
            matricula = input("Digite a matrícula do aluno que deseja remover: ")
            if matricula in alunos:
                del alunos[matricula]
                print(f"Aluno de matrícula {matricula} removido com sucesso!")
            else:
                print("Aluno não encontrado!")

        elif opcao == "5":
            if alunos:
                print("\nLista de todos os alunos cadastrados:")
                for matricula, dados in alunos.items():
                    print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Idade: {dados['idade']}, Curso: {dados['curso']}")

            else:
                print("Nenhum aluno encontrado")

        elif opcao == "6":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

cadastro_de_alunos()