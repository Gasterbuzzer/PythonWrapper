"""Settings Window"""

import customtkinter


class SettingsWindow:
    """
    Settings Window Class to call it.
    """

    def __init__(self, object_to_display, master_app) -> None:
        """
        Class repressenting a settings window.

        :param object_to_display: Object to display in Window.
        :param master_app: Main Window Reference
        """

        # Values
        self.object_to_display = object_to_display
        self.app = master_app

        # Window Constants
        self.width = 400
        self.height = 400

        self.toplevel = None

    def open_window(self) -> None:
        """
        Opens the window for the top level.
        """

        self.toplevel = customtkinter.CTkToplevel(self.app)

        self.toplevel.title(f"Settings Window -- {self.object_to_display.__class__.__name__.title()}")
        self.toplevel.geometry(f"{self.width}x{self.height}")
        self.toplevel.grid_propagate(False)
        self.toplevel.resizable(False, False)

        self.toplevel.grab_set()
        self.toplevel.mainloop()
