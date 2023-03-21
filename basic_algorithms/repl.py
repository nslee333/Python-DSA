from code import InteractiveConsole
from celsius_to_f import convert_to_f


header = "Please enter a celsius number:"
footer = "have a great day!"

scope_vars = {"fn": convert_to_f}

InteractiveConsole(locals=scope_vars).interact(header, footer)

