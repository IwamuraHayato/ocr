import streamlit as st
from PIL import Image
import pyocr
import platform

if platform.system() == "Windows":
    pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
else:
    pyocr.tesseract.TESSERACT_CMD =  r'/opt/homebrew/bin/tesseract'

set_language_list = {
    "日本語" :"jpn",
    "英語" :"eng",
}

st.title("文字認識アプリ")
set_language = st.selectbox("音声認識する言語を選んでください。",set_language_list.keys()) # 言語選択のためのリスト
file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください。")

if(file_upload !=None):
    
    st.image(file_upload)# 画像分析する画像を表示

    #OCRエンジンを取得
    engines = pyocr.get_available_tools() # pyocrが認識できるOCR外部ツールを検知
    engine = engines[0] # ツールを複数選択して、エラーにならないように１つだけ選択
    
    txt = engine.image_to_string(Image.open("moji.png"), lang="jpn")
    st.write(txt) # 分析結果を表示

    st.write("感情分析の結果") # 案内表示
    from asari.api import Sonar
    sonar = Sonar()
    res = sonar.ping(text=txt)
    st.write(res["classes"]) 