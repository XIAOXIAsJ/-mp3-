from faster_whisper import WhisperModel

print("正在加载语音识别模型，请稍候……")

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

print("正在识别录音……")

segments, info = model.transcribe(
    "lesson.mp3",
    language="zh"
)

text = ""

for segment in segments:
    text += segment.text + "\n"

with open("transcript.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("识别完成！文字已保存到 transcript.txt")