import bpy

bl_info = {
    "name": "Hide Selected",
    "author": "Micah Denn",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Scene > Hide/Show Selected",
    "description": "Enables (or disables) the visibility of all selected objects in render and sets a key frame for them.",
    "warning": "This was written fast and dirty because we needed it and it might crash if you try to hide objects that are already hidden or vice versa",
    #"doc_url": "",
    "category": "RND",
}

class OBJECT_OT_show(bpy.types.Operator):
    """Show selected objects in render and add keyframe"""
    bl_idname = "object.show"
    bl_label = "Show Selected"
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = False
            obj.keyframe_insert(data_path="hide_render") # Keyframe it.
            
        return {'FINISHED'}
        
class OBJECT_OT_hide(bpy.types.Operator):
    """Hide selected objects in render and add keyframe"""
    bl_idname = "hide.selected"
    bl_label = "Hide Selected"
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = True
            obj.keyframe_insert(data_path="hide_render") # Keyframe it.
            
        return {'FINISHED'}
    
    
class OBJECT_OT_hidev(bpy.types.Operator):
    """Hide selected objects in viewport and add keyframe"""
    bl_idname = "object.hidev"
    bl_label = "Hide In Viewport"
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_set(True)
            #obj.keyframe_insert(data_path="hide_viewport") # Keyframe it.
            
        return {'FINISHED'}


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Scene properties window"""
    bl_label = "Hide/Show Selected"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    
    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Royals Next Door Layout Addon")

        row = layout.row()
        row.operator("hide.selected")
        
        row = layout.row()
        row.operator("object.show")
        
        row = layout.row()
        
        row = layout.row()
        row.operator("object.hidev")

    
def register():
    bpy.utils.register_class(OBJECT_OT_hide)
    bpy.utils.register_class(OBJECT_OT_show)
    bpy.utils.register_class(OBJECT_OT_hidev)
    bpy.utils.register_class(HelloWorldPanel)

    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_hide)
    bpy.utils.unregister_class(OBJECT_OT_show)
    bpy.utils.unregister_class(OBJECT_OT_hidev)
    bpy.utils.unregister_class(HelloWorldPanel)
    
if __name__ == "__main__":
    register()
    
