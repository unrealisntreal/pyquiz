from modules import sound_player
import rich

def main():
  sound_player.start_music()

  rich.print("[blue]Program  started[/blue]")

  while True:
    import time
    time.sleep(3.0)

if __name__ == "__main__":
  main()