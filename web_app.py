import subprocess
import sys
from pathlib import Path

import streamlit as st


project_dir = Path(__file__).parent

st.set_page_config(page_title="AI 听课总结", page_icon="🎧")
st.title("🎧 AI 听课总结")
st.write("上传课堂录音，自动生成课程总结。")

audio_file = st.file_uploader("请选择 MP3 录音", type=["mp3"])

if audio_file is not None:
    st.audio(audio_file)

    if st.button("开始总结"):
        audio_path = project_dir / "lesson.mp3"

        try:
            # Windows 上旧的 lesson.mp3 可能被标记为只读，先恢复写权限再替换。
            if audio_path.exists():
                audio_path.chmod(0o666)
                audio_path.unlink()
            audio_path.write_bytes(audio_file.getbuffer())

            with st.spinner("正在处理录音，请耐心等待……"):
                subprocess.run(
                    [sys.executable, "run_all.py"],
                    cwd=project_dir,
                    check=True,
                )

            summary_path = project_dir / "summary.md"
            summary = summary_path.read_text(encoding="utf-8")

            st.success("总结完成！")
            st.markdown(summary)
            st.download_button(
                "下载总结",
                data=summary,
                file_name="summary.md",
                mime="text/markdown",
            )
        except Exception as error:
            st.error("处理失败：请确认 lesson.mp3 没有被其他程序占用")
            st.code(str(error))
