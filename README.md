Manipulação do Jogo Através do RNG
# tetris_gatinho

O artigo (https://piaui.folha.uol.com.br/como-as-bets-produziram-a-pandemia-do-vicio/) me fez pensar em como os jogos podem ser manipulados. De forma simples, vou aqui explicar através deste jogo criado para demonstrar a manipulação.

O jogo é uma implementação em Python utilizando a biblioteca Pygame, inspirado no clássico Tetris. A mecânica central do jogo envolve a geração aleatória de peças, onde a manipulação do Gerador de Números Aleatórios (RNG) pode impactar significativamente a experiência do jogador, resultando em desafios que podem levar à derrota.

Estrutura do Código

![image](https://github.com/user-attachments/assets/0f4c268a-7536-400f-bf75-48631477ee3c)


BLOCK_SIZE: Define o tamanho de cada bloco no grid.
WIDTH e HEIGHT: Definem a largura e a altura do grid, respectivamente.
SHAPES: Contém as diferentes formas que as peças podem assumir, representadas por matrizes.
COLORS: Lista de cores que serão atribuídas aleatoriamente às peças.
SPEEDS: Define a velocidade de queda das peças, que aumenta conforme o nível do jogo.

Classe Piece
A classe Piece é responsável por gerenciar as peças do jogo:

![image](https://github.com/user-attachments/assets/260d48bc-e88e-48d3-8ba6-c0cb33aa0ced)

get_shape: Método crucial que utiliza pesos para determinar a forma da peça gerada. A manipulação dos pesos pode ser uma estratégia para aumentar a dificuldade.

Geração de Formas e Pesos

![image](https://github.com/user-attachments/assets/7fb666ae-0ff6-498d-9d15-346bbb921652)


Pesos: Cada forma tem um peso associado. Por exemplo, formas mais difíceis podem receber pesos maiores, aumentando a chance de serem escolhidas. Essa manipulação pode ser ajustada para criar uma experiência de jogo mais desafiadora, levando o jogador à derrota.

Lógica de Jogo
Colisão e Limpeza de Linhas
A função check_collision verifica se a peça atual colide com outras peças ou com os limites do tabuleiro, enquanto clear_lines remove linhas completas, aumentando a pontuação do jogador.

Loop Principal
O loop principal do jogo gerencia a lógica de atualização e renderização:

![image](https://github.com/user-attachments/assets/52d503dd-4476-478c-8d4e-6bdbb2604103)


Manipulação do Tempo: O tempo de queda das peças é controlado pela lista SPEEDS. Ajustar esses valores pode aumentar a velocidade do jogo, dificultando a reação do jogador.

#Estratégias de Manipulação

Alteração de Pesos

Aumentar os pesos de peças mais difíceis ou diminuir os de peças mais fáceis pode ser uma forma eficaz de manipular a experiência do jogador. Por exemplo, se o jogador estiver se saindo bem, aumentar a probabilidade de peças mais desafiadoras pode levar à perda.

Ajuste de Velocidade

Reduzir o intervalo de tempo entre a queda das peças (diminuindo os valores em SPEEDS) pode criar uma pressão adicional sobre o jogador, dificultando a colocação correta das peças.

Criação de Cenários de Game Over

A lógica que determina o término do jogo pode ser ajustada para ser mais sensível a colisões, tornando o jogo mais punitivo. Por exemplo, permitir que uma peça comece em uma posição mais alta no grid pode resultar em um game over mais rápido.

A manipulação do RNG e a lógica do jogo são ferramentas poderosas para moldar a experiência do jogador. Ao ajustar os pesos das formas e a velocidade do jogo, é possível criar um ambiente desafiador que pode levar à derrota do jogador, mesmo que ele tenha habilidades adequadas. A implementação cuidadosa dessas estratégias pode resultar em uma experiência de jogo que, embora divertida, também pode ser frustrante e desafiadora.

Como jogar

O jogo utiliza a biblioteca Pygame. Para instalá-la, abra o terminal ou o prompt de comando e execute: pip install pygame

O jogo está em um repositório do GitHub, você pode cloná-lo.

O código faz referência a uma imagem chamada gatinhos.png, você pode criar uma ou usar qualquer outra imagem, mas lembre-se de renomeá-la para gatinhos.png.

Use as setas do teclado para mover as peças e a barra de espaço para girá-las. Você também pode reiniciar ou pausar o jogo usando os botões na tela.




