"""Class File containing an Element of the Hierarchy"""

import customtkinter


class HE:
    """
    Class File containing an Element of the Hierarchy (Frame and so on)
    """

    def __init__(self, outside_reference, object_reference, element_text="DefaultName", current_recursion=0,
                 row=0) -> None:
        """
        Class representing a Frame, Text and some Symbol of an Element of the Hierarchy.

        :param outside_reference: Reference to LeftFrame.
        :param object_reference: Reference to Object to represent when clicking on it.
        :param element_text: Text to be displayed on Text.
        :param current_recursion: Current Recursion Step
        """

        # Self Values
        self.left_frame = outside_reference
        self.object_reference = object_reference
        self.element_text = element_text
        self.current_recursion = current_recursion
        self.row = row

        # CONSTANTS
        default_width_row = 360
        child_modifier_size = 40

        # Calculate width and padx based on recursion depth.
        width_row = default_width_row - child_modifier_size * self.current_recursion
        padx_value = 5 + child_modifier_size * self.current_recursion

        # Create the Frame
        new_frame_member = customtkinter.CTkFrame(master=self.left_frame)
        new_frame_member.configure(border_width=2, height=38, width=width_row)
        new_frame_member.grid(row=self.row, column=0, padx=(padx_value, 0), pady=5)
        new_frame_member.grid_propagate(False)

        new_frame_member.bind("<Button-1>", self.open_settings)

        # Frame Name:
        new_group_member = customtkinter.CTkLabel(new_frame_member, height=30,
                                                  width=width_row - 30,
                                                  text=f"{element_text.title()}{object_reference.index}")
        new_group_member.grid(row=self.row, column=0, padx=(5, 0), pady=5)
        new_group_member.grid_propagate(False)

        new_group_member.bind("<Button-1>", self.open_settings)

        self.left_frame.hierarchy_render.append(new_frame_member)
        self.left_frame.hierarchy_info.append(object_reference)

    def open_settings(self, event=None) -> None:
        """
        Opens the settings for the given object.
        :param event:
        """
        print(self.object_reference)
