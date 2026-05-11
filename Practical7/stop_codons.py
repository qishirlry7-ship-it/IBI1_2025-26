import re

start = 'ATG'
stop = {'TAA', 'TAG', 'TGA'}

input_file = './Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = './stop_genes.fa'

fasta = open(input_file, 'r')
out = open(output_file, 'w')

gene_name = ''
seq = ''

for line in fasta:
    line = line.rstrip()

    if line.startswith('>'):

        if seq != '':
            found_stops = set()

            match = re.search(start, seq)

            if match:
                i = match.start()

                for j in range(i + 3, len(seq) - 2, 3):
                    codon = seq[j:j+3]

                    if codon in stop:
                        found_stops.add(codon)

            if len(found_stops) > 0:
                out.write('>' + gene_name + ';' + ','.join(sorted(found_stops)) + '\n')

                for k in range(0, len(seq), 60):
                    out.write(seq[k:k+60] + '\n')

        gene_name = line[1:].split()[0]
        seq = ''

    else:
        seq = seq + line


if seq != '':
    found_stops = set()

    match = re.search(start, seq)

    if match:
        i = match.start()

        for j in range(i + 3, len(seq) - 2, 3):
            codon = seq[j:j+3]

            if codon in stop:
                found_stops.add(codon)

    if len(found_stops) > 0:
        out.write('>' + gene_name + ';' + ','.join(sorted(found_stops)) + '\n')

        for k in range(0, len(seq), 60):
            out.write(seq[k:k+60] + '\n')

fasta.close()
out.close()