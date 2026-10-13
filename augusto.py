```python
import pygame
import random
import math
import sys

pygame.init()

LARGURA, ALTURA = 1000, 650
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("AUGUSTO.EXE - SISTEMA DE ANIVERSÁRIO")

clock = pygame.time.Clock()

BRANCO = (255, 255, 255)
PRETO = (10, 0, 20)

fonte_gigante = pygame.font.SysFont("arialblack", 53)
fonte_media = pygame.font.SysFont("arialblack", 30)
fonte_pequena = pygame.font.SysFont("consolas", 20)

particulas = []
estrelas = [
    (random.randrange(LARGURA), random.randrange(ALTURA))
    for _ in range(150)
]

inicio = pygame.time.get_ticks()
explodir = False


def criar_explosao(x, y):
    for _ in range(100):
        angulo = random.random() * math.tau
        velocidade = random.uniform(2, 10)

        particulas.append([
            x, y,
            math.cos(angulo) * velocidade,
            math.sin(angulo) * velocidade,
            random.randint(3, 8),
            random.choice([
                (255, 0, 100),
                (0, 255, 255),
                (255, 255, 0),
                (150, 0, 255),
                (0, 255, 100)
            ])
        ])


def texto_centralizado(texto, fonte, cor, y):
    imagem = fonte.render(texto, True, cor)
    retangulo = imagem.get_rect(center=(LARGURA // 2, y))
    tela.blit(imagem, retangulo)


rodando = True

while rodando:
    tempo = pygame.time.get_ticks() / 1000
    matiz = int((math.sin(tempo * 3) + 1) * 127)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            criar_explosao(*evento.pos)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                for _ in range(5):
                    criar_explosao(
                        random.randint(100, 900),
                        random.randint(100, 550)
                    )

            if evento.key == pygame.K_ESCAPE:
                rodando = False

    # FUNDO CÓSMICO
    tela.fill((15, 0, 30))

    # ESTRELAS
    for x, y in estrelas:
        brilho = random.randint(100, 255)
        pygame.draw.circle(
            tela, (brilho, brilho, brilho),
            (x, y), random.choice([1, 1, 2])
        )

    # BARRAS RGB
    for i in range(0, LARGURA, 20):
        cor = (
            int((math.sin(tempo * 4 + i * 0.02) + 1) * 127),
            int((math.sin(tempo * 3 + i * 0.03 + 2) + 1) * 127),
            int((math.sin(tempo * 5 + i * 0.01 + 4) + 1) * 127)
        )
        pygame.draw.rect(tela, cor, (i, 0, 10, ALTURA))

    # JANELA CENTRAL
    pygame.draw.rect(
        tela, PRETO,
        (55, 45, 890, 560),
        border_radius=25
    )

    pygame.draw.rect(
        tela, (255, matiz, 255),
        (55, 45, 890, 560), 4,
        border_radius=25
    )

    # ALERTA
    texto_centralizado(
        "!!! ALERTA DE ANIVERSARIO !!!",
        fonte_media,
        (255, matiz, 50),
        100
    )

    # NOME DO ALVO
    texto_centralizado(
        "AUGUSTO.EXE",
        fonte_gigante,
        (255, 50, 180),
        180
    )

    # MENSAGEM PRINCIPAL
    texto_centralizado(
        "PARABENS MALDITO!!",
        fonte_media,
        (0, 255, 255),
        270
    )

    texto_centralizado(
        "MUITOS ANOS DE VIDA",
        fonte_media,
        (255, 255, 0),
        320
    )

    texto_centralizado(
        "DO LADO DA YASMIN",
        fonte_media,
        (255, 100, 200),
        370
    )

    texto_centralizado(
        "STATUS: VELHICE INSTALADA COM SUCESSO",
        fonte_pequena,
        (0, 255, 100),
        445
    )

    texto_centralizado(
        "CLIQUE NA TELA OU APERTE ESPACO",
        fonte_pequena,
        BRANCO,
        495
    )

    texto_centralizado(
        "ESC = FUGIR DA RESPONSABILIDADE",
        fonte_pequena,
        (255, 100, 100),
        535
    )

    # PARTICULAS EXPLOSIVAS
    for p in particulas[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 0.12

        pygame.draw.circle(
            tela, p[5],
            (int(p[0]), int(p[1])),
            max(1, int(p[4]))
        )

        if p[4] <= 0:
            particulas.remove(p)

    # EXPLOSOES ALEATORIAS
    if random.random() < 0.025:
        criar_explosao(
            random.randint(100, 900),
            random.randint(100, 550)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```