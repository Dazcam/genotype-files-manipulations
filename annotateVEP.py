#! /usr/bin/env python

"""
Adds information on SNPs from a tab file to a tab file with
[VEP](http://www.ensembl.org/info/docs/tools/vep/) information.

# VEP.input:

## ENSEMBL VARIANT EFFECT PREDICTOR v99.0
#Uploaded_variation	Location	Allele	Gene	Feature	Feature_type	Consequence	cDNA_position	CDS_position	Protein_position	Amino_acids	Codons	Existing_variation	IMPACT	DISTANCE	STRAND	FLAGS	VARIANT_CLASS	SYMBOL	SYMBOL_SOURCE	HGNC_ID	NEAREST
1_14670_C/T	1:14670	T	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001
1_14686_C/T/A	1:14686	T	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001
1_14686_C/T/A	1:14686	A	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001
1_19796_C/T	1:19796	T	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001
1_762142_C/T/*	1:762142	T	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	upstream_gene_variant	-	-	-	-	-	-	MODIFIER	2210	1	-	sequence_alteration	SLC66A2	VGNC	-	ENSCAFG00000000009
1_762142_C/T/*	1:762142	T	ENSCAFG00000000010	ENSCAFT00000080007	Transcript	3_prime_UTR_variant	3828	-	-	-	-	-	MODIFIER	-	-1	-	sequence_alteration	CTDP1	VGNC	-	ENSCAFG00000000009
1_763214_T/C	1:763214	C	ENSCAFG00000000009	ENSCAFT00000000011	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009
1_763214_T/C	1:763214	C	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	upstream_gene_variant	-	-	-	-	-	-	MODIFIER	1138	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009
1_763214_T/C	1:763214	C	ENSCAFG00000000010	ENSCAFT00000080007	Transcript	missense_variant	2756	2756	919	Q/R	cAa/cGa	-	MODERATE	-	-1	-	SNV	CTDP1	VGNC	-	ENSCAFG00000000009
1_763842_C/T	1:763842	T	ENSCAFG00000000009	ENSCAFT00000000011	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009
1_763842_C/T	1:763842	T	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	upstream_gene_variant	-	-	-	-	-	-	MODIFIER	510	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009
1_763842_C/T	1:763842	T	ENSCAFG00000000010	ENSCAFT00000080007	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	-1	-	SNV	CTDP1	VGNC	-	ENSCAFG00000000009
1_765121_A/G	1:765121	G	ENSCAFG00000000009	ENSCAFT00000000011	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009
1_765121_A/G	1:765121	G	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009

# annotation.tab:

#CHROM	POS	INFO
1	14670	0.600
1	14686	0.529
1	19796	0.641
1	762142	0.112
1	763214	0.243
1	763842	0.423
1	765121	0.196

# output:

#Uploaded_variation	Location	Allele	Gene	Feature	Feature_type	Consequence	cDNA_position	CDS_position	Protein_position	Amino_acids	Codons	Existing_variation	IMPACT	DISTANCE	STRAND	FLAGS	VARIANT_CLASS	SYMBOL	SYMBOL_SOURCE	HGNC_ID	NEAREST	INFO
1_14670_C/T	1:14670	T	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001	0.600
1_14686_C/T/A	1:14686	T	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001	0.529
1_14686_C/T/A	1:14686	A	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001	0.529
1_19796_C/T	1:19796	T	-	-	-	intergenic_variant	-	-	-	-	-	-	MODIFIER	-	-	-	SNV	-	-	-	ENSCAFG00000000001	0.641
1_762142_C/T/*	1:762142	T	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	upstream_gene_variant	-	-	-	-	-	-	MODIFIER	2210	1	-	sequence_alteration	SLC66A2	VGNC	-	ENSCAFG00000000009	0.112
1_762142_C/T/*	1:762142	T	ENSCAFG00000000010	ENSCAFT00000080007	Transcript	3_prime_UTR_variant	3828	-	-	-	-	-	MODIFIER	-	-1	-	sequence_alteration	CTDP1	VGNC	-	ENSCAFG00000000009	0.112
1_763214_T/C	1:763214	C	ENSCAFG00000000009	ENSCAFT00000000011	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009	0.243
1_763214_T/C	1:763214	C	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	upstream_gene_variant	-	-	-	-	-	-	MODIFIER	1138	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009	0.243
1_763214_T/C	1:763214	C	ENSCAFG00000000010	ENSCAFT00000080007	Transcript	missense_variant	2756	2756	919	Q/R	cAa/cGa	-	MODERATE	-	-1	-	SNV	CTDP1	VGNC	-	ENSCAFG00000000009	0.243
1_763842_C/T	1:763842	T	ENSCAFG00000000009	ENSCAFT00000000011	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009	0.423
1_763842_C/T	1:763842	T	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	upstream_gene_variant	-	-	-	-	-	-	MODIFIER	510	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009	0.423
1_763842_C/T	1:763842	T	ENSCAFG00000000010	ENSCAFT00000080007	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	-1	-	SNV	CTDP1	VGNC	-	ENSCAFG00000000009	0.423
1_765121_A/G	1:765121	G	ENSCAFG00000000009	ENSCAFT00000000011	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009	0.196
1_765121_A/G	1:765121	G	ENSCAFG00000000009	ENSCAFT00000078338	Transcript	intron_variant	-	-	-	-	-	-	MODIFIER	-	1	-	SNV	SLC66A2	VGNC	-	ENSCAFG00000000009	0.196

# command:

$ python annotateVEP.py -i VEP.input -a annotation.tab -o output

# contact:

Dmytro Kryvokhyzha dmytro.kryvokhyzha@evobio.eu

"""

############################# modules #############################

import argparse, sys  # for input options

############################# options #############################

class CommandLineParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = CommandLineParser()
parser.add_argument('-i', '--input', help = 'name of the VEP file', type=str, required=True)
parser.add_argument('-a', '--annotation', help = 'name of the file with SNPs annotation info', type=str, required=True)
parser.add_argument('-o', '--output', help = 'name of the output file', type=str, required=True)
args = parser.parse_args()

############################# functions #############################

def list2print(Lits):
  LitsP = '\t'.join(str(e) for e in Lits)
  return LitsP

############################# program #############################

with open(args.annotation) as annotFile: 
  annotHeader = annotFile.readline().rstrip().split('\t')[2:]
  annotDic = {}
  for line in annotFile:
    annotWords = line.rstrip().split('\t')
    annotCoord = str(annotWords[0]) + ":" + str(annotWords[1])
    annot = annotWords[2:]
    annotDic[annotCoord] = annot
annotFile.close()
counter = 0

output = open(args.output, 'w')

with open(args.input) as VEP:
    VEPheader = VEP.readline()
    while VEPheader.startswith("##"):
      VEPheader = VEP.readline().rstrip()
    annotHeaderP = list2print(annotHeader)
    output.write("%s\t%s\n" % (VEPheader, annotHeaderP))

    for line in VEP:
      words = line.rstrip().split('\t')
      VEPcoord = words[1]     
      try:
          lineAnnot = annotDic[VEPcoord][:]
      except:
          lineAnnot = ['-']*len(annot)
      lineAnnotP = list2print(lineAnnot)
      output.write("%s\t%s\n" % (line.rstrip(), lineAnnotP))

VEP.close()
output.close()
print('Done!')
