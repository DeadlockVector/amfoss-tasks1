from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt 
import os

class PokemonWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.w = None        
        self.setFixedSize(550, 700)
        self.setWindowTitle("Pokédex")

        self.right_button = QPushButton("Right", self)
        self.right_button.setGeometry(325, 625, 200, 50)
        self.right_button.clicked.connect(self.goRight)

        self.left_button = QPushButton("Left", self)
        self.left_button.setGeometry(25, 625, 200, 50)
        self.left_button.clicked.connect(self.goLeft)

        self.label_pokemonName = QLabel("", self)
        self.label_pokemonName.setGeometry(255, 540, 200, 50)

        self.list_images = []
        self.image_index = 0
        for path in os.listdir('./task-08/pokemon_images'):
            self.list_images.append(f"./task-08/pokemon_images/{path}")
        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(25, 25, 500, 500)
        if len(self.list_images) != 0:
            image_pixmap = QPixmap(self.list_images[self.image_index])
            self.pokemon_image_label.setPixmap(image_pixmap.scaled(self.pokemon_image_label.size(), Qt.KeepAspectRatio))
            self.label_pokemonName.setText(self.list_images[self.image_index][25:-4].capitalize())

    def goLeft(self):
        # Decrement the image index
        self.image_index -= 1
        if self.image_index < 0:
            self.image_index = len(self.list_images) - 1  # Wrap around to the last image if at the beginning
        self.update_image()
        
    def goRight(self):
        # Increment the image index
        self.image_index += 1
        if self.image_index >= len(self.list_images):
            self.image_index = 0  # Wrap around to the first image if at the end
        self.update_image()

    def update_image(self):
        image_pixmap = QPixmap(self.list_images[self.image_index])
        self.pokemon_image_label.setPixmap(image_pixmap.scaled(self.pokemon_image_label.size(), Qt.KeepAspectRatio))
        self.label_pokemonName.setText(self.list_images[self.image_index][25:-4].capitalize())

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = PokemonWindow()
    window.show()
    sys.exit(app.exec())


