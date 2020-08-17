def verificarArquivo(nome_do_arquivo=''):
    '''
    --> Responsável pela verificação da existência de um arquivo.
    :param nome_do_arquivo: É passado o nome do arquivo juntamente com sua extensão.
    :return: Se o arquivo não existir, retorna False. Caso exista, retorna True.
    '''

    try:
       arq = open(nome_do_arquivo, 'rt')
       arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_do_arquivo='', primeira_linha=''):
    '''
    --> Responsável pela criação de um arquivo.
    :param nome_do_arquivo: É passado o nome do arquivo juntamente com sua extensão.
    :return: Sem retorno
    '''

    try:
       arq = open(nome_do_arquivo, 'wt+')
       arq.write(primeira_linha + '\n')
       arq.close()
    except:
        print('Não foi possível criar o arquivo')
    else:
        print(f'Arquivo "{nome_do_arquivo}" criado')


def adicionarNoArquivo(inf_para_adicionar='', nome_do_arquivo=''):
    '''
    --> Responsável por adicionar informações no arquivo.
    :param inf_para_adicionar: Informações que serão adicionadas.
    :param nome_do_arquivo: Nome do arquivo juntamente com sua extensão.
    :return: Sem retorno.
    '''
    arq = open(nome_do_arquivo, 'at')
    arq.write(inf_para_adicionar + '\n')
    arq.close()


def cabeçalho(caracter='-', frase='', cor='', tamanho=20):
    '''
    --> Cria um cabeçalho com uma frase centralizada.
    :param caracter: Caracter que formará a linha superior e inferior.
    :param frase: Frase a ser centralizada.
    :param cor: Cor que será usada.
    :param tamanho: Tamanho das linhas traçadas em cima e embaixo da frase.
    :return: Sem retorno.
    '''
    print(caracter * (len(frase) + tamanho))
    print((' ' * int(tamanho / 2)) + f'{cor}{frase}\033[m')
    print(caracter * (len(frase) + tamanho))


def pegarTelefone():
    '''
    --> Responsável por receber e padronizar visualmente o DDD e Número Telefonico.
    :return: Retorna a padronização telefonica (XX)xxxxx-xxxx.
    '''
    repetição = True
    while repetição:
        ddd = None
        while ddd is None:
            try:
                ddd = str(input('DDD: ')).strip()
            except:
                frase = 'Dado inválido'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                ddd = None
            else:
                if ddd == '':
                    frase = 'O DDD não foi preenchido. Tente novamente.'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    ddd = None
                elif len(ddd) != 2:
                    frase = 'DDD é composto por dois dígitos'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    ddd = None
                elif not ddd.isnumeric():
                    frase = 'Apenas números são válidos'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    ddd = None

        telefone = None
        while telefone is None:
            try:
                telefone = str(input('Telefone: ')).strip()
            except:
                frase = 'Dado inválido'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                telefone = None
            else:
                if not telefone.isnumeric():
                    frase = 'Digite apenas números'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    telefone = None
                elif len(telefone) != 9:
                    frase = 'O padrão telefônico é composto por 9 digitos'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    telefone = None

        ddd = f'({ddd})'#Padroniza o DDD colocando entre parentêses.
        lista = []
        for num in telefone:
            lista.append(num) #Adiciona na lista número a número como elementos separados.
        lista.insert(5, '-') #Padroniza com o hífen '-' na posição correta.
        telefone = ddd + ''.join(lista) #Atribui na váriavel a forma padronizada de DDD + Número telefonico.
        if análiseDeRepetição(telefone, 1, 'cadastro.txt') is not True: #Função para análise de repetição com números já armazenados.
            repetição = False
            return telefone
        else:
            frase = 'O Nº de Telefone passado já foi cadastrado, tente novamente'
            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
            ddd = None


