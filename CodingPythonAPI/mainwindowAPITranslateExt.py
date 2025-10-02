import requests
from CodingPythonAPI.mainwindowAPITranslate import Ui_MainWindow


class mainwindowAPITranslateExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.translate_text)

    def showWindow(self):
        self.MainWindow.show()

    def translate_text(self):
        api_key = "AIzaSyC5Zqr-D9HaSvK3WiMbGwRYegHCt4dTiGA"
        text_to_translate = self.lineEditInput.text()
        source_lang = self.comboBoxSource.currentText()
        target_lang = self.comboBoxTarget.currentText()

        url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
        params = {
            'q': text_to_translate,
            'source': source_lang,
            'target': target_lang,
        }

        try:
            response = requests.post(url, params=params)
            data = response.json()
            print(data)

            if "data" in data:
                translated_text = data['data']['translations'][0]['translatedText']
                self.labelKetqua.setText(translated_text)
            else:
                # show API error
                self.labelKetqua.setText("API Error: " + str(data))
        except Exception as e:
            self.labelKetqua.setText("Error: " + str(e))

