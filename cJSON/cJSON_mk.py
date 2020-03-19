from pybuild.Module import ModuleHandle, GCC_CompilerOpts


def getSrcs(mh: ModuleHandle):
    return mh.getAllSrcsC()


def getIncs(mh: ModuleHandle):
    return mh.getAllIncsC()


def getCompilerOpts(mh: ModuleHandle):
    opts = GCC_CompilerOpts(mh.getGeneralCompilerOpts())
    opts.setControlCOpts(['-std=c89'])
    return opts
