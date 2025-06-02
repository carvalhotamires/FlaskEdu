from loguru import logger
import os
caminho = os.path.join('glossario.csv')


with open(caminho, 'r', encoding='utf-8') as f:
    conteudo = f.read()

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
    for idx in range(len(bd)):
        print(f'{idx+1} | {bd[idx][0]} | {bd[idx][1]}')

def alterar_termo(bd, indice, termo, definicao):
    bd[indice][0] = termo
    bd[indice][1] = definicao
    return bd

def deletar_termo(bd, indice):
    # Verifica se o índice é válido para evitar erros
    if 0 <= indice < len(bd):
        termo_a_remover = bd[indice][0]  # Pega o termo antes de deletar para a mensagem de log
        del bd[indice]
        logger.info(f"Termo '{termo_a_remover}' deletado com sucesso!")
        return bd
    else:
        logger.warning(f"Índice {indice + 1} inválido. Termo não encontrado!")
        return bd

def salvar_termos(bd):
    with open('bd_termos.txt', 'w', encoding='utf-8') as arquivo:
        for idx in range(len(bd)):
            logger.info(f'Salvando os termos {bd[idx][0]}')
            arquivo.write(f'{bd[idx][1]}, {bd[idx][0]}\n')

