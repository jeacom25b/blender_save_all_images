import bpy

bl_info = {
    "name": "Save All Images",
    "description": "Save all images data_blocks",
    "author": "jean Da Costa Machado",
    "version": (0, 0, 1),
    "blender": (2, 78, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Image"}


class SaveAllPanel(bpy.types.Panel):
    bl_idname = "save_image.save_panel"
    bl_label = "Save All Images"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Save_images"
    
    def draw(self, context):
        layout = self.layout
        layout.label("Save all images at once")
        layout.operator("save_image.save_all")


class SaveAllImages(bpy.types.Operator):
    bl_idname = "save_image.save_all"
    bl_label = "Save All Images"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        
        for image in bpy.data.images:
            image.save()
        return {"FINISHED"}
    



def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
