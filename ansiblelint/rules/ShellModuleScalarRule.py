from ansiblelint import AnsibleLintRule

class ShellModuleScalarRule(AnsibleLintRule):
  id = '700'
  shortdesc = 'Use scalar(">") for shell commands with multiple args'
  description = 'Requires scalar if shell command consist of args greater than three'
  tags = ['productivity']

  # pylint: disable=R0201
  def match(self, file, line):
    commands = line.strip().split()
    return (len(commands) > 0) and (commands[0] == "shell:" and len(commands) > 4)
