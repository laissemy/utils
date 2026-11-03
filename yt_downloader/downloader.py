from pathlib import Path
from typing import Callable, Optional
from yt_dlp import YoutubeDL


def baixar(
    url: str,
    path: str = "downloads",
    apenas_audio: bool = False,
    qualidade: Optional[int] = 720,
    playlist: bool = False,
    progresso: Optional[Callable[[dict], None]] = None,
):

  
    Path(path).mkdir(parents=True, exist_ok=True)
    opcoes = {
        "outtmpl": str(Path(path) / "%(title)s.%(ext)s"),
        "noplaylist": not playlist,
        "quiet": True,
        "no_warnings": True,
    }

    if progresso:
        opcoes["progress_hooks"] = [progresso]


    if apenas_audio:
        opcoes["format"] = "bestaudio/best"
        opcoes["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    else:
        if qualidade:
            opcoes["format"] = (
                f"bestvideo[height<={qualidade}]+bestaudio/best[height<={qualidade}]"
            )
        else:
            opcoes["format"] = "bestvideo+bestaudio/best"
        opcoes["merge_output_format"] = "mp4"

    with YoutubeDL(opcoes) as ydl:
        ydl.download([url])