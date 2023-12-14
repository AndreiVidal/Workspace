from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.prompt import Prompt

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


def table(func):
    def wrapper(*args, **kwargs):
        console = Console()
        table = Table(
            title_style="magenta",
            box=box.HEAVY,
            title_justify="center",
            expand=True,
            highlight=True,
        )
        table.add_column("Opção", justify="center")
        table.add_column("Categoria", justify="center")
        result = func(*args, **kwargs)
        for idx, item in enumerate(result):
            table.add_row(str(idx + 1), str(item))
        console.print(table)

    return wrapper
