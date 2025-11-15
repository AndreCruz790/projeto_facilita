#[I] Declaração de importação e variáveis
import time         #Importando os comandos do nicho Tempo
logo = "████████████████████████████████████████████████████████████████\n█|   __|██| __ |██|   __|█| |█| |████| |█|__   __|██| __ |██| |█\n█|  |████| |██| |█|  |████| |█| |████| |████| |████| |██| |█|_|█\n█|   _|██| |__| |█|  |████| |█| |████| |████| |████| |__| |█████\n█|__|████|_|██|_|█|_____|█|_|█|____|█|_|████|_|████|_|██|_|█|_|█\n████████████████████████████████████████████████████████████████"
intro = "• Bem-vindo ao 𝙋𝙧𝙤𝙟𝙚𝙩𝙤 𝙁𝙖𝙘𝙞𝙡𝙞𝙩𝙖!\n Conosco sua vida fica mais fácil"
                    #"logo" e "intro" armazenam a introdução do Projeto, serão impressas para o usuário quando o código for executado
verificador = False #Chave que confirma se o Cadastro foi realizado ou não
op = -1             #Chave para acessar outras opções do projeto, após o Cadastro
tempo_inicial = time.time() #Marca o tempo de duração do código

#[II] Declaração de Funções
def introducao_facilita(logo): #Declaração da Função "introducao_facilita"
  '''
  Esta função imprime a logo do projeto ("Facilita!"), e dá boas vindas ao usuário.
  '''
  if logo:                     #Se a variável "logo" tem algum dado armazenado nela
    print(logo)                #Imprimindo a variável "logo"
    return intro               #Retorna a variável "intro"

def encontra_pos_maior(lista_compras):     #Declarando a Função "encontra_pos_maior" ("pos" de posição)
  '''
  Esta função encontra a posição do maior elemento
  da lista de compras
  '''
  maior = None                             #Variável que receberá o valor do maior preço
  pos_maior = None                         #Variável que receberá a posição do maior preço
  if not lista_compras:                    #Se a lista_compras estiver vazia
    aviso = "- Lista vazia, tente novamente quando tiver algum produto na lista.\n"
    time.sleep(0.5)
    return aviso                           #Retorna a variável "aviso"
  for chave in lista_compras:              #Repetição For
    preco = lista_compras[chave][0]        #Variável que receberá um "endereço" do dicionário "lista_compras"
    if (maior is None) or (preco > maior): #Se "maior" estiver vazia, ou se o valor de "preco" for maior que o de "maior"
      maior = preco                        #"maior" recebe o valor de "preco"
      pos_maior = chave                    #"pos_maior" recebe o valor de chave
  return pos_maior                         #Retorna o maior elemento da lista

def ordenacao_selecao_maior(lista_compras):             #Declarando a Função "ordenacao_selecao_maior"
  '''
  Esta função adiciona a uma nova variável a lista de compras reordenada,
  a partir da função "encontra_pos_maior".
  '''
  lista_aux = lista_compras.copy()                      #"aux" de auxiliar, vai armazenar uma cópia da variável "lista_compras"
  lista_ord = []                                        #"ord" de ordenação, armazenará a lista reordenada
  while lista_aux:                                      #enquanto "lista_aux" tiver algum valor armazenado nela
    pos_maior = encontra_pos_maior(lista_aux)           #variável que receberá o valor retornado da função "encontra_pos_maior", usando "lista-aux" 
    lista_ord.append([pos_maior, lista_aux[pos_maior]]) #"lista_ord" receberá a posição e os outros dados do maior valor da "lista_compras"
    del lista_aux[pos_maior]                            #deletando o maior valor da "lista_compras"
  return lista_ord                                      #Retorna a lista de compras reordenada

def encontra_pos_menor(lista_compras):     #Declarando a Função "encontra_pos_menor" ("pos" de posição)
  '''
  Esta função encontra a posição do menor elemento
  da lista de compras
  '''
  menor = None                             #Variável que receberá o valor do menor preço
  pos_menor = None                         #Variável que receberá a posição do menor preço
  if not lista_compras:                    #Se a lista_compras estiver vazia
    aviso = "- Lista vazia, tente novamente quando tiver algum produto na lista.\n"
    time.sleep(0.5)                        #Pausa de 0.5 segundos (todos os "time.sleep()" são apenas para o visual do projeto)
    return aviso                           #Retorna a variável "aviso"
  for chave in lista_compras:              #Repetição For
    preco = lista_compras[chave][0]        #Variável que receberá um "endereço" do dicionário "lista_compras"
    if (menor is None) or (preco < menor): #Se "menor" estiver vazia, ou se o valor de "preco" for menor que o de "menor"
      menor = preco                        #"menor" recebe o valor de "preco"
      pos_menor = chave                    #"pos_menor" recebe o valor de chave
  return pos_menor                         #Retorna o menor elemento da lista

