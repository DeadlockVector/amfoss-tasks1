from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDialog, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests
import shutil
import os

from pokemon_window import PokemonWindow

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        self.w = None        
        self.setFixedSize(850, 500)
        self.setWindowTitle("Pokédex")
        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)

        self.textbox.setStyleSheet("background-color: black; color:white;")
        

        self.background = QLabel(self)
        pixmap = QPixmap("../task-08/assets/landing.jpg")
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, 850, 500)
        self.background.lower()
      
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)
        label1.setStyleSheet("color: white;")

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.getPokeInfo)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capturePoke)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.getPoke)

        
        self.image_label = QLabel(self)
        self.image_label.setGeometry(500, 25, 200, 200)

        self.label2 = QLabel("", self) 
        self.label2.setGeometry(500, 225, 200, 43)
        #self.label2.setStyleSheet("color: white;")

        self.label3 = QLabel("", self) 
        self.label3.setGeometry(500, 245, 250, 43)
        #self.label3.setStyleSheet("color: white;")

        self.label4 = QLabel("", self) 
        self.label4.setGeometry(500, 265, 200, 43)
        #self.label4.setStyleSheet("color: white;")
        
        self.label5 = QLabel("", self) 
        self.label5.setGeometry(500, 285, 200, 43)
        #self.label5.setStyleSheet("color: white;")

        self.label6 = QLabel("", self) 
        self.label6.setGeometry(500, 305, 200, 43)
        #self.label6.setStyleSheet("color: white;")

        self.label7 = QLabel("", self) 
        self.label7.setGeometry(500, 325, 200, 43)
        #self.label7.setStyleSheet("color: white;")

        self.label8 = QLabel("", self) 
        self.label8.setGeometry(500, 345, 200, 43)
        #self.label8.setStyleSheet("color: white;")

        self.label9 = QLabel("", self) 
        self.label9.setGeometry(500, 365, 200, 43)
        #self.label9.setStyleSheet("color: white;")

        self.label10 = QLabel("", self) 
        self.label10.setGeometry(500, 385, 200, 43)
        #self.label10.setStyleSheet("color: white;")

        self.label11 = QLabel("", self) 
        self.label11.setGeometry(500, 405, 200, 43)
        #self.label11.setStyleSheet("color: white;")
    
    def captureConfirmed(self):
        capture_message = QDialog()
        capture_message.setWindowTitle("Captured!")
        capture_message.setFixedSize(300, 100)
        layout = QVBoxLayout()

        label = QLabel("Pokemon is captured!", capture_message)
        label.setAlignment(Qt.AlignCenter)

        ok_button = QPushButton("OK", capture_message)
        ok_button.clicked.connect(capture_message.accept)

        layout.addWidget(label)
        layout.addWidget(ok_button)

        capture_message.setLayout(layout)
        capture_message.exec_()

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets
    def getPokeInfo(self):

        pokemon_name = self.textbox.text()
        if pokemon_name != "":
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()

                official_artwork_url = response['sprites']['other']['official-artwork']['front_default']
                image_response = requests.get(official_artwork_url, stream=True)
                with open(f"../task-08/{pokemon_name}.png", 'wb') as out_file:
                    shutil.copyfileobj(image_response.raw, out_file)

                image_pixmap = QPixmap(f"../task-08/{pokemon_name}.png")
                self.image_label.setPixmap(image_pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))  
                os.remove(f"../task-08/{pokemon_name}.png")         # no need to download yet

                self.label2.setText(f"Name: {pokemon_name}")

                abilities = ""
                for i in range(len(response['abilities'])):
                    abilities = abilities+", "+response['abilities'][i]['ability']['name']
                self.label3.setText(f"Abilities: {abilities}") 

                type = response['types'][0]['type']['name']
                self.label4.setText(f"Type: {type}")

                self.label5.setText("Stats:")

                hp = response['stats'][0]['base_stat']
                self.label6.setText(f"Hp: {hp}")

                attack = response['stats'][1]['base_stat']
                self.label7.setText(f"Attack: {attack}")

                defense = response['stats'][1]['base_stat']
                self.label8.setText(f"Defense: {defense}")

                special_attack = response['stats'][2]['base_stat']
                self.label9.setText(f"Special Attack: {special_attack}")

                special_defense = response['stats'][3]['base_stat']
                self.label10.setText(f"Special Defense: {special_defense}")

                speed = response['stats'][4]['base_stat']
                self.label11.setText(f"Speed: {speed}")
                self.background.clear()


            except:
                self.label2.setText("API error")    # incase the user isn't a pokemon fan
                self.label3.setText("")
                self.label4.setText("")
                self.label5.setText("")
                self.label6.setText("")
                self.label7.setText("")
                self.label8.setText("")
                self.label9.setText("")
                self.label10.setText("")
                self.label11.setText("")
                self.image_label.clear()
        else:
            self.label2.setText("Please enter a pokemon")

        

    # 2 #
    # Capture the Pokémon i.e. download the image.
    def capturePoke(self):
        pokemon_name = self.textbox.text()
        
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
        official_artwork_url = response['sprites']['other']['official-artwork']['front_default']
        image_response = requests.get(official_artwork_url, stream=True)

        with open(f"../task-08/pokemon_images/{pokemon_name}.png", 'wb') as out_file:
            shutil.copyfileobj(image_response.raw, out_file)
        self.captureConfirmed()


    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.
    def getPoke(self):
        if self.w is None:
            self.w = PokemonWindow()
        self.w.show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())

