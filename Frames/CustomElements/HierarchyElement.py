"""Class File containing an Element of the Hierarchy"""

import customtkinter
from Frames.SettingsWindow import SettingsWindow


class HE:
    """
    Class File containing an Element of the Hierarchy (Frame and so on)
    """

    def __init__(self, outside_reference, object_reference, element_text="DefaultName", current_recursion=0,
                 row=0, leftframe_class_reference=None) -> None:
        """
        Class representing a Frame, Text and some Symbol of an Element of the Hierarchy.

        :param outside_reference: Reference to LeftFrame.
        :param object_reference: Reference to Object to represent when clicking on it.
        :param element_text: Text to be displayed on Text.
        :param current_recursion: Current Recursion Step
        :param row: Row to display
        :param leftframe_class_reference: Left Frame Reference
        """

        # Self Values
        self.left_frame = outside_reference
        self.object_reference = object_reference
        self.element_text = element_text
        self.current_recursion = current_recursion
        self.row = row
        self.leftframe_class_reference = leftframe_class_reference

        try:
            index_value = object_reference.index
        except AttributeError:
            # Given Object does not have an Index and thus must be a group (for now):
            index_value = ""

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
                                                  text=f"{element_text.title()}{index_value}")
        new_group_member.grid(row=self.row, column=0, padx=(5, 0), pady=5)
        new_group_member.grid_propagate(False)

        new_group_member.bind("<Button-1>", self.open_settings)

        self.leftframe_class_reference.hierarchy_render.append(new_frame_member)
        self.leftframe_class_reference.hierarchy_info.append(object_reference)

    def open_settings(self, event=None) -> None:
        """
        Opens the settings for the given object.
        :param event:
        """
        settings_window = SettingsWindow(self.object_reference, self.leftframe_class_reference.app.app)
        settings_window.open_window()