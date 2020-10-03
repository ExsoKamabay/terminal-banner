from init import Terminal_banner

print("\n\n",Terminal_banner(string="test",color="rgb(106, 90, 205)",bg_color="#006347").strings)

print(Terminal_banner(string="test",font="univers",color="cyan",bg_color=None).font)

print(Terminal_banner(string="test",font="fancy5",decoration="wave2",color="yellow",bg_color="black").textArt)