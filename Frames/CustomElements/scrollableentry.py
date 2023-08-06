"""Class File containing a Scrollable Entry Widget"""

import customtkinter


class ScrollableEntry:
    """
    Class File containing a Scrollable Entry Widget
    """

    def __init__(self, master, width=100, height=7, placeholder_text="23", justify="center",
                 row=0, column=0, padx=(5, 0), pady=(10, 0), text_in_front="", _type="float",
                 disable_negative_zero=False) -> None:
        """
        Class File containing a Scrollable Entry Widget
        :param master:
        """
        # Parameters
        self.master = master
        self.width = width
        self.height = height
        self.placeholder_text = placeholder_text
        self.justify = justify
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady
        self.text_in_front = text_in_front
        self.type = _type
        self.disable_negative_zero = disable_negative_zero

        if self.text_in_front != "":
            # Text in front:
            self.front_label = customtkinter.CTkLabel(self.master, text=self.text_in_front, justify="right",
                                                      width=20)
            self.front_label.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady)

            self.column += 1

        # First Button (Minus)
        self.button_minus = customtkinter.CTkButton(master=self.master, text="-", width=20, height=self.height,
                                                    command=self.minus_value)
        self.button_minus.grid(row=self.row, column=self.column, padx=(5, 0), pady=self.pady)

        # Entry Box
        self.textbox = customtkinter.CTkEntry(master=self.master, width=self.width, height=self.height,
                                              placeholder_text=self.placeholder_text, justify=self.justify)

        self.textbox.grid(row=self.row, column=self.column + 1, padx=(5, 0), pady=self.pady)

        # Second Button (Plus)
        self.button_plus = customtkinter.CTkButton(master=self.master, text="+", width=20, height=self.height,
                                                   command=self.plus_value)
        self.button_plus.grid(row=self.row, column=self.column + 2, padx=self.padx, pady=self.pady)

    def get_value(self) -> float:
        """
        Gets the value stored in the entry.
        :return: (Float) Returns the given float value.
        """
        current_value = self.textbox.get()

        if current_value == "":
            if self.type.lower() == "float":
                return float(self.placeholder_text)
            elif self.type.lower() == "int":
                return int(self.placeholder_text)

        return current_value

    def minus_value(self) -> None:
        """
        Removes 1.0/1 from the given text.
        """

        text_box_value = self.textbox.get()
        text_box_value_ = text_box_value

        if text_box_value == "":
            text_box_value_ = self.placeholder_text

        if self.type.lower() == "float":
            current_value = float(text_box_value_)
        elif self.type.lower() == "int":
            current_value = int(text_box_value_)
        else:
            current_value = float(text_box_value_)

        if self.disable_negative_zero and current_value-1 < 0:
            return

        current_value -= 1

        self.textbox.delete(0, len(text_box_value))
        self.textbox.insert(0, current_value)

    def plus_value(self) -> None:
        """
        Adds 1.0/1 to the given text.
        """
        text_box_value = self.textbox.get()
        text_box_value_ = text_box_value

        if text_box_value == "":
            text_box_value_ = self.placeholder_text

        if self.type.lower() == "float":
            current_value = float(text_box_value_)
        elif self.type.lower() == "int":
            current_value = int(text_box_value_)
        else:
            current_value = float(text_box_value_)

        current_value += 1

        self.textbox.delete(0, len(text_box_value))
        self.textbox.insert(0, current_value)
