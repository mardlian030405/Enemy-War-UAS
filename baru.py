import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1000
FPS = 60

# Inisialisasi layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game dengan Objek Rumah dan Batu")
clock = pygame.time.Clock()

# Kelas Pemain
class Player:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speed = 5
        self.hp = 100

    def move(self, keys, obstacles):
        initial_position = self.rect.topleft

        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.rect.topleft = initial_position

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        draw_text(f"You: {self.hp} HP", font, (255, 255, 255), surface, 10, 10)

# Kelas Objek
class Obstacle:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

# Kelas Musuh
class Enemy:
    def __init__(self, x, y, width, height, image_path, hp):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speed = 2
        self.hp = hp

    def move_towards_player(self, player, obstacles):
        initial_position = self.rect.topleft

        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.rect.topleft = initial_position
                break

        initial_position = self.rect.topleft

        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.rect.topleft = initial_position
                break

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        draw_text(f"Enemy: {self.hp} HP", font, (255, 0, 0), surface, self.rect.x, self.rect.y - 20)

# Kelas Utama Game
class Game:
    def __init__(self):
        # Latar belakang
        self.bg_image = pygame.image.load("imageasd.jpg")
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Pemain
        self.player = Player(100, 100, 60, 60, "player.png")

        # Musuh
        self.level = 1
        self.enemy = self.create_enemy()

        # Tanaman
        self.plants = [
            Obstacle(random.randint(0, SCREEN_WIDTH - 32), random.randint(0, SCREEN_HEIGHT - 32), 46, 50, "pohon.png")
            for _ in range(10)
        ]

        # Rumah
        self.houses = [
            Obstacle(200, 150, 140, 100, "rumah.png"),
            Obstacle(500, 300, 140, 100, "rumah.png")
        ]

        # Batu
        self.rocks = [
            Obstacle(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40), 40, 40, "batu.png")
            for _ in range(10)
        ]

    def create_enemy(self):
        enemy_hp = 50 + (self.level - 1) * 20
        return Enemy(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40), 40, 40, "enemy.png", enemy_hp)

    def check_battle(self):
        if self.player.rect.colliderect(self.enemy.rect):
            self.enemy.hp -= 10
            self.player.hp -= 5

            if self.enemy.hp <= 0:
                print(f"Enemy defeated! Level up to {self.level + 1}")
                self.level += 1
                self.enemy = self.create_enemy()

        # Periksa jika pemain kalah
        if self.player.hp <= 0:
            self.game_over_screen()

    def game_over_screen(self):
        screen.fill((0, 0, 0))  # Layar hitam
        draw_text("GAME OVER", font, (255, 0, 0), screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        draw_text("Press R to Restart", font, (255, 255, 255), screen, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)
        pygame.display.flip()

        # Tunggu pemain untuk memulai ulang
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    waiting = False
                    self.reset_game()

    def reset_game(self):
        # Reset semua atribut permainan
        self.player = Player(100, 100, 60, 60, "player.png")
        self.level = 1
        self.enemy = self.create_enemy()
        self.plants = [
            Obstacle(random.randint(0, SCREEN_WIDTH - 32), random.randint(0, SCREEN_HEIGHT - 32), 46, 50, "pohon.png")
            for _ in range(10)
        ]
        self.houses = [
            Obstacle(200, 150, 140, 100, "rumah.png"),
            Obstacle(500, 300, 140, 100, "rumah.png")
        ]
        self.rocks = [
            Obstacle(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40), 40, 40, "batu.png")
            for _ in range(10)
        ]

    def run(self):
        running = True
        obstacles = self.plants + self.houses + self.rocks

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys, obstacles)

            # Gerakan musuh
            self.enemy.move_towards_player(self.player, obstacles)

            # Periksa battle
            self.check_battle()

            # Gambar latar belakang
            screen.blit(self.bg_image, (0, 0))

            # Gambar semua objek
            self.player.draw(screen)
            if self.enemy.hp > 0:
                self.enemy.draw(screen)
            for plant in self.plants:
                plant.draw(screen)
            for house in self.houses:
                house.draw(screen)
            for rock in self.rocks:
                rock.draw(screen)

            # Refresh layar
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

# Fungsi untuk menggambar teks
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Font
font = pygame.font.Font(None, 36)

# Jalankan game
if __name__ == "__main__":
    game = Game()
    game.run()
