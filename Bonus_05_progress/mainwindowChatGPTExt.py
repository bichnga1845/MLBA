import openai
import requests
from Bonus_05_progress.mainwindowChatGPT import Ui_MainWindow
import openai

class mainwindowChatGPTExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.translate_text)

    def showWindow(self):
        self.MainWindow.show()

    def translate_text(self):
        api_key = "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"  # 🔑 Thay API key của bạn vào đây
        # dạ api này hết hạn nên e để tầy xem code ạ, do no yeu cauco phi a
        text_to_translate = self.lineEdit.text().strip()

        if not text_to_translate:
            self.labelKetqua.setText("Vui lòng nhập văn bản cần dịch!")
            return

        # mặc định dịch sang tiếng Việt
        target_lang = "Vietnamese"

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": f"You are a translator that translates text into {target_lang}."},
                {"role": "user", "content": text_to_translate}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            print(result)

            if "choices" in result:
                translated_text = result["choices"][0]["message"]["content"]
                self.labelKetqua.setText(translated_text.strip())
            else:
                self.labelKetqua.setText("API Error: " + str(result))
        except Exception as e:
            self.labelKetqua.setText("Error: " + str(e))
