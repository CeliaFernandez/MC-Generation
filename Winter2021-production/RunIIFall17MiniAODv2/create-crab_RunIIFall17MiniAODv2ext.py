import os, sys, optparse

parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
parser.add_option('-s', '--nSplit', action='store', type=int, dest='nSplit', default=10, help='Events per job')
parser.add_option('-d', '--dataset', action='store', type=str, dest='dataset', default='none', help='Events per job')
parser.add_option('-H', '--hMass', action='store', type=int, dest='hMass', help='Higgs mass (in GeV)')
parser.add_option('-X', '--xMass', action='store', type=int, dest='xMass', help='LL X mass (in GeV)')
parser.add_option('-T', '--ctau', action='store', type=int, dest='ctau', help='X lifetime (in mm)')
(opts, args) = parser.parse_args()


template = '''
import CRABClient
from CRABClient.UserUtilities import config

config = config()

# All output/log files go in directory workArea/requestName/
#config.General.workArea = 'crab_projects'

config.General.requestName = 'crab_NLO_HToSSTo4l_MHMASSHIGGS_MSMASSX_ctauSCTAU_13TeV-miniaod'

config.General.transferOutputs = True
config.General.transferLogs = True
config.General.instance = 'prod'

# Set pluginName = Analysis if you are reading a dataset, or to PrivateMC if not (so you are generating events)
config.JobType.pluginName = 'Analysis'
# CMSSW cfg file you wish to run
config.JobType.psetName = 'EXO-RunIIFall17MiniAODv2ext_cfg.py'
# Increase virtual memory limit (sum needed by all threads) from default of 2000 MB.
config.JobType.maxMemoryMB = 2500
# Number of threads to use.
#config.JobType.numCores = 2
# To allow use of SL7 CMSSW versions that were SL6 at time of original DATA/MC production.
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = 'INPUTDATASET'
config.Data.inputDBS = 'phys03'


# Units of "totalUnits" and "unitsPerJob" (e.g. files, events, lumi sections)
config.Data.splitting = 'FileBased'
# Total number of these units to be processed.
#config.Data.totalUnits = NTOTAL
# Requested number in each subjob.
config.Data.unitsPerJob = NSPLITTING
config.Data.outLFNDirBase = '/store/user/fernance/'
config.Data.publication = True

config.Data.outputDatasetTag = 'RunIIFall17MiniAODv2ext'

config.Site.storageSite = 'T2_ES_IFCA'
'''    

def makeFile(higgsmass, xmass, ctau, inputdataset, nsplitting):


    text = template
    text = text.replace('MASSX', xmass)
    text = text.replace('CTAU', ctau)
    text = text.replace('MASSHIGGS', higgsmass)
    text = text.replace('INPUTDATASET', inputdataset)
    text = text.replace('NSPLITTING', nsplitting)


    name = 'crab_NLO_HToSSTo4l_MH{0}_MS{1}_ctauS{2}_13TeV-miniaod.py'.format(higgsmass, xmass, ctau)
    f = open(name, 'w')
    f.write(text + '\n')
    f.close()
 


makeFile(str(opts.hMass), str(opts.xMass), str(opts.ctau), opts.dataset, str(opts.nSplit))



