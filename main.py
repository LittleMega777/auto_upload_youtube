import pyautogui
import time
import keyboard
import random
import pyperclip

# --- SEUS MAPEAMENTOS ---
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

# Variáveis temporárias pro agendamento
data_post = "15/10/2026"
hora_post = "18:00"

# --- FUNÇÕES DE AJUDA ---
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

# --- FLUXO PRINCIPAL ---
print("Bot pronto! Começando em 3 segundos...")
pausa_aleatoria(3, 3)

print("1. Clicando no primeiro rascunho...")
clicar(PRIMEIRO_RASCUNHO)
pausa_aleatoria(1.5, 2) # Espera a tela de edição abrir bem

print("2. Clicando no título...")
clicar(CAMPO_TITULO)

print("2. Clicando no título para extrair data e hora...")
clicar(CAMPO_TITULO)

# Seleciona tudo e copia o texto original (ex: "shorts2 0908")
pyautogui.hotkey('ctrl', 'a')
pausa_aleatoria(0.5, 1.0)
pyautogui.hotkey('ctrl', 'c')
pausa_aleatoria(0.5, 1.0)

# Puxa o texto da área de transferência
titulo_original = pyperclip.paste().strip()
print(f"-> Título capturado: {titulo_original}")

# Lógica para converter "shorts2 0908" nas datas e horários
# Quebra o texto no espaço. partes[0] = 'shorts2', partes[1] = '0908'
partes = titulo_original.split() 

if len(partes) >= 2:
    tipo_shorts = partes[0].lower()
    codigo_data = partes[1]

    # Define o horário
    if tipo_shorts == 'shorts2':
        hora_post = "18:00"
    else:
        hora_post = "12:00"

    # Define a data (Pega '09' para mês e '08' para dia)
    mes = codigo_data[0:2]
    dia = codigo_data[2:4]
    data_post = f"{dia}/{mes}/2026"
else:
    # Failsafe caso o título fuja do padrão, você preenche na mão se der erro
    hora_post = "12:00"
    data_post = "01/01/2026" 

print(f"-> Agendamento definido para: {data_post} às {hora_post}")

limpar()
print("-> PAUSADO! Digite o título e aperte '0' para o robô continuar.")
keyboard.wait('0') 
pausa_aleatoria(0.5, 1.0)
# Como você vai estar com o campo de título selecionado, ao apertar '&' 
# ele vai digitar esse símbolo no título. Então o robô apaga ele logo em seguida:
pyautogui.press('backspace') 

pausa_aleatoria(1, 2)
print("3. Preenchendo descrição...")
clicar(CAMPO_DESCRIPITION)
limpar_e_escrever(DESCRICAO)

print("4. Rolando a tela e marcando 'Não é para crianças'...")
# O scroll do pyautogui usa números negativos para descer. 
# Se não descer o suficiente, é só aumentar esse número (ex: -3000)
pyautogui.scroll(-2000) 
pausa_aleatoria(1, 2)
clicar(BOTAO_FEITO_PARA_CRIANCA)

print("5. Avançando para próxima tela...")
clicar(BOTAO_PROXIMO)
pausa_aleatoria(2, 3) 

print("6. Adicionando vídeo relacionado...")
clicar(BOTAO_ADD_RELATED_VIDEO)
pausa_aleatoria(1.5, 2.5) # Espera a janela de busca abrir

clicar_duas_vezes(CAMPO_RELATED_VIDEO)
pausa_aleatoria(1.5, 2.5)
escrever_humano(RELATED_VIDEO)
pausa_aleatoria(2, 3) # Espera a busca do YouTube achar o vídeo
clicar(FIRST_RELATED_VIDEO)

# print("7. Avançando 2x...")
clicar(BOTAO_PROXIMO) # Tela de verificações
clicar(BOTAO_PROXIMO) # Tela de visibilidade

pausa_aleatoria(1, 2)
print("8. Configurando Data e Hora...")
clicar(BOTAO_SCHEDULE_CONFIG)
pausa_aleatoria(1, 2)
clicar(BOTAO_DATA)
limpar_e_escrever(data_post)
pyautogui.press('enter')

clicar(BOTAO_HORARIO)
limpar_e_escrever(hora_post)
pyautogui.press('enter') # Dá um enter pra fixar o horário, as vezes o YT é chato com isso

print("9. Finalizando o agendamento...")
clicar(BOTAO_SCHEDULE_FINAL)
pausa_aleatoria(1, 2)
print("Feito! Vídeo agendado com sucesso. Indo para o proximo")
clicar(BOTAO_CLOSE)
pausa_aleatoria(1, 2)
# # Atualiza a página
print("Atualizando a lista de rascunhos (F5)...")
pyautogui.press('f5')

# Pausa maior para a página carregar inteira antes do robô recomeçar o loop
pausa_aleatoria(6, 8)