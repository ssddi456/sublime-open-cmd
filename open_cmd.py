import sublime
import sublime_plugin
import os

class OpencurcmdpathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    curfile = view.file_name()
    if curfile != None :
      filepath = os.path.dirname( view.file_name() )
      cmd = u'''start cd /d "%s"''' % filepath
      os.system( cmd.encode('cp936') )