from googletrans import Translator
import eel


# googletransをpipする際のバージョンに注意！
# https://qiita.com/gausukyanon/items/0ca0234808d1233989df
# https://qiita.com/_yushuu/items/83c51e29771530646659


def start_program():
    # ウエブコンテンツを持つフォルダー
    eel.init("web")
    # 最初に表示するhtmlページ
    eel.start("index.html", size=(600, 600))


@eel.expose
def translate(inputWord: str, beforeLanguage: str, afterLanguage: str) -> str:
    print("入力されたテキスト", inputWord)
    print("変換前言語", inputWord)
    print("変換する言語", afterLanguage)

    translator = Translator()
    changetext = translator.translate(inputWord, src=beforeLanguage, dest=afterLanguage)
    print("翻訳→", changetext.text)

    return changetext.text


if __name__ == "__main__":
    start_program()
