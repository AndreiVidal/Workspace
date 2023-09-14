from rich.console import Console
from rich.prompt import Prompt

from style import panel
from style import table
from style import prompt_ask


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

    @prompt_ask
    def retry_ask(self, response_chosen):
        if response_chosen == "s":
            return True

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
