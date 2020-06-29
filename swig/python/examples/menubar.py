#!/usr/bin/env python3
# vim: set et ts=4 sw=4:
#coding:utf-8
#############################################################################
#
# mga-dialogs.py  -  Show mga msg dialog and about dialog.
#
# License: GPLv3
# Author:  Angelo Naselli <anaselli@linux.it>
#############################################################################

###########
# imports #
###########
import sys
sys.path.insert(0,'../../../build/swig/python')
import os

import yui

log = yui.YUILog.instance()
log.setLogFileName("/tmp/debug.log")
log.enableDebugLogging( True )
appl = yui.YUI.application()
appl.setApplicationTitle("Show dialogs example")

#################
# class mainGui #
#################
class Info(object):
    def __init__(self,title,richtext,text):
        self.title=title
        self.richtext=richtext
        self.text=text

class mainGui():
    """
    Main class
    """

    def __init__(self):
        self.factory = yui.YUI.widgetFactory()
        self.mgafactory = yui.YMGAWidgetFactory.getYMGAWidgetFactory(yui.YExternalWidgets.externalWidgetFactory("mga"))
        self.dialog = self.factory.createPopupDialog()
        mainvbox = self.factory.createVBox(self.dialog)
        self.menubar = self.mgafactory.createMenuBar(mainvbox)

        mItem = yui.YMGAMenuItem("&File")
        mItem.this.own(False)
        tmi = yui.YMGAMenuItem(mItem, "&New")
        tmi.this.own(False)
        item = yui.YMGAMenuItem( tmi, "New &1" , "document-new")
        item.this.own(False)
        item = yui.YMGAMenuItem( tmi, "New &2" , "contact-new")
        item.this.own(False)
        item = yui.YMenuSeparator(mItem);
        item.this.own(False)
        item = yui.YMGAMenuItem(mItem, "&Open", "document-open.png")
        item.this.own(False)
        item = yui.YMenuSeparator(mItem);
        item.this.own(False)
        item = yui.YMGAMenuItem(mItem, "&Save", "document-save.png")
        item.this.own(False)
        item = yui.YMGAMenuItem(mItem, "&Save as", "document-save-as")
        item.this.own(False)
        item = yui.YMenuSeparator(mItem);
        item.this.own(False)
        self.quitMenu = yui.YMGAMenuItem(mItem, "&Quit", "application-exit")
        self.quitMenu.this.own(False)

        self.menubar.addItem(mItem)

        #mItem1 = yui.YMGAMenuItem("&Edit")
        #yui.YMGAMenuItem(mItem1, "&Undo", "edit-undo.png")
        #yui.YMGAMenuItem(mItem1, "&Redo", "edit-redo.png")
        #yui.YMenuSeparator(mItem1);
        #yui.YMGAMenuItem(mItem1, "Cu&t", "edit-cut.png")
        #yui.YMGAMenuItem(mItem1, "&Copy", "edit-copy.png")
        #yui.YMGAMenuItem(mItem1, "&Paste", "edit-paste.png")
        #mItem1.this.own(False)
        #self.menubar.addItem(mItem1)

        frame    = self.factory.createFrame(mainvbox,"Test frame")
        HBox     = self.factory.createHBox(frame)
        self.aboutbutton = self.factory.createPushButton(HBox,"&About")
        self.closebutton = self.factory.createPushButton(self.factory.createRight(HBox), "&Close")


    def aboutDialog(self):
        dlg = self.mgafactory.createAboutDialog("About dialog title example", "1.0.0", "GPLv3",
                                        "Angelo Naselli", "This beautiful test example shows how it is easy to play with libyui bindings", "")
        dlg.show();


    def handleevent(self):
        """
        Event-handler for the 'widgets' demo
        """
        while True:
            event = self.dialog.waitForEvent()
            eventType = event.eventType()
            if eventType == yui.YEvent.CancelEvent:
                break
            elif (eventType == yui.YEvent.MenuEvent) :
                pass
            elif (eventType == yui.YEvent.WidgetEvent) :
                # widget selected
                widget  = event.widget()
                if (widget == self.closebutton) :
                    break
                elif widget == self.aboutbutton:
                    self.aboutDialog()

        self.dialog.destroy()

if __name__ == "__main__":
    main_gui = mainGui()
    main_gui.handleevent()

    yui.YDialog.deleteAllDialogs()
    # next line seems to be a workaround to prevent the qt-app from crashing
    # see https://github.com/libyui/libyui-qt/issues/41
    yui.YUILoader.deleteUI()

