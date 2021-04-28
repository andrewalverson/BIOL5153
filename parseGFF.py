#! /usr/bin/env python3

import csv
import re
import argparse
from Bio import SeqIO
from collections import defaultdict

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)


def get_seq(s, e, str, genome):
	# extract the sequence
	fragment = genome.seq[int(s):int(e)]

	# check for "+" or "-" strand and return as-is or reverse complement
	if(str == '+'):
		return fragment
	else:
		return fragment.reverse_complement()


def get_args():
	# create an argument parser object
	parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

	# add positional arguments
	parser.add_argument("gff", help='name of the GFF file')
	parser.add_argument("fasta", help='name of the FASTA file')

	# parse the arguments
	return parser.parse_args()


def read_fasta():

	# read in and return the genome sequence
	return SeqIO.read(args.fasta, 'fasta')


def parse_gff(genome):

	# create a dictionary for genes with introns/multiple exons
	# key = gene name, value = list of exon sequences
	exons_dict = defaultdict(dict)

	# open and read in GFF file
	with open(args.gff, 'r') as gff_in:

		# create a csv reader object
		reader = csv.reader(gff_in, delimiter='\t')

		# loop over all the lines in our reader object (i.e., parsed file)
		for line in reader:
			species      = line[0].replace(" ", "_")
			feature_type = line[2]
			start        = line[3]
			end          = line[4]
			strand       = line[6]

			# split the attributes field in a list
			attr_fields = line[8].split()

			gene_name = attr_fields[1]

			if(feature_type == 'CDS'):

				# search for "exon" annotation
				match = re.search("exon\s+(\d+)", line[8])

				# test for whether there are multiple exons
				if(match):
					# create FASTA header, which will also be our key for "exons"
					header = species + "_" + gene_name
					
					# get the exon number
					exon_number = match.group(1)

					# get the sequence for this exon
					exon = get_seq(int(start)-1, int(end), strand, genome)

					if(header in exons_dict):
						exons_dict[header][exon_number] = exon
					else:
						exons_dict[header] = defaultdict(dict)
						exons_dict[header][exon_number] = exon

				# just print genes that don't have introns
				else:
					# print the FASTA header
					print(">" + species + "_" + gene_name)
					# extract and print the sequence
					print(get_seq(int(start)-1, int(end), strand, genome))

			# skip all other feature types
			else:
				continue


	# loop over exons dictionary (h = header, j = list of exons)
	for i, j in exons_dict.items():
		print('>' + i)

		for k in sorted(j):	
			print(j[k], end='')
		print()


# the 'main' function
def main():
	genome = read_fasta()
	parse_gff(genome)


# get the command-line arguments
args = get_args()

# set the environment for this script
# is this main, or is this a module being called by another script
if __name__ == '__main__':
	main()




