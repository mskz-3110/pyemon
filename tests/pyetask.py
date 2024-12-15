from pyemon.task import *

class CamelizeTask(Task):
  def run(self, argv):
    for arg in argv:
      print(inflection.camelize(arg))
Task.set(CamelizeTask("<words>"))

class UnderscoreTask(Task):
  def run(self, argv):
    for arg in argv:
      print(inflection.underscore(arg))
Task.set(UnderscoreTask("<words>"))

class SingularizeTask(Task):
  def run(self, argv):
    for arg in argv:
      print(inflection.singularize(arg))
Task.set(SingularizeTask("<words>"))

class PluralizeTask(Task):
  def run(self, argv):
    for arg in argv:
      print(inflection.pluralize(arg))
Task.set(PluralizeTask("<words>"))
