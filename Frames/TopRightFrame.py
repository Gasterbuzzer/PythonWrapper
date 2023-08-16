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

        # Select File Format

        self.available_formats = ["PNG", "JPG"]

        self.currently_selected_format = self.available_formats[0]

        self.format_label = customtkinter.CTkLabel(self.frame, text="File Format: ", justify="left",
                                                   width=20, font=("Franklin Gothic Medium", 22))

        self.format_label.grid(row=0, column=0, padx=15, pady=(10, 0), columnspan=4)

        self.format_select_box = customtkinter.CTkComboBox(self.frame,
                                                           values=self.available_formats, width=200, height=24,
                                                           command=self.update_currently_selected_format,
                                                           state="readonly")
        self.format_select_box.set(self.currently_selected_format)
        self.format_select_box.grid(row=1, column=0, padx=(5, 0), pady=(10, 0), columnspan=4)

        # Generate image without saving

        # Generate image and save.

    def update_currently_selected_format(self, event) -> None:
        """
        Updates the internal selection to newly selected format.
        :param event: Event when triggered
        """

        print(f"Debug Log: Updated Image format to '{self.format_select_box.get()}'.")

        self.currently_selected_format = self.format_select_box.get()
