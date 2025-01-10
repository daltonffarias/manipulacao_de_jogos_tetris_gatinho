import pygame
import random

# Definições de tamanhos
BLOCK_SIZE = 30
WIDTH, HEIGHT = 10, 20  # Tamanho do grid

# Formas das peças
SHAPES = [
    [['🐱']],  # 1x1
    [['🐱', '🐱']],  # 1x2
    [['🐱', '🐱', '🐱']],  # 1x3
    [['🐱', '🐱', '🐱', '🐱']],  # 1x4
    [[' ', '🐱'], ['🐱', '🐱']],  # L invertido
    [['🐱', '🐱'], ['🐱 ', ' '], ['🐱', '🐱']],  # T normal
    [['🐱', '🐱'], [' ', '🐱'], ['🐱', '🐱']],  # T invertido
    [['🐱', ' '], ['🐱', '🐱']],  # L normal
    [['🐱', '🐱'], ['🐱', ' ']],  # Z
]

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)
]

# Definição das velocidades para cada nível
SPEEDS = [500, 400, 300, 200, 100]  # Velocidades em milissegundos

class Piece:
    def __init__(self):
        self.shape = self.get_shape()
        self.color = random.choice(COLORS)
        self.x = WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def get_shape(self):
        shapes_with_weights = [
            (SHAPES[0], 1),
            (SHAPES[1], 1),
            (SHAPES[2], 2),
            (SHAPES[3], 1),
            (SHAPES[4], 1),
            (SHAPES[5], 1),
            (SHAPES[6], 2),
            (SHAPES[7], 1),
            (SHAPES[8], 1),
        ]
        total_weight = sum(weight for _, weight in shapes_with_weights)
        rand_value = random.randint(1, total_weight)

        for shape, weight in shapes_with_weights:
            if rand_value <= weight:
                return shape
            rand_value -= weight

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def clear_lines(board, revealed_rows):
    lines_cleared = 0
    for i in range(len(board)):
        if all(board[i][j] != ' ' for j in range(WIDTH)):
            board.pop(i)
            board.insert(0, [' ' for _ in range(WIDTH)])
            revealed_rows.pop(i)
            revealed_rows.insert(0, True)  # Revelar a linha do topo
            lines_cleared += 1
    return lines_cleared

def draw_board(screen, piece, board, revealed_rows, background_image, show_congratulations):
    # Se o jogo foi concluído, desenhar a imagem completa
    if show_congratulations:
        screen.blit(background_image, (0, 50))  # Desenha a imagem completa
    else:
        # Desenhar as linhas do tabuleiro
        for i, row in enumerate(board):
            for j, block in enumerate(row):
                if block != ' ':
                    pygame.draw.rect(screen, (255, 255, 255), (j * BLOCK_SIZE, i * BLOCK_SIZE + 50, BLOCK_SIZE, BLOCK_SIZE))
                    font = pygame.font.Font(None, 40)
                    text = font.render(block, True, (255, 255, 255))
                    screen.blit(text, (j * BLOCK_SIZE + 5, i * BLOCK_SIZE + 55))

        # Desenhar a peça atual
        for i, row in enumerate(piece.shape):
            for j, block in enumerate(row):
                if block != ' ':
                    pygame.draw.rect(screen, piece.color, ((piece.x + j) * BLOCK_SIZE, (piece.y + i) * BLOCK_SIZE + 50, BLOCK_SIZE, BLOCK_SIZE))
                    font = pygame.font.Font(None, 40)
                    text = font.render(block, True, (0, 0, 0))
                    screen.blit(text, ((piece.x + j) * BLOCK_SIZE + 5, (piece.y + i) * BLOCK_SIZE + 55))

        # Revelar imagem nas linhas concluídas
        for i, revealed in enumerate(revealed_rows):
            if revealed:
                screen.blit(background_image, (0, 50 + i * BLOCK_SIZE), pygame.Rect(0, i * BLOCK_SIZE, WIDTH * BLOCK_SIZE, BLOCK_SIZE))

