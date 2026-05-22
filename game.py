from random import randint

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

HERO_ART = r"""
   /\
  /  \
  |[]|
  |  |
 /____\
  /::\
"""

ENEMY_ART = r"""
 (\_/)
 (o.o)
 />💀
"""


def show_intro() -> None:
    console.print(
        Panel.fit(
            f"[bold cyan]Daniel's ASCII RPG[/bold cyan]\n{HERO_ART}",
            border_style="cyan",
        )
    )


def show_status(hero_hp: int, enemy_hp: int) -> None:
    table = Table(title="Battle Status")
    table.add_column("Character", style="bold")
    table.add_column("HP", justify="right")
    table.add_row("Hero", str(hero_hp))
    table.add_row("Goblin", str(enemy_hp))
    console.print(table)


def battle() -> None:
    hero_hp = 20
    enemy_hp = 15

    console.print(Panel.fit(f"[red]A wild goblin appears![/red]\n{ENEMY_ART}", border_style="red"))

    while hero_hp > 0 and enemy_hp > 0:
        show_status(hero_hp, enemy_hp)
        action = Prompt.ask("Choose action", choices=["attack", "heal"], default="attack")

        if action == "attack":
            damage = randint(3, 7)
            enemy_hp = max(0, enemy_hp - damage)
            console.print(f"[green]You strike for {damage} damage![/green]")
        else:
            heal = randint(2, 5)
            hero_hp = min(20, hero_hp + heal)
            console.print(f"[blue]You heal for {heal} HP.[/blue]")

        if enemy_hp <= 0:
            break

        enemy_damage = randint(2, 6)
        hero_hp = max(0, hero_hp - enemy_damage)
        console.print(f"[red]Goblin hits you for {enemy_damage} damage![/red]")

    if hero_hp > 0:
        console.print("[bold green]Victory! The goblin has been defeated.[/bold green]")
    else:
        console.print("[bold red]Defeat... the goblin wins this time.[/bold red]")


def main() -> None:
    show_intro()
    battle()


if __name__ == "__main__":
    main()