def pegarCPF():
    '''
    --> Recebe a númeração do CPF e organiza utilizando pontos e hífen.
    :return: Retorna a padronização do CPF (xxx.xxx.xxx-xx).
    '''
    cpf = None
    while cpf is None:
        try:
            cpf = str(input('CPF: ')).strip()
        except:
            frase = 'Dado inválido'
            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
            cpf = None
        else:
            if cpf == '':
                frase = 'O CPF não foi preenchido. Tente Novamente.'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                cpf = None
            elif '.' in cpf or '-' in cpf:
                frase = 'Preencha somente com a numeração'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                cpf = None
            elif not cpf.isnumeric():
                frase = 'Preencha somente com a numeração'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                cpf = None
            elif len(cpf) != 11:
                frase = 'Preencha o CPF corretamente com 11 algarismos'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                cpf = None
            else:
                lista = []
                for elementos in cpf:
                    lista.append(elementos) #Insere na lista cada número passado de modo separado.
                lista.insert(3, '.') #Coloca a primeira pontução após os 3 primeiros dígitos.
                lista.insert(7, '.') #Coloca a segunda pontuação após os 6 primeiros dígitos.
                lista.insert(11, '-') #Coloca o hífen após os 9 primeiros digítos.
                cpf = ''.join(lista) #Atribui na variavel a forma padronizada.
                if análiseDeRepetição(cpf, 0, 'cadastro.txt') is True:
                    frase = 'O CPF passado já foi cadastrado, tente novamente'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    cpf = None
                else:
                    return cpf


def pegarEmail(cadastro=True):
    email = None
    while email is None:
        try:
            email = str(input('E-mail: ')).strip()
        except:
            frase = 'Dado inválido'
            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
            email = None
        else:
            if email == '':  # Verifica se o e-mail está vazio.
                frase = 'O e-mail estava vazio. Tente novamente.'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                email = None
            elif not (email.replace('@', '').replace('_', '').replace('.', '')).isalnum():
                print('~' * 80)
                print('''\033[31m\t\tO e-mail deve ser constituido por letras de A-Z e números de 0-9. 
                Além desses, somente "@", "_" e "." e sem espaços.\033[m''')
                print('~' * 80)
                email = None
            elif '@' not in email:  # Verifica se o e-mail contém '@'.
                frase = 'E-mail inválido. Tente novamente.'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                email = None
            elif '.' not in email:  # Verifica se o e-mail contém '.'.
                frase = 'E-mail inválido. Tente novamente.'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                email = None
            elif cadastro is True:  # Verifica se a função está em modo cadastro.
                if análiseDeRepetição(email, 2, 'cadastro.txt') is True:
                    frase = 'O E-mail passado já foi cadastrado, tente novamente'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    email = None
                else:
                    return email
            else:
                return email


def pegarSenha():
    senha = None
    while senha is None:
        try:
            senha = str(input('Senha: ')).strip()
        except:
            frase = 'Dado inválido'
            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
            senha = None
        else:
            if senha == '':
                frase = 'A senha estava vazia, tente novamente.'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                senha = None
            elif len(senha) < 7:
                frase = 'A senha deve ter no mínimo 7 digitos'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                senha = None
            elif not senha.isalnum():
                frase = 'A senha só pode conter números e letras'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                senha = None
            else:
                return senha


def análiseDeRepetição(informação, posição, nome_do_arquivo=''):
    '''
    ->Faz uma análise da informação passa com as já cadastradas para verificar repetições.
    :param informação: A informação que será analisada.
    :param posição: A posição no arquivo que está o conjunto de dados do mesmo tipo.
    :param nome_do_arquivo: Nome do arquivo.txt a ser aberto.
    :return: Retorna False para caso o arquivo esteja vazio ou não haja repetição. Retorna True caso haja repetição.
    '''
    arq = open(nome_do_arquivo, 'rt')
    arq.readline()
    for linhas in arq:
        if linhas == '':
            arq.close()
            return False
        if informação == linhas.split(';')[posição]: #Comparação da informação com a coluna especificada de dados do arquivo.
            arq.close()
            return True
        else:
            arq.close()
            return False


