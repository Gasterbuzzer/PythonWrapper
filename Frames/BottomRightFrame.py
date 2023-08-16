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
        # Useless value to ignore static warning
        self.useless = ""

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

        # Base Information.
        parent_json = {"screen": self.app.screen, "medium": self.app.medium, "objects": []}

        if not self.app.sources:
            parent_json["sources"] = self.app.sources

        for _object in self.app.hierarchy:
            json_object = self.recurse_over_object(_object)

            # parent_json.update(json_object)
            parent_json["objects"].append(json_object)

        return parent_json

    def recurse_over_object(self, object_to_recurse_over) -> Union[Any, dict]:
        """
        Recurse over given an object and hopefully terminates at some point.

        :return: JSON File containing
        """
        debug = False

        print(f"Debug Log: {object_to_recurse_over} being recurse over for saving. {self.useless}")

        # Extract the key
        object_name = list(object_to_recurse_over.keys())[0]

        # Extract the value
        object_found = object_to_recurse_over[object_name]

        if object_name.lower() == "sphere":
            # extracting sphere info and writing it.
            object_we_are_creating = {object_name.lower(): {}}

            object_we_are_creating[object_name.lower()]["position"] = object_found.position
            object_we_are_creating[object_name.lower()]["radius"] = object_found.radius

            object_we_are_creating[object_name.lower()]["color"] = self.color_as_json(object_found.color)

            object_we_are_creating[object_name.lower()]["index"] = object_found.index

            # Now we check the special stuff.
            # This will require special ordering
            check_if_anything_hits = (object_found.check_if_default(object_found.translation, "translation")
                                      and object_found.check_if_default(object_found.rotation, "rotation")
                                      and object_found.check_if_default(object_found.scaling, "scaling"))
            if debug:
                print(f"\nDebug Log: {check_if_anything_hits}\n")

            if not check_if_anything_hits:
                if not object_found.check_if_default(object_found.translation, "translation"):
                    object_we_are_creating = \
                        {"translation":
                            {
                                "factors": object_found.translation,
                                "subject": object_we_are_creating
                            }}

                if not object_found.check_if_default(object_found.rotation, "rotation"):
                    object_we_are_creating = \
                        {"rotation":
                            {
                                "angle": object_found.rotation[0],
                                "direction": object_found.rotation[1],
                                "subject": object_we_are_creating
                            }}
                if not object_found.check_if_default(object_found.scaling, "scaling"):
                    object_we_are_creating = \
                        {"scaling":
                            {
                                "factors": object_found.scaling,
                                "subject": object_we_are_creating
                            }}
                return object_we_are_creating
            else:
                # The object does not have any special attributes.
                return object_we_are_creating

        elif object_name.lower() == "halfspace":
            # extracting sphere info and writing it.

            object_we_are_creating = {"halfSpace": {}}

            object_we_are_creating["halfSpace"]["position"] = object_found.position
            object_we_are_creating["halfSpace"]["normal"] = object_found.normal

            object_we_are_creating["halfSpace"]["color"] = self.color_as_json(object_found.color)

            object_we_are_creating["halfSpace"]["index"] = object_found.index

            # Now we check the special stuff.
            # This will require special ordering
            check_if_anything_hits = (object_found.check_if_default(object_found.translation, "translation")
                                      and object_found.check_if_default(object_found.rotation, "rotation")
                                      and object_found.check_if_default(object_found.scaling, "scaling"))
            if not check_if_anything_hits:
                if not object_found.check_if_default(object_found.translation, "translation"):
                    object_we_are_creating = \
                        {"translation":
                            {
                                "factors": object_found.translation,
                                "subject": object_we_are_creating
                            }}

                if not object_found.check_if_default(object_found.rotation, "rotation"):
                    object_we_are_creating = \
                        {"rotation":
                            {
                                "angle": object_found.rotation[0],
                                "direction": object_found.rotation[1],
                                "subject": object_we_are_creating
                            }}
                if not object_found.check_if_default(object_found.scaling, "scaling"):
                    object_we_are_creating = \
                        {"scaling":
                            {
                                "factors": object_found.scaling,
                                "subject": object_we_are_creating
                            }}
                return object_we_are_creating
            else:
                # The object does not have any special attributes.
                return object_we_are_creating

        elif object_name.lower() == "group":
            # extracting sphere info and writing it.
            print("\nDebug Log: Found Group, now looping through its objects.")

            object_we_are_creating = {object_found.special: []}

            # Now we add the objects to the objects_we_are_creating
            for _object in object_found.objects:
                temp_json_object = self.recurse_over_object(_object)

                object_we_are_creating[object_found.special].append(temp_json_object)

            print("Debug Log: Finished looping through objects from group.\n")
            # Now we check the special stuff.
            # This will require special ordering
            check_if_anything_hits = (object_found.check_if_default(object_found.translation, "translation")
                                      and object_found.check_if_default(object_found.rotation, "rotation")
                                      and object_found.check_if_default(object_found.scaling, "scaling"))
            if not check_if_anything_hits:
                if not object_found.check_if_default(object_found.translation, "translation"):
                    object_we_are_creating = \
                        {"translation":
                            {
                                "factors": object_found.translation,
                                "subject": object_we_are_creating
                            }}

                if not object_found.check_if_default(object_found.rotation, "rotation"):
                    object_we_are_creating = \
                        {"rotation":
                            {
                                "angle": object_found.rotation[0],
                                "direction": object_found.rotation[1],
                                "subject": object_we_are_creating
                            }}
                if not object_found.check_if_default(object_found.scaling, "scaling"):
                    object_we_are_creating = \
                        {"scaling":
                            {
                                "factors": object_found.scaling,
                                "subject": object_we_are_creating
                            }}
                return object_we_are_creating
            else:
                # The object does not have any special attributes.
                return object_we_are_creating

        else:
            return {"test_value": "New Value"}

    def color_as_json(self, color_object) -> dict:
        """
        Converts a color object to json format.
        :param color_object: Object to convert.
        :return: JSON Dictionary containing the information of the color object.
        """

        print(f"Debug Log: Converting color of object to json." + self.useless)

        json_to_create = {"ambient": color_object.ambient, "diffuse": color_object.diffuse,
                          "specular": color_object.specular, "reflected": color_object.reflected,
                          "refracted": color_object.refracted, "shininess": color_object.shininess}

        return json_to_create

    def save_location_prompt(self) -> None:
        """
        Prompts the user for a location to store the
        :return: (Str) Absolute Path to file.
        """

        print("\nDebug Log: Starting saving prompt: ")

        # Request Input
        json_file = filedialog.asksaveasfile(initialdir=os.getcwd(), title="Select location to store changes to "
                                                                           "JSON File",
                                             filetypes=(("JSON Files", "*.json"), ("all files", "*.*")),
                                             defaultextension=".json")

        # If the user did not select anything, we just state that no file was selected.
        # Could be improved to
        # return the currently selected one.
        print(f"Debug Log: (With objects {self.app.hierarchy}) File Location: '{json_file}'.")
        if json_file == "" or json_file is None:
            print("Weak Error: Save Location is invalid or does not exist.")
            return

        # Getting write data
        json_values = self.get_json_object_from_hierarchy()

        # Writing
        json.dump(json_values, json_file, separators=(',', ': '), indent=4)

        # Finished Saving
        json_file.close()

        print("Debug Log: Successfully finished saving json file.\n")
