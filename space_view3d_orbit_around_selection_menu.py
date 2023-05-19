bl_info = {
    "name": "Orbit Around Selection Menu",
    "author": "Daniel Hilpert",
    "location": "View > Navigation > Orbit Around Selection",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "category": "3D View",
}

import bpy


class OrbitAroundSelection(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "view3d.orbit_around_selection"
    bl_label = "Orbit Around Selection"

    def execute(self, context):
        bpy.context.preferences.inputs.use_rotate_around_active = not \
            bpy.context.preferences.inputs.use_rotate_around_active
        return {'FINISHED'}


def menu_func(self, context):
    # make the menu function toggle the state
    self.layout.operator(
        OrbitAroundSelection.bl_idname,
        text=OrbitAroundSelection.bl_label,
        icon='CHECKBOX_HLT' if
        bpy.context.preferences.inputs.use_rotate_around_active else
        'CHECKBOX_DEHLT'
    )


def register():
    bpy.utils.register_class(OrbitAroundSelection)
    bpy.types.VIEW3D_MT_view_navigation.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OrbitAroundSelection)


if __name__ == "__main__":
    register()
