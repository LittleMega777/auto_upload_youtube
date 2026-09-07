import pyautogui
import time
import random
import keyboard
import pyperclip

# --- MAPEAMENTOS ---
PRIMEIRO_RASCUNHO = pyautogui.Point(x=482, y=396)
CAMPO_TITULO = pyautogui.Point(x=973, y=379)
CAMPO_DESCRIPITION = pyautogui.Point(x=943, y=597)
BOTAO_FEITO_PARA_CRIANCA = pyautogui.Point(x=859, y=1076)
BOTAO_PROXIMO = pyautogui.Point(x=1706, y=1309)
BOTAO_ADD_RELATED_VIDEO = pyautogui.Point(x=1665, y=404)
CAMPO_RELATED_VIDEO = pyautogui.Point(x=934, y=449)
FIRST_RELATED_VIDEO = pyautogui.Point(x=912, y=545)
BOTAO_SCHEDULE_CONFIG = pyautogui.Point(x=914, y=670)
BOTAO_DATA = pyautogui.Point(x=955, y=577)
BOTAO_HORARIO = pyautogui.Point(x=1074, y=584)
BOTAO_SCHEDULE_FINAL = pyautogui.Point(x=1693, y=1306)
BOTAO_CLOSE = pyautogui.Point(x=1485, y=875)

# --- CONSTANTES ---
RELATED_VIDEO = "AULA 017"
DESCRICAO = "VIDEO COMPLETO NO CANAL !!!"

# --- FUNÇÕES DE AJUDA BÁSICAS ---
def pausa_aleatoria(min_seg, max_seg):
    time.sleep(random.uniform(min_seg, max_seg))

def clicar(ponto):
    pyautogui.click(ponto.x, ponto.y)
    pausa_aleatoria(1.0, 2.0)

def clicar_duas_vezes(ponto):
    pyautogui.doubleClick(ponto.x, ponto.y)
    pausa_aleatoria(1.0, 2.0)

def escrever_humano(texto):
    pyautogui.write(texto, interval=0.05)

def limpar_e_escrever(texto):
    limpar()
    pausa_aleatoria(0.5, 1.0)
    escrever_humano(texto)

def limpar():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

def extrair_data_hora(titulo_original):
    partes = titulo_original.split() 
    if len(partes) >= 2:
        tipo_shorts = partes[0].lower()
        codigo_data = partes[1]
        hora_post = "18:00" if tipo_shorts == 'shorts2' else "12:00"
        mes = codigo_data[0:2]
        dia = codigo_data[2:4]
        data_post = f"{dia}/{mes}/2026"
    else:
        hora_post = "12:00"
        data_post = "01/01/2026" 
    return data_post, hora_post

# --- FUNÇÕES DE BLOCO DO ROBO ---

def primeiras_etapas():
    print("1. Clicando no primeiro rascunho...")
    clicar(PRIMEIRO_RASCUNHO)
    pausa_aleatoria(1.5, 2) 

    print("2. Clicando no título para extrair data e hora...")
    clicar(CAMPO_TITULO)

    pyautogui.hotkey('ctrl', 'a')
    pausa_aleatoria(0.5, 1.0)
    pyautogui.hotkey('ctrl', 'c')
    pausa_aleatoria(0.5, 1.0)

    titulo_original = pyperclip.paste().strip()
    data_post, hora_post = extrair_data_hora(titulo_original)
    
    print(f"-> Título capturado: {titulo_original}")
    print(f"-> Agendamento definido para: {data_post} às {hora_post}")

    limpar()
    print("-> PAUSADO! Digite o título definitivo e aperte '0' para o robô continuar.")
    keyboard.wait('0') 
    pausa_aleatoria(0.5, 1.0)
    pyautogui.press('backspace') 
    pausa_aleatoria(1, 2)
    
    return data_post, hora_post

# Substitua apenas essa função no seu utils.py
def etapas_intermediarias(video_relacionado):
    print("3. Preenchendo descrição...")
    clicar(CAMPO_DESCRIPITION)
    limpar_e_escrever(DESCRICAO)

    print("4. Rolando a tela e marcando 'Não é para crianças'...")
    pyautogui.scroll(-2000) 
    pausa_aleatoria(1, 2)
    clicar(BOTAO_FEITO_PARA_CRIANCA)

    print("5. Avançando para próxima tela...")
    clicar(BOTAO_PROXIMO)
    pausa_aleatoria(2, 3) 

    print("6. Adicionando vídeo relacionado...")
    clicar(BOTAO_ADD_RELATED_VIDEO)
    pausa_aleatoria(1.5, 2.5) 

    clicar_duas_vezes(CAMPO_RELATED_VIDEO)
    pausa_aleatoria(0.5, 1.0)
    
    # O robô digita a variável que veio lá do main.py
    escrever_humano(video_relacionado)
    
    pausa_aleatoria(2, 3) 
    clicar(FIRST_RELATED_VIDEO)

    print("7. Avançando telas finais...")
    clicar(BOTAO_PROXIMO) 
    clicar(BOTAO_PROXIMO) 
    pausa_aleatoria(1, 2)

def etapas_finais(data_post, hora_post):
    print("8. Configurando Data e Hora...")
    clicar(BOTAO_SCHEDULE_CONFIG)
    pausa_aleatoria(1, 2)
    
    clicar(BOTAO_DATA)
    limpar_e_escrever(data_post)
    pyautogui.press('enter')

    clicar(BOTAO_HORARIO)
    limpar_e_escrever(hora_post)
    pyautogui.press('enter') 

    print("9. Finalizando o agendamento...")
    clicar(BOTAO_SCHEDULE_FINAL)
    pausa_aleatoria(1, 2)
    
    print("Feito! Vídeo agendado com sucesso. Indo para o próximo...")
    clicar(BOTAO_CLOSE)
    pausa_aleatoria(3, 4)
    
    print("Atualizando a lista de rascunhos (F5)...")
    pyautogui.press('f5')
    pausa_aleatoria(6, 8)