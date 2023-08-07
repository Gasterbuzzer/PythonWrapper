"""Settings Window for Colors"""

import customtkinter
from Frames.CustomElements.scrollableentry import ScrollableEntry


class ColorSettingsWindow:
    """
    Settings Window Class to call the color updater.
    """

    def __init__(self, object_to_display, previous_window_reference, class_reference) -> None:
        """
        Class representing a settings window for colors.

        :param object_to_display: Object to display in Window.
        :param previous_window_reference: Main Window Reference
        """

        # Values
        self.object_to_display = object_to_display
        self.previous_window_reference = previous_window_reference
        self.class_reference = class_reference

        # Window Constants
        self.width = 400
        self.height = 800

        self.toplevel = None

        # Frame
        self.main_frame = None

        # Ambient
        self.ambient_label = None
        self.ambient_box_0 = None
        self.ambient_box_1 = None
        self.ambient_box_2 = None

        # diffuse
        self.diffuse_label = None
        self.diffuse_box_0 = None
        self.diffuse_box_1 = None
        self.diffuse_box_2 = None

        # specular
        self.specular_label = None
        self.specular_box_0 = None
        self.specular_box_1 = None
        self.specular_box_2 = None

        # reflected
        self.reflected_label = None
        self.reflected_box_0 = None
        self.reflected_box_1 = None
        self.reflected_box_2 = None

        # refracted
        self.refracted_label = None
        self.refracted_box_0 = None
        self.refracted_box_1 = None
        self.refracted_box_2 = None

        # shininess
        self.shininess_label = None
        self.shininess_box_0 = None

        # Save Button
        self.save_button = None

    def open_window(self) -> None:
        """
        Opens the window for settings. (Must have created instance of class or else this will fail)
        """

        # Main Window
        self.toplevel = customtkinter.CTkToplevel(self.previous_window_reference)

        self.toplevel.title(f"Settings Window -- Color")
        self.toplevel.geometry(f"{self.width}x{self.height}")
        self.toplevel.grid_propagate(False)
        self.toplevel.resizable(False, False)

        # Most Important Frame
        self.main_frame = customtkinter.CTkFrame(self.toplevel)
        self.main_frame.configure(border_width=2, height=790, width=390)
        self.main_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.main_frame.grid_propagate(False)

        # Ambient
        ambient_values = self.object_to_display.color.ambient

        self.ambient_label = customtkinter.CTkLabel(self.main_frame, text="Ambient: ", justify="center",
                                                    width=20, font=("Franklin Gothic Medium", 22))
        self.ambient_label.grid(row=0, column=0, padx=15, pady=(20, 0))

        self.ambient_box_0 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=ambient_values[0], column=1,
                                             text_in_front="1.: ", pady=(20, 0))

        self.ambient_box_1 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=ambient_values[1], column=1, row=2,
                                             text_in_front="2.: ")

        self.ambient_box_2 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=ambient_values[2], column=1, row=3,
                                             text_in_front="3.: ")

        # Diffuse
        diffuse_values = self.object_to_display.color.diffuse

        self.diffuse_label = customtkinter.CTkLabel(self.main_frame, text="Diffuse: ", justify="center",
                                                    width=20, font=("Franklin Gothic Medium", 22))
        self.diffuse_label.grid(row=4, column=0, padx=15, pady=(20, 0))

        self.diffuse_box_0 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=diffuse_values[0], column=1, row=4,
                                             text_in_front="1.: ", pady=(20, 0))

        self.diffuse_box_1 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=diffuse_values[1], column=1, row=5,
                                             text_in_front="2.: ")

        self.diffuse_box_2 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=diffuse_values[2], column=1, row=6,
                                             text_in_front="3.: ")

        # Specular
        specular_values = self.object_to_display.color.specular

        self.specular_label = customtkinter.CTkLabel(self.main_frame, text="Specular: ", justify="center",
                                                     width=20, font=("Franklin Gothic Medium", 22))
        self.specular_label.grid(row=7, column=0, padx=15, pady=(20, 0))

        self.specular_box_0 = ScrollableEntry(master=self.main_frame,
                                              placeholder_text=specular_values[0], column=1, row=7,
                                              text_in_front="1.: ", pady=(20, 0))

        self.specular_box_1 = ScrollableEntry(master=self.main_frame,
                                              placeholder_text=specular_values[1], column=1, row=8,
                                              text_in_front="2.: ")

        self.specular_box_2 = ScrollableEntry(master=self.main_frame,
                                              placeholder_text=specular_values[2], column=1, row=9,
                                              text_in_front="3.: ")

        # Reflected
        reflected_values = self.object_to_display.color.reflected

        self.reflected_label = customtkinter.CTkLabel(self.main_frame, text="Reflected: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.reflected_label.grid(row=10, column=0, padx=15, pady=(20, 0))

        self.reflected_box_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=reflected_values[0], column=1, row=10,
                                               text_in_front="1.: ", pady=(20, 0))

        self.reflected_box_1 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=reflected_values[1], column=1, row=11,
                                               text_in_front="2.: ")

        self.reflected_box_2 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=reflected_values[2], column=1, row=12,
                                               text_in_front="3.: ")

        # Refracted
        refracted_values = self.object_to_display.color.refracted

        self.refracted_label = customtkinter.CTkLabel(self.main_frame, text="Refracted: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.refracted_label.grid(row=13, column=0, padx=15, pady=(20, 0))

        self.refracted_box_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=refracted_values[0], column=1, row=13,
                                               text_in_front="1.: ", pady=(20, 0))

        self.refracted_box_1 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=refracted_values[1], column=1, row=14,
                                               text_in_front="2.: ")

        self.refracted_box_2 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=refracted_values[2], column=1, row=15,
                                               text_in_front="3.: ")

        # Shininess
        shininess_value = self.object_to_display.color.shininess

        self.shininess_label = customtkinter.CTkLabel(self.main_frame, text="Shininess: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.shininess_label.grid(row=16, column=0, padx=15, pady=(20, 0))

        self.shininess_box_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=shininess_value, column=1, row=16,
                                               text_in_front="Shininess: ", pady=(20, 0))

        # Save Button
        self.save_button = customtkinter.CTkButton(master=self.main_frame, text="Save Changes",
                                                   command=self.class_reference.update_object_with_new_data)
        self.save_button.grid(row=17, column=0, padx=5, pady=(10, 0), sticky="sw")

        # Actually Running:
        self.toplevel.grab_set()
        self.toplevel.mainloop()
