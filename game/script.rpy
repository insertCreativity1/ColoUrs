# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Protag or support
define black = Character(_("Onyx"), color="#000000")
define white = Character(_("Pale mf"), color="#ffffff")


# Options~
define red = Character(_("Vermilion"), color="#E34234")
define orange = Character(_("Persimmon"), color="#EC5800")
define yellow = Character(_("Maize"), color="#FBEC5D")
define green = Character(_("Aventurine"), color="#04b75a")
define blue = Character(_("Aoi/Azure"), color="#007FFF")
define purple = Character(_("Orchid"), color="#DA70D6")
define grey = Character(_("Ash"), color="#B2BEB5")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
