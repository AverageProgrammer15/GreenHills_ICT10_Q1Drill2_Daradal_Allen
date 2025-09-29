from pyscript import *

def give(e):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    document.getElementById("output").innerHTML = ""

    message = f"""
    👤 Student Profile \n\tName   : {name}\n\tAge    : {age}\n\tSchool : {school}
    """

    print(message)
    display(message, target="output")

    Note =f"""
        ✏️ Notes: \n\t{name} is currently {age} years old and studies at {school}.\nThis information was gathered through input fields and displayed using
        a multiline string in Python via PyScript.
    """

    print(Note)


    display(Note, target="output")

    Caption =f"""
        💬 Caption:\n\tHere’s my Student Profile using Python strings in PyScript!
    """

    print(Caption)
    display(Caption, target="output")
