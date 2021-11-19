from tkinter import Canvas, Entry, Tk, LEFT, GROOVE
from tkinter.ttk import Frame


def add_models_tree(root_window: Tk, view_width: int) -> None:
    """
    Creates a view containing all contextual models and definitions.

    Args:
        root_window: The window to attach the models tree canvas to
        view_width (int): The width of the canvas
    """
    models_tree_canvas = Frame(root_window, width=view_width, height=root_window.winfo_screenheight(), borderwidth=1, relief=GROOVE)
    models_tree_canvas.pack(side=LEFT)

    # models_tree_entry = Entry(root_window)
    # models_tree_canvas.create_window(view_width // 2, 20, window=models_tree_entry)
