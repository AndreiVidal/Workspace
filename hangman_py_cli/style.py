from rich.console import Console
from rich.panel import Panel

console = Console()


def panel(*args):
    func = args[0]

    def wrapper(*args):
        msg, title, style = func(*args)
        console.print(
            Panel(
                f"[white b]{msg}[/] ",
                title=title,
                highlight=True,
                style=style,
            )
        )

    return wrapper