def realizarLogin(pos1, pos2, login1='', login2='', nome_do_arquivo=''):
    '''
    ->Verifica o login do usuário, com base nos dados passados e os que estão cadastrados.
    :param pos1: Posição no arquivo do primeiro elemento de verificação.
    :param pos2: Posição no arquivo do segundo elemento de verificação.
    :param login1: Primeiro elemento para efetuação do login. Ex: e-mail, código de login e etc...
    :param senha: Segundo elemento para efetuação do login. Ex: Senhas, códigos e etc...
    :param nome_do_arquivo: Nome do arquivo com sua extensão a ser analisado.
    :return: Caso haja correspondência das informações, logo havendo login, retorna True. Senão, retorna False.
    '''
    arq = open(nome_do_arquivo, 'rt')
    arq.readline()
    tupla = (login1, login2)
    lista = []
    for linhas in arq:
        tupla_dados = (linhas.split(';')[pos1], linhas.split(';')[pos2].replace('\n', '')) #Pega as informações das posições passadas do arquivo, colocando eles em uma tupla.
        lista.append(tupla_dados)
    if tupla in lista: #Verifica se a tupla contendo os dados passados consta na lista com as tuplas de dados cadastrados.
        print('-- Login efetuado --')
        return True
    else:
        print('~Não há conta com estas informações~')
        return False


def ordenarProdutos(ord_de_cód=False, crescente=True):
    '''
    ->Realiza a ordenação com base nos preços ou códigos dos produtos contidos no arquivo "produtos.txt".
    :param ord_de_cód: Caso True, irá ordenar por código. Caso False, permite a ordenação por preço.
    :param crescente: Caso True, irá ordenar do mais barato ao mais caro. Caso False, ordena do mais caro ao mais barato.
    :return: Sem retorno.
    '''
    lista = []  # Lista que irá receber as linhas do arquivo divididas por split().
    lista_produtos = []  # Lista que irá receber os dados de cada produto em dicionários.
    with open("produtos.txt", "r", encoding="utf8") as arquivo:
        arquivo.readline()
        for produto in arquivo:
            lista.append(produto.split(";"))  # Envia para a lista as linhas do arquivo.
        for linha in lista:
            lista_produtos.append({"codigo": linha[0], "produto": linha[1], "preço": float(linha[2]), "estoque": int(linha[3])})  # Percorre a lista e envia os dados como valores de chaves.

    if ord_de_cód is False:
        if crescente:
            lista_ordenada = []  # Lista que receberá os dicionários ordenados por preço.
            while not lista_produtos == []:
                menor_preço = lista_produtos[0]["preço"]  # Atribui a menor_preço o preço do primeiro produto.
                for produto in lista_produtos: # Percorre os dicionários da lista.
                    if produto["preço"] < menor_preço:  # Verifica se o preço do produto é menor que menor_preço.
                        menor_preço = produto["preço"]  # Caso seja menor, menor_preço recebe o preço desse produto.
                for produto in lista_produtos:  # Percorre os dicionários da lista.
                    if produto["preço"] == menor_preço:  # Analisa quais produtos tem um preço igual a menor_preço.
                        lista_ordenada.append(produto)  # Envia o dicionário do produto para a lista_ordenada.
                        lista_produtos.remove(produto)  # Remove o diconário do produto da lista_produtos.
        else:
            lista_ordenada = []  # Lista que receberá os dicionários ordenados por preço.
            while not lista_produtos == []:
                menor_preço = lista_produtos[0]["preço"]  # Atribui a menor_preço o preço do primeiro produto.
                for produto in lista_produtos:
                    if produto["preço"] > menor_preço:
                        menor_preço = produto["preço"]
                for produto in lista_produtos:
                    if produto["preço"] == menor_preço:
                        lista_ordenada.append(produto)
                        lista_produtos.remove(produto)

        print('', '_' * 81)
        for produto in lista_ordenada:
            print(f"| Codigo: {produto['codigo']}     Produto: {produto['produto']:<18}", f"Preço: R${float(produto['preço']):<10.2f}".replace('.', ','), f"Estoque: {produto['estoque']:<5}", f"{'|':<1}")
        print('', '-' * 81)
    else:
        print('', '_' * 81)
        for produto in lista_produtos:
            print(f"| Código: {produto['codigo']}     Produto: {produto['produto']:<18}", f"Preço: R${float(produto['preço']):<10.2f}".replace('.', ','), f"Estoque: {produto['estoque']:<5}", f"{'|':<1}")
        print('', '-' * 81)


