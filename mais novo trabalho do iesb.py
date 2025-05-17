#Foi chamado a biblioteca "random" a este codigo, para que gere valores aleatorios de
#verificação para os novos usuarios, ter um codigo promocional a ser inserindo ao fim da
#compra e ganhar sua primeira refeição gratis.
import random

#Um dicionário vazio que vai armazenar os dados dos clientes recem cadastrados.
clientes = {}

#Dicionario de um cardapio contendo: itens, ingredientes, produtos, preços para o freques.
#Será imprimido poteriormente  este dicionario a função 'def menu_pedidos():
cardapio = {      
    '1': {'nome': 'Pão de Queijo', 'preco': 5.00, 'ingredientes': 'Queijo, Polvilho, Sal, Óleo'},
    '2': {'nome': 'Mix de Frutas Vermelhas', 'preco': 7.00, 'ingredientes': 'Açúcar, Morango, Groselha'},
    '3': {'nome': 'Café Expresso', 'preco': 4.50, 'ingredientes': 'Café, Água'},
    '4': {'nome': 'Bolo de Cenoura', 'preco': 6.00, 'ingredientes': 'Farinha, Cenoura, Açúcar, Ovos'},
}

#Essa função exibe a tela inicial do sistema  perguntando se o usuário já é cadastrado.
#Se sim'S' ele chama a função login() . Se não'N' é chamado a função cadastro() .
def tela_inicial():
    print('=============Seja bem-vindo===============')
    print('-------------------------Caféteria--------------------------------')
    print('------------------Coffee Shops Tia Rosa---------------------')
    print(' ')
    print('É um prazer servi-lo(a)!')
    print(' ')
    while True:
        print('AO 1º CADASTRO VOCÊ TERA UMA REFEIÇÃO GRATIS')
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        print('Você já tem cadastro em nosso sistema?')
        print('Se SIM digite: "S".\nSe NÃO digite: "N".')
        resposta = input('Sua Resposta:').strip().upper()
        if resposta == 'S':
            login()
            break
        elif resposta == 'N':
            cadastro()
            break
        else:
            print("Opção inválida. Digite S para Sim ou N para Não.")

#Se a resposta ao campo "Você já tem cadastro em nosso sistema?" for S. Ele é redirecio-
#nado a esta função "def login():" para inserir seu nome, telefone e prosegui sem o direito a
#uma refeição gratis por já ser um cliente cadastrado ao "CARDAPIO def(menu_pedidos):"           
def login():
    print("\n-_-_-_-_-_Seja bem vindo de volta!_-_-_-_-_-_-")
    nome = input("Digite seu nome: ").strip()
    telefone = input("Digite seu telefone: ").strip()
    print(' ')
    print(f"Olá, {nome}! Vamos para o cardápio:")
    menu_pedidos(nome, telefone, primeira_refeicao=False)

#Se a resposta ao campo "Você já tem cadastro em nosso sistema?" for N. Ele é redirecio-
#nado a esta função "def cadastro():" para cadastrar-se no sitema da loja com seu nome e 
#número. Com o cadastro feito, é gerado um código de verificação, que mais tarde será 
#pedido para ser incerido e condecorado com uma primeira refeição gratis. 
def cadastro():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Você digitou "N". Então vamos para a área de Cadastro!')
    print('Sinta-se mais do que bem vindo a entrar a nossa Família!')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    nome = input("Digite seu nome: ").strip()
    telefone = input("Digite seu telefone: ").strip()
    codigo_verificacao = random.randint(1000, 9999)
    clientes[telefone] = {'nome': nome, 'primeira_refeicao': True, 'codigo': codigo_verificacao}
    print('_______________________________________________________________')
    print(f'Cadastro realizado com sucesso! Seu código de verificação é: {codigo_verificacao} ')
    print('Informe esse código ao finalizar o pedido para garantir sua refeição GRÁTIS!')
    print('_______________________________________________________________')
    menu_pedidos(nome, telefone, primeira_refeicao=True)

#Passando pelo campo de login com as respectivas respostas 'S' ou 'N' atendidas o usuario
#é redirecionado para está parte de CARDAPIO(def menu_pedidos) onde faz seu pedido  
#Digitando a númeração da refeição que verá na tela e podendo em seguida selecionar
#a quantidade.
def menu_pedidos(nome, telefone, primeira_refeicao):
    print(' ')
    print(f'{"CARDAPIO":*^70}')
    for codigo, item in cardapio.items():
        print(f"{codigo} - {item['nome']} - R${item['preco']:.2f} - Ingredientes: {item['ingredientes']}")
    pedido = input('Digite o código do item que deseja: ').strip()
    if pedido in cardapio:
        item_selecionado = cardapio[pedido]
        while True:
            try:
                quantidade = int(input(f"Quantos {item_selecionado['nome']} você deseja? ").strip())
                if quantidade <= 0:
                    print('Por favor, digite uma quantidade positiva.')
                    continue
                break
            except:
                print('Quantidade inválida. Digite um número.')
        total = item_selecionado['preco'] * quantidade
        if primeira_refeicao:
            verificar_codigo(telefone, total)
        else:
            print(f"\nVocê escolheu {quantidade}x {item_selecionado['nome']} por R${total:.2f}")
            print(f'Ingredientes: {item_selecionado["ingredientes"]}')
            confirmar_pedido(total)
    else:
        print('Código inválido. Tente novamente.')
        menu_pedidos(nome, telefone, primeira_refeicao)
        
#Feito o pedido. Ao usuario recem cadastrado será-lhe pedido a inserção do código promo-
#cional de sua primeira refeição. É importante digita-lo certinho!
def verificar_codigo(telefone, total):
    codigo_informado = input('Informe o código de verificação para ativar o desconto: ').strip()
    if codigo_informado == str(clientes[telefone]['codigo']):
        print(f'\nCódigo confirmado! Você ganhou a refeição grátis!')
        total = 0.0
    else:
        print('Código incorreto. O desconto não será aplicado.')
    confirmar_pedido(total)

#Caso o usuario novato digite o codigo promocinal correto aparecera apena o tempo de 
#Espara para a refeição. Caso contrario se o codigo digitado conter algum erro, assim como
#Aos veteranos será lhe imposto o valor da refeição. 
def confirmar_pedido(total):
    while True:
        resposta = input('\nDeseja confirmar o pedido? \n"S" para SIM.\n"N" para NÃO.\n').strip().upper()
        if resposta == 'S':
            print(f'Pedido confirmado! Total a pagar: R${total:.2f}')
            print('Obrigado pela preferência! Seu pedido estará pronto em 15 minutos.')
            break
        elif resposta == 'N':
            print('Pedido cancelado.')
            break
        else:
            print('Opção inválida. Digite S para Sim ou N para Não.')

tela_inicial()