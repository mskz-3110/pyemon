from .option import *
from .command import *
import inflection

class Task:
  __Tasks = {}

  def __init__(self, optionParser = None):
    name = inflection.underscore(self.__class__.__name__)
    if name.endswith("_task"):
      name = name[:-5]
    self.__Name = name.replace("_", ".")
    if optionParser is None:
      optionParser = OptionParser()
    self.OptionParser = optionParser

  @property
  def Name(self):
    return self.__Name

  def run(self, argv):
    None

  def to_string(self, indent = ""):
    strings = []
    strings.append("""{}{}""".format(indent, self.__Name))
    string = self.OptionParser.to_string("""{}  """.format(indent))
    if 0 < len(string):
      strings.append(string)
    return "\n".join(strings)

  @classmethod
  def set(cls, task):
    Task.__Tasks[task.Name] = task
    return task

  @classmethod
  def get(cls, name):
    if name in Task.__Tasks:
      return Task.__Tasks[name]
    else:
      return None

  @classmethod
  def tasks(cls):
    return tuple(Task.__Tasks.values())

  @classmethod
  def parse(cls, argv = None):
    if argv is None:
      argv = sys.argv[1:]
    if 0 < len(argv):
      name = argv[0]
      if name in Task.__Tasks:
        Task.__Tasks[name].run(argv[1:])
      else:
        sys.exit(Task.to_undefined_string(name))

  @classmethod
  def parse_if_main(cls, name, task):
    if name == "__main__" or name == "pyemon.cli":
      Task.parse([task.Name] + sys.argv[1:])

  @classmethod
  def to_undefined_string(self, name):
    return """{} task is undefined.""".format(Command.to_error_string(name))
