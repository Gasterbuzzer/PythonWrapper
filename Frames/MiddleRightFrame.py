"""Middle Right Frame"""
import customtkinter
from PIL import Image


class MiddleRightFrame:
    """
    Middle Right Frame Class
    """

    def __init__(self, main_menu_reference) -> None:
        """
        Middle Right Frame Class (Showcase Image)

        :param main_menu_reference: Reference to Main Class (Not the Main Window)
        """
        # References
        self.main_menu_reference = main_menu_reference

        self.height = 590
        self.width = 790

        self.difference_pad = 5

        self.image_width = self.width - self.difference_pad * 3
        self.image_height = self.height - self.difference_pad * 4

        # Main Frame
        self.frame = customtkinter.CTkFrame(self.main_menu_reference.app)
        self.frame.configure(border_width=2, height=self.height, width=self.width)
        self.frame.grid(row=1, column=1, padx=(0, 5), pady=5, sticky="nse")
        self.frame.grid_propagate(False)

        # Image Display:

        self.image = customtkinter.CTkLabel(self.frame, text="")
        self.image.grid(row=0, column=0, padx=self.difference_pad, pady=self.difference_pad)

    def update_image(self, image=None) -> None:
        """
        Updates the image to a new one.
        :param image: Image to display (can be None)
        """

        if image is None:
            background_image = Image.open("data/generated/generated.jpg").resize((self.image_width, self.image_height))

            image_ctk_b = customtkinter.CTkImage(background_image, size=(self.image_width, self.image_height))

            self.image.configure(image=image_ctk_b)
            return

        else:
            # If not, we will decide our own.
            self.image.configure(image=image)
