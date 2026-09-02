import random

def generate_note(note):
    split_note = note.split(",")
    columns = ["36", "109", "182", "258", "329", "402", "475"]
    column = columns[random.randint(0,6)]
    new_note_list = split_note
    new_note_list[0] = str(column)
    new_note = (",").join(new_note_list)
    return(new_note)
