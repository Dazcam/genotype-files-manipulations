#!/usr/bin/env python
'''
This script extracts gene names from a bed file by provided coordinates. Even if a gene lays partially in the given
coordinates, it will be extracted.

interval.file:

scaffold	start	end	PBS_Agrarian
chr_1	0	200000	-0.016555885830866
chr_1	100000	300000	-0.010313301839769
chr_1	200000	400000	-0.020869524360204
chr_1	300000	500000	-0.017030975605522
chr_1	400000	600000	0.021486007322708
chr_1	500000	700000	-0.020413308202349
chr_1	600000	800000	-0.078826122311685
chr_1	700000	900000	-0.090577984830186
chr_1	800000	1000000	-0.112500336742253
chr_1	900000	1100000	-0.073761180200637
chr_1	1000000	1200000	-0.009002909143476
chr_1	1100000	1300000	0.053471631319655
chr_1	1200000	1400000	0.060618693368847
chr_1	1300000	1500000	0.032328437384539
chr_1	1400000	1600000	0.02816522346207
chr_1	1500000	1700000	0.026759960043252
chr_1	1600000	1800000	0.035754546403737
chr_1	1700000	1900000	-0.007562459090992
chr_1	1800000	2000000	-0.133867568450309
chr_1	1900000	2100000	-0.204497290230584
chr_1	2000000	2200000	0.116681125754271
chr_1	2100000	2300000	0.1557943644781
chr_1	2200000	2400000	-0.014173163504313
chr_1	2300000	2500000	-0.121627123490784
chr_1	2400000	2600000	-0.102117983376004
chr_1	2500000	2700000	0.05933628376811
chr_1	2600000	2800000	0.135565771935509
chr_1	2700000	2900000	0.138946486476081
chr_1	2800000	3000000	0.051765657271909

bed.file:

chr_1	247829	322180	ENSCAFG00000000001
chr_1	270005	275409	ENSCAFG00000030108
chr_1	363607	364548	ENSCAFG00000000002
chr_1	509125	565905	ENSCAFG00000000005
chr_1	600162	635340	ENSCAFG00000000007
chr_1	692602	722173	ENSCAFG00000024219
chr_1	722179	735934	ENSCAFG00000000008
chr_1	744461	746178	ENSCAFG00000031133
chr_1	757903	800885	ENSCAFG00000000009
chr_1	805901	806622	ENSCAFG00000032297
chr_1	886083	886640	ENSCAFG00000028976
chr_1	893016	945737	ENSCAFG00000000010
chr_1	1026337	1120990	ENSCAFG00000000011
chr_1	1135209	1374294	ENSCAFG00000000012
chr_1	1412056	1428328	ENSCAFG00000000013
chr_1	1583270	1583752	ENSCAFG00000000014
chr_1	2729331	2741331	ENSCAFG00000000015
chr_1	2859535	2952664	ENSCAFG00000000016
chr_1	2976676	3061231	ENSCAFG00000000017
chr_1	3308328	3387600	ENSCAFG00000000019
chr_1	4226210	4231399	ENSCAFG00000000020
chr_1	4303857	4311455	ENSCAFG00000000021
chr_1	4418731	4839753	ENSCAFG00000000022
chr_1	4876977	4911976	ENSCAFG00000000024
chr_1	4913526	4931752	ENSCAFG00000023363
chr_1	4931122	4932015	ENSCAFG00000029366
chr_1	4961135	4978043	ENSCAFG00000000025
chr_1	4984225	4985882	ENSCAFG00000030462
chr_1	5028105	5066827	ENSCAFG00000023159
chr_1	5070925	5106749	ENSCAFG00000000026
chr_1	5154793	5155707	ENSCAFG00000000027
chr_1	5176098	5181304	ENSCAFG00000000028
chr_1	5182244	5231417	ENSCAFG00000000029
chr_1	6114120	6225821	ENSCAFG00000000031
chr_1	6378248	6382024	ENSCAFG00000000032
chr_1	6843453	6844356	ENSCAFG00000008376
chr_1	7926236	7931932	ENSCAFG00000030634
chr_1	8082389	8083996	ENSCAFG00000000036
chr_1	8180888	8324919	ENSCAFG00000000037
chr_1	8350657	8453845	ENSCAFG00000000038
chr_1	8453902	8816575	ENSCAFG00000000039
chr_1	9202411	9341613	ENSCAFG00000000040
chr_1	9395293	9436811	ENSCAFG00000000043

output.file:

scaffold	start	end	PBS_Agrarian	genes
chr_1	0	200000	-0.016555885830866	NA
chr_1	100000	300000	-0.010313301839769	ENSCAFG00000000001,ENSCAFG00000030108
chr_1	200000	400000	-0.020869524360204	ENSCAFG00000000001,ENSCAFG00000030108,ENSCAFG00000000002
chr_1	300000	500000	-0.017030975605522	ENSCAFG00000000001,ENSCAFG00000000002
chr_1	400000	600000	0.021486007322708	ENSCAFG00000000005
chr_1	500000	700000	-0.020413308202349	ENSCAFG00000000005,ENSCAFG00000000007,ENSCAFG00000024219
chr_1	600000	800000	-0.078826122311685	ENSCAFG00000000007,ENSCAFG00000024219,ENSCAFG00000000008,ENSCAFG00000031133,ENSCAFG00000000009
chr_1	700000	900000	-0.090577984830186	ENSCAFG00000024219,ENSCAFG00000000008,ENSCAFG00000031133,ENSCAFG00000000009,ENSCAFG00000032297,ENSCAFG00000028976,ENSCAFG00000000010
chr_1	800000	1000000	-0.112500336742253	ENSCAFG00000000009,ENSCAFG00000032297,ENSCAFG00000028976,ENSCAFG00000000010
chr_1	900000	1100000	-0.073761180200637	ENSCAFG00000000010,ENSCAFG00000000011
chr_1	1000000	1200000	-0.009002909143476	ENSCAFG00000000011,ENSCAFG00000000012
chr_1	1100000	1300000	0.053471631319655	ENSCAFG00000000011,ENSCAFG00000000012
chr_1	1200000	1400000	0.060618693368847	ENSCAFG00000000012
chr_1	1300000	1500000	0.032328437384539	ENSCAFG00000000012,ENSCAFG00000000013
chr_1	1400000	1600000	0.02816522346207	ENSCAFG00000000013,ENSCAFG00000000014
chr_1	1500000	1700000	0.026759960043252	ENSCAFG00000000014
chr_1	1600000	1800000	0.035754546403737	NA
chr_1	1700000	1900000	-0.007562459090992	NA
chr_1	1800000	2000000	-0.133867568450309	NA
chr_1	1900000	2100000	-0.204497290230584	NA
chr_1	2000000	2200000	0.116681125754271	NA
chr_1	2100000	2300000	0.1557943644781	NA
chr_1	2200000	2400000	-0.014173163504313	NA
chr_1	2300000	2500000	-0.121627123490784	NA
chr_1	2400000	2600000	-0.102117983376004	NA
chr_1	2500000	2700000	0.05933628376811	NA
chr_1	2600000	2800000	0.135565771935509	ENSCAFG00000000015
chr_1	2700000	2900000	0.138946486476081	ENSCAFG00000000015,ENSCAFG00000000016
chr_1	2800000	3000000	0.051765657271909	ENSCAFG00000000016,ENSCAFG00000000017


command:

python select_genes_by_intervals.py -i interval.file -b bed.file -o output.file


contact:

Dmytro Kryvokhyzha dmytro.kryvokhyzha@evobio.eu

'''

