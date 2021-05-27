# Instructions

First install the CMSSW_10_2_22 release, used to generate this model <strong>with a slc6 architecture</strong>:

```
export SCRAM_ARCH=slc6_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_22/src ] ; then
  echo release CMSSW_10_2_22 already exists
else
  scram p CMSSW CMSSW_10_2_22
fi
cd CMSSW_10_2_22/src
eval `scram runtime -sh`
```

Then we just have to generate the fragment of the mass point we just want to produce e.g. 50000 events with mH = 125 GeV, mX = 30 GeV and ctau = 10 mm:

```
python generator_TuneCP5.py -n 50000 -H 125 -X 30 -T 10
```

This command will produce the corresponding fragment in the ```Configuration/GenProduction/python/``` directory. The example fragment is then:

```
Configuration/GenProduction/python/NLO_HToSSTo4l_MH_125_MS30_ctauS10_13TeV.py
```


The configuration file is created by running the following ```cmsDriver.py``` command:

```
SEED=$(($(date +%s) % 100 + 1))
cmsDriver.py Configuration/GenProduction/python/NLO_HToSSTo4l_MH_125_MS30_ctauS10_13TeV.py --python_filename EXO-RunIIFall18wmGS-125_30_10_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:EXO-RunIIFall18wmLHEGS.root --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc -n 10
```

## Crab launching

```
voms-proxy-init --voms cms
```

and run the command:

```
python create-crab_2018gen.py -n 50000 -s 50 -c EXO-RunIISummer15wmGS-125_30_10_cfg.py -H 125 -X 30 -T 10
```