def compras(nome_do_arquivo=''):
    '''
    ->Sistema de compras para análise do produto escolhido, quantidade a ser comprada e então alterar no armazenamento a quantidade do estoque.
    :param nome_do_arquivo: Nome do arquivo com sua extensão.
    :return: Retorna uma lista com dicionários que contém as informações de compra de cada produto escolhido.
    '''
    org = {} #Dicionário que irá conter as informações da compra de um produto.
    lista_geral = [] #Lista que irá conter os dicionários de cada produto da compra.
    cód_produtos = [] #Lista que irá armazenar os códigos de todos os produtos da loja.
    cód_usados = [] #Lista que armazena os códigos já usados, para analise de repetições.
    inf_do_arq = [] #Lista que irá conter as informações do arquivo, para sua modificação com base na compra.
    try:
        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
            arq.readline()
            for linhas in arq:
                inf_do_arq.append(linhas)
                cód_produtos.append(linhas.split(';')[0]) #Passa todos os códigos de produto para a lista.
    except:
        frase = 'Não foi possível a leitura do arquivo de produtos'
        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
    else:
        continuar_compra = True
        while continuar_compra:
            código = None
            repetição = False  # Variável para análise de repetição.
            while código is None:
                try:
                    código = str(input('Código do produto: ')).strip()  # Código do produto que será comprado.
                except:
                    frase = 'Digite uma numeração composta por 4 digitos'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    código = None
                else:
                    if código == '':  # Verifica se o código está vazio.
                        frase = 'Por favor, preencha com um código de produto'
                        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        código = None
                    elif not código.isnumeric():  # Verifica se é composto por somente números.
                        frase = 'O código dos produtos são compostos somente por números'
                        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        código = None
                    elif código not in cód_produtos:  # Verifica se o código se encontra entre os códigos de produtos.
                        frase = 'O código digitado não corresponde a um produto'
                        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        código = None

                    if código is not None:
                        if código not in cód_usados:  # Verifica se o código não foi usado antes, para criação de um novo dicionário.
                            with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
                                arq.readline()
                                for linhas in arq:
                                    if código == linhas.split(';')[0]:  # Verifica qual o produto escolhido.
                                        if int(linhas.split(';')[3]) == 0:  # Verifica se está sem estoque.
                                            frase = 'No momento estamos com falta do produto'
                                            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                                            perg = str(input('Quer continuar a compra?[Sim/Não] ')).strip().upper()
                                            while perg not in ['SIM', 'NÃO', 'NAO']:
                                                frase = 'Digite SIM ou NÃO'
                                                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                                                perg = str(input('Quer continuar a compra?[Sim/Não] ')).strip().upper()
                                            if perg == 'SIM':
                                                código = None
                                            else:
                                                continuar_compra = False
                                        else:  # Se houver estoque, passa informações para o dicionário.
                                            org['produto'] = linhas.split(';')[1]
                                            org['código'] = linhas.split(';')[0]
                                            org['preçoUnidade'] = float(linhas.split(';')[2])
                                            org['estoque'] = int(linhas.split(';')[3])
                                            cód_usados.append(código)

                        else:
                            repetição = True  # Caso o código esteja na lista de já usados, a var recebe True.

            if continuar_compra:
                quantidade = None
                while quantidade is None:
                    try:
                        quantidade = int(input('Quantidade a ser comprada:'))  # Quantidade do produto a ser comprada.
                    except:
                        frase = 'Dado inválido'
                        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        quantidade = None
                    else:
                        if quantidade <= 0:
                            frase = 'Compra inválida, digite uma quantidade superior a 0'
                            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                            quantidade = None
                        else:
                            if not repetição:  # Verifica se a var de repetição é False.
                                org['quantidade'] = quantidade  # Não sendo repetição, adiciona informação no dicionário.
                                if org['quantidade'] > org['estoque']:  # Verifica se a quantidade excede o estoque do produto.
                                    frase = f'A quantia excede o estoque de {org["estoque"]} {org["produto"]}'
                                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                                    quantidade = None
                                else:
                                    org['estoque'] -= org['quantidade'] #Se não exceder, refaz o estoque com a subtração da quantidade comprada.
                                    org["preçoTot"] = org['quantidade'] * org['preçoUnidade']  # Adiciona no dicionário o preço total de compra daquele produto.
                                    lista_geral.append(org.copy())  # Manda para a lista que irá conter todos os dicionários, uma cópia das informações.
                            else:
                                for num, dicionários in enumerate(lista_geral): #Percorre a lista, pegando seus índices e dicionários.
                                    if dicionários['código'] == código: #Verifica em qual dicionário está a correspondência de código.
                                        if quantidade <= dicionários['estoque']: #Verifica se a quantidade não excede o estoque do produto.
                                            lista_geral[num]['quantidade'] += quantidade  #Adiciona nas informações já existentes daquele produto, a quantidade a mais a ser comprada.
                                            lista_geral[num]['preçoTot'] += quantidade * lista_geral[num]['preçoUnidade'] #Adiciona no preço total a quantia com base na quantidade comprada.
                                            lista_geral[num]['estoque'] -= quantidade #Refaz o estoque do produto, subtraindo novamente com a quantidade a mais comprada.
                                        else:
                                            frase = f'A quantidade excede o estoque de {lista_geral[num]["estoque"]} {lista_geral[num]["produto"]}'
                                            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                                            quantidade = None
                perg = str(input('Deseja realizar mais uma compra?[Sim/Não] ')).strip().upper()
                while perg not in ['SIM', 'NÃO', 'NAO']:
                    frase = 'Digite SIM ou NÃO'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    perg = str(input('Deseja realizar mais uma compra?[Sim/Não] ')).strip().upper()
                if perg == 'NÃO' or perg == 'NAO': #Verifica se quer fazer mais uma compra.
                    continuar_compra = False

    if lista_geral:
        with open(nome_do_arquivo, 'wt+', encoding='utf8') as arq:  # Cria um novo arquivo de mesmo nome.
            arq.write('código;produto;preço;estoque' + '\n')  # Digita a primeira linha de organização.
        with open(nome_do_arquivo, 'at', encoding='utf8') as arq:  # Abre o arquivo récem criado, para incremento de informação.
            for num, linhas in enumerate(inf_do_arq):  # Percorre a lista com as linhas do arquivo apagado e recriado.
                for dicionários in lista_geral:  # Percorre os dicionários contidos na lista.
                    if linhas.split(';')[0] == dicionários['código']:  # Verifica se algum código das linhas armazenadas é igual a algum código de compra armazenado.
                        correção = linhas.split(';')  # Cria a var correção, para modificar o arquivo com base nas compras feitas.
                        correção[3] = str(dicionários['estoque'])  # Refaz o estoque do arquivo com base no estoque alterado pela compra.
                        linhas = ';'.join(correção) + '\n'
                arq.write(linhas)

        return lista_geral  # Retorna a lista que contém todos os dados de compra dos produtos.


