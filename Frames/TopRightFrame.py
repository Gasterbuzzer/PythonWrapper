"""Top Right Frame"""
import customtkinter


class TopRightFrame:
    """
    Top Right Frame Class
    """
    def __init__(self, main_menu_reference) -> None:
        """
        Top Right Frame Class (Settings for Image)

        :param main_menu_reference: Reference to Main Class (Not the Main Window)
        """

        # Main Frame
        self.frame = customtkinter.CTkFrame(main_menu_reference.app)
        self.frame.configure(border_width=2, height=100, width=790)
        self.frame.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="nw")
        self.frame.grid_propagate(False)