############################# modules #############################

import calls # my custom module

############################# options #############################

parser = calls.CommandLineParser()
parser.add_argument('-i', '--interval_file', help = 'name of the file with genome intervals', type=str, required=True)
parser.add_argument('-o', '--output', help = 'name of the output file', type=str, required=True)
parser.add_argument('-b', '--bed_file', help = 'file containing list of genes with scaffolds and position information', type=str, required=True)
parser.add_argument('-v', '--overhang', help = 'overhang size', type=int, required=False)
args = parser.parse_args()

############################# program #############################

if not args.overhang:
  overhang = 0
else:
  assert isinstance(args.overhang, int), "-v (--overhang) is not an integer: %r" % args.overhang
  overhang = args.overhang
  
with open(args.bed_file) as GenesFile:
  genesWords = GenesFile.readline().rstrip().split("\t")
  InterDicts = {genesWords[0]: [genesWords[1:]]}
  prevChr = genesWords[0]
  for gline in GenesFile:
    glineWords = gline.rstrip().split("\t")
    chr = glineWords[0]
    if chr != prevChr:
      InterDicts[chr] = [glineWords[1:]]
    else:
      InterDicts[chr].append(glineWords[1:])
    prevChr = chr
GenesFile.close()

geneList = []

with open(args.interval_file) as intervalFile:
  header_words = intervalFile.readline()
  output = open(args.output, 'w')
  output.write("%s\tgenes\n" % header_words.rstrip())
  for line in intervalFile:
    intervalWords = line.split()
    intervalScaf = intervalWords[0]
    # revert coordinates if necessary
    if int(intervalWords[1]) > int(intervalWords[2]):
      intervalStart = int(intervalWords[2])-overhang
      intervalEnd = int(intervalWords[1])+overhang
    else:
      intervalStart = int(intervalWords[1])-overhang
      intervalEnd = int(intervalWords[2])+overhang
        
    try:
      chrInterDict = InterDicts[intervalScaf]
    except:
      intervalWordsP = '\t'.join(str(e) for e in intervalWords)
      output.write('%s\tNA\n' % (intervalWordsP))
      continue

    for geneCoord in chrInterDict:
      geneStart = int(geneCoord[0])
      geneEnd = int(geneCoord[1])
      geneName = geneCoord[2]
    
    

      # if a gene start or ends in the interval, or the interval is within a gene.
      if (intervalStart <= geneStart and geneStart <= intervalEnd) or \
         (intervalStart <= geneEnd and  geneEnd <= intervalEnd) or \
         (geneStart <= intervalStart and intervalEnd <= geneEnd):
        geneList.append(geneName)

    if intervalWords != []:
      intervalWordsP = '\t'.join(str(e) for e in intervalWords)
      if geneList==[]:
        geneListP = "NA"
      else:
        geneListP = ','.join(str(e) for e in geneList)
      output.write('%s\t%s\n' % (intervalWordsP, geneListP))
    geneList = []


intervalFile.close()
output.close()
print('Done!')