def mudarEstoque(nome_do_arquivo='', nome_arquivo_adição=''):
    cód_produtos = [] #Lista que irá armazenar o código de todos os produtos.
    lista_linhas = [] #Lista que irá armazenar as linhas com informações dos produtos do arquivo.
    lista_adição = [] #Lista que irá armazenar as linhas de um arquivo com os produtos que terão seu estoque adicionado no arquivo principal.
    try:
        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
            arq.readline()
            for linhas in arq:
                lista_linhas.append(linhas) #Insere as linhas do arquivo na lista.
                cód_produtos.append(linhas.split(';')[0]) #Passa todos os códigos de produto para a lista.
    except:
        print('-- Não foi possível a leitura do arquivo de produtos --')
    else:
        frase = 'Tabela De Alteração'
        cabeçalho(frase=frase)
        print('[1] - Adicionar estoque manualmente')
        print('[2] - Zerar estoque')
        print('[3] - Adicionar estoque por arquivo ')

        opção = None
        while opção is None:
            try:
                opção = int(input('Opção: '))
            except:
                frase = 'Digite um número inteiro válido'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                opção = None
            else:
                if opção < 1 or opção > 3:
                    frase = 'Opção não correspondente, tente novamente'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    opção = None

        if opção == 3:
            with open(nome_arquivo_adição, 'rt', encoding='utf8') as arq:
                arq.readline()
                for linhas in arq:
                    lista_adição.append(linhas)  # Insere na lista o código e estoque do arquivo.
                for num, linhas in enumerate(lista_linhas):
                    produto = linhas.split(';')  # Produto recebe uma lista com dados do produto.
                    for linhas2 in lista_adição:
                        adição = linhas2.split(';')[1]  # Adição recebe uma lista com código e estoque.
                        if produto[0] == linhas2.split(';')[0]:  # Verifica se o código do Produto é igual ao código de Adição.
                            if int(produto[3]) + int(adição) >= 0:  # Verifica se a adição do estoque não dará uma quantidade negativa.
                                produto[3] = str(int(produto[3]) + int(adição)) + '\n'  # Adiciona o estoque de Adição ao estoque de Produto.
                                lista_linhas[num] = ';'.join(produto)

        else:

            código = None
            while código is None:
                try:
                    código = str(input('Código do produto: ')).strip()  # Código do produto que será comprado.
                except:
                    frase = 'Digite uma numeração composta por 4 digitos'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    código = None

                else:
                    if not código.isnumeric():  # Verifica se é composto por somente números.
                        frase = 'O código dos produtos são compostos somente por números'
                        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        código = None
                    elif código not in cód_produtos:  # Verifica se o código se encontra entre os códigos de produtos.
                        frase = 'O código digitado não corresponde a um produto'
                        cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                        código = None

            if opção == 1:
                for num, linhas in enumerate(lista_linhas):
                    if código == linhas.split(';')[0]:  # Verifica qual o produto correspondente ao código.
                        produto = linhas.split(';')  # Atribui a var produto uma lista com os dados do produto.
                        print(f'O estoque de {produto[1]} atualmente é {produto[3]}'.replace('\n', ''))
                        print('--Para subtrair do estoque, basta colocar o sinal de "-" primeiro--')

                        adicionar = None
                        while adicionar is None:
                            try:
                                adicionar = int(input('Quanto deseja adicionar?'))
                            except:
                                frase = 'Dado inválido'
                                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                                adicionar = None
                            else:
                                produto[3] = int(produto[3]) + adicionar  # Adiciona ao estoque de produto.
                                if int(produto[3]) < int(0):  # Verifica se essa adição tornou o estoque negativo.
                                    frase = 'Não é possível um estoque negativo, tente novamente'
                                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                                    adicionar = None
                                else:
                                    produto[3] = str(produto[3]) + '\n'
                                    lista_linhas[num] = ';'.join(produto)  # Faz a lista de dados receber os dados do produto alterados.
            else:
                for num, linhas in enumerate(lista_linhas):
                    if código == linhas.split(';')[0]:  # Verifica qual o produto correspondente ao código.
                        produto = linhas.split(';')  # Atribui a produto uma lista com os dados do produto.
                        produto[3] = '0' + '\n'  # Insere no estoque a quantidade 0 em string.
                        lista_linhas[num] = ';'.join(produto)  # Insere na lista os novos dados agora alterados do produto.

    with open(nome_do_arquivo, 'wt+', encoding='utf8') as arq:  # Cria um novo arquivo de mesmo nome.
        arq.write('código;produto;preço;estoque' + '\n')  # Digita a primeira linha de organização.
    with open(nome_do_arquivo, 'at', encoding='utf8') as arq:  # Abre o arquivo récem criado, para incremento de informação.
        for linhas in lista_linhas:  # Percorre a lista com as linhas do arquivo apagado e recriado.
            arq.write(linhas)


