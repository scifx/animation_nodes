import bpy
from . import tree_info
from . import event_handler
from . update import updateEverything
from . utils.handlers import eventHandler
from . execution.measurements import resetMeasurements

class EventState:
    def __init__(self):
        self.reset()
        self.isRendering = False

    def reset(self):
        self.treeChanged = False
        self.fileChanged = False
        self.addonChanged = False
        self.propertyChanged = False

    def getActives(self):
        events = set()
        if self.treeChanged: events.add("Tree")
        if self.fileChanged: events.add("File")
        if self.addonChanged: events.add("Addon")
        if self.propertyChanged: events.add("Property")
        return events

event = EventState()

@eventHandler("ALWAYS")
def evaluateRaisedEvents():
    event_handler.update(event.getActives())
    event.reset()

evaluatedDepsgraph = None
@eventHandler("FRAME_CHANGE_POST")
def frameChanged(scene, depsgraph):
    global evaluatedDepsgraph
    evaluatedDepsgraph = depsgraph
    event_handler.update(event.getActives().union({"Frame"}))
    evaluatedDepsgraph = None

# This handler is only defined as a workaround for a limitation in Blender, where the frame changed
# handler doesn't execute if a scene is not being rendered during the rendering pipeline, for
# instance, when a sequence editor is active and doesn't reference a scene sequence strip. So in
# this handler, we call the update handler as a frame update if we determine that the frame changed
# handler will not run due to the aforementioned reasons.
@eventHandler("RENDER_PRE")
def renderPre(scene):
    if not scene.render.use_sequencer or scene.sequence_editor is None: return
    for sequence in scene.sequence_editor.sequences_all:
        if sequence.type != "SCENE": continue
        if sequence.frame_final_start <= scene.frame_current <= sequence.frame_final_end: return

    event_handler.update(event.getActives().union({"Frame"}))

@eventHandler("DEPSGRAPH_UPDATE_POST")
def sceneChanged(scene, depsgraph):
    global evaluatedDepsgraph
    evaluatedDepsgraph = depsgraph
    event_handler.update(event.getActives().union({"Scene"}))
    evaluatedDepsgraph = None

def propertyChanged(self = None, context = None):
    event.propertyChanged = True
    resetMeasurements()

@eventHandler("FILE_LOAD_POST")
def fileLoaded():
    from . base_types.update_file import updateFile
    from . nodes.subprogram.subprogram_sockets import forceSubprogramUpdate
    updateFile()
    tree_info.updateIfNecessary()
    forceSubprogramUpdate()
    event.fileChanged = True
    treeChanged()

    # Always handler doesn't work when in background mode. Update everything
    # here instead to facilitate manual tree execution.
    if bpy.app.background:
        updateEverything()

@eventHandler("ADDON_LOAD_POST")
def addonChanged():
    event.addonChanged = True
    treeChanged()

@eventHandler("VERSION_UPDATE")
def versioningDone():
    from . base_types.update_file import runVersioning
    runVersioning()

def executionCodeChanged(self = None, context = None):
    treeChanged()
    propertyChanged()

def networkChanged(self = None, context = None):
    treeChanged()

def treeChanged(self = None, context = None):
    event.treeChanged = True
    tree_info.treeChanged()


@eventHandler("RENDER_INIT")
def renderInitialized():
    event.isRendering = True

@eventHandler("RENDER_CANCEL")
@eventHandler("RENDER_COMPLETE")
def renderEnd():
    event.isRendering = False

def isRendering():
    return event.isRendering
