"""Bottom Right Frame"""
import customtkinter
from tkinter import filedialog
from PIL import Image
import os
import json
from typing import Union, Any


class BottomRightFrame:
    """
    Bottom Right Frame Class
    """

    def __init__(self, main_menu_reference) -> None:
        """
        Bottom Right Frame Class (Load and Save functions)

        :param main_menu_reference: Reference to Main Class (Not the Main Window)
        """

        # References
        self.app = main_menu_reference

        # Frames
        self.frame = customtkinter.CTkFrame(main_menu_reference.app)
        self.frame.configure(border_width=2, height=100, width=790)
        self.frame.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="sew")
        self.frame.grid_propagate(False)

        self.inside_frame = customtkinter.CTkFrame(master=self.frame)
        self.inside_frame.configure(border_width=2, height=38, width=200)
        self.inside_frame.grid(row=0, column=0, padx=(5, 0), pady=5)
        self.inside_frame.grid_propagate(False)

        # Label
        self.label_location = customtkinter.CTkLabel(self.inside_frame, text="No file selected.",
                                                     justify="left",
                                                     anchor="w",
                                                     width=len("No file selected.") * 6, height=20)
        self.label_location.grid(row=0, column=1, padx=(15, 0), pady=5)

        self.label_location.grid_propagate(False)

        # Image associated with the Load Button:
        background_image = Image.open("data/icons/edit.png").resize((25, 25))
        image_ctk_b = customtkinter.CTkImage(background_image, size=(25, 25))

        self.image = customtkinter.CTkLabel(self.inside_frame, image=image_ctk_b, text="")
        self.image.grid(row=0, column=0, padx=(15, 0), pady=5)

        # Load Button
        self.load_json_button = customtkinter.CTkButton(self.frame, text=f"Browse",
                                                        command=self.get_location_prompt, height=38)
        self.load_json_button.grid(row=0, column=1, padx=2, pady=5, sticky="nw")

        # Save Button
        # Saves the json changes from the user.
        self.save_json_button = customtkinter.CTkButton(self.frame, text=f"Save changes",
                                                        command=self.save_location_prompt, height=38)
        self.save_json_button.grid(row=0, column=2, padx=(5, 2), pady=5, sticky="nw")

    def get_location_prompt(self) -> None:
        """
        Prompts the user for a json file.
        :return: (Str) Absolute Path to file.
        """

        # Request Input
        json_location = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Scene JSON",
                                                   filetypes=(("JSON Files", "*.json"), ("all files", "*.*")))

        # If the user did not select anything, we just state that no file was selected. Could be improved to
        # return the currently selected one.
        print(f"File Location: '{json_location}'.")
        if json_location == "":
            self.app.file_location = ""
            self.label_location.configure(text="No file selected.")
            self.label_location.configure(width=len("No file selected.") * 6)
            return

        self.app.file_location = json_location

        # Configure Label to represent our filename.
        json_location = os.path.basename(json_location)

        self.label_location.configure(text=json_location)
        self.label_location.configure(width=len(json_location) * 7)

        # Now we load the given file into memory.
        self.app.load_file()
        self.app.prepare_file()

        # Now we update our hierarchy:
        self.app.left_frame.destroy_frame_objects()

        self.app.left_frame.create_hierarchy()
        self.app.left_frame.render_frame_objects()

    def get_json_object_from_hierarchy(self) -> dict:
        """
        Gets the current hierarchy and
        converts it into json format.
        Basically inverting the initial process.

        :return: JSON object containing the hierarchy converted back.
        """

        parent_json = {"test_value": 2}

        for _object in self.app.hierarchy:
            json_object = self.recurse_over_object(_object)

            parent_json.update(json_object)

        return parent_json

    def recurse_over_object(self, object_to_recurse_over) -> Union[Any, dict]:
        """
        Recurses over given obect and hopefully terminates at some point.

        :return: JSON File containing
        """

        return {"test_value": "New Value"}

    def save_location_prompt(self) -> None:
        """
        Prompts the user for a location to store the
        :return: (Str) Absolute Path to file.
        """

        # Request Input
        json_file = filedialog.asksaveasfile(initialdir=os.getcwd(), title="Select location to store changes to "
                                                                           "JSON File",
                                             filetypes=(("JSON Files", "*.json"), ("all files", "*.*")),
                                             defaultextension=".json")

        # If the user did not select anything, we just state that no file was selected.
        # Could be improved to
        # return the currently selected one.
        print(f"Debug Log: (With objects {self.app.hierarchy}) File Location: '{json_file}'.")
        if json_file == "":
            print("Weak Error: Save Location is invalid or does not exist.")
            return

        # Getting write data
        json_values = self.get_json_object_from_hierarchy()

        # Writing
        json.dump(json_values, json_file)

        # Finished Saving
        json_file.close()

        print("Debug Log: Successfully finished saving json file.\n")
