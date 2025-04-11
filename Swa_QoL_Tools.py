bl_info = {
    "name": "Swa's QoL Tools",
    "author": "SwaMusic",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar > Swa's QoL Tools",
    "description": "Tools to speed up some repetitive and tedious actions.",
    "category": "Development",
}

import bpy

class MESH_OT_collapse_every_other(bpy.types.Operator):
    """Checker Deselect and Collapse Edge Rings"""
    bl_idname = "mesh.collapse_every_other_edge"
    bl_label = "Collapse Every Other Edge"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_mode(use_verts=True)
        return {"FINISHED"}

class MESH_OT_add_split_normals(bpy.types.Operator):
    """Add Custom Split Normals to Selected Meshes"""
    bl_idname = "mesh.add_custom_split_normals"
    bl_label = "Add Custom Split Normals"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        for obj in sel_objs:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.customdata_custom_splitnormals_add()
        return {"FINISHED"}

class MESH_OT_rename_to_material(bpy.types.Operator):
    """Rename Selected Objects to Their Material Name"""
    bl_idname = "mesh.rename_to_material"
    bl_label = "Rename to Material Name"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH' and len(obj.data.materials) > 0:
                material = obj.data.materials[0]
                if material:
                    material_name = material.name
                    obj.name = material_name
                    obj.data.name = f"{material_name}"
        return {"FINISHED"}

class VIEW3D_PT_my_custom_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Swa's QoL Tools"
    bl_label = "Swa's QoL Tools"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.collapse_every_other_edge", text="Collapse Every Other Edge")
        layout.operator("mesh.add_custom_split_normals", text="Add Split Normals")
        layout.operator("mesh.rename_to_material", text="Rename to Material")

def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.register_class(MESH_OT_collapse_every_other)
    bpy.utils.register_class(MESH_OT_add_split_normals)
    bpy.utils.register_class(MESH_OT_rename_to_material)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.unregister_class(MESH_OT_collapse_every_other)
    bpy.utils.unregister_class(MESH_OT_add_split_normals)
    bpy.utils.unregister_class(MESH_OT_rename_to_material)

if __name__ == "__main__":
    register()
