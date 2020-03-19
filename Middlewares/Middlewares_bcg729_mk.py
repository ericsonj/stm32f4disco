from pybuild.Module import ModuleHandle, GCC_CompilerOpts
from pybuild import git 

git.addSubmodule('https://github.com/ericsonj/bcg729.git', 'Middlewares/Third_Party/bcg729')

def getSrcs(mh: ModuleHandle):
    srcs = [
        'Third_Party/bcg729/src/LP2LSPConversion.c',
		'Third_Party/bcg729/src/LPSynthesisFilter.c',
		'Third_Party/bcg729/src/LSPQuantization.c',
		'Third_Party/bcg729/src/adaptativeCodebookSearch.c',
		'Third_Party/bcg729/src/codebooks.c',
		'Third_Party/bcg729/src/computeAdaptativeCodebookGain.c',
		'Third_Party/bcg729/src/computeLP.c',
		'Third_Party/bcg729/src/computeWeightedSpeech.c',
		'Third_Party/bcg729/src/decodeAdaptativeCodeVector.c',
		'Third_Party/bcg729/src/decodeFixedCodeVector.c',
		'Third_Party/bcg729/src/decodeGains.c',
		'Third_Party/bcg729/src/decodeLSP.c',
		'Third_Party/bcg729/src/decoder.c',
		'Third_Party/bcg729/src/encoder.c',
		'Third_Party/bcg729/src/findOpenLoopPitchDelay.c',
		'Third_Party/bcg729/src/fixedCodebookSearch.c',
		'Third_Party/bcg729/src/gainQuantization.c',
		'Third_Party/bcg729/src/interpolateqLSP.c',
		'Third_Party/bcg729/src/postFilter.c',
		'Third_Party/bcg729/src/postProcessing.c',
		'Third_Party/bcg729/src/preProcessing.c',
		'Third_Party/bcg729/src/qLSP2LP.c',
		'Third_Party/bcg729/src/utils.c',
		'Third_Party/bcg729/src/cng.c',
		'Third_Party/bcg729/src/vad.c',
		'Third_Party/bcg729/src/dtx.c'
    ]
    return mh.getSrcsByPath(srcs)
    

def getIncs(mh: ModuleHandle):
    return [
        'Middlewares/Third_Party/bcg729/src',
        'Middlewares/Third_Party/bcg729/include'
    ]

def getCompilerOpts(mh: ModuleHandle):
    opts = GCC_CompilerOpts(mh.getGeneralCompilerOpts())
    opts.setOptimizationOpts(['-Ofast'])
    return opts