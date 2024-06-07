bl_info = {
    "name": "Swa's QoL Tools",
    "author": "SwaMusic",
    "version": (0,0,1),
    "blender": (2,80,0),
    "location": "3D Viewport > Sidebar > Swa's QoL Tools",
    "description": "Tools to speed up some repetitive and tedious actions.",
    "category": "Development",
}

# give Python access to Blender's functionality
import bpy

class MESH_OT_collapse_every_other(bpy.types.Operator):
    """Checker Deselect and Collapse Edge Rings"""
    
    bl_idname = "mesh.collapse_every_other_edge"
    bl_label = "Collapse Every Other Edge"
    
    def execute(self, context):
        
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_mode(use_verts=True)
        
        return {"FINISHED"}

class VIEW3D_PT_my_custom_panel(bpy.types.Panel): # class naming convention 'CATEGORY_PT_name'
    pass
    # where to add the panel in the UI
    bl_space_type = "VIEW_3D" # 3D Viewport area
    bl_region_type = "UI" # Sidebar region

    # add labels
    bl_category = "Swa's QoL Tools" # found in the Sidebar
    bl_label = "Swa's QoL Tools" # found at the top of the Panel
    
    def draw(self, context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("mesh.collapse_every_other_edge", text="Collapse Every Other Edge")


# register the panel with Blender
def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.register_class(MESH_OT_collapse_every_other)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.unregister_class(MESH_OT_collapse_every_other)

if __name__ == "__main__":
    register()