def draw_buttons(screen):
    font = pygame.font.Font(None, 18)  # 75% menor que os botões

    restart_button = pygame.Rect(10, 10, 80, 30)
    pause_button = pygame.Rect(100, 10, 80, 30)
    play_button = pygame.Rect(200, 10, 80, 30)

    pygame.draw.rect(screen, (200, 200, 200), restart_button)
    pygame.draw.rect(screen, (200, 200, 200), pause_button)
    pygame.draw.rect(screen, (200, 200, 200), play_button)

    restart_text = font.render('Restart', True, (0, 0, 0))
    pause_text = font.render('Pause', True, (0, 0, 0))
    play_text = font.render('Play', True, (0, 0, 0))

    screen.blit(restart_text, (restart_button.x + (restart_button.width - restart_text.get_width()) // 2,
                               restart_button.y + (restart_button.height - restart_text.get_height()) // 2))
    screen.blit(pause_text, (pause_button.x + (pause_button.width - pause_text.get_width()) // 2,
                             pause_button.y + (pause_button.height - pause_text.get_height()) // 2))
    screen.blit(play_text, (play_button.x + (play_button.width - play_text.get_width()) // 2,
                            play_button.y + (play_button.height - play_text.get_height()) // 2))

    return restart_button, pause_button, play_button

def check_collision(piece, board):
    for i, row in enumerate(piece.shape):
        for j, block in enumerate(row):
            if block != ' ':
                # Verifica se a peça está dentro dos limites do tabuleiro
                if (piece.x + j < 0 or piece.x + j >= WIDTH or piece.y + i >= HEIGHT):
                    return True
                # Verifica se colide com outras peças
                if piece.y + i >= 0 and board[piece.y + i][piece.x + j] != ' ':
                    return True
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE + 50))
    pygame.display.set_caption("Jogo do Gatinho - Estilo Tetris")

    clock = pygame.time.Clock()
    piece = Piece()
    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    revealed_rows = [False for _ in range(HEIGHT)]

    background_image = pygame.image.load('gatinhos.png')
    background_image = pygame.transform.scale(background_image, (WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE))

    level = 0
    score = 0
    game_over = False
    paused = False
    last_drop_time = pygame.time.get_ticks()
    lines_cleared_total = 0  # Contador de linhas completas

    while True:
        current_time = pygame.time.get_ticks()

        if not paused and not game_over and current_time - last_drop_time > SPEEDS[level]:
            piece.y += 1

            if check_collision(piece, board):
                piece.y -= 1
                for i, row in enumerate(piece.shape):
                    for j, block in enumerate(row):
                        if block != ' ':
                            board[piece.y + i][piece.x + j] = block
                lines_cleared = clear_lines(board, revealed_rows)
                lines_cleared_total += lines_cleared  # Atualiza o total de linhas limpas
                score += lines_cleared
                if lines_cleared > 0:
                    level = min(level + lines_cleared // 10, len(SPEEDS) - 1)

                piece = Piece()
                
                # Verifica Game Over
                if check_collision(piece, board):
                    game_over = True  # Muda para True ao invés de fechar o jogo

            last_drop_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                restart_button, pause_button, play_button = draw_buttons(screen)
                if restart_button.collidepoint(x, y):
                    piece = Piece()
                    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
                    revealed_rows = [False for _ in range(HEIGHT)]
                    level = 0
                    score = 0
                    paused = False
                    game_over = False  # Reinicia o estado do jogo
                    lines_cleared_total = 0  # Reinicia o contador de linhas
                elif pause_button.collidepoint(x, y):
                    paused = True
                elif play_button.collidepoint(x, y):
                    paused = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.x -= 1
                    if check_collision(piece, board):
                        piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    piece.x += 1
                    if check_collision(piece, board):
                        piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    piece.y += 1
                    if check_collision(piece, board):
                        piece.y -= 1
                elif event.key == pygame.K_SPACE:
                    piece.rotate()
                    if check_collision(piece, board):
                        piece.rotate()  # Reverte a rotação se houver colisão

        screen.fill((0, 0, 0))  # Limpa a tela
        show_congratulations = lines_cleared_total >= 5  # Verifica se 5 linhas foram completadas
        draw_board(screen, piece, board, revealed_rows, background_image, show_congratulations)
        draw_buttons(screen)

        # Exibe mensagem de Congratulations se 5 linhas forem completadas
        if show_congratulations and not game_over:
            font = pygame.font.Font(None, 50)
            text = font.render("Congratulations!", True, (255, 0, 0))
            screen.blit(text, (WIDTH * BLOCK_SIZE // 2 - text.get_width() // 2, HEIGHT * BLOCK_SIZE // 2 - text.get_height() // 2))

        pygame.display.flip()  # Atualiza a tela
        clock.tick(60)  # Limita a 60 FPS

if __name__ == "__main__":
    main()