import os

class FileStatus:
  def __init__(self, path, status = "skip"):
    self.Path = path
    self.Status = status

  def exists(self):
    return os.path.isfile(self.Path)

  def skip(self):
    self.Status = "skip"

  def done(self):
    self.Status = "done"

  def print(self):
    print("""\033[40m\033[36m{}\033[0m is {}.""".format(self.Path, self.Status))
