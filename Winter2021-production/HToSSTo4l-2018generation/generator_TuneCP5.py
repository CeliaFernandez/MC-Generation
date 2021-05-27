import os, sys, optparse

parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
parser.add_option('-n', '--nEvents', action='store', type=int, dest='nEvents', default=10, help='Events per model')
parser.add_option('-H', '--hMass', action='store', type=int, dest='hMass', help='Higgs mass (in GeV)')
parser.add_option('-X', '--xMass', action='store', type=int, dest='xMass', help='LL X mass (in GeV)')
parser.add_option('-T', '--ctau', action='store', type=int, dest='ctau', help='X lifetime (in mm)')
(opts, args) = parser.parse_args()


gridpack_dict = {}
gridpack_dict['110']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M110/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M110_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['125']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M125/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M125_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['150']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M150/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M150_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['200']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M200/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M200_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['300']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M300/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M300_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['400']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M400/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M400_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['450']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M450/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M450_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['500']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M500/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M500_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['600']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M600/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M600_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['750']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M750/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M750_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['800']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M800/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M800_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['900']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M900/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M900_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'
gridpack_dict['1000']  = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M1000/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M1000_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'


preamble = '''
import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('GRIDPACKFILE'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
'''


template = '''
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            'POWHEG:nFinal = 1',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
            '9000006:all = sk   skbar    0        0          0       MASSX  WIDTH  MMIN  MMAX CTAU',
            '9000006:oneChannel = 1  0.5 101  11 -11',
            '9000006:addChannel = 1  0.5 101  13 -13',
            '9000006:mayDecay = on',
            '9000006:isResonance = on',
            '25:m0 = MASSHIGGS',
            '25:onMode = off',
            '25:addChannel = 1 0.000000001 101 9000006 -9000006',
            '25:onIfMatch = 9000006 -9000006',
            '9000006:onMode = off',
            '9000006:onIfAny = 11 13',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)'''





def makeFile(higgsmass, xmass, ctau):

    width = str(300.0/float(ctau) * 6.57733e-16)

    if float(xmass) < 60:
        minmass = str(1)
        maxmass = str(75)
    elif float(xmass) < 150:
        minmass = str(1)
        maxmass = str(75)
    else:
        minmass = str(0.5 * float(xmass))
        maxmass = str(1.5 * float(xmass))

    gridpack = gridpack_dict[str(higgsmass)]

    text = preamble + template
    text = text.replace('GRIDPACKFILE', gridpack)
    text = text.replace('MASSX', xmass)
    text = text.replace('WIDTH', width)
    text = text.replace('MMIN', minmass)
    text = text.replace('MMAX', maxmass)
    text = text.replace('CTAU', ctau)
    text = text.replace('MASSHIGGS', higgsmass)


    name = 'NLO_HToSSTo4l_MH_{0}_MS{1}_ctauS{2}_13TeV.py'.format(higgsmass, xmass, ctau)
    f = open('Configuration/GenProduction/python/' + name, 'w')
    f.write(text + '\n')
    f.close()
 

if not os.path.exists('Configuration/GenProduction/python'):
    os.makedirs('Configuration/GenProduction/python')

makeFile(str(opts.hMass), str(opts.xMass), str(opts.ctau))


### Option to run multiple models:
"""
#Available gridpacks
higgsmass_ = [110, 125, 150, 200, 300, 400, 450, 500, 600, 750, 800, 900, 1000]


#In the AN
#higgsmass = [125, 200, 400, 1000]
xmass_ = [10, 20, 30, 50, 150, 350]


#ctaus that I propose in mm:
ctaus_ = [1, 10, 100, 1000, 10000, 100000, 1000000] 

#With these conditions


numberofmodels = 0
for h in higgsmass_:
    for x in xmass_:
        for ct in ctaus_:
            if h < 2.0 * x:
                continue  
            makeFile(str(h), str(x), str(ct))
            numberofmodels = numberofmodels + 1


print 'Produced a total of ', numberofmodels, 'models, with a total of', numberofmodels*eventspermodel, 'events'
"""


