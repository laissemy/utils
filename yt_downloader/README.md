# YT Downloader

Baixador de vídeos e áudios do YouTube feito em Python, usando o [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Recursos

| Recurso | Descrição |
|---------|-----------|
| Vídeo | Baixa em MP4, com escolha de qualidade (360p até 1080p ou a melhor disponível) |
| Áudio | Baixa só o áudio em MP3 |
| Playlist | Baixa uma playlist inteira de uma vez |
| Menu | Pergunta o formato e a qualidade se você não passar opções |

## Requisitos

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html) instalado e no PATH

## Como usar

```bash
git clone https://github.com/laissemy/yt-downloader.git
cd yt-downloader
pip install -r requirements.txt
```

Rode e siga o menu:

```bash
python -m yt_downloader
```

Ou passe as opções direto:

```bash
python -m yt_downloader "URL" -a                  # só áudio (MP3)
python -m yt_downloader "URL" -q 480              # vídeo até 480p
python -m yt_downloader "URL" -p -o minha_pasta   # playlist em outra pasta
```

## Opções

| Opção | Descrição |
|-------|-----------|
| `-o`, `--pasta` | Pasta de destino (padrão: `downloads`) |
| `-a`, `--audio` | Baixar apenas o áudio em MP3 |
| `-q`, `--qualidade` | Altura máxima do vídeo, ex.: 720 |
| `-p`, `--playlist` | Baixar a playlist inteira |

## Usando em outro código

```python
from yt_downloader import baixar

baixar("URL", path="videos", qualidade=1080)
baixar("URL", apenas_audio=True)
```

## Estrutura

```
yt-downloader/
├── yt_downloader/
│   ├── downloader.py   # lógica do download
│   └── cli.py          # menu e comandos do terminal
├── requirements.txt
└── README.md
```

## Problemas comuns

Se o download parar de funcionar, atualize o yt-dlp:

```bash
pip install -U yt-dlp
```


feito por [@laissemy](https://github.com/laissemy).
