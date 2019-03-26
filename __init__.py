import bpy
import _thread,time
from bl_ui.space_toolsystem_common import ToolSelectPanelHelper
from bpy.types import Panel
import os
from itertools import cycle
from bpy.props import BoolProperty, PointerProperty, \
    StringProperty, EnumProperty




bl_info = {
    "name": "Leftclick Mouse Select",
    "description": "LeftclickMouse seleccion configurator",
    "author": "Jorge Hernandez - Melenedez , Sav Martin",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User"
}

def start_thread():
    _thread.start_new_thread(thrd_func,())

def thrd_func():
    time.sleep(.1)
    keymaps_default_manipulator(False)
    

def keymaps_default_manipulator(modo):

# Disable Active tools
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    
    #Disable TransForm

    wm.keyconfigs.default.keymaps['3D View Tool: Transform'].keymap_items['transform.from_gizmo'].active = modo
    
    #Disable Move

    wm.keyconfigs.default.keymaps['3D View Tool: Move'].keymap_items['transform.translate'].active = modo
    
    #Disable Rotate

    wm.keyconfigs.default.keymaps['3D View Tool: Rotate'].keymap_items['transform.rotate'].active = modo
    
    #Disable Scale

    wm.keyconfigs.default.keymaps['3D View Tool: Scale'].keymap_items['transform.resize'].active = modo
    
    #Disable Select Box

    for kmi in wm.keyconfigs.default.keymaps['3D View Tool: Select Box'].keymap_items:
        kmi.active = modo

    #Disable Select Circle

    for kmi in wm.keyconfigs.default.keymaps['3D View Tool: Select Circle'].keymap_items:
        kmi.active = modo    

    #Disable Select Box

    for kmi in wm.keyconfigs.default.keymaps['3D View Tool: Select Lasso'].keymap_items:
        kmi.active = modo
    
    #Disable Set Tool By Name
    if 'wm.tool_set_by_name' in wm.keyconfigs.default.keymaps['3D View'].keymap_items:
        wm.keyconfigs.default.keymaps['3D View'].keymap_items['wm.tool_set_by_name'].active = modo

    #Disable Set 3D Cursor

    wm.keyconfigs.default.keymaps['3D View'].keymap_items['view3d.cursor3d'].active = modo

    #Disable Set 3D Cursor Move

    wm.keyconfigs.default.keymaps['3D View'].keymap_items['transform.translate'].active = modo


    #Disable Lasso Select Right Click +Ctrl
    
    for ki in  wm.keyconfigs.default.keymaps['3D View'].keymap_items:
        if "mode" in ki.properties:
            if ki.properties.mode == 'SUB':
                ki.active = modo
    
    #Disable Lasso Select Right Click shift+Ctrl 

    for ki in  wm.keyconfigs.default.keymaps['3D View'].keymap_items:
        if "mode" in ki.properties:
            if ki.properties.mode == 'ADD':
                ki.active = modo

    #Disable Call Menu Objet Mode

    for ki in  wm.keyconfigs.default.keymaps['Object Mode'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_object_context_menu':
                ki.active = modo
    
    #Disable Call Menu Edit Mode

    for ki in  wm.keyconfigs.default.keymaps['Mesh'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_edit_mesh_context_menu':
                ki.active = modo

    #Disable Call Menu Pose

    for ki in  wm.keyconfigs.default.keymaps['Pose'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_pose_context_menu':
                ki.active = modo

    #Disable Call Menu Shade Editor

    for ki in  wm.keyconfigs.default.keymaps['Node Editor'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'NODE_MT_context_menu':
                ki.active = modo

    #Disable Call Menu Curve

    for ki in  wm.keyconfigs.default.keymaps['Curve'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_edit_curve_context_menu':
                ki.active = modo

    #Disable Call Menu Armature

    for ki in  wm.keyconfigs.default.keymaps['Armature'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_armature_context_menu':
                ki.active = modo 

    #Disable Call Menu Weight Paint

    wm.keyconfigs.default.keymaps['Weight Paint'].keymap_items['wm.call_panel'].active = modo

    #Disable Call Menu Vertex Paint

    wm.keyconfigs.default.keymaps['Vertex Paint'].keymap_items['wm.call_panel'].active = modo 
    
    #Disable Call Menu Particle

    wm.keyconfigs.default.keymaps['Particle'].keymap_items['wm.call_menu'].active = modo
    
    #Disable  Lasso Shade Editor

    for item in wm.keyconfigs.default.keymaps['Node Editor'].keymap_items:
        if item.idname == 'node.select_lasso':
            item.active = modo

    #Disable  Lasso Weight Paint Vertex Selection

    for item in wm.keyconfigs.default.keymaps['Weight Paint Vertex Selection'].keymap_items:
        if item.idname == 'view3d.select_lasso':
            item.active = modo   






addon_keymaps = []


def register_keymap():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon 

    # Leftclik Keymap configuration     ************************************************************************************************************************************

    #Add Select in Select Box
    km = kc.keymaps.new(name="3D View Tool: Select Box", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

    #Add Select in Select Circle

    km = kc.keymaps.new(name="3D View Tool: Select Circle", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))    

    #Add Select in Select Lasso

    km = kc.keymaps.new(name="3D View Tool: Select Lasso", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

    #Add Select in Transform

    km = kc.keymaps.new(name="3D View Tool: Transform", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

    #Add Select in Move

    km = kc.keymaps.new(name="3D View Tool: Move", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

    #Add Select in Rotate

    km = kc.keymaps.new(name="3D View Tool: Rotate", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

    #Add Select in Scale

    km = kc.keymaps.new(name="3D View Tool: Scale", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select", 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi)) 
    
    #Add Call Menu In Objetc Mode

    km = kc.keymaps.new(name="Object Mode", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_MT_object_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Edit Mode

    km = kc.keymaps.new(name="Mesh", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_MT_object_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Dopesheet

    km = kc.keymaps.new(name="Dopesheet", space_type="DOPESHEET_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'DOPESHEET_MT_context_menu'
    addon_keymaps.append((km, kmi))

    # Add Call Menu In Animation Channels

    km = kc.keymaps.new(name="Animation Channels", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'DOPESHEET_MT_channel_context_menu'
    addon_keymaps.append((km, kmi))

    # Add Call Menu In Graph Editor
    
    km = kc.keymaps.new(name="Graph Editor", space_type="GRAPH_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'GRAPH_MT_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Pose

    km = kc.keymaps.new(name="Pose", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_MT_pose_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu Shade Editor

    km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'NODE_MT_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu Clip Editor

    km = kc.keymaps.new(name="Clip Editor", space_type="CLIP_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'CLIP_MT_tracking_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Curve

    km = kc.keymaps.new(name="Curve", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_MT_edit_curve_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Armature

    km = kc.keymaps.new(name="Armature", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_MT_armature_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Weight Paint

    km = kc.keymaps.new(name="Weight Paint", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_panel", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_PT_paint_weight_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Weight Paint

    km = kc.keymaps.new(name="Vertex Paint", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_panel", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_PT_paint_vertex_context_menu'
    addon_keymaps.append((km, kmi))
    
    #Add Call Menu In Particle

    km = kc.keymaps.new(name="Particle", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS')
    kmi.properties.name = 'VIEW3D_MT_particle_context_menu'
    addon_keymaps.append((km, kmi))


    #Add Set 3D Cursor

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.cursor3d", 'RIGHTMOUSE', 'PRESS', alt = True)
    addon_keymaps.append((km, kmi))

    #Add Set 3D Cursor Move

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("transform.translate", 'EVT_TWEAK_R', 'ANY', alt = True)
    kmi.properties.cursor_transform = True
    kmi.properties.release_confirm = True
    addon_keymaps.append((km, kmi))
    
    #Add Set Deselect

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select_or_deselect_all", 'RIGHTMOUSE', 'CLICK')
    addon_keymaps.append((km, kmi))

    #Add Vertex Connect Path

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("mesh.vert_connect_path", 'RIGHTMOUSE', 'CLICK', shift = True)
    addon_keymaps.append((km, kmi))




    # *********************************************************************************************************************************************
    
    # box select:
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.select_box", 'EVT_TWEAK_R', 'ANY')
    kmi.properties.mode = 'SET'
    kmi.active = False
    addon_keymaps.append((km, kmi))
    
    kmi = km.keymap_items.new("view3d.select_box", 'EVT_TWEAK_R', 'ANY', shift=True)
    kmi.properties.mode = 'ADD'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("view3d.select_box", 'EVT_TWEAK_R', 'ANY', ctrl=True, shift=True)
    kmi.properties.mode = 'XOR'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("view3d.select_box", 'EVT_TWEAK_R', 'ANY', ctrl=True)
    kmi.properties.mode = 'SUB'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    # lasso:
    kmi = km.keymap_items.new("view3d.select_lasso", 'EVT_TWEAK_R', 'ANY')
    kmi.properties.mode = 'SET'
    kmi.active = False
    addon_keymaps.append((km, kmi))
    
    kmi = km.keymap_items.new("view3d.select_lasso", 'EVT_TWEAK_R', 'ANY', shift=True)
    kmi.properties.mode = 'ADD'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("view3d.select_lasso", 'EVT_TWEAK_R', 'ANY', ctrl=True)
    kmi.properties.mode = 'SUB'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    # Circle:
    kmi = km.keymap_items.new("view3d.select_circle", 'EVT_TWEAK_R', 'ANY')
    kmi.properties.mode = 'ADD'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("view3d.select_circle", 'EVT_TWEAK_R', 'ANY', ctrl=True)
    kmi.properties.mode = 'SUB'
    kmi.active = False
    addon_keymaps.append((km, kmi))

    # ciclico:
    kmi = km.keymap_items.new("mode.selection", 'W', 'PRESS', ctrl=True)
    addon_keymaps.append((km, kmi))


def unregister_keymap():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def initianSettings(target):
    current = target
    if current == 'lasso':
        for km, kmi in addon_keymaps:
            if kmi.idname == "view3d.select_box":
                if kmi.active:
                    kmi.active = False
            elif kmi.idname == "view3d.select_circle":
                if kmi.active:
                    kmi.active = False
            elif kmi.idname == "view3d.select_lasso":
                if not kmi.active:
                    kmi.active = True
    elif current == 'circle':
        for km, kmi in addon_keymaps:
            if kmi.idname == "view3d.select_lasso":
                if kmi.active:
                    kmi.active = False
            elif kmi.idname == "view3d.select_box":
                if kmi.active:
                    kmi.active = False
            elif kmi.idname == "view3d.select_circle":
                if not kmi.active:
                    kmi.active = True
    elif current == 'box':
        for km, kmi in addon_keymaps:
            if kmi.idname == "view3d.select_lasso":
                if kmi.active:
                    kmi.active = False
            elif kmi.idname == "view3d.select_circle":
                if kmi.active:
                    kmi.active = False
            elif kmi.idname == "view3d.select_box":
                if not kmi.active:
                    kmi.active = True

def comboChanged(self, context):
    current = bpy.context.scene.lcmcomboBox
    initianSettings(current)


def mySceneProperties():
    
    dirname = bpy.utils.resource_path('LOCAL')
    filename = os.path.join(dirname, "datafiles", "icons", 'ops.generic.select_box' + ".dat")
    icob =  bpy.app.icons.new_triangles_from_file(filename)

    filename = os.path.join(dirname, "datafiles", "icons", 'ops.generic.select_circle' + ".dat")
    icoc =  bpy.app.icons.new_triangles_from_file(filename)

    filename = os.path.join(dirname, "datafiles", "icons", 'ops.generic.select_lasso' + ".dat")
    icol =  bpy.app.icons.new_triangles_from_file(filename)

    comboItems = [
        ("box", " ", "", icob, 1),
        ("circle", " ", "", icoc, 2),
        ("lasso", " ", "", icol, 3),
    ]
    bpy.types.Scene.lcmcomboBox = bpy.props.EnumProperty(
        items=comboItems,
        name="Selection",
        description="Selection Type",
        default="box",
        update=comboChanged
    )


class Switcher(bpy.types.Operator):
    bl_label = "Select Mode"
    bl_idname = "mode.selection"
    bl_description = "Select Mode"

    modos = ['box', 'circle', 'lasso']
    pool = cycle(modos)

    def execute(self, context):
        self.modo = next(self.pool)
        bpy.context.scene.lcmcomboBox = self.modo
        return {'FINISHED'}


class ICON_PT_Icon(ToolSelectPanelHelper, Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = ""
    bl_options = {'HIDE_HEADER'}

    @staticmethod
    def draw(self, context):
        scn = bpy.context.scene
        layout = self.layout
        row = layout.row(align=True)
        row.scale_y = 2.0
        row.scale_x = 2.0
        row.prop(scn, "lcmcomboBox", text="", icon_only=True)

    @classmethod
    def tools_from_context(cls, context, mode=None):
        if mode is None:
            mode = context.mode
        for tools in (cls._tools[None], cls._tools.get(mode, ())):
            for item in tools:
                print(item)
                if not (type(item) is ToolDef) and callable(item):
                    yield from item(context)
                else:
                    yield item

    @classmethod
    def tools_all(cls):
        yield from cls._tools.items()


    _tools = { None: [] }


class SAM_PrefPanel(bpy.types.AddonPreferences):
    bl_idname = __name__
        
    prefs_tabs : EnumProperty(
        items=(('info', "Info", "Info"),))
    
    def draw(self, context):
            layout = self.layout
            wm = bpy.context.window_manager
            
            
            row= layout.row(align=True)
            row.prop(self, "prefs_tabs", expand=True)
            layout = self.layout
            layout.label(text="Modified Keymap :")
            row= layout.row(align=True)
            
            layout.label(text="Deselect everyting                                      LEFTMOUSE / RIGHTMOUSE")
            layout.label(text="3D Cursor                                                                 ALT + RIGHTMOUSE ")
            layout.label(text="Box Select, Lasso Select, Circle Select                             RIGHTMOUSE")
            layout.label(text="Change Default Selecction                                                       CTRL + W")
            layout.label(text="Connect Vertex Path (Edit Mode)                        SHIFT + RIGHTMOUSE")
            layout.label(text="All Contex Menus                                                                                   W")
            layout.operator("wm.url_open", text="GitHub").url = "https://github.com/SavMartin/LeftClickAddon"


classes = ( 
    ICON_PT_Icon,
    Switcher,
    SAM_PrefPanel,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    start_thread()
    register_keymap()
    mySceneProperties()
    initianSettings("box")
    
    


def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        unregister_class(cls)

    del bpy.types.Scene.lcmcomboBox
    keymaps_default_manipulator(True)
    unregister_keymap()


if __name__ == "__main__":
    register()
