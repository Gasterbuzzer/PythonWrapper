"""Top Right Frame"""
import customtkinter
from PIL import Image
import subprocess
import sys


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

        self.available_formats = ["PNG", "JPG"]

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

    def update_currently_selected_format(self, event) -> None:
        """
        Updates the internal selection to newly selected format.
        :param event: Event when triggered
        """

        print(f"Debug Log: Updated Image format to '{self.format_select_box.get()}'.")

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

        # We create the image from our c++ library/project.
        if sys.platform.lower() == "linux" or sys.platform.lower() == "linux2":
            # Linux Command
            print("Debug Log: Platform has been identified as linux.")
            print("Debug Log: Running image generation...")
            _subp = subprocess.Popen("ping www.google.com", shell=True, stdout=subprocess.PIPE).communicate()[0]

            print("Debug Log: Image has been generated!")
            # Now you would technically get the image location and load it from there.

            # Simulating an image.
            background_image = Image.open("data/generated/generated_2.jpg").resize((image_width, image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(image_width, image_height))

            self.main_menu_reference.middle_right_frame.update_image(image=image_ctk_b)

            print("Debug Log: Displaying generated image.")

        elif sys.platform.lower() == "windows" or sys.platform.lower() == "win32":
            print("Debug Log: Platform has been identified as windows.")

            print("Debug Log: Running image generation...")
            _subp = subprocess.Popen("ping www.google.com", shell=True, stdout=subprocess.PIPE).communicate()[0]

            print("Debug Log: Image has been generated!")

            # Now you would technically get the image location and load it from there.

            # Simulating an image.
            background_image = Image.open("data/generated/generated_2.jpg").resize((image_width, image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(image_width, image_height))

            self.main_menu_reference.middle_right_frame.update_image(image=image_ctk_b)

            print("Debug Log: Displaying generated image.")

        else:
            print(f"Error Log: Unknown Platform {sys.platform}. Could not generate image, using fallback.")

            background_image = Image.open("data/generated/generated.jpg").resize((image_width, image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(image_width, image_height))

            self.main_menu_reference.middle_right_frame.update_image(image=image_ctk_b)

            print("Debug Log: Displaying fallback image.")