def adicionarProduto(nome_do_arquivo=''):
    '''
    --> Função para inserir no arquivo um novo produto..
    :param nome_do_arquivo: Nome do arquivo juntamente com sua extensão.
    :return: Sem retorno.
    '''
    cód_produtos = [] #Lista que armazena o código dos produtos do arquivo.
    nome_produtos = [] #Lista que armazena o nome dos produtos do arquivo.
    try:
        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
            arq.readline()
            for linhas in arq:
                nome_produtos.append(linhas.split(';')[1]) #Passa todos os nomes de produto para a lista.
                cód_produtos.append(linhas.split(';')[0]) #Passa todos os códigos de produto para a lista.
    except:
        print('-- Não foi possível a leitura do arquivo de produtos --')
    else:
        código = str(int(cód_produtos[-1]) + 1) #Pega o último código da lista e acrescenta 1 ao seu valor inteiro, depois o transforma em string.
        while len(código) < 4: #Verifica se o código possui 4 algarismos, não tendo, o loop permanece.
            código = '0' + código #Acrescenta '0' a frente do código a cada loop.

        nome = None
        while nome is None:
            try:
                nome = str(input('Nome do produto: ')).strip()
            except:
                frase = 'Digite um dado válido'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                nome = None
            else:
                if nome == '': #Verifica se o nome é uma string vazia.
                    frase = 'Preencha o nome do produto'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    nome = None
                elif not nome.isalnum():
                    frase = 'O nome do produto deve ser composto somente por letras e números'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    nome = None
                elif nome in nome_produtos: #Verifica se o nome está dentro da lista com o nome de todos os produtos.
                    frase = 'Um produto com este nome já está cadastrado'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    nome = None

        preço = None
        while preço is None:
            try:
                preço = float(input('Preço do produto: '))
            except:
                frase = 'Digite um preço válido'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                preço = None
            else:
                if preço <= 0:
                    frase = 'Digite um preço válido, maior que zero.'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    preço = None


        estoque = None
        while estoque is None:
            try:
                estoque = int(input('Estoque do produto: '))
            except:
                frase = 'Digite um estoque válido'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                estoque = None
            else:
                if estoque < 0:
                    frase = 'Estoques negativos não são possíveis'
                    cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                    estoque = None
                else:
                    adicionarNoArquivo(f'{código};{nome};{preço};{estoque}', nome_do_arquivo) #Adiciona ao arquivo os dados do novo produto.


