from ...option import *
from ...command import *
from ...task import *

class PackageUploadTask(Task):
  def __init__(self):
    super().__init__(OptionParser([Option("p", "pypi", None, "PYPI")]))
  def run(self, argv):
    self.OptionParser.parse(argv)
    repository = self.OptionParser.find_option_from_long_name("pypi").value_by_bool("pypi", "testpypi")
    Command(["python", "-m", "twine", "upload", "--repository", repository, "dist/*"]).run()
Task.parse_if_main(__name__, Task.set(PackageUploadTask()))
