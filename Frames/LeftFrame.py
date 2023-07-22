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

            return_value = self.recurse_over_app(group_app)

            # Getting return value name:
            object_name = next(iter(return_value))

            if object_name == "sphere":
                self.app.hierarchy.append(return_value)
            else:
                # We don't do anything for now.
                print(f"H: {self.app.hierarchy}")

        # Now that we have loaded each object into memory, we can try rendering.
        print("\n")

    def recurse_over_app(self, object_app, object_name="NoNameGiven", group_index="RecursiveFunctionNoGroupGiven",
                         _index_possibly_given="", debug=False) -> dict:
        """
        Recurses over objects and gets, the according objects.
        """

        index_possibly_given = _index_possibly_given

        # Find out the name
        if object_name == "NoNameGiven":
            for name in object_app.keys():
                if debug:
                    print("Object Name: " + name + "\n")
                if name.lower() == "index":
                    index_possibly_given = name
                else:
                    object_name = name

        # Loop Now
        if object_name.lower() == "sphere":
            object_app = object_app["sphere"]
            try:
                position = object_app["position"]
            except KeyError:
                print(f"Weak Error Log: Sphere Position for {group_index} is not given.")
                position = None

            try:
                radius = object_app["radius"]
            except KeyError:
                print(f"Weak Error Log: Sphere Radius for {group_index} is not given.")
                radius = None

            try:
                color_json = object_app["color"]
                # Now that we have the color, we must convert it to a functioning object. :(

                try:
                    color_ambient = color_json["ambient"]
                except KeyError:
                    print(f"Weak Error Log: Color Ambient for {object_app} {group_index} is not given.")
                    color_ambient = None
                try:
                    color_diffuse = color_json["diffuse"]
                except KeyError:
                    print(f"Weak Error Log: Color Diffuse for {object_app} {group_index} is not given.")
                    color_diffuse = None
                try:
                    color_specular = color_json["specular"]
                except KeyError:
                    print(f"Weak Error Log: Color Specular for {object_app} {group_index} is not given.")
                    color_specular = None
                try:
                    color_reflected = color_json["reflected"]
                except KeyError:
                    print(f"Weak Error Log: Color Reflected for {object_app} {group_index} is not given.")
                    color_reflected = None
                try:
                    color_refracted = color_json["refracted"]
                except KeyError:
                    print(f"Weak Error Log: Color Refracted for {object_app} {group_index} is not given.")
                    color_refracted = None
                try:
                    color_shininess = color_json["shininess"]
                except KeyError:
                    print(f"Weak Error Log: Color Shininess for {object_app} {group_index} is not given.")
                    color_shininess = None

                # Create Object
                color = Color(color_ambient, color_diffuse, color_specular, color_reflected,
                              color_refracted, color_shininess)
                # Now we have the object, we continue

            except KeyError:
                print(f"Weak Error Log: Sphere Color for {group_index} is not given.")
                color = None

            try:
                if index_possibly_given == "":
                    i = object_app["index"]
                else:
                    i = index_possibly_given
            except KeyError:
                print(f"Weak Error Log: Sphere Index for {group_index} is not given.")
                i = None

            return {"sphere": Sphere(position, radius, color, i)}

        elif object_name.lower() == "union":

            union_elements = []

            for _e in object_app["union"]:

                # Getting Object Name
                _e_name = "NoNameFoundRecursive"
                for name in _e:
                    _e_name = name

                if _e_name != "index":
                    union_elements.append(self.recurse_over_app(_e, _e_name))

            return {"Group": union_elements}

        elif object_name.lower() == "translation":

            new_recursive_object = object_app["translation"]["subject"]

            # Getting Object Name
            new_recursive_object_name = "NoNameFoundRecursive"
            for name in new_recursive_object:

                if name.lower() == "index":
                    index_possibly_given = name
                else:
                    new_recursive_object_name = name

            return self.recurse_over_app(new_recursive_object, new_recursive_object_name,
                                         _index_possibly_given=index_possibly_given)

        elif object_name.lower() == "scaling":

            new_recursive_object = object_app["scaling"]["subject"]

            # Getting Object Name
            new_recursive_object_name = "NoNameFoundRecursive"
            for name in new_recursive_object:

                if name.lower() == "index":
                    index_possibly_given = name
                else:
                    new_recursive_object_name = name

            return self.recurse_over_app(new_recursive_object, new_recursive_object_name,
                                         _index_possibly_given=index_possibly_given)

        elif object_name.lower() == "halfspace":

            return {"ObjectNotImplemented": object_name}

        else:
            return {"ObjectNotFound": object_name}

    def render_frame_objects(self) -> None:
        """
        Renders the created objects. (!!!Must be created beforehand!!!)
        """
        index_row = 0
        width_row = 360
        child_modifier_size = 40

        for index, group in enumerate(self.app.hierarchy):

            # Get the Name of group
            group_name = "Could not get Name."
            name = "NameCouldNotBeFound"
            for name in group.keys():
                group_name: str = name

            if group_name == "sphere":
                # We got an Object and not a frame

                # Create the Frame
                new_frame_member = customtkinter.CTkFrame(master=self.hierarchy_frame)
                new_frame_member.configure(border_width=2, height=38, width=width_row)
                new_frame_member.grid(row=index_row, column=0, padx=(5, 0), pady=5)
                new_frame_member.grid_propagate(False)

                # Frame Name:
                new_group_member = customtkinter.CTkLabel(new_frame_member, height=30,
                                                          width=width_row - 30,
                                                          text=f"{name.title()}{group[group_name].index}")
                new_group_member.grid(row=index_row, column=0, padx=(5, 0), pady=5)
                new_group_member.grid_propagate(False)

                self.hierarchy_render.append(new_frame_member)

                index_row += 1
                continue

            else:
                print(f"Group Name: {group_name}")

            # Create the Frame
            new_frame_group = customtkinter.CTkFrame(master=self.hierarchy_frame)
            new_frame_group.configure(border_width=2, height=38, width=width_row)
            new_frame_group.grid(row=index_row, column=0, padx=(5, 0), pady=5)
            new_frame_group.grid_propagate(False)

            # Frame Name:
            new_group_name = customtkinter.CTkLabel(new_frame_group, height=30, width=width_row - 30, text=group_name)
            new_group_name.grid(row=0, column=0, padx=5, pady=5)
            new_group_name.grid_propagate(False)

            self.hierarchy_render.append(new_frame_group)

            # Now for each group we render their respective objects (for now only the name)
            for group_member in group.values():

                # We set the parent of the member
                parent = group_name

                # We adapt to a type of object
                if type(group_member) is Sphere:
                    name = "Sphere"
                else:
                    print(f"List: {group_member}")
                    name = "Unknown Type"

                # Create the Frame
                new_frame_member = customtkinter.CTkFrame(master=self.hierarchy_frame)
                new_frame_member.configure(border_width=2, height=38, width=width_row - child_modifier_size)
                new_frame_member.grid(row=index_row + 1, column=0, padx=(45, 0), pady=5)
                new_frame_member.grid_propagate(False)

                # Frame Name:
                new_group_member = customtkinter.CTkLabel(new_frame_member, height=30,
                                                          width=width_row - child_modifier_size - 30, text=name)
                new_group_member.grid(row=0, column=0, padx=5, pady=5)
                new_group_member.grid_propagate(False)

                self.hierarchy_render.append(new_frame_member)

                index_row += 2

        index_row += 1

    def destroy_frame_objects(self) -> None:
        """
        Destroy all Objects
        """
        for object_app in self.hierarchy_render:
            object_app.destroy()

        self.app.hierarchy = []
        self.hierarchy_render = []
