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


class testPostSave(sublime_plugin.EventListener):
  """test PostSave"""
  def on_post_save(self, view):
    full_path = view.file_name()
    dirname = os.path.dirname(full_path)
    basename = os.path.basename(full_path)
    basepath,extname = os.path.splitext(full_path)
    print ( 'post save ' + basename + ' ' + extname )
    
    
    