def ordenacao_selecao_menor(lista_compras):               #Declarando a Função "ordenacao_selecao_menor"
  '''
  Esta função adiciona a uma nova variável a lista de compras reordenada,
  a partir da função "encontra_pos_menor".
  '''
  lista_aux = lista_compras.copy()                        #"aux" de auxiliar, vai armazenar uma cópia da variável "lista_compras"
  lista_ord = []                                          #"ord" de ordenação, armazenará a lista reordenada
  while lista_aux:                                        #enquanto "lista_aux" tiver algum valor armazenado nela
    pos_menor = encontra_pos_menor(lista_aux)             #variável que receberá o valor retornado da função "encontra_pos_menor", usando "lista-aux"
    lista_ord.append(([pos_menor, lista_aux[pos_menor]])) #"lista_ord" receberá a posição e os outros dados do menor valor da "lista_compras"
    del lista_aux[pos_menor]                              #deletando o menor valor da "lista_compras"
  return (lista_ord)                                      #Retorna a lista de compras reordenada

def selecao_item(lista_compras):        #Declarando a Função "selecao_item"
  try:                                  #Tentar:
    print("Qual o item que você deseja selecionar?")
    time.sleep(0.5)
    print(lista_compras)                #Imprimindo a lista de compras atual
    item = input("> ")                  #Solicitando ao usuário qual item ele deseja consultar
    item_p = item.lower()               #Convertendo para caracteres minúsculo
    if item_p in lista_compras:         #Se o item enviado pelo usuário estiver na lista de compras:
      print(f"Preço e quantidade de {item_p}:")
      selecao = lista_compras[item_p]   #Variável que receberá os dados do item desejado
      time.sleep(1) 
      return selecao                    #Retorna ao usuário o item desejado
      print ("\n" + "=" * 80)           #Apenas para o visual do projeto, para separar as seções
    else:                               #Caso contrário
      return "- Item não encontrado!\n" #Retornar que o item não foi encontrado
      time.sleep(0.5)
      print ("\n" + "=" * 80)
  except Exception:                     #Caso o valor enviado pelo usuário não seja compatível com a variável "item"
    print("- Valor inválido, tenta novamente.\n")
    time.sleep(0.5)

def preco_atual(lista_compras):                                                       #Declarando a Função "preco_atual"
  total_atual = 0
  if not lista_compras:                                                               #Se a lista_compras estiver vazia
    aviso = "- Lista vazia, tente novamente após inserir um item á lista\n"
    time.sleep(0.5)
    return aviso                                                                      #Retorna ao usuário a variável "aviso"
  else:                                                                               #Se não:
    for item_p, (preco, quantidade) in lista_compras.items():                         #Repetição For, do nome do item, preço e quantidade, na variável "lista_compras"
      subtotal = preco * quantidade                                                   #Subtotal do item equivale ao preço multiplicado pela quantidade
      total_atual += subtotal                                                         #Total atual acumulará todos os subtotais dos itens da lista de compras
      print(f"{item_p}: R${preco:.2f}, ({quantidade}x) → Subtotal: R${subtotal:.2f}") #Imprimindo o preço, quantidade e subtotal de cada item
      time.sleep(0.3)
    print(f"\n→ Total Atual: {total_atual:.2f}")                                      #Imprimindo o total atual
    return ""                                                                         #Retorna nada ao usuário (para não retornar "None")
    time.sleep(0.5)
    print ("\n" + "=" * 80)

