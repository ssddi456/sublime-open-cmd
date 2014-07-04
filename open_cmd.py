import sublime
import sublime_plugin
import platform
import os
from subprocess import Popen, PIPE

class OpenCmdCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    ''' open cmd with cur sublime edit file path '''
    if platform.system() != 'Windows':
      return
    pkgpath = pkg_path = os.path.abspath(os.path.dirname(__file__))
    Popen(['cmd', '/k', "cd /d %s" % pkg_path])