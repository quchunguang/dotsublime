import sublime, sublime_plugin
from datetime import datetime

class dateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        date = datetime.now().strftime('%Y-%m-%d')
        title = '\n[' + date + '] \n' + '=' * 79 + '\n\n'
        self.view.insert(edit, self.view.sel()[0].begin(), title)
