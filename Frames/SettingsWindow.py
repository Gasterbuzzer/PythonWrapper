"""Settings Window"""

import customtkinter
from Frames.CustomElements.scrollableentry import ScrollableEntry


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

        # Frame
        self.main_frame = None

        # Label and Textbox for Position
        self.position_label = None
        self.position_textbox_x = None
        self.position_textbox_y = None
        self.position_textbox_z = None

        # Save
        self.save_button = None

        # Later Initialized Values
        self.object_coordinates = None
        self.name = None

    def open_window(self) -> None:
        """
        Opens the window for settings. (Must have created instance of class or else this will fail)
        """

        # Main Window
        self.toplevel = customtkinter.CTkToplevel(self.app)

        # Getting name
        self.name = self.object_to_display.__class__.__name__.title()

        self.toplevel.title(f"Settings Window -- {self.name}")
        self.toplevel.geometry(f"{self.width}x{self.height}")
        self.toplevel.grid_propagate(False)
        self.toplevel.resizable(False, False)

        # Most Important Frame
        self.main_frame = customtkinter.CTkFrame(self.toplevel)
        self.main_frame.configure(border_width=2, height=390, width=390)
        self.main_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.main_frame.grid_propagate(False)

        # Coordinates of Object (If it is not a Group)
        if self.name == "Group":
            print("Debug Log: Given Object is a Group and does not contain any coordinates.")
        else:

            # Label and Textbox for Position
            self.position_label = customtkinter.CTkLabel(self.main_frame, text="Position: ", justify="center",
                                                         width=20, font=("Franklin Gothic Medium", 22))
            self.position_label.grid(row=0, column=0, padx=15, pady=(10, 0))

            self.object_coordinates = self.object_to_display.position

            self.position_textbox_x = ScrollableEntry(master=self.main_frame,
                                                      placeholder_text=self.object_coordinates[0], column=1,
                                                      text_in_front="X: ")
            self.position_textbox_y = ScrollableEntry(master=self.main_frame,
                                                      placeholder_text=self.object_coordinates[1], column=1, row=1,
                                                      text_in_front="Y: ")
            self.position_textbox_z = ScrollableEntry(master=self.main_frame,
                                                      placeholder_text=self.object_coordinates[2], column=1, row=2,
                                                      text_in_front="Z: ")

        self.save_button = customtkinter.CTkButton(master=self.main_frame, text="Save Changes")
        self.save_button.grid(row=3, column=0, padx=5, pady=(10, 0))

        # Actually Running:
        self.toplevel.grab_set()
        self.toplevel.mainloop()
