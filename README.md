# Bloonds-TD-6-
1.0 apenas uma copia para apenas aprender a programar.
Reino dos Guardiões — Tower Defense
Jogo Tower Defense 2D original feito em Python e Pygame. O projeto usa ilustrações vetoriais próprias, criadas por código, sem arquivos comerciais ou dependências pagas.
Conteúdo incluído
- 20 torres com três caminhos de evolução e cinco níveis por caminho (300 melhorias cadastradas).
- 25 tipos de inimigos, 10 chefes e 8 heróis.
- 30 mapas, com ambientes e trajetos próprios.
- 120 rodadas configuradas, além de geração de ondas infinitas.
- 10 modos de jogo e 50 conquistas.
- Menus, seleção de mapas, enciclopédia, configurações e salvamento local.
- Efeitos, partículas, projéteis, animações vetoriais, áudio sintético e progressão.
- 93 artes SVG originais que podem ser geradas pelo utilitário incluído.
Instalação no Windows
1. Instale Python 3.10 ou superior: https://www.python.org/downloads/
2. Abra a pasta do projeto.
3. Abra o Prompt de Comando nessa pasta.
4. Execute:
py -m pip install -r requirements.txt
py main.py
Também é possível executar run.bat.
Instalação no Linux
python3 -m pip install -r requirements.txt
python3 main.py
Ou execute ./run.sh após permitir a execução do arquivo.
Gerar as imagens vetoriais
O jogo desenha seus personagens e cenários em tempo real. Para criar também os arquivos SVG individuais:
python -m tools.generate_art
Os arquivos serão salvos em assets_generated/, separados em towers, enemies, bosses, heroes e maps.
Controles
Tecla / ação	Função
Clique em uma torre no Arsenal	Selecionar unidade para posicionar
Clique no terreno livre	Posicionar torre selecionada
Clique em uma torre instalada	Abrir melhorias e opções
Espaço	Iniciar a próxima rodada
1 / 2 / 3	Velocidade normal, 2x ou 3x
P ou Esc	Pausar / continuar
E	Ativar habilidade da torre selecionada ou do herói
Tab	Alterar prioridade de alvo
F2	Mostrar ou ocultar alcance
F5	Salvar perfil
F11	Alternar tela cheia
Roda do mouse no Arsenal	Mudar página de torres


Salvamento
O perfil fica em ~/.reino_dos_guardioes/profile.json (no Windows, dentro da pasta do usuário). O arquivo é local; não é necessário criar conta ou conectar à internet.
