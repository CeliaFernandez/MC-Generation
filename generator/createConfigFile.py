import os, argparse
import ROOT as r
from string import Template

"""
>> Script to create config files to generate MC models with:

-One massive particle with M1 GeV
-Othe massive particle with M2 GeV which comes from the decay of the first one and has a decay length of CT

>> Example command to run:

python createConfigFile.py --template TEMPLATE_DisplacedSUSY_squarkToQuarkChi_MSquark_M1_MChi_M2_ctau_CTmm_TuneCP2_13TeV_pythia8_80X_cff.py --M1 1500 --M2 494 --CT 160 --N 10

"""

##############################################################################################

def computeWidth(ctau):

    # Function which receives a decay length value in (mm) and returns the width of the particle

    HSLAH = 6.582119624E-25 # hslash value in GeV*s
    tau = ctau*1.0E-3/3.0E8 # lifetime in seconds
    width = HSLAH/tau # width in GeV

    return width



def writeOutputFile(template_path, mapp):

    ## Get the output file name

    input_name = template_path.split('/')[-1]
    print('>>> Input template: ' + input_name)     

    for key in mapp.keys():

        if key not in input_name: continue

        index = input_name.find(key)
        input_name = input_name[:index] + '${' + input_name[index:index + 2] + '}' + input_name[index+2:]

    output_name = Template(input_name).safe_substitute(mapp)
    output_name = output_name.replace(".0", "")

    if 'TEMPLATE' in output_name: output_name = output_name[9:] # delete the TEMPLATE name

    print('>>> Output file: ' + output_name)


    ## Root output file names
    root_name = 'EXO-' + output_name[:-7] + '.root'
    mapp['ROOT'] = root_name

    ## Get the output file text

    input_file = open(template_path, 'r')
    input_text = input_file.read()
    output_text = Template(input_text).safe_substitute(mapp)
    input_file.close()


    ## Write the output file

    output_file = open(output_name, 'w')
    output_file.write(output_text)
    output_file.close()

    print('---> SUCCESS: The config file has been created')


##############################################################################################


if __name__ == '__main__':


    ### Parser object to store the values required to create the config files

    parser = argparse.ArgumentParser( description = 'Introduce the values of some model parameters to create the generation config files')
    parser.add_argument('--template', dest='template', type=str, action='store', required=True, help='Path to the template of the config file')
    parser.add_argument('--M1', dest='M1', type=float, action='store', required=True)
    parser.add_argument('--M2', dest='M2', type=float, action='store', required=True)
    parser.add_argument('--CT', dest='CT', type=float, action='store', required=True)
    parser.add_argument('--N', dest='N', type=int, action='store', default=1000)

    args = parser.parse_args()

    ### Create the mapping to the variables

    mapping = {}

    mapping['M1'] = args.M1
    mapping['M2'] = args.M2
    mapping['CT'] = args.CT
    mapping['N'] = args.N
    mapping['WIDTH'] = computeWidth(args.CT)


    ### Open the template and prepare the text 

    writeOutputFile(args.template, mapping)