def excluirProduto(nome_do_arquivo=''):
    '''
    --> Função para excluir produtos de um arquivo por meio do código escolhido.
    :param nome_do_arquivo: Nome do arquivo juntamente com sua extensão.
    :return: Sem retorno.
    '''
    códigos = [] #Lista para armazenar os códigos de todos os produtos.
    conteudo = [] #Lista para armazenar as linhas do arquivo.
    with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
        arq.readline()
        for linhas in arq:
            conteudo.append(linhas) #Insere as linhas do arquivo na lista.
            códigos.append(linhas.split(';')[0]) #Insere os códigos dos produtos na lista.

    cabeçalho(frase='Remoção de Produto')
    código = None
    while código is None:
        try:
            código = str(input('Código do produto: ')).strip()
        except:
            frase = 'Dado inválido'
            cabeçalho(caracter='~', frase=frase, cor='\033[31m')
        else:
            if not código.isnumeric(): #Verifica se o código é composto por números.
                frase = 'Os códigos são compostos somente por numeros'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                código = None
            elif código not in códigos: #Verifica se o código digitado encontra-se entre os códigos de algum produto.
                frase = 'Não há um produto com esse código'
                cabeçalho(caracter='~', frase=frase, cor='\033[31m')
                código = None

    for num, linhas in enumerate(conteudo):
        produto = linhas.split(';') #Atribui a produto uma lista com a linha do arquivo dividida pelo split().
        if código == produto[0]: #Verifica qual o produto do código digitado.
            del conteudo[num] #Deleta o produto.
            print(f'{produto[1]} foi removido do arquivo')

    cód_corretor = '0001'
    for num, linhas in enumerate(conteudo):
        produto = linhas.split(';') #Atribui a produto uma lista com a linha do arquivo dividida pelo split().
        if num == 0:
            produto[0] = cód_corretor #Sendo a primeira linha de produto, atribui ao código dele '0001'.
            conteudo[0] = ';'.join(produto) #Repassa a linha alterada para a lista de linhas do arquivo.
        else:
            cód_corretor = str(int(cód_corretor) + 1) #Soma 1 ao código, logo ficando '2'... '3'... e segue.
            while len(cód_corretor) < 4: #Verifica se o código possui 4 digitos, não tendo, o loop é refeito e um '0' é acrescentado a frente.
                cód_corretor = '0' + cód_corretor #Acrescenta '0' a frente do código. Ex: '12' ficará '0012'.
            produto[0] = cód_corretor #Altera o código para sua versão seguindo a ordenação devida.
            conteudo[num] = ';'.join(produto) #Manda para a lista a linha devidamente alterada.

    with open(nome_do_arquivo, 'wt+', encoding='utf8') as arq:
        arq.write('código;produto;preço;estoque\n') #Ao recriar o arquivo, agora vazio, incrementa a primeira linha de explicação dos dados.
    with open(nome_do_arquivo, 'at', encoding='utf8') as arq:
        for linhas in conteudo:
            arq.write(linhas) #Insere no arquivo cada elemento da lista, correspondente as linhas do arquivo anterior alteradas.


