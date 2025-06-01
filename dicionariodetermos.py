from loguru import logger

bd_termos = [
    ['a', 'vogal'],
    ['b', 'consoante'],
    ['c', 'consoante']
]

def adicionar_termos(bd, termo, definicao):
    dicionario = [termo, definicao]
    bd.append(dicionario)
    return bd

def visualizar_termos(bd):
    logger.info('Visualização dos termos.')
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][0]} | {bd[i][1]}')

def alterar_termo(bd, indice, termo, definicao):
    bd[indice][0] = termo
    bd[indice][1] = definicao
    return bd

def deletar_termo(bd, indice, termo, definicao):
    bd[indice][0] = termo
    bd[indice][1] = definicao
    return bd

def salvar_termos(bd):
    with open('bd_termos.txt', 'w', encoding='utf-8') as arquivo:
        for i in range(len(bd)):
            logger.info(f'Salvando os termos {bd[i][0]}')
            arquivo.write(f'{bd[i][1]}, {bd[i][0]}\n')

while True:
    print('1 - Adicionar Termo')
    print('2 - Visualizar Termos')
    print('3 - Alterar Termo')
    print('4 - Deletar Termo')
    print('5 - Salvar Termos')

    try:
        op = int(input('Digite uma opção: '))
    except Exception as e:
        logger.error(f'Erro: {e}')
        logger.info('Digite um valor numérico.')
        op = -1

    if op == 1:
        logger.info('Iniciando o cadstro do termo.')
        termo = input('Digite o termo que deseja adicionar: ')
        definicao = input('Digite a definição do termo: ')
        bd_termos = adicionar_termos(
            bd=bd_termos,
            termo=termo,
            definicao=definicao
        )
        print('Termo e definição cadastrados!')

    elif op == 2:
        logger.info('Iniciando a visualização dos termos.')
        visualizar_termos(bd_termos)
        logger.info('Termos visualizados com sucesso!')

    elif op == 3:
        logger.info('Iniciando a alteração do termo.')
        visualizar_termos(bd_termos)
        print(visualizar_termos(bd_termos))
        i = int(input('Qual termo deseja alterar? '))
        termo = input('Digite o novo termo: ')
        definicao = input('Digite a nova definição para o termo: ')
        bd_termos = alterar_termo(
            bd=bd_termos,
            indice=(i-1),
            termo=termo,
            definicao=definicao
        )
        logger.info('Termo alterado com sucesso!')
        logger.info('Termo cadastrado com sucesso!')

    elif op == 4:
        logger.info('Iniciando a exclusão do termo.')
        visualizar_termos(bd_termos)
        i = int(input('Qual termo deseja deletar? '))

        bd_termos = deletar_termo(
            bd=bd_termos,
            indice=(i-1),
            termo=termo,
            definicao=definicao
        )
        logger.info('Termo deletado com sucesso!')

    elif op == 5:
        logger.info('Iniciando persistência dos termos.')
        salvar_termos(bd_termos)
        logger.info('Termos salvos com sucesso!')

    else:
        print(f'Opção {op} inválida!')