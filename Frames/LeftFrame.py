"""Left Frame"""
import customtkinter
from Objects.Sphere import Sphere
from Objects.Color import Color


class LeftFrame:
    """
        Left Frame Class
    """

    def __init__(self, main_menu_reference) -> None:

        self.app = main_menu_reference

        # Frames
        self.frame = customtkinter.CTkFrame(main_menu_reference.app)
        self.frame.configure(border_width=2, height=790, width=400)
        self.frame.grid(row=0, column=0, padx=5, pady=5, sticky="nws", rowspan=3)
        self.frame.grid_propagate(False)

        self.inside_frame_top = customtkinter.CTkFrame(master=self.frame)
        self.inside_frame_top.configure(border_width=2, height=38, width=390)
        self.inside_frame_top.grid(row=0, column=0, padx=(5, 0), pady=5)
        self.inside_frame_top.grid_propagate(False)

        # Title for Frame
        self.title = customtkinter.CTkLabel(self.inside_frame_top, font=("Franklin Gothic Medium", 22), height=30,
                                            width=370, text="Hierarchy")
        self.title.grid(row=0, column=0, padx=5, pady=5)
        self.title.grid_propagate(False)

        # Frame for Hierarchy (We will make it scrollable later.)
        self.hierarchy_frame = customtkinter.CTkFrame(master=self.frame)
        self.hierarchy_frame.configure(border_width=2, height=672, width=390)
        self.hierarchy_frame.grid(row=1, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
        self.hierarchy_frame.grid_propagate(False)

        # Frame for Buttons
        self.button_frame = customtkinter.CTkFrame(master=self.frame)
        self.button_frame.configure(border_width=2, height=55, width=390)
        self.button_frame.grid(row=2, column=0, padx=(5, 0), pady=(5, 0), sticky="s")
        self.button_frame.grid_propagate(False)

        # Hierarchy
        self.hierarchy_render = []

    def create_hierarchy(self) -> None:
        """
        Creates the view for the objects.
        """

        # We have different Object Groups, we then go through each group and read the objects.
        for index, group_app in enumerate(self.app.objects):
            # print(f"{group_app}\n")

            group_index = f"Group{index}"

            # Create Group in Hierarchy (For now at least, later we look into it further)
            self.app.hierarchy.append({group_index: {}})

            # Now we append the objects.
            for object_name, object_app in group_app.items():

                if object_name == "sphere":
                    # Try getting the info of the object

                    try:
                        position = object_app["position"]
                    except KeyError:
                        print(f"Error Log: Sphere Position for {group_index} is not given.")
                        position = None

                    try:
                        radius = object_app["radius"]
                    except KeyError:
                        print(f"Error Log: Sphere Radius for {group_index} is not given.")
                        radius = None

                    try:
                        color_json = object_app["color"]
                        # Now that we have the color, we must convert it to a functioning object. :(

                        try:
                            color_ambient = color_json["ambient"]
                        except KeyError:
                            print(f"Error Log: Color Ambient for {object_app} {group_index} is not given.")
                            color_ambient = None
                        try:
                            color_diffuse = color_json["diffuse"]
                        except KeyError:
                            print(f"Error Log: Color Diffuse for {object_app} {group_index} is not given.")
                            color_diffuse = None
                        try:
                            color_specular = color_json["specular"]
                        except KeyError:
                            print(f"Error Log: Color Specular for {object_app} {group_index} is not given.")
                            color_specular = None
                        try:
                            color_reflected = color_json["reflected"]
                        except KeyError:
                            print(f"Error Log: Color Reflected for {object_app} {group_index} is not given.")
                            color_reflected = None
                        try:
                            color_refracted = color_json["refracted"]
                        except KeyError:
                            print(f"Error Log: Color Refracted for {object_app} {group_index} is not given.")
                            color_refracted = None
                        try:
                            color_shininess = color_json["shininess"]
                        except KeyError:
                            print(f"Error Log: Color Shininess for {object_app} {group_index} is not given.")
                            color_shininess = None

                        # Create Object
                        color = Color(color_ambient, color_diffuse, color_specular, color_reflected,
                                      color_refracted, color_shininess)
                        # Now we have the object, we continue

                    except KeyError:
                        print(f"Error Log: Sphere Color for {group_index} is not given.")
                        color = None

                    try:
                        i = object_app["index"]
                    except KeyError:
                        print(f"Error Log: Sphere Index for {group_index} is not given.")
                        i = None

                    self.app.hierarchy[index][group_index] = Sphere(position, radius, color, i)
                    # print(self.app.hierarchy[index][group_index])

                else:
                    print(f"Current Unknown Object: {object_app}")

        # Now that we have loaded each object into memory, we can try rendering.
        print("\n")

    def render_frame_objects(self) -> None:
        """
        Renders the created objects. (!!!Must be created beforehand!!!)
        """

        for index, group in enumerate(self.app.hierarchy):
            # Create the Frame
            new_frame_group = customtkinter.CTkFrame(master=self.hierarchy_frame)
            new_frame_group.configure(border_width=2, height=38, width=380)
            new_frame_group.grid(row=index, column=0, padx=(5, 0), pady=5)
            new_frame_group.grid_propagate(False)

            # Frame Name:
            new_group_name = customtkinter.CTkLabel(new_frame_group, height=30, width=370, text=group)
            new_group_name.grid(row=0, column=0, padx=5, pady=5)
            new_group_name.grid_propagate(False)

            self.hierarchy_render.append(new_frame_group)