def notaFiscal(lista=[], nome_do_arquivo='', cpf='', exibir=False):
    '''
    --> Função para criação ou exibição da nota fiscal.
    :param lista: Lista contendo os dados referentes a compra.
    :param nome_do_arquivo: Nome do arquivo que será criado.
    :param cpf: CPF do responsável pela compra.
    :param exibir: Parâmetro para definição de uso da função.
    :return: Sem retorno.
    '''
    import datetime

    if exibir:
        print('\n\n')
        cabeçalho(frase='NOTA FISCAL', tamanho=90, cor='\033[1m')
        print(f'CPF: {cpf}')
        preço_total = 0
        for produtos in lista:  # Percorre os dicionários com dados da compra.
            preço_total += produtos['preçoTot']  # Cálculo do preço total da compra.
            produtos['preçoUnidade'] = f"{produtos['preçoUnidade']:.2f}".replace('.', ',')  # Formatação para preço em Real.
            produtos['preçoTot'] = f"{produtos['preçoTot']:.2f}".replace('.', ',')  # Formatação para preço em Real.
            print(f'Código:{produtos["código"]} - Produto:{produtos["produto"]} - PreçoUnidade:R${produtos["preçoUnidade"]} - ',end='')
            print(f'Quantidade:{produtos["quantidade"]} - PreçoTotal:R${produtos["preçoTot"]}')
        print(f'\033[1mTotal da compra: R${preço_total:.2f}\033[m'.replace('.', ','))
        print('-' * 101)

    else:
        data = [str(datetime.date.today().day), str(datetime.date.today().month), str(datetime.date.today().year)]
        for num, momento in enumerate(data):
            if len(momento) < 2:  # Verifica se o componente da data ocupa duas casas.
                data[num] = '0' + data[num]  # Coloca um '0' na frente para a padronização.
        nome_do_arquivo = nome_do_arquivo + ';' + '.'.join(data) + '.txt'  # Nome do arquivo que será gerado.
        try:
            with open(nome_do_arquivo, 'wt+', encoding='utf8') as arq:
                arq.write('--Nota Fiscal--\n')
                arq.write(f"CPF:{cpf}\n")
        except:
            print('O arquivo não pôde ser criado')
        else:
            try:
                arq = open(nome_do_arquivo, 'at', encoding='utf8')
                preço_total = 0
                for dic in lista:
                    preço_total += float(str(dic['preçoUnidade']).replace(',', '.'))
                    arq.write(f'Código:{dic["código"]};Produto:{dic["produto"]};PreçoUnidade:R${dic["preçoUnidade"]};')
                    arq.write(f'Quantidade:{dic["quantidade"]};PreçoTotal:R${dic["preçoTot"]}\n')
                arq.write(f'TotalDaCompra:R${preço_total:.2f}'.replace('.', ','))
            except:
                print('Não foi possível adicionar dados na nota')
            else:
                print('-Nota fiscal criada-')
            finally:
                arq.close()
