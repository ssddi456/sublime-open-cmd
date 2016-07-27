import sublime
import sublime_plugin
import os
import sys

python_version = sys.version_info[0]


class OpencurcmdpathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    curfile = view.file_name()
    if curfile != None :
      filepath = os.path.dirname( view.file_name() )
      cmd = u'''start cd /d "%s"''' % filepath
      if python_version == 3:
      	os.system( cmd )
      else :
      	os.system( cmd.encode('cp936') )