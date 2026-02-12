import os 

restaurantes = [{'nome':'bololo', 'categoria': 'mexicana', 'ativo': False},
                {'nome': 'pizzahut', 'categoria': 'italiana', 'ativo':True},
                {'nome':'MAC', 'categoria': 'hamburguer', 'ativo': False}]

def exibir_nome_do_programa():

    print('Sabor Express\n')
def exibir_opcoes():

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
        os.system('cls')
        print('finalizando app')

def opcao_invalida():
       print('opcao invalida!\n')
       input('digite uma tecla para voltar ao menu principal')
       main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes\n')
    nome_do_restaurante=input("digite o nome do restaurante que deseja cadastrar:  ")
    categoria = input(f'digite o nome da categoria do restaurante {nome_do_restaurante}:  ')
    dados_do_restaurantes = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurantes)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('digite uma tecla para voltar ao menu principal')
    main()

def listar_restaurantes():
      os.system('cls')
      print('listando os restaurantes\n')

      print(f'{'restaurantes'.ljust(17)} | {'categoria'.ljust(14)} | status\n')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante ['ativo'] else "desativado"
            print(f'- {nome_restaurante.ljust(15)} | {categoria.ljust(15)}| {ativo.ljust(15)}\n')
      input('digite uma tecla para voltar ao menu principal\n')
      main()


def alternar_estado_restaurante():
        os.system('cls')
        print('alterando estado do restaurante\n')
        nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado: ')
        restaurante_encontrado = False
        for restaurante in restaurantes:
                if nome_restaurante == restaurante['nome']:
                        restaurante_encontrado = True
                        restaurante['ativo'] = not restaurante['ativo']
                        if restaurante['ativo']:
                                mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso!'
                        else:
                                mensagem = f'o restaurante {nome_restaurante} foi desativado com sucesso!'
                        print(mensagem)
                        break
        if not restaurante_encontrado:
                print('o restaurante não foi encontrado!')

        input('digite uma tecla para voltar ao menu principal')
        main()


def escolher_opcao():
    try:
        opção_escolhida= int(input('escolha uma opção:'))
            
        if opção_escolhida ==1:
                cadastrar_novo_restaurante()
        elif opção_escolhida==2:
                listar_restaurantes()
        elif opção_escolhida==3:
                alternar_estado_restaurante()
        elif opção_escolhida == 4:
                finalizar_app()
        else:
                opcao_invalida()
    except:
          opcao_invalida()

def main():
       os.system('cls')
       exibir_nome_do_programa()
       exibir_opcoes()
       escolher_opcao()


if __name__=='__main__':
        main()