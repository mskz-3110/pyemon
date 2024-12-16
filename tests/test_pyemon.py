from pyemon.task import *
from pyemon.path import *
from pyemon.time import *

class PyemonTestTask(Task):
  def run(self, argv):
    assert(argv == ["テスト"])
Task.set(PyemonTestTask())

def test_pyemon():
  stopwatch = Stopwatch()

  assert(Path.join("file", "") == "file")
  assert(Path.join("file", "ext") == "file.ext")
  assert(Path.join("file", "ext", "directory") == "directory/file.ext")

  filePath = "./directory/file.ext"
  directory, file, ext = Path.split(filePath)
  assert(Path.join(file, ext, directory) == filePath)
  directory, file, ext = Path.split(filePath)
  path = Path(directory, file, ext)
  assert(path.Directory == "./directory")
  assert(path.File == "file")
  assert(path.Ext == "ext")
  assert(path.to_string() == filePath)
  assert(path.exists() == False)

  filePath = "file.ext"
  directory, file, ext = Path.split(filePath)
  assert(Path.join(file, ext, directory) == filePath)
  path = Path(directory, file, ext)
  assert(path.Directory == "")
  assert(path.File == "file")
  assert(path.Ext == "ext")
  assert(path.exists() == False)
  path.makedirs()

  Task.parse(["pyemon.test", "テスト"])
  Time.cycle_sleep(0.9, 1.0)

  stopwatch.stop()
  print("""ElapsedTime={}""".format(stopwatch))
