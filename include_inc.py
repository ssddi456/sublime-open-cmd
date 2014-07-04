import sublime, sublime_plugin, os

class IncludeScriptCommand(sublime_plugin.TextCommand):
  

  def writeInc (self, resolvers, edit) :
    tmpl = '''<%%include file="%s"%%>'''
    def write ( idx ):
      if idx == -1 :
        return
      curpoint = self.view.sel()[0].begin()
      self.view.insert(edit, curpoint, tmpl % resolvers[idx] )
    return write

  def getLocalIncs ( self ) :
    return [['1231','456']]
  def getGlobleIncs ( self ) :
    return [['1232','456']]
  def getGlobleScripts ( self ) :
    return [['1233','456']]
  def run(self, edit):
    resolvers = []
    resolvers += self.getLocalIncs()
    resolvers += self.getGlobleIncs()
    resolvers += self.getGlobleScripts()

    self.view.window().show_quick_panel( resolvers,
                                         self.writeInc(resolvers, edit))


class RunFisScriptCommand(sublime_plugin.WindowCommand):
  """docstring for RunFisScriptCommand"""
  def run( self ):
    folder = self.window.folders()
    fis_conf = os.path.join( folder[0], 'fis-conf.js')
    os.system('''start "" /d "%s" fis release -wd local''' % folder[0])
    os.system('''start "" /d "%s" livereload -i .jade -i .less''' % folder[0])

  def is_enabled ( self ):
    folder = self.window.folders()
    fis_conf = os.path.join( folder[0], 'fis-conf.js')
    if os.path.exists( fis_conf ):
      return True
    return False
  