from cx_Freeze import setup, Executable

setup(name = "ScriptToBeExecutable" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("/home/tzablock/IdeaProjects/PythonLearn/src/spark/python/cxFreezCreatingPythonExecutable/ScriptToBeExecutable.py")])