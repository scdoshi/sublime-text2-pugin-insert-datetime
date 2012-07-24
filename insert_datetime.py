# coding=utf-8
import sublime_plugin, datetime

class insertDatetimeCommand(sublime_plugin.TextCommand):
  def run(self, edit, format):
    timestamp = datetime.datetime.now()
    if format == "ymd":
        # yyyy-mm-dd
        timestamp = timestamp.strftime("%Y-%m-%d")
    elif format == "ymdhms":
        # %X = %H:%M:%S
        timestamp = timestamp.strftime("%Y-%m-%d %X")
    elif format == "ymdhm":
        # yyyy-mm-dd_hh-mm
        timestamp = timestamp.strftime("%Y-%m-%d_%H-%M")

    #for region in the selection
    for r in self.view.sel():
      #put in the timestamp
      #(if text is selected, it'll be replaced in an intuitive fashion)
      self.view.erase(edit, r)
      self.view.insert(edit, r.begin(), timestamp)