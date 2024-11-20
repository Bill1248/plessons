def wrap_brackets( text ):
    return "(" + text + ")"

def wrap_square_brackets( text):
    return "[" + text + "]"

def wrap_direction_brackets( text):
    return "<" + text + ">"

conteiner = wrap_direction_brackets(
    wrap_direction_brackets(
        wrap_direction_brackets(
            wrap_square_brackets(
                wrap_square_brackets(
                    wrap_square_brackets(
                        wrap_brackets("12345")
                    )
                )
            )
        )
    )
)

print(conteiner)