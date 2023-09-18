"""Top Right Frame"""
import customtkinter
from PIL import Image
import subprocess
import sys
from tkinter import filedialog
import os
import shutil
import time


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

        self.main_menu_reference = main_menu_reference

        self.frame = customtkinter.CTkFrame(self.main_menu_reference.app)
        self.frame.configure(border_width=2, height=100, width=790)
        self.frame.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="nw")
        self.frame.grid_propagate(False)

        # Select File Format

        self.available_formats = ["PNG", "JPG", "PPM"]

        self.currently_selected_format = self.available_formats[0]

        self.format_label = customtkinter.CTkLabel(self.frame, text="File Format: ", justify="left",
                                                   width=20, font=("Franklin Gothic Medium", 22))

        self.format_label.grid(row=0, column=0, padx=15, pady=(10, 0))

        self.format_select_box = customtkinter.CTkComboBox(self.frame,
                                                           values=self.available_formats, width=200, height=24,
                                                           command=self.update_currently_selected_format,
                                                           state="readonly")
        self.format_select_box.set(self.currently_selected_format)
        self.format_select_box.grid(row=1, column=0, padx=(5, 0), pady=(10, 0))

        # Generate image without saving

        self.save_button_without_close = customtkinter.CTkButton(master=self.frame, text="Generate Image",
                                                                 command=self.generate_image, width=150)
        self.save_button_without_close.grid(row=0, column=1, padx=25, pady=(20, 0), rowspan=4)

        # Generate image and save.

        self.save_button_without_close = customtkinter.CTkButton(master=self.frame, text="Generate Image\n&\nSave",
                                                                 command=self.save_and_generate, width=150)
        self.save_button_without_close.grid(row=0, column=2, padx=25, pady=(20, 0), rowspan=4)

    def update_currently_selected_format(self, event) -> None:
        """
        Updates the internal selection to newly selected format.
        :param event: Event when triggered
        """

        print(f"Debug Log: Updated Image format to '{self.format_select_box.get()}' with event {event}.")

        self.currently_selected_format = self.format_select_box.get()

    def generate_image(self) -> None:
        """
        Generates an Image based on the object we currently have.
        """

        print("\nDebug Log: Generating image based on json file:")

        image_width = self.main_menu_reference.middle_right_frame.image_width
        image_height = self.main_menu_reference.middle_right_frame.image_height

        # If the objects are empty, we set a placeholder image.
        if not self.main_menu_reference.hierarchy:
            self.main_menu_reference.middle_right_frame.update_image()
            return

        # We create the command:

        os.environ['PYTHONIOENCODING'] = 'utf-8'

        # Specify the path to the binary file
        binary_path = os.path.abspath("../raytracing_c++/bin/run.exe")

        # Specify the parameters you want to pass to the binary
        # Old Output: "{os.path.abspath('../data/generated/')}/generated_2".replace("\\", "/")"
        binary_parameters = [f"-j", f"{self.main_menu_reference.file_location}",
                             f"-o", f"generated_2",
                             f"-f", f"{self.currently_selected_format.lower()}"]

        # Create the command by combining the binary path and parameters
        command = [binary_path] + binary_parameters

        # New Image location
        image_location = os.path.abspath(f"../raytracing_c++/bin/generated_2.{self.currently_selected_format.lower()}")

        print(f"Debug Log: Command to be executed: '{command}'")

        # We create the image from our c++ library/project.
        if sys.platform.lower() == "linux" or sys.platform.lower() == "linux2":
            # Linux Command
            print("Debug Log: Platform has been identified as linux.")
            print("Debug Log: Running image generation...")
            _subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            stdout, stderr = _subp.communicate()

            # Check the return code to see if the process was successful (return code 0 usually indicates success)
            return_code = _subp.returncode

            print(f"Debug Log: Information: Output: '{stdout}'\nError: '{stderr}'\nReturnCode: '{return_code}'")

            print("Debug Log: Image has hopefully been generated!")
            # Now you would technically get the image location and load it from there.
            time.sleep(6)

            # For now, since we don't actually generate an image, we copy that
            source_image_location = os.path.abspath(f"generated_2.{self.currently_selected_format.lower()}")
            source_image_location_2 = f"{os.getcwd()}\\data\\img.{self.currently_selected_format.lower()}"

            shutil.copyfile(source_image_location, source_image_location_2)

            # Opening the image "generated_2.jpg"
            background_image = Image.open(source_image_location_2).resize((image_width, image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(image_width, image_height))

            self.main_menu_reference.middle_right_frame.update_image(image=image_ctk_b)

            print("Debug Log: Displaying generated image.")

        elif sys.platform.lower() == "windows" or sys.platform.lower() == "win32":
            print("Debug Log: Platform has been identified as windows.")

            print("Debug Log: Running image generation...")
            _subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            stdout, stderr = _subp.communicate()

            # Check the return code to see if the process was successful (return code 0 usually indicates success)
            return_code = _subp.returncode

            print(f"Debug Log: Information: Output: '{stdout}'\nError: '{stderr}'\nReturnCode: '{return_code}'")

            print("Debug Log: Image has hopefully been generated!")
            # Now you would technically get the image location and load it from there.
            time.sleep(6)

            # For now, since we don't actually generate an image, we copy that
            source_image_location = os.path.abspath(f"generated_2.{self.currently_selected_format.lower()}")
            source_image_location_2 = f"{os.getcwd()}\\data\\img.{self.currently_selected_format.lower()}"

            shutil.copyfile(source_image_location, source_image_location_2)

            # Opening the image "generated_2.jpg"
            background_image = Image.open(source_image_location_2).resize((image_width, image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(image_width, image_height))

            self.main_menu_reference.middle_right_frame.update_image(image=image_ctk_b)

            print("Debug Log: Displaying generated image.")

        else:
            print(f"Error Log: Unknown Platform {sys.platform}. Could not generate image, using fallback.")

            background_image = Image.open("data/generated/generated.jpg").resize((image_width, image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(image_width, image_height))

            self.main_menu_reference.middle_right_frame.update_image(image=image_ctk_b)

            print("Debug Log: Displaying fallback image.")

    def save_and_generate(self) -> None:
        """
        Saves and generates an Image.
        """

        # Ask for Image save location.

        print("Debug Log: Asking for save location.")

        # Request Input
        image_file_location = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                                           title="Select location to store the generated "
                                                                 "Image",

                                                           filetypes=((self.currently_selected_format,
                                                                       f"*.{self.currently_selected_format.lower()}"),
                                                                      ("all files", "*.*")),

                                                           defaultextension=f"."
                                                                            f"{self.currently_selected_format.lower()}")

        # If the user did not select anything, we just state that no file was selected.
        # Could be improved to
        # return the currently selected one.
        print(f"Debug Log: Create Image at {image_file_location}.")
        if image_file_location == "" or image_file_location is None:
            print("Weak Error: Save Location is invalid or does not exist.")
            return

        # If we have the location given, we now run the program
        self.generate_image()

        # Copy generated image to new location:
        # First we get the file name for later
        # filename = os.path.basename(image_file_location)
        source_image_location = f"{os.getcwd()}\\data\\generated\\img.{self.currently_selected_format.lower()}"

        shutil.copyfile(source_image_location, image_file_location)
