

def column_to_x(column: int) -> int:

    match column:
        case 1:
            return 36

        case 2:
            return 109

        case 3:
            return 182

        case 4:
            return 258

        case 5:
            return 329

        case 6:
            return 402
        case 7:
            return 475

        case _:
            return None
