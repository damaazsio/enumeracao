import socket

while True: 
    def buscar_ip():
        IP = input('Digite o IP alvo: ')
        print(socket.gethostbyaddr(IP))


    def busca_simples():
        print('Bom estuso !')
        domain = input('Digite o dominio: ')
        nomes = ['nome', 'ns2', 'www', 'ftp', 'intranet']

        for nome in nomes:
            DNS = nome + "." + domain

            try :
                print(DNS + ':' + socket.gethostbyname(DNS)) # "socket.gethosbyname(DNS)" TODAS INFORMAÇÕES DNS

            except:
                print('Nada foi encontrado') #PRINT E FACULTATIVO, PODE SER COLOCADO O COMANDO "except socket.gaierror"




    def busca_lista ():
        print('O arquivo Text contendo os endereços tem que estar na mesma pasta do enumeracao.py')
        print('bons estudos ! \n')
        domain = 'domminio.com'
        with open("bruteforce.txt") as arquivo:
            nomes = arquivo.readlines()

        for nome in nomes:
            DNS = nome.strip('\n') + '.' + domain  
            try:
                print( DNS + ":" + socket.gethostbyname(DNS)) # "socket.gethostbyname(DNS)" BUSCA POR DNS POR IP
            except:
                print('Nada encontrado ')
                pass     

    print('\nFerramenta apenas voltada para estudos \n')
    print('1 - Ataque de Enumeração silples \n')
    print('2 - Brute force de varios DNS \n')
    print('3 - Buscar DNS por IP \n')
    print('by The Nightamres \n')


    opcao = input('Qual sua opção? ')


    if opcao == '1':
        busca_simples()

    elif opcao == '2':
        busca_lista()

    elif opcao == '3':
        buscar_ip()


