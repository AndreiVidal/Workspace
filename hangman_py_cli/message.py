from rich.console import Console
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel


class Message:
    def __init__(self):
        self.console = Console()

    def _panel(self, msg, title, style="blue"):
        return Panel(
            f"[white b]{msg}[/] ",
            title=title,
            highlight=True,
            style=style,
        )

    def gameover(self, word: str):
        self.console.print(
            self._panel(
                f"A palavra era {word}",
                "GAMEOVER",
                "red",
            ),
            justify="center",
        )

    def won(self, word: str):
        self.console.print(
            self._panel(
                f"Parabéns! A palavra é {word}",
                "YOU WIN",
                "blue",
            ),
            justify="center",
        )

    def retry_ask(self):
        r = ""
        while r not in ("s", "n"):
            r = input("Deseja tentar novamente [s/n]").lower().strip()
            if r == "s":
                return True
            elif r == "n":
                return False

    def choice_menu(self, categories):
        self.console.rule("CATEGORIAS DISPONÍVEIS")
        table = Table(
            title_style="magenta",
            box=box.HEAVY,
            title_justify="center",
            expand=True,
            highlight=True,
        )
        table.add_column("Opção", justify="center")
        table.add_column("Categoria", justify="center")
        for idx, item in enumerate(categories):
            table.add_row(str(idx + 1), str(item))
        self.console.print(table)

    def choose_category(self):
        return Prompt.ask(
            "[black on white]Escolha uma categoria[/]",
            choices=["1", "2", "3"],
            show_choices=True,
        )

    def choosed_category(self, category):
        self.console.rule(
            f"CATEGORIA ESCOLHIDA: {category} ".upper(),
            style="red",
            characters="=",
        )
