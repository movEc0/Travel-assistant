from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from app_gui1 import Ui_mainwindow
import openai
import requests
import re



def call_ai_api(prompt):
    print("calling api")

    initial_prompt="Structure the request in this exact format:" \
    "Method1(the most applicable to either eco,speed or price eg: Bus,Bike,Train,walk):" \
    "LINEBREAK" \
    "each step needed with prices and locations eg:bus stops, train stations, roads to cycle.also include duration of travel. Add a line break between each" \
    "LINEBREAK" \
    "generate no extra notes,keep it simple and under 50 characters" \
    "" \
    ""

    openai.api_key = 'api key'
    openai.api_base = "server url"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": initial_prompt},
            {"role": "user", "content": prompt},
        ]
    )

    print("Api called")
    main_text=completion.choices[0].message.content
    return main_text



class api_call(QThread):

    response_recieved=pyqtSignal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt=prompt


    def run(self):
        response=call_ai_api(self.prompt)
        self.response_recieved.emit(response)


class MainWindow(QMainWindow, Ui_mainwindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


        
        self.stacked_widget.setCurrentIndex(1)

        self.button_eco.clicked.connect(self.eco_mode)
        self.button_fastest.clicked.connect(self.fast_mode)
        self.button_cost.clicked.connect(self.cost_mode)

        self.current_location_button.clicked.connect(self.current_location)

        self.create_route_button.clicked.connect(self.start_api)

        self.enter_button.clicked.connect(self.change_window)



    def current_location(self):
        
        ip_adress=requests.get("https://api.ipify.org").text
        response=requests.get(f"http://ip-api.com/json/{ip_adress}").json()
        location=response["city"]
        
        self.line_edit_start.setText(location)


    def eco_mode(self):
        
        self.button_fastest.setDisabled(True)
        self.button_cost.setDisabled(True)

        global mode
        mode="eco"


    def fast_mode(self):

        self.button_eco.setDisabled(True)
        self.button_cost.setDisabled(True)

        global mode
        mode="fast"


    def cost_mode(self):

        self.button_fastest.setDisabled(True)
        self.button_eco.setDisabled(True)

        global mode
        mode="cost"
    

    def start_api(self):
        print("connecting")

        self.button_fastest.setDisabled(False)
        self.button_cost.setDisabled(False)
        self.button_eco.setDisabled(False)

        start=self.line_edit_start.text()
        destination=self.line_edit_destination.text()

        self.line_edit_start.setText("")
        self.line_edit_destination.setText("")

        self.heading_box.setPlainText(f"")

        if mode=="eco":
            prompt=f"give instructions the most eco friendly and low emmision way to travel from {start} to {destination}. highlight the modes of transport including prices and which bus stop and number what train station ect in bullet points, keep it concise and simple with no unecesary text in the reply"
            self.heading_box.setPlainText(f"Eco friendly route from {start} to {destination}... ")
            
        elif mode=="fast":
            prompt=f"give instructions the fastest way to travel from {start} to {destination}. highlight the modes of transport including prices and which bus stop and number what train station ect in bullet points, keep it concise and simple with no unecesary text in the reply"
            self.heading_box.setPlainText(f"Fastest route from {start} to {destination}... ")

        elif mode=="cost":
            prompt=f"give instructions the cheapest way to travel from {start} to {destination}. highlight the modes of transport including prices and which bus stop and number what train station ect in bullet points, keep it concise and simple with no unecesary text in the reply"
            self.heading_box.setPlainText(f"Cheapest route from {start} to {destination}... ")

        else:
            quit()

        self.thread=api_call(prompt)
        self.thread.response_recieved.connect(self.display_response)
        self.thread.start()


    def display_response(self,response):

        formatted_text = re.sub(r'\*\*(.*?)\*\*', r'~\1~', response)
        formatted_text = re.sub(r'\*(.*?)\*', r'~\1~', formatted_text)
        self.output_box.setPlainText(formatted_text)


    def change_window(self):
        self.stacked_widget.setCurrentIndex(0)


def main():
    app=QApplication([])
    window=MainWindow()
    app.exec_()


main()   