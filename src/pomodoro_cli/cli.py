import typer
import pomodoro
from rich.console import Console

console = Console()
app = typer.Typer()

@app.command()
def cycle(work: int, long_break: int, short_break: int, cycles: int):
    pomodoro.pomodoro_cycle(work=work, long_break=long_break, short_break=short_break, cycles=cycles)
    console.print("Cycles completed!", style="blue")

@app.command()
def start():
    console.print("Work: 25 minutes \nShort break: 5 minutes \nLong break: 15 minutes", style="blue")
    pomodoro.pomodoro_cycle()
    console.print("Cycles completed!", style="blue")
    
if __name__ == "__main__":
    app()
    