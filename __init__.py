from aqt import mw
from aqt.utils import showInfo, askUser
from aqt.qt import *

def accept():
    reset = askUser("<div style='font-size: 16px'> Reset all cards to new?<br><font color=red>This action can't be undone.</font></div>".format(user_ease), defaultno=True, title="Reset Cards")
    if reset:
        anki_ease = 0
        mw.col.db.execute("update cards set queue = ?", anki_ease)
        showInfo("Done".format(user_ease), title="Reset Cards")
    else:
        pass


action = QAction("Reset &Cards", mw)
action.triggered.connect(accept)
mw.form.menuTools.addAction(action)
