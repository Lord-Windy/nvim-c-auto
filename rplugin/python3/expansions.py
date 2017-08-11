import neovim

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('samfor')
    def doItPython(self, args):
        self.vim.command('echo "Sams thing this time"')

