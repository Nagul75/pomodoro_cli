import time
from datetime import timedelta

from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()


def format_time(seconds: int) -> str:
    return str(timedelta(seconds=seconds))


def pomodoro_session(label: str, duration_minutes: int) -> None:
    total_seconds = duration_minutes * 60
    start = time.monotonic()

    with Live(console=console, refresh_per_second=4) as live:
        while True:
            elapsed = int(time.monotonic() - start)
            remaining = total_seconds - elapsed

            if remaining <= 0:
                break

            text = Text.assemble(
                (f"{label}\t", "red"),
                (format_time(remaining), "green"),
            )

            live.update(text)
            time.sleep(1)

    console.print(f"{label} complete!", style="bold green")
    console.print("\a", end="")  # terminal bell


def pomodoro_cycle(work=25, short_break=5, long_break=15, cycles=4):
    for i in range(1, cycles+1):
        pomodoro_session(f"Work {i}/{cycles}", work)

        if i == cycles:
            pomodoro_session(f"Long Break", long_break)
        else:
            pomodoro_session("Short Break", short_break)

if __name__ == "__main__":
    pomodoro_session("Focus", 2)