def calculo_compras(): #Declarando a Função "calculo_compras"
  '''
  Esta função registra as compras, podendo ser uma lista infinita ou limitada, de acordo com o valor que o usuário declarar,
   consultar a lista de compras, remover itens e consultar valor final da compra.
  É possível entender como funciona a função a partir do "Dúvidas Frequentes".
  '''
  tempo_i_calc = time.time()                                                             #Marca o tempo inicial da seção de calcular compras
  print("\n• Vamos à compras!\n")
  time.sleep(1)
  tipo = -1                                                                              #Será usado para declarar a escolha de opção do usuário
  lista_compras = {}                                                                     #Variável que armazenará todos os itens inseridos pelo usuário
  total_geral = 0                                                                        #Total Geral da compra
  while tipo != 0:
    print("Qual tipo de compra você deseja fazer?\n")
    time.sleep(1)
    print("| Compra Livre  | Compra Limitada | Dúvidas Frequentes |  Encerrar Compra |") #Informando ao usuário as opções presentes
    print("| pressione [1] |  pressione [2]  |    pressione [3]   |   pressione [0]  |")
    time.sleep(1)
    try:                                                                                 #Tentar:
      tipo = int(input("\n> "))                                                          #Solicitando o usuário a enviar qual opção ele deseja
    except Exception:                                                                    #Caso o usuário envie um valor que a variável "tipo" não armazene:
      print("- Digite apenas um dos números disponíveis.\n")                             #Informando ao usuário para enviar apenas os números disponíveis (1, 2, 3 ou 0)
      time.sleep(0.5)
      continue
    if tipo < 0 or tipo > 3:                                                             #Se o usuário enviar um número menor que 0 ou maior que 3:
      print("- Digite apenas um dos números disponíveis.\n")                             #Informando ao usuário para enviar apenas os números disponíveis (1, 2, 3 ou 0)
      time.sleep(0.5)
      continue
    if tipo == 0:                                                                        #[0] Encerrar Compra, Se o usuário enviar 0:
      tempo_f_calc = time.time()                                                         #Marca o tempo final da seção de calcular compras
      print(f"\n• Tempo de execução de cálculo total: {(tempo_f_calc - tempo_i_calc)/60:.2f} minuto(s).") #Informando ao usuário os minutos ele ficou usando a seção de Calcular Compras
      time.sleep(0.5)
      print("Compra encerrada.\n")                                                       #Informando ao usuário que a compra foi encerrada
      print ("\n" + "=" * 80)
      return ""                                                                          #Retorna vazio, para não retornar "None" para o usuário
      break                                                                              #Quebra a repetição, e aseção de Calcular Compras
                                                                      #[••] Compra Livre
    elif tipo == 1:                                                   #Se o usuário enviar 1:
      print("\n• Compra Livre, compras sem limites!")                 #Informando que não há limite de itens na compra
      time.sleep(0.5)
      escolha = -1                                                    #Variável que receberá a escolha do usuário
      while escolha != 0:                                             #Repetição While enquanto "escolha" for diferente de 0
        print("\n O que você deseja fazer agora?\n")
        time.sleep(1)
        print("| Adicionar Item à Compra | Ver Lista de Compras | Remover Item do Carrinho | Finalizar Compra |") #Informando ao usuário as opções presentes
        print("|      pressione [1]      |     pressione [2]    |      pressione [3]       |   pressione [0]  |")
        add = False                                                   #Verificará se o item foi adicionado ou não à lista
        time.sleep(1)
        try:                                                          #Tentar:
          escolha = int(input("\n> "))                                #Solicitar o usuário qual opção ele deseja acessar
        except ValueError:                                            #Caso o usuário envie um valor que a variável "escolha" não consiga armazenar
          print("- Digite apenas um dos números disponíveis.\n")      #Informando o usuário que ele insire apenas um dos números disponíveis (1, 2, 3 ou 0)
          time.sleep(0.5)
          continue
                                                                      #[•] Adicionar Item à Compra
        if escolha == 1:                                              #Se "escolha" for 1:
          while add != True:                                          #Enquanto a variável "add" for diferente de True:
            print("\nQual o item que você deseja comprar?")           
            time.sleep(0.5)
            item = input("> ")                                        #Solicitando ao usuário o nome do item
            item_p = item.lower()                                     #Convertendo o nome do item para caracteres minúsculo, para evitar erros ortográficos
            if item_p == "":                                          #Se "item_p" estiver vazio:
              print("- Erro, tente adicionar o produto novamente.\n") #Informando ao usuário para tentar adicionar o produto novamente
              time.sleep(0.5)
              continue
            preco = 0                                                 #Variável que receberá o preço do item
            try:                                                      #Tentar: (Se o nome do item não for vazio, caso contrário repitirá o 1º If infinitamente)
              print("\nQual o preço?")
              time.sleep(0.5)
              preco = float(input("> "))                              #Solicitando ao usuário o preço do item
              if preco <= 0:                                          #Se o preço enviado for menor ou igual a 0 (zero):
                print("- Erro, tente inserir o preço novamente.\n")   #Informando ao usuário para tentar enviar o preço novamente, voltando para a parte de inserir o nome
                time.sleep(0.5)
                continue
              print("\nQual a quantidade?")
              time.sleep(0.5)
              quantidade = int(input("> "))                           #Solicitando ao usuário a quantidade do item
              if quantidade <= 0:                                     #Se a quantidade enviado for menor ou igual a 0 (zero):
                print("- Erro, tente inserir a quantidade novamente.\n") #Informando ao usuário para tentar inserir a quantidade novamente, voltando para a parte de inserir o nome
                time.sleep(0.5)
                continue
            except ValueError:                                        #Caso o usuário envie um valor que não seja possível ser armazenado em uma ou mais variáveis
              print("- Erro, tente adicionar o produto novamente.\n") #Informa ao usuário que houve um erro, e para tentar adicionar o produto novamente
              time.sleep(0.5)
              continue
            lista_compras[item_p] = [preco, quantidade]               #"lista_compras" recebe a lista com o nome do item, contendo seu preço e quantidade
            print("\n• Item adicionado ao carrinho com sucesso!")     #Informando o usuário que o item foi adicionado ao carrinho
            time.sleep(0.5)
            print("Lista de Compras:\n| 'ITEM': [PREÇO, QUANTIDADE] |")
            time.sleep(0.5)
            print(lista_compras)                                      #Mostrando a lista de compras atual
            time.sleep(0.5)
            print("\n" + "=" * 80)
            add = True                                                #"add" armazena True, finalizando o While
                                                                            #[•] Ver Lista de Compras
        elif escolha == 2:                                                  #Se o usuário enviar 2:
          if not lista_compras:                                             #Se a "lista_compras" estiver vazia:
            print("- Sua lista de compras está vazia, tente novamente.\n")  #Informando ao usuário que a lista está vazia, e para tentar novamente
            time.sleep(0.5)
            continue
          print("• Lista de Compras:\n| 'ITEM': [PREÇO, QUANTIDADE] |")
          time.sleep(0.5)
          print(lista_compras)                                              #Imprimindo a lista de compras atual
          time.sleep(0.5)
          print("Gostaria ver na lista?\n")  #Perguntando o que o usuário gostaria de ver na lista, e logo em seguida mostrando as opções ao usuário
          time.sleep(1)
          print("| Ver do Mais Caro ao Mais Barato | Ver do Mais Barato ao Mais Caro | Ver Item da Lista | Ver Total Atual da Lista | Não Quero Consultar Agora |")
          print("|          pressione [1]          |           pressione [2]         |   pressione [3]   |      pressione [4]       |       pressione [0]       |")
          time.sleep(1)
          try:                               #Tentar:
            sub_escolha = int(input("\n> ")) #Solicitando o usuário a sub-escolha
            if sub_escolha == 1:             #Se o usuário enviar 1:
              print(ordenacao_selecao_maior(lista_compras)) #Será impresso a Função "ordenacao_selecao_maior", usando a variável "lista_compras"
            elif sub_escolha == 2:           #Se não, se o usuário enviar 2:
              print(ordenacao_selecao_menor(lista_compras)) #Será impresso a Função "ordenacao_selecao_menor", usando a variável "lista_compras"
            elif sub_escolha == 3:           #Se não, se o usuário enviar 3:
              print(selecao_item(lista_compras))            #Será impresso a Função "selecao_item", usando a variável "lista_compras"
            elif sub_escolha == 4:           #Se não, se o usuário enviar 4:
              print(preco_atual(lista_compras))             #Será impresso a Função "preco_atual", usando a variável "lista_compras"
            elif sub_escolha == 0:           #Se não, se o usuário enviar 0:
              continue                                      #O usuário voltará para seção da Compra Livre
            elif sub_escolha < 0 or sub_escolha > 4:                 #Se não, se o usuário enviar um número menor que 0 ou maior que 4:
              print("- Digite apenas um dos números disponíveis.\n") #Informando o usuário para enviar um dos números disponíveis (1, 2, 3, 4 ou 0)
              time.sleep(0.5)
              continue
          except ValueError:                                         #Caso o usuário envie um valor que a variável "sub_escolha" não possa armazenar
            print("- Digite apenas um dos números disponíveis.\n")   #Informando o usuário para enviar um dos números disponíveis (1, 2, 3, 4 ou 0)
            time.sleep(0.5)
                                                                           #[•] Remover Item do Carrinho
        elif escolha == 3:                                                 #Se "escolha" for 3:
          if not lista_compras:                                            #Se "lista_compra" estiver vazia:
            print("- Sua lista de compras está vazia, tente novamente.\n") #Informando o usuário que a lista está vazia, e para tentar novamente
            time.sleep(0.5)
            continue
          if lista_compras:                                                #Se "lista_compras" não estiver vazia:
            try:                                                           #Tentar:
              print("Qual o item que você deseja remover?")
              time.sleep(0.5)
              print(lista_compras)                                         #Imprimindo a lista de compras atual, para facilitar a consulta
              time.sleep(0.5)
              item = input("> ")                                           #Solicitando qual o item o usuário deseja remover da lista de compras
              item_p = item.lower()                                        #Convertendo os caractere inseridos pelo usuário para caracteres minúsculos
              if item_p in lista_compras:                                  #Se o item enviado pelo usuário estiver presente na variável "lista_compras"
                lista_compras.pop(item_p)                                  #Removendo o item que o usuário deseja, usando .pop()
                print("\n• Item removido com sucesso!\n")                  #Informando o usuário que o item foi removido da lista de compras
                time.sleep(0.5)
                print ("\n" + "=" * 80)
                continue
              else:                                                        #Se não:
                print("- Item não encontrado!\n")                         #Retornar ao usuário que o item não foi encontrado
                time.sleep(0.5)
                print ("\n" + "=" * 80)
                continue
            except Exception:                                               #Caso o usuário envie um valor que a variável "sub_escolha" não possa armazenar
              print("- Valor inválido, tenta novamente.\n")                 #Informando o usuário que o valor é inválido, e para tentar novamente
              time.sleep(0.5)
              continue
                                                                                            #[•] Finalizar Compra
        elif escolha == 0:                                                                  #Se "escolha" for 0:
          if not lista_compras:                                                             #Se "lista_compra" estiver vazia:
            return "- Sua lista de compras está vazia, a compra será reiniciada.\n• Retornando à página principal..." #Informando o usuário que a lista está vazia, e para tentar novamente
            time.sleep(0.5)
            continue
          print("- Lista de Compras:\n| 'ITEM': [PREÇO, QUANTIDADE] |")
          time.sleep(0.5)
          print(lista_compras)                                                              #Imprimindo a lista de compras final
          time.sleep(0.5)
          print("• Total da Compra:")                                                       #Mostrando o total da compra
          time.sleep(0.5)
          total_geral = 0                                                                   #Variável que receberá o valor total da compra
          for item_p, (preco, quantidade) in lista_compras.items():                         #Repetição For
            subtotal = preco * quantidade                                                   #Subtotal do item equivale ao preço multiplicado pela quantidade
            total_geral += subtotal                                                         #Total atual acumulará todos os subtotais dos itens da lista de compras 
            print(f"{item_p}: R${preco:.2f}, ({quantidade}x) → Subtotal: R${subtotal:.2f}") #Imprimindo o subtotal de cada item presente na lista de compras
            time.sleep(0.5)
          print(f"\n→ Total Geral: {total_geral:.2f}\n")                                    #Imprimindo o total da compra
          time.sleep(0.5)
          print("• Obrigado pela preferência de utilizar o nosso serviço!\n")               #Agradecendo o usuário por usar o serviço do Projeto
          time.sleep(0.5)
          tempo_f_calc = time.time()                                                        #Marca o tempo final da seção de calcular compras
          print(f"\n• Tempo de execução de cálculo total: {(tempo_f_calc - tempo_i_calc)/60:.2f} minuto(s).") #Imprimindo o tempo total de uso da funcionalidade de calcular compras
          print("\n" + "=" * 80)
          return ""                                                                         #Retornando vazio, para não retornar "None" ao usuário
          break                                                                             #Quebrando a repetição
        if escolha < 0 or escolha > 3:                                                      #Se "escolha" for menor que 0 ou maior que 3:
          print("- Digite apenas um dos números disponíveis.\n")                            #Informando o usuário a enviar apenas um dos números disponíveis (1, 2, 3 e 0)
          time.sleep(0.5)
          continue
                                                                                #[••] Compra Limitada
    elif tipo == 2:                                                             #Se o usuário enviar 2:
      print("• Vamos às compras!") 
      time.sleep(1)
      try:
        limite = None
        limite = float(input("Quantos reais você tem em mãos no momento?\n> ")) #Solicitando o usuário o valor limite da compra
      except ValueError:                                                        #Caso o usuário envie um valor que a variável "sub_escolha" não possa armazenar
        print("- Digite um valor válido, tente novamente.\n")                   #Informando para o usuário enviar um valor válido, e tentar novamente
        time.sleep(0.5)
        continue
      time.sleep(0.5)
      if limite:                                                                #Se "limite" for verdadeiro:
        print("\n• Você apenas poderá Finalizar a Compra se não ultrapassar ou ser o mesmo valor que você tem!\n") #Informando o usuário que a compra só será finalizada se não ultrapassar ou ser o mesmo valor limite inserido inicialmente
        lista_compras = {}                                                      #Declarando o dicionário
        print(f"• Compra Limitada, dá pra comprar em até R${limite:.2f}!")      #Informando que há limite de itens na compra
        time.sleep(0.5)
        escolha = -1
        while escolha != 0:                                        #Repetição While enquanto "escolha" for diferente de 0
          print("\nO que você deseja fazer agora?\n")
          time.sleep(1)
          print("| Adicionar Item à Compra | Ver Lista de Compras | Remover Item do Carrinho | Finalizar Compra |") #Informando ao usuário as opções presentes
          print("|      pressione [1]      |     pressione [2]    |      pressione [3]       |   pressione [0]  |")
          add = False                                              #Verificará se o item foi adicionado ou não à lista
          time.sleep(1)
          try:                                                     #Tentar:
            escolha = int(input("\n> "))                           #Solicitando o usuário qual das opções ele deseja
          except ValueError:                                       #Caso o usuário envie um valor que a variável "escolha" não possa armazenar
            print("- Digite apenas um dos números disponíveis.\n") #Informando o usuário que ele insire apenas um dos números disponíveis (1, 2, 3 ou 0)
            time.sleep(0.5)
            continue
          if escolha < 0 or escolha > 3:                           #Se "escolha" for menor que 0 ou maior que 3:
            print("- Digite apenas um dos números disponíveis.\n") #Informando o usuário a enviar apenas um dos números disponíveis (1, 2, 3 e 0)
            time.sleep(0.5)
            continue
                                                                        #[•] Adicionar Item à Compra
          if escolha == 1:                                              #Se "escolha" for 1:
            while add != True:                                          #Enquanto a variável "add" for diferente de True:
              print("\nQual o item que você deseja comprar?")
              time.sleep(0.5)
              item = input("> ")                                        #Solicitando ao usuário o nome do item
              item_p = item.lower()                                     #Convertendo o nome do item para caracteres minúsculo, para evitar erros ortográficos
              if item_p == "":                                          #Se "item_p" estiver vazio:
                print("- Erro, tente adicionar o produto novamente.\n") #Informando ao usuário para tentar adicionar o produto novamente
                time.sleep(0.5)
                continue
              preco = 0                                                 #Variável que receberá o preço do item
              try:                                                      #Tentar: (Se o nome do item não for vazio, caso contrário repitirá o 1º If infinitamente)
                print("\nQual o preço?")
                time.sleep(0.5)
                preco = float(input("> "))                              #Solicitando ao usuário o preço do item
                if preco <= 0:                                          #Se o preço enviado for menor ou igual a 0 (zero):
                  print("- Erro, tente inserir o preço novamente.\n")   #Informando ao usuário para tentar enviar o preço novamente, voltando para a parte de inserir o nome
                  time.sleep(0.5)
                  continue
                print("\nQual a quantidade?")
                time.sleep(0.5)
                quantidade = int(input("> "))                           #Solicitando ao usuário a quantidade do item
                if quantidade <= 0:                                     #Se a quantidade enviado for menor ou igual a 0 (zero):
                  print("- Erro, tente inserir a quantidade novamente.\n") #Informando ao usuário para tentar inserir a quantidade novamente, voltando para a parte de inserir o nome
                  time.sleep(0.5)
                  continue
              except ValueError:                                        #Caso o usuário envie um valor que não seja possível ser armazenado em uma ou mais variáveis
                print("- Erro, tente adicionar o produto novamente.\n") #Informa ao usuário que houve um erro, e para tentar adicionar o produto novamente
                time.sleep(0.5)
                continue
              lista_compras[item_p] = [preco, quantidade]               #"lista_compras" recebe a lista com o nome do item, contendo seu preço e quantidade
              print("\n• Item adicionado ao carrinho com sucesso!")     #Informando o usuário que o item foi adicionado ao carrinho
              time.sleep(0.5)
              print("Lista de Compras:\n| 'ITEM': [PREÇO, QUANTIDADE] |")
              time.sleep(0.5)
              print(lista_compras)                                      #Mostrando a lista de compras atual
              time.sleep(0.5)
              add = True                                                #"add" armazena True, finalizando o While
              print ("\n" + "=" * 80)
                                                                             #[•] Ver Lista de Compras
          elif escolha == 2:                                                 #Se o usuário enviar 2:
            if not lista_compras:                                            #Se a "lista_compras" estiver vazia:
              print("- Sua lista de compras está vazia, tente novamente.\n") #Informando ao usuário que a lista está vazia, e para tentar novamente
              time.sleep(0.5)
              continue
            print("• Lista de Compras:\n| 'ITEM': [PREÇO, QUANTIDADE] |")
            time.sleep(0.5)
            print(lista_compras)                                             #Imprimindo a lista de compras atual
            time.sleep(0.5)
            print("Gostaria ver na lista?\n") #Perguntando o que o usuário gostaria de ver na lista, e logo em seguida mostrando as opções ao usuário
            time.sleep(1)
            print("| Ver do Mais Caro ao Mais Barato | Ver do Mais Barato ao Mais Caro | Ver Item da Lista | Ver Total Atual da Lista | Não Quero Consultar Agora |")
            print("|          pressione [1]          |           pressione [2]         |   pressione [3]   |      pressione [4]       |       pressione [0]       |")
            time.sleep(1)
            try:                                                             #Tentar:
              sub_escolha = int(input("\n> "))                               #Solicitando o usuário a sub-escolha
              if sub_escolha == 1:   #Se o usuário enviar 1:
                print(ordenacao_selecao_maior(lista_compras)) #Será impresso a Função "ordenacao_selecao_maior", usando a variável "lista_compras"
              elif sub_escolha == 2: #Se não, se o usuário enviar 2:
                print(ordenacao_selecao_menor(lista_compras)) #Será impresso a Função "ordenacao_selecao_menor", usando a variável "lista_compras"
              elif sub_escolha == 3: #Se não, se o usuário enviar 3:
                print(selecao_item(lista_compras)) #Será impresso a Função "selecao_item", usando a variável "lista_compras"
              elif sub_escolha == 4: #Se não, se o usuário enviar 4:
                print(preco_atual(lista_compras)) #Será impresso a Função "preco_atual", usando a variável "lista_compras"
              elif sub_escolha == 0: #Se não, se o usuário enviar 0:
                continue                          #O usuário voltará para seção da Compra Livre
              elif sub_escolha < 0 or sub_escolha > 4:                 #Se não, se o usuário enviar um número menor que 0 ou maior que 4:
                print("- Digite apenas um dos números disponíveis.\n") #Informando o usuário para enviar um dos números disponíveis (1, 2, 3, 4 ou 0)
                time.sleep(0.5)
                continue
            except ValueError:                                         #Caso o usuário envie um valor que a variável "sub_escolha" não possa armazenar
              print("- Digite apenas um dos números disponíveis\n")    #Informando o usuário para enviar um dos números disponíveis (1, 2, 3, 4 ou 0)
              time.sleep(0.5)
                                                                             #[•] Remover Item do Carrinho
          elif escolha == 3:                                                 #Se "escolha" for 3:
            if not lista_compras:                                            #Se "lista_compra" estiver vazia:
              print("- Sua lista de compras está vazia, tente novamente.\n") #Informando o usuário que a lista está vazia, e para tentar novamente
              time.sleep(0.5)
              continue
            if lista_compras:                                                #Se "lista_compras" não estiver vazia:
              try:                                                           #Tentar:
                print("Qual o item que você deseja remover?")
                time.sleep(0.5)
                print(lista_compras)                                         #Imprimindo a lista de compras atual, para facilitar a consulta
                time.sleep(0.5)
                item = input("> ")                                           #Solicitando qual o item o usuário deseja remover da lista de compras
                item_p = item.lower()                                        #Convertendo os caractere inseridos pelo usuário para caracteres minúsculos
                if item_p in lista_compras:                                  #Se o item enviado pelo usuário estiver presente na variável "lista_compras"
                  lista_compras.pop(item_p)                                  #Removendo o item que o usuário deseja, usando .pop()
                  print("\n• Item removido com sucesso!\n")                  #Informando o usuário que o item foi removido da lista de compras
                  time.sleep(0.5)
                  print ("\n" + "=" * 80)
                  continue
                else:                                                        #Se não:
                  print("- Item não encontrado!\n")                         #Retornar ao usuário que o item não foi encontrado
                  time.sleep(0.5)
                  print ("\n" + "=" * 80)
                  continue
              except Exception:                                               #Caso o usuário envie um valor que a variável "sub_escolha" não possa armazenar
                print("- Valor inválido, tenta novamente.\n")                 #Informando o usuário que o valor é inválido, e para tentar novamente
                time.sleep(0.5)
                continue
                                                                             #[•] Finalizar Compra
          elif escolha == 0:                                                 #Se "escolha" for 0:
            if not lista_compras:                                            #Se "lista_compra" estiver vazia:
              return "- Sua lista de compras está vazia, a compra será reiniciada.\n• Retornando à página principal..." #Informando o usuário que a lista está vazia, e para tentar novamente
              time.sleep(0.5)
              continue
            print("Lista de Compras:\n| 'ITEM': [PREÇO, QUANTIDADE] |")
            time.sleep(0.5)
            print(lista_compras)                                             #Imprimindo a lista de compras final
            time.sleep(0.5)
            print("• Total da Compra:")                                      #Mostrando o total da compra
            time.sleep(0.5)
            total_geral = 0                                                  #Variável que receberá o valor total da compra
            for item_p, (preco, quantidade) in lista_compras.items():        #Repetição For
              subtotal = preco * quantidade                                  #Subtotal do item equivale ao preço multiplicado pela quantidade
              total_geral += subtotal                                        #Total atual acumulará todos os subtotais dos itens da lista de compras
              print(f"{item_p}: R${preco:.2f}, ({quantidade}x) → Subtotal: R${subtotal:.2f}") #Imprimindo o subtotal de cada item presente na lista de compras
              time.sleep(0.5) 
            if total_geral >= limite: #Se o "total_geral" armazenar um valor maior ou igual ao armazenado em "limite":
              print("- Você alcançou o limite de valor que tinha, refaça à lista de compras e tente novamente.\n") #Informando o usuário que o valor limite foi ultrapassado, e por isso a compra foi cancelada
              time.sleep(0.5)
              print(f"\n→ Total Geral: {total_geral:.2f}/{limite:.2f} ← Valor Limite\n") #Mostrando ao usuário o "total_geraç" em comparação com o "limite"
              time.sleep(0.5)
              continue
              return ""                                                           #Retornando vazio, para não retornar "None" ao usuário
            else:
              print(f"\n→ Total Geral: {total_geral:.2f}\n")                      #Imprimindo o total da compra
              time.sleep(0.5)
              print("• Obrigado pela preferência de utilizar o nosso serviço!\n") #Agradecendo o usuário por usar o serviço do Projeto
              time.sleep(0.5)
              tempo_f_calc = time.time()                                          #Marca o tempo final da seção de calcular compras
              print(f"\n• Tempo de execução de cálculo total: {(tempo_f_calc - tempo_i_calc)/60:.2f} minuto(s).") #Imprimindo o tempo total de uso da funcionalidade de calcular compras
              print("\n" + "=" * 80)
              return ""                                                           #Retornando vazio, para não retornar "None" ao usuário
              break                                                               #Quebrando a repetição
          if escolha < 0 or escolha > 3:                                          #Se "escolha" for menor que 0 ou maior que 3:
            print("- Digite apenas um dos números disponíveis.\n")                #Informando o usuário a enviar apenas um dos números disponíveis (1, 2, 3 e 0)
            time.sleep(0.5)
            continue
                    #[••] Dúvidas Frequentes
    elif tipo == 3: #Se o usuário enviar 3:
      print("======================================================================================================================================")
      print("\n• Dúvidas Frequentes!\nComo funciona?")
      print(". Compra Livre                      → Você pode por quantos itens quiser na lista, sem limite de valor total")
      print(". Compra Limitada                   → Você pode por os itens no carrinho enquanto não ultrapassar o valor limite inserido por você mesmo,")
      print("                                       se a compra for finalizada e o valor total for ultrapassado, a compra será cancelada e deverá")
      print("                                       ser feita novamente.")
      print("\n• Dentro da Compra Livre/Limitada:")
      print(" . Adicionar Item à Compra           → Você insere o nome, preço e quantidade do produto desejado.")
      print(" . Ver Lista de Compras              → Você pode ver à lista de compras os itens inseridos")
      print("   - Ver do Mais Caro ao Mais Barato → Reordena à lista de compras, do mais caro ao mais barato.")
      print("   - Ver do Mais Barato ao Mais Caro → Reordena à lista de compras, do mais barato ao mais caro.")
      print("   - Ver Item da Lista               → Você insere qual item da lista de compras você deseja consultar.")
      print("   - Ver Total Atual da Lista        → Mostra para você o total atual da lista de compras")
      print("   - Não Quero Consultar             → Você volta à página principal da Compra Livre/Limitada.")
      print(" . Remover Item do Carrinho          → Remove um item da lista de compras.")
      print(" . Finalizar Compra                  → Finaliza a compra mostrando o total geral das compras. Se estiver na Compra Limitada e o total for")
      print("                                       maior que o limite, a compra será cancelada.\n")
      print(". Encerrar Compras                  → Finaliza essa seção de Cálculo de Compras.")
      print("======================================================================================================================================")
      time.sleep(3) #Explicativo de todas as funcionalidades da seção de calcular compras para o usuário

