from desafio import quero_curso as qc
from time import sleep

if not qc.verificarArquivo('cadastro.txt'): #Verifica se o arquivo 'cadastro.txt' existe
    qc.criarArquivo('cadastro.txt', 'cpf;telefone;e-mail;senha') #Cria o arquivo caso o mesmo não já tenha sido criado

qc.cabeçalho(frase='SUPERMERCADO ABA')
print('''
[1] - Login Cliente
[2] - Fazer Cadastro
[3] - Login Funcionário
''')
while True:
    try:
        opção = int(input('Opção: '))
    except:
        frase = 'Digite um número inteiro válido'
        qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
        continue
    else:
        if opção < 1 or opção > 3:
            frase = 'Digite uma opção válida'
            qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
            continue
        else:
            break

if opção == 3:
    login_f = False
    while not login_f:
        qc.cabeçalho(frase='LOGIN')

        código_f = None
        while código_f is None:
            try:
                código_f = str(input('Código: ')).strip().upper()
            except:
                frase = 'Dado inválido. Tente novamente'
                qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                código_f = None
            else:
                if código_f == '':
                    frase = 'Preencha com o código de funcionário'
                    qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    código_f = None

        senha_f = None
        while senha_f is None:
            try:
                senha_f = str(input('Senha: ')).strip()
            except:
                frase = 'Dado inválido. Tente novamente'
                qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                senha_f = None
            else:
                if senha_f == '':
                    frase = 'Preencha com a senha de funcionário'
                    qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    senha_f = None

        login_f = qc.realizarLogin(pos1=0, pos2=2, login1=código_f, login2=senha_f, nome_do_arquivo='funcionários.txt')

    if login_f:
        qc.cabeçalho(frase='ÁREA DE ESTOQUE')

        continuar = True
        while continuar:
            perg = str(input('Quer ver a lista de produtos?[Sim/Não] ')).strip().upper()
            while perg not in ['SIM', 'NÃO', 'NAO']:
                frase = 'Digite SIM ou NÃO'
                qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                perg = str(input('Quer ver a lista de produtos?[Sim/Não] ')).strip().upper()
            if perg == 'SIM':
                qc.ordenarProdutos(ord_de_cód=True)
            print('-COMANDOS-')
            print('[1] - Adicionar um novo produto')
            print('[2] - Mudança no estoque')
            print('[3] - Retirar um produto')

            opção = None
            while opção is None:
                try:
                    opção = int(input('Opção De Mudança: '))
                except:
                    frase = 'Digite um número inteiro'
                    qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    opção = None
                else:
                    if opção < 1 or opção > 3:
                        frase = 'Opção não correspondente, tente novamente.'
                        qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        opção = None
                    else:
                        if opção == 1:
                            qc.adicionarProduto('produtos.txt')
                        elif opção == 2:
                            qc.mudarEstoque('produtos.txt','adicionar_estoque.txt')
                        else:
                            qc.excluirProduto('produtos.txt')

                        perg = str(input('Fim das alterações?[Sim/Não] ')).strip().upper()
                        while perg not in ['SIM', 'NÃO', 'NAO']:
                            frase = 'Digite SIM ou NÃO'
                            qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                            perg = str(input('Fim das alterações?[S/N] ')).strip().upper()
                        if perg == 'SIM':
                            print('\033[1mAlterações Concluídas\033[m')
                            continuar = False

else:

    if opção == 2:
        qc.cabeçalho(frase="CADASTRO")
        cpf = qc.pegarCPF() #A partir daqui váriaveis globais recebem o retorno das funções correspondentes
        tell = qc.pegarTelefone()
        email = qc.pegarEmail()
        senha = qc.pegarSenha() #Fim da atribuição dessas váriaveis
        qc.adicionarNoArquivo(f'{cpf};{tell};{email};{senha}', 'cadastro.txt') #Adiciona no arquivo 'cadastro.txt' os dados, dividos por ';'.
        print('-- Cadastro Finalizado --')
        print('    Redirecionando...')
        sleep(2)

    login = False
    while not login:
        qc.cabeçalho(frase='LOGIN')
        email_login = qc.pegarEmail(False)
        senha_login = qc.pegarSenha()
        login = qc.realizarLogin(login1=email_login, login2=senha_login, nome_do_arquivo='cadastro.txt', pos1=2, pos2=3) #Análise da correspondência do e-mail e senha com os já armazenados

    if login:  # Verifica se o login foi efetuado.
        qc.cabeçalho(frase='ÁREA DE COMPRAS')
        print('Modos de exibição:')
        print('[1] - Do mais barato ao mais caro.')
        print('[2] - Do mais caro ao mais barato.')
        print('[3] - Ordem de código dos produtos.')

        opção = None
        while opção is None:
            try:
                opção = int(input('Opção: '))
            except:
                frase = 'Digite um número inteiro'
                qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                opção = None
            else:
                if opção < 1 or opção > 3:
                    frase = 'Opção não correspondente, tente novamente.'
                    qc.cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    opção = None
                else:
                    if opção == 1:
                        qc.ordenarProdutos(crescente=True)  # Ordena do mais barato ao mais caro.
                    elif opção == 2:
                        qc.ordenarProdutos(crescente=False)  # Ordena do mais caro ao mais barato.
                    else:
                        qc.ordenarProdutos(ord_de_cód=True)  # Ordena de modo crescente com base no código.

        lista_compras = qc.compras('produtos.txt')

        cpf = 0
        with open('cadastro.txt', 'rt', encoding='utf8') as arq:
            arq.readline()
            for cadastros in arq:
                divisão_dados = cadastros.split(';')
                if email_login == divisão_dados[2] and senha_login == divisão_dados[3].replace('\n', ''):  # Verifica a linha do arquivo em que os dados estão cadastrados.
                    cpf = divisão_dados[0]  # Atribui o cpf da pessoa que está fazendo compras.
                    break

        qc.notaFiscal(lista=lista_compras, cpf=cpf, nome_do_arquivo=cpf, exibir=True)  # Exibe a nota fiscal.
        qc.notaFiscal(lista=lista_compras, cpf=cpf, nome_do_arquivo=cpf, exibir=False)  # Cria o arquivo nota fiscal.
        print('Super Mercado ABA agradece a preferência. Volte sempre!')
        print('Finalizando...')
        sleep(2)
