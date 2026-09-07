import utils

# --- SUAS CONFIGURAÇÕES DESTA RODADA ---
QUANTIDADE_VIDEOS = 2 
V_RELACIONADO = "AULA 017"

print(f"Bot pronto! Vamos processar {QUANTIDADE_VIDEOS} vídeos. Começando em 3 segundos...")
utils.pausa_aleatoria(3, 3)

for i in range(QUANTIDADE_VIDEOS):
    print(f"\n--- Iniciando vídeo {i + 1} de {QUANTIDADE_VIDEOS} ---")

    # 1. Abre o rascunho, pega as datas e pausa para você colocar o título
    data, hora = utils.primeiras_etapas()

    # 2. Faz o trabalho braçal e envia a variável do vídeo relacionado
    utils.etapas_intermediarias(V_RELACIONADO)

    # 3. Preenche a data/hora que foi pega lá no começo e salva o vídeo
    utils.etapas_finais(data, hora)

print("\nTodos os vídeos foram agendados com sucesso!")