#[III] Projeto Facilita
print(introducao_facilita(logo)) #Imprimindo a Função "introducao_facilita", usando a variável "logo"

time.sleep(1)
print("\nPara começarmos, vamos realizar o 𝙨𝙚𝙪 cadastro!")                       #Informando ao Usuário sobre o cadastro
time.sleep(1.5)
while verificador != True:                                                       #Repetição While enquanto a variável "verificador" for diferente de "True"
  nome = input("Insira o seu nome, se quiser depois você poderá alterá-lo:\n> ") #O usuário escreverá seu nome
  if len(nome) > 0:                                                              #Se o usuário não enviou vazio
    print("\n• Dados validos! Sua conta foi criada com sucesso.")                #Informando ao usuário que os dados foram válidos
    verificador = True                                                           #A variável "verificador" armazenará "True", que resultará no fim da repetição While
    print("Acesso à conta concedido.")                                           #Informará ao usuário que o acesso à conta foi concedido
  else:                                                                          #Se o If não for executado
    print("- O seu nome não pode estar vazio, tente novamente.\n")               #Informa ao usuário que o nome não pode estar vazio, ou seja, nulo
time.sleep(0.5)
print("\n" + "=" * 80)
print("\n• Vamos dar início ao Projeto!\n")                                      #Após a Função ser executada, o Projeto realmente começará

