import sublime, sublime_plugin, os

class RunFisScriptCommand(sublime_plugin.WindowCommand):
  """docstring for RunFisScriptCommand"""
  def run( self ):
    folder = self.window.folders()
    fis_conf = os.path.join( folder[0], 'fis-conf.js')
    os.system('''start "" /d "%s" fis release -wd local --verbose''' % folder[0])
    os.system('''start "" /d "%s" livereload -i .jade -i .less''' % folder[0])

  def is_enabled ( self ):
    folder = self.window.folders()
    fis_conf = os.path.join( folder[0], 'fis-conf.js')
    if os.path.exists( fis_conf ):
      return True
    return False
  