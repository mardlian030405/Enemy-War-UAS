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
pygame.display.set_caption("Game dengan Level dan Pemenang")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Fungsi untuk menggambar teks
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Kelas Dasar GameObject
class GameObject:
    """
    Kelas dasar yang merepresentasikan semua objek dalam game.
    Menggunakan konsep inheritance agar kelas lain dapat mewarisi atribut dan metode dari kelas ini.
    """
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)  # Atribut untuk posisi dan ukuran
        self.image = pygame.image.load(image_path)  # Gambar objek
        self.image = pygame.transform.scale(self.image, (width, height))  # Skala gambar

    def draw(self, surface):
        """Metode untuk menggambar objek ke layar."""
        surface.blit(self.image, (self.rect.x, self.rect.y))

# Kelas Pemain
class Player(GameObject):
    
    def __init__(self, x, y, width, height, image_path):
        super().__init__(x, y, width, height, image_path)  # Memanggil konstruktor dari kelas induk
        self.speed = 5  # Kecepatan pemain
        self.hp = 500  # Health point pemain

    def move(self, keys, obstacles):
        """
        Metode untuk menggerakkan pemain dengan kontrol keyboard.
        Menggunakan parameter obstacles untuk mendeteksi tabrakan.
        """
        initial_position = self.rect.topleft  # Menyimpan posisi awal untuk rollback jika ada tabrakan

        # Menggerakkan pemain berdasarkan input keyboard
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed

        # Memeriksa tabrakan dengan obstacle
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.rect.topleft = initial_position  # Kembali ke posisi awal jika tabrakan terjadi

    def draw(self, surface):
        """Menggambar pemain ke layar dan menampilkan status HP."""
        super().draw(surface)  # Memanggil metode draw dari kelas induk
        draw_text(f"You: {self.hp} HP", font, (255, 255, 255), surface, 10, 10)

# Kelas Musuh
class Enemy(GameObject):
    """
    Kelas yang merepresentasikan musuh, turunan dari GameObject.
    Menambahkan atribut dan metode untuk AI sederhana.
    """
    def __init__(self, x, y, width, height, image_path, hp):
        super().__init__(x, y, width, height, image_path)  # Memanggil konstruktor dari kelas induk
        self.speed = 2  # Kecepatan musuh
        self.hp = hp  # Health point musuh

    def move_towards_player(self, player, obstacles):
        """
        Metode untuk membuat musuh bergerak mendekati pemain.
        Menghindari tabrakan dengan obstacles.
        """
        initial_position = self.rect.topleft

        # Logika untuk bergerak mendekati pemain secara horizontal
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        # Menghindari tabrakan dengan obstacles
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.rect.topleft = initial_position
                break

        initial_position = self.rect.topleft

        # Logika untuk bergerak mendekati pemain secara vertikal
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

        # Menghindari tabrakan dengan obstacles
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.rect.topleft = initial_position
                break

    def draw(self, surface):
        """Menggambar musuh ke layar dan menampilkan status HP."""
        super().draw(surface)  # Memanggil metode draw dari kelas induk
        draw_text(f"Enemy: {self.hp} HP", font, (255, 0, 0), surface, self.rect.x, self.rect.y - 20)

# Kelas Utama Game
class Game:
    """
    Kelas utama yang mengatur seluruh jalannya permainan.
    Menggunakan komposisi untuk mengelola pemain, musuh, dan obstacles.
    """
    def __init__(self):
        # Latar belakang
        self.bg_image = pygame.image.load("assets/map2.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Pemain
        self.player = Player(100, 100, 60, 60, "assets/player.png")

        # Musuh
        self.level = 1  # Level awal permainan
        self.enemy = self.create_enemy()

        # Obstacle
        self.plants = [
            GameObject(random.randint(0, SCREEN_WIDTH - 32), random.randint(0, SCREEN_HEIGHT - 32), 60, 70, "assets/pohon.png")
            for _ in range(10)
        ]
        self.houses = [
            GameObject(200, 150, 140, 100, "assets/rumah.png"),
            GameObject(500, 300, 140, 100, "assets/rumah.png")
        ]
        self.rocks = [
            GameObject(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40), 40, 40, "assets/batu.png")
            for _ in range(10)
        ]

    def create_enemy(self):
        """
        Metode untuk membuat musuh berdasarkan level.
        HP dan gambar musuh berubah seiring kenaikan level.
        """
        enemy_hp = 50 + (self.level - 1) * 20
        enemy_images = ["assets/enemy_level_1.png", "assets/enemy_level_2.png", "assets/enemy.png", "assets/enemy_level_5.png"]
        enemy_image = enemy_images[min(self.level - 1, len(enemy_images) - 1)]
        return Enemy(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40), 60, 60, enemy_image, enemy_hp)

    def check_battle(self):
        """
        Metode untuk memeriksa apakah pemain bertarung dengan musuh.
        Mengurangi HP dari pemain dan musuh jika mereka bertabrakan.
        """
        if self.player.rect.colliderect(self.enemy.rect):
            self.enemy.hp -= 10
            self.player.hp -= 5

            if self.enemy.hp <= 0:
                if self.level == 4:
                    self.win_screen()  # Menampilkan layar kemenangan jika level terakhir selesai
                else:
                    print(f"Enemy defeated! Level up to {self.level + 1}")
                    self.level += 1
                    self.enemy = self.create_enemy()

        if self.player.hp <= 0:
            self.game_over_screen()  # Menampilkan layar game over jika pemain mati

    def game_over_screen(self):
        """Menampilkan layar game over."""
        screen.fill((0, 0, 0))
        draw_text("GAME OVER", font, (255, 0, 0), screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        draw_text("Press R to Restart", font, (255, 255, 255), screen, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        self.wait_for_restart()

    def win_screen(self):
        """Menampilkan layar kemenangan."""
        screen.fill((0, 255, 0))
        draw_text("YOU WIN!", font, (0, 0, 255), screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        pygame.display.flip()
        self.wait_for_restart()

    def wait_for_restart(self):
        """
        Menunggu pemain untuk memulai ulang permainan.
        Menggunakan pendekatan event-driven untuk mendeteksi input.
        """
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
        """Mereset permainan ke kondisi awal."""
        self.__init__()  # Memanggil ulang konstruktor untuk reset

    def run(self):
        """
        Metode utama untuk menjalankan loop game.
        Melibatkan semua komponen seperti pemain, musuh, dan obstacles.
        """
        obstacles = self.plants + self.houses + self.rocks

        while True:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Pergerakan pemain
            keys = pygame.key.get_pressed()
            self.player.move(keys, obstacles)

            # Pergerakan musuh
            self.enemy.move_towards_player(self.player, obstacles)

            # Logika pertempuran
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

            # Perbarui layar
            pygame.display.flip()
            clock.tick(FPS)

# Jalankan game
if __name__ == "__main__":
    game = Game()  # Membuat instance dari kelas Game
    game.run()  # Menjalankan game
