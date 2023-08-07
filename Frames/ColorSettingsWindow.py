"""Settings Window for Colors"""

import customtkinter
from Frames.CustomElements.scrollableentry import ScrollableEntry


class ColorSettingsWindow:
    """
    Settings Window Class to call the color updater.
    """

    def __init__(self, object_to_display, previous_window_reference, class_reference, function_recurse_pointer) -> None:
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
        self.height = 850

        self.toplevel = None

        # Frame
        self.main_frame = None

        # Ambient
        self.ambient_label = None
        self.ambient_box_0 = None
        self.ambient_box_1 = None
        self.ambient_box_2 = None
        self.ambient_values = None

        # diffuse
        self.diffuse_label = None
        self.diffuse_box_0 = None
        self.diffuse_box_1 = None
        self.diffuse_box_2 = None
        self.diffuse_values = None

        # specular
        self.specular_label = None
        self.specular_box_0 = None
        self.specular_box_1 = None
        self.specular_box_2 = None
        self.specular_values = None

        # reflected
        self.reflected_label = None
        self.reflected_box_0 = None
        self.reflected_box_1 = None
        self.reflected_box_2 = None
        self.reflected_values = None

        # refracted
        self.refracted_label = None
        self.refracted_box_0 = None
        self.refracted_box_1 = None
        self.refracted_box_2 = None
        self.refracted_values = None

        # shininess
        self.shininess_label = None
        self.shininess_box_0 = None
        self.shininess_value = None

        # Save Button
        self.save_button_without_close = None
        self.save_button_with_close = None
        self.close_without_saving_button = None

        # Function Pointer
        self.function_recurse_pointer = function_recurse_pointer

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
        self.main_frame.configure(border_width=2, height=self.height-10, width=self.width-10)
        self.main_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.main_frame.grid_propagate(False)

        # Ambient
        self.ambient_values = self.object_to_display.color.ambient

        self.ambient_label = customtkinter.CTkLabel(self.main_frame, text="Ambient: ", justify="center",
                                                    width=20, font=("Franklin Gothic Medium", 22))
        self.ambient_label.grid(row=0, column=0, padx=15, pady=(20, 0))

        self.ambient_box_0 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=self.ambient_values[0], column=1,
                                             text_in_front="1.: ", pady=(20, 0))

        self.ambient_box_1 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=self.ambient_values[1], column=1, row=2,
                                             text_in_front="2.: ")

        self.ambient_box_2 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=self.ambient_values[2], column=1, row=3,
                                             text_in_front="3.: ")

        # Diffuse
        self.diffuse_values = self.object_to_display.color.diffuse

        self.diffuse_label = customtkinter.CTkLabel(self.main_frame, text="Diffuse: ", justify="center",
                                                    width=20, font=("Franklin Gothic Medium", 22))
        self.diffuse_label.grid(row=4, column=0, padx=15, pady=(20, 0))

        self.diffuse_box_0 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=self.diffuse_values[0], column=1, row=4,
                                             text_in_front="1.: ", pady=(20, 0))

        self.diffuse_box_1 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=self.diffuse_values[1], column=1, row=5,
                                             text_in_front="2.: ")

        self.diffuse_box_2 = ScrollableEntry(master=self.main_frame,
                                             placeholder_text=self.diffuse_values[2], column=1, row=6,
                                             text_in_front="3.: ")

        # Specular
        self.specular_values = self.object_to_display.color.specular

        self.specular_label = customtkinter.CTkLabel(self.main_frame, text="Specular: ", justify="center",
                                                     width=20, font=("Franklin Gothic Medium", 22))
        self.specular_label.grid(row=7, column=0, padx=15, pady=(20, 0))

        self.specular_box_0 = ScrollableEntry(master=self.main_frame,
                                              placeholder_text=self.specular_values[0], column=1, row=7,
                                              text_in_front="1.: ", pady=(20, 0))

        self.specular_box_1 = ScrollableEntry(master=self.main_frame,
                                              placeholder_text=self.specular_values[1], column=1, row=8,
                                              text_in_front="2.: ")

        self.specular_box_2 = ScrollableEntry(master=self.main_frame,
                                              placeholder_text=self.specular_values[2], column=1, row=9,
                                              text_in_front="3.: ")

        # Reflected
        self.reflected_values = self.object_to_display.color.reflected

        self.reflected_label = customtkinter.CTkLabel(self.main_frame, text="Reflected: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.reflected_label.grid(row=10, column=0, padx=15, pady=(20, 0))

        self.reflected_box_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.reflected_values[0], column=1, row=10,
                                               text_in_front="1.: ", pady=(20, 0))

        self.reflected_box_1 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.reflected_values[1], column=1, row=11,
                                               text_in_front="2.: ")

        self.reflected_box_2 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.reflected_values[2], column=1, row=12,
                                               text_in_front="3.: ")

        # Refracted
        self.refracted_values = self.object_to_display.color.refracted

        self.refracted_label = customtkinter.CTkLabel(self.main_frame, text="Refracted: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.refracted_label.grid(row=13, column=0, padx=15, pady=(20, 0))

        self.refracted_box_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.refracted_values[0], column=1, row=13,
                                               text_in_front="1.: ", pady=(20, 0))

        self.refracted_box_1 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.refracted_values[1], column=1, row=14,
                                               text_in_front="2.: ")

        self.refracted_box_2 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.refracted_values[2], column=1, row=15,
                                               text_in_front="3.: ")

        # Shininess
        self.shininess_value = self.object_to_display.color.shininess

        self.shininess_label = customtkinter.CTkLabel(self.main_frame, text="Shininess: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.shininess_label.grid(row=16, column=0, padx=15, pady=(20, 0))

        self.shininess_box_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.shininess_value, column=1, row=16,
                                               text_in_front="Shininess: ", pady=(20, 0))

        # Save Button
        save_padx = 0
        save_pady = (20, 0)
        columnspan = 8

        self.save_button_without_close = customtkinter.CTkButton(master=self.main_frame, text="Save Changes ",
                                                                 command=self.save_colors, width=200)
        self.save_button_without_close.grid(row=17, column=1, padx=save_padx, pady=(30, 0), sticky="n",
                                            columnspan=columnspan)

        self.save_button_with_close = customtkinter.CTkButton(master=self.main_frame, text="Save Changes & Exit",
                                                              command=self.save_and_close, width=200)
        self.save_button_with_close.grid(row=18, column=1, padx=save_padx, pady=save_pady, sticky="n",
                                         columnspan=columnspan)

        self.close_without_saving_button = customtkinter.CTkButton(master=self.main_frame,
                                                                   text="Exit & Discard Unsaved Changes",
                                                                   command=self.close_self, width=200)
        self.close_without_saving_button.grid(row=19, column=1, padx=save_padx, pady=save_pady,
                                              sticky="n", columnspan=columnspan)

        # Actually Running:
        self.toplevel.grab_set()
        self.toplevel.mainloop()

    def save_colors(self) -> None:
        """
        Saves the given color changes to the object.
        """

        print("Debug Log: Saving Colors.")

        self.ambient_values[0] = self.ambient_box_0.get_value()
        self.ambient_values[1] = self.ambient_box_1.get_value()
        self.ambient_values[2] = self.ambient_box_2.get_value()

        self.diffuse_values[0] = self.diffuse_box_0.get_value()
        self.diffuse_values[1] = self.diffuse_box_1.get_value()
        self.diffuse_values[2] = self.diffuse_box_2.get_value()

        self.specular_values[0] = self.specular_box_0.get_value()
        self.specular_values[1] = self.specular_box_1.get_value()
        self.specular_values[2] = self.specular_box_2.get_value()

        self.reflected_values[0] = self.reflected_box_0.get_value()
        self.reflected_values[1] = self.reflected_box_1.get_value()
        self.reflected_values[2] = self.reflected_box_2.get_value()

        self.refracted_values[0] = self.refracted_box_0.get_value()
        self.refracted_values[1] = self.refracted_box_1.get_value()
        self.refracted_values[2] = self.refracted_box_2.get_value()

        self.shininess_value = self.shininess_box_0.get_value()

        # Now we have to overwrite the given element.

        debug = False

        for obj in self.class_reference.main.app.hierarchy:

            if debug:
                print(f"\nDebug Log: (Colors) Current Object: {obj} with the name {obj.__class__.__name__.title()}"
                      f" (Finding: {self.object_to_display}).")

            object_found = self.function_recurse_pointer(self.object_to_display, obj,
                                                         obj.__class__.__name__.title(),
                                                         debug)
            if object_found is not None:
                # If the Object is not empty (meaning we didn't find it)
                print("\nDebug Log: (Colors) Found the object, writing the object colors new.")

                # Writing Color Values
                object_found.color.ambient = self.ambient_values
                object_found.color.diffuse = self.diffuse_values
                object_found.color.specular = self.specular_values
                object_found.color.reflected = self.reflected_values
                object_found.color.refracted = self.refracted_values
                object_found.color.shininess = self.shininess_value

                return

        # If no object was found.
        # Let's hope that doesn't happen.

    def close_self(self) -> None:
        """
        Closes the current Window. (Must be active beforehand)
        """

        # Ambient
        self.ambient_label.destroy()
        self.ambient_box_0.destroy()
        self.ambient_box_1.destroy()
        self.ambient_box_2.destroy()

        # diffuse
        self.diffuse_label.destroy()
        self.diffuse_box_0.destroy()
        self.diffuse_box_1.destroy()
        self.diffuse_box_2.destroy()

        # specular
        self.specular_label.destroy()
        self.specular_box_0.destroy()
        self.specular_box_1.destroy()
        self.specular_box_2.destroy()

        # reflected
        self.reflected_label.destroy()
        self.reflected_box_0.destroy()
        self.reflected_box_1.destroy()
        self.reflected_box_2.destroy()

        # refracted
        self.refracted_label.destroy()
        self.refracted_box_0.destroy()
        self.refracted_box_1.destroy()
        self.refracted_box_2.destroy()

        # shininess
        self.shininess_label.destroy()
        self.shininess_box_0.destroy()

        # Save Button
        self.save_button_without_close.destroy()
        self.save_button_with_close.destroy()
        self.close_without_saving_button.destroy()

        # Frame
        self.main_frame.destroy()

        # Window
        self.toplevel.destroy()

    def save_and_close(self) -> None:
        """
        Saves and closes the window.
        """
        self.save_colors()
        self.close_self()

    def destroy(self) -> None:
        """
        Similar to closing just an alias.
        """
        self.close_self()
