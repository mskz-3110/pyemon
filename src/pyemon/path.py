import os

class Path:
  def __init__(self, directory = ".", file = "", ext = ""):
    self.Directory = directory
    self.File = file
    self.Ext = ext

  def exists(self):
    return os.path.exists(self.to_string())

  def makedirs(self):
    os.makedirs(self.Directory, exist_ok = True)

  def to_string(self):
    return Path.join(self.File, self.Ext, self.Directory)

  def __str__(self):
    return self.to_string()

  @classmethod
  def split(cls, path):
    directory, fileAndExt = os.path.split(path)
    file, ext = os.path.splitext(fileAndExt)
    if 0 < len(ext):
      ext = ext[1:]
    return directory, file, ext

  @classmethod
  def join(cls, file, ext, directory = ""):
    if len(ext) == 0:
      path = file
    else:
      path = """{}.{}""".format(file, ext)
    if 0 < len(directory):
      path = """{}/{}""".format(directory, path)
    return path