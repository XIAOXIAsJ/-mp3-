import subprocess
import sys

print("第一步：正在把录音转换成文字……")
subprocess.run([sys.executable, "transcribe.py"], check=True)

print("第二步：正在生成听课总结……")
subprocess.run([sys.executable, "summarize.py"], check=True)

print("全部完成！请打开 summary.md")