while op != 0:                                              #Repetição While enquanto a variável "op" armazenar um dado diferente de 0 (zero)
  time.sleep(1)
  print(f"O que você gostaria de acessar agora, {nome}?\n") #Demonstrando as opções de funcionalidades do Projeto ao usuário
  print("| Cálculo de Compras | Configuração do Usuário |  Sair da Conta  |")
  print("|    pressione [1]   |       pressione [2]     |  pressione [0]  |")
  time.sleep(1)
  try:                                                      #Tentar:
    op = int(input("\n> "))                                 #Solicitando o usuário o digito-chave
  except ValueError:                                        #Exceção em caso o usuário digite caracteres ou um número que não está listado nas opções
    print("- Digite apenas um dos números disponíveis\n")   #Informando que deve ser inserido apenas um dos números disponíveis (1, 2 ou 0)
    time.sleep(0.5)
  if op == 1:                #Se o usuário enviar 1:
    print(calculo_compras()) #Imprimirá a Função "calculo_compras"
  if op == 2:                #Se o usuário enviar 2:
    sub_escolha = -1
    while sub_escolha != 2:
      print("\n• Configuração do Usuário")       #[•] - Configuração do Usuário
      time.sleep(0.5)
      print("Gostaria de mudar o seu nome?\n")
      time.sleep(1)
      print("|      Sim      |      Não      |") #Demonstrando as opções de "Sim" ou "Não" ao usuário
      print("| pressione [1] | pressione [2] |")
      time.sleep(1)
      try:                                       #Tentar:
        sub_escolha = int(input("\n> "))         #Solicitando ao usuário a sub_escolha
      except ValueError:                         #Exceção em caso o usuário digite caracteres ou um número que não está listado nas opções
        print("- Digite apenas um dos números disponíveis, tente novamente.\n")
        time.sleep(0.5)
      if sub_escolha == 1:                                                      #Se o usuário enviar 1:
        nome = ""
        while nome == "":                                                       #Repetição While enquanto a variável "nome" for vazia
          nome = input("\n Qual o novo nome que você deseja?\n> ")              #Solicitando ao usuário o novo nome que ele deseja enviar
          if nome == "":                                                        #Se o nome enviado pelo usuário for vazio:
            print("- O nome não pode estar vazio, tente novamente.\n")          #Informando ao usuário que o nome não pode estar vazio
            time.sleep(0.5)
        if nome:                                                                #Se o nome enviado pelo usuário não for vazio:    
          print("\n• Nome atualizado!")                                         #Informando ao usuário que o nome foi atualizado
          time.sleep(0.5)
          print("\n• Retornando à página principal...")                         #Informando ao usuário que ele será direcionado à seção principal
          print("\n" + "=" * 80)
          break                                                                 #Saindo do While
      elif sub_escolha == 2:                                                    #Se o usuário enviar 2:
        print("\n• Retornando à página principal...")                           #Informando ao usuário que ele será direcionado à seção principal
        print("\n" + "=" * 80)
        break                                                                   #Saindo do While, e da Opção 2
  if op < 0 or op > 2:                                                      #Se o usuário enviar um número que não está listado nas opções:                 
    print("- Digite apenas um dos números disponíveis, tente novamente.\n") #Informando ao usuário enviar apenas um dos números disponíveis das opções (1 ou 2)
    time.sleep(0.5)

#Encerramento do Projeto, se o usuário enviar 0
if op == 0:
  time.sleep(0.5)
  print("_____________________\n|                   |\n|   Obrigado por    |\n|       usar o      |\n| Projeto Facilita! |\n|        ~•~        |\n|___________________|")
  tempo_final = time.time() #Tempo que o código encerrou
  time.sleep(1)
  print(f"\n> Tempo de execução do Projeto: {(tempo_final - tempo_inicial)/60:.2f} minuto(s).") #Imprimindo o tempo total de duração do código
