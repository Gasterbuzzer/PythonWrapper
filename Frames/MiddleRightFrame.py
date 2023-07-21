"""Middle Right Frame"""
import customtkinter


class MiddleRightFrame:
    """
        Middle Right Frame Class
    """
    def __init__(self, main_menu_reference) -> None:

        self.frame = customtkinter.CTkFrame(main_menu_reference.app)
        self.frame.configure(border_width=2, height=590, width=790)
        self.frame.grid(row=1, column=1, padx=(0, 5), pady=5, sticky="nse")
        self.frame.grid_propagate(False)
