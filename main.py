import playsound3
import asyncio
import rich

def get_music() -> Sound:
  return playsound3.playsound("assets/music.mp3", False)

def main():
  music = get_music()

  rich.print("[blue]Program  started[/blue]")

if __name__ == "__main__":
  main()