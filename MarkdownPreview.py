import webbrowser

import sublime_plugin

class MarkdownPreviewCommand (sublime_plugin.TextCommand) :

  def run (self, edit) :
    self.view.file_name() and webbrowser.open_new_tab('file://' + self.view.file_name())

  def is_visible (self) :
    return self.view.file_name() is not None and (
      self.view.file_name()[-3:] == '.md' or
      self.view.file_name()[-9:] == '.markdown' or
      self.view.file_name()[-6:] == '.mdown'
    )
