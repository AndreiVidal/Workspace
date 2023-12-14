from rich.console import Console
from rich.prompt import Prompt

from style import panel
from style import table


class Message:
    def __init__(self):
        self.console = Console()

    @panel
    def gameover(self, word: str):
        msg = f"A palavra era {word}"
        title = "GAMEOVER"
        style = "red"
        return msg, title, style

    @panel
    def won(self, word: str):
        msg = f"Parabéns! A palavra é {word}"
        title = "Você venceu"
        style = "blue"
        return msg, title, style

    def retry_ask(self):
        prompt = Prompt
        response_chosen = (
            prompt.ask("Deseja tentar novamente", choices=["s", "n"]).lower().strip()
        )
        if response_chosen == "n":
            return False
        return response_chosen

    @table
    def choice_menu(self, categories):
        return categories

    def choose_category(
        self,
    ):
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
