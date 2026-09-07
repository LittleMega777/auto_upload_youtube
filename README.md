# 🤖 YouTube Shorts Auto-Scheduler

Um bot local em Python criado para automatizar o agendamento de vídeos (Shorts) no YouTube Studio. Ele assume o controle do mouse e teclado (nível do sistema operacional) para evitar bloqueios de anti-bot, trabalhando de forma híbrida (robô + humano) para agilizar o trabalho repetitivo.

## 🎯 O que ele faz?
O bot roda em cima da lista de rascunhos (Drafts) do seu canal e executa as seguintes etapas:
1. Entra no modo de edição do primeiro rascunho da lista.
2. Captura o título provisório (ex: `shorts2 0908`) e converte isso automaticamente em **Data e Hora de postagem**.
3. Pausa para você digitar o **Título definitivo** do vídeo.
4. Preenche a descrição padrão.
5. Marca a opção obrigatória "Não é conteúdo para crianças".
6. Adiciona um **Vídeo Relacionado** (pesquisado automaticamente).
7. Navega até a aba de Visibilidade e preenche o agendamento (Schedule) com os dados extraídos no passo 2.
8. Salva, fecha a janela e dá um **F5** na página para puxar o próximo rascunho da fila.

## 🏗️ Arquitetura do Projeto
O código foi dividido em dois arquivos para facilitar a manutenção:

* **`utils.py`:** É o "motor" do bot. Aqui ficam salvos os mapeamentos dos botões (Coordenadas X e Y da sua tela), as constantes de texto (Descrição, etc) e as funções que simulam o comportamento humano (pausas aleatórias, digitação letra por letra).
* **`main.py`:** É o painel de controle. Um script super enxuto com apenas 10 linhas lógicas, onde você define quantos vídeos quer subir e qual é o vídeo relacionado da rodada.

## 🛠️ Pré-requisitos
Você vai precisar instalar as bibliotecas que controlam o sistema operacional e a área de transferência. Abra o terminal e rode:

    pip install pyautogui keyboard pyperclip

## 🚀 Como usar

1. **Faça o Upload:** Suba todos os seus vídeos em massa para o YouTube normalmente e deixe-os como **Rascunho** (Draft). O nome do arquivo deve seguir o padrão: `tipo_shorts mesdia` (ex: `shorts2 0908` vira dia 08/09 às 18:00, e `shorts 0910` vira dia 10/09 às 12:00).
2. **Filtre a tela:** No YouTube Studio, aplique o filtro `Visibility: Draft` na aba de Shorts.
3. **Mapeie sua tela (Importante):** O bot clica em coordenadas exatas. Se você mudou de monitor ou deu zoom na página, atualize os valores `pyautogui.Point(x, y)` dentro do arquivo `utils.py`.
4. **Configure a rodada:** Abra o `main.py` e edite as variáveis no topo do arquivo:
   * `QUANTIDADE_VIDEOS = 5` (Quantos rascunhos o bot vai processar)
   * `V_RELACIONADO = "AULA 017"` (Qual o vídeo relacionado que será linkado)
5. **Rode o script:**
   * Inicie o `main.py`. Você terá 3 segundos para clicar na aba do YouTube.
   * Quando o robô pausar, digite o título definitivo e aperte `0` para ele continuar.

## 🛑 Failsafe (Freio de Emergência)
Como o PyAutoGUI assume o controle do mouse, se algo der errado no meio do processo (a internet cair ou a página travar), basta **jogar o cursor do mouse rapidamente para qualquer um dos 4 cantos da tela**. Isso aciona a trava de segurança da biblioteca e aborta o script instantaneamente.