import argparse
import sys
 
from .downloader import baixar
 
QUALIDADES = {
    "1": ("Melhor qualidade disponível", None),
    "2": ("1080p", 1080),
    "3": ("720p", 720),
    "4": ("480p", 480),
    "5": ("360p", 360),
}
 
 
def mostrar_progresso(d: dict) -> None:
    if d["status"] == "downloading":
        porcentagem = d.get("_percent_str", "").strip()
        velocidade = d.get("_speed_str", "").strip()
        print(f"\rBaixando: {porcentagem} ({velocidade})", end="", flush=True)
    elif d["status"] == "finished":
        print("\nDownload concluído, processando arquivo...")
 
 
def perguntar(titulo: str, opcoes: dict) -> str:
    print(f"\n{titulo}")
    for chave, valor in opcoes.items():
        nome = valor[0] if isinstance(valor, tuple) else valor
        print(f"  {chave}) {nome}")
    while True:
        escolha = input("Escolha uma opção: ").strip()
        if escolha in opcoes:
            return escolha
        print("Opção inválida, tente novamente.")
 
 
def menu_interativo() -> tuple:
    formato = perguntar("O que você quer baixar?", {"1": "Vídeo (MP4)", "2": "Só o áudio (MP3)"})
    if formato == "2":
        return True, None
 
    qualidade = perguntar("Qual qualidade de vídeo?", QUALIDADES)
    return False, QUALIDADES[qualidade][1]
 
 
def main() -> int:
    parser = argparse.ArgumentParser(
        description="Baixa vídeos e áudios do YouTube usando yt-dlp."
    )
    parser.add_argument("url", nargs="?", help="URL do vídeo ou playlist")
    parser.add_argument("-o", "--pasta", default="downloads", help="pasta de destino")
    parser.add_argument("-a", "--audio", action="store_true", help="baixar só o áudio (MP3)")
    parser.add_argument("-q", "--qualidade", type=int, help="altura máxima, ex.: 720")
    parser.add_argument("-p", "--playlist", action="store_true", help="baixar a playlist inteira")
    args = parser.parse_args()
 
    url = args.url or input("Cole a URL do vídeo: ").strip()
    if not url:
        print("Nenhuma URL informada.", file=sys.stderr)
        return 1
 
    if args.audio or args.qualidade:
        apenas_audio, qualidade = args.audio, args.qualidade
    else:
        apenas_audio, qualidade = menu_interativo()
 
    try:
        baixar(
            url=url,
            path=args.pasta,
            apenas_audio=apenas_audio,
            qualidade=qualidade,
            playlist=args.playlist,
            progresso=mostrar_progresso,
        )
    except Exception as erro:
        print(f"\nErro: {erro}", file=sys.stderr)
        return 1
 
    print("Pronto!")
    return 0
 
 
if __name__ == "__main__":
    sys.exit(main())