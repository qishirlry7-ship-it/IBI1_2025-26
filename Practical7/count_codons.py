import re
import matplotlib.pyplot as plt

start = 'ATG'
all_stops = {'TAA', 'TAG', 'TGA'}

target_stop = input('Please choose the stop codons from TAA, TAG and TGA:')
target_stop = target_stop.strip().upper()

while target_stop not in all_stops:
    target_stop = input('Invalid input. Please enter TAA, TAG, or TGA: ')
    target_stop = target_stop.strip().upper()

input_file = './Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_chart = './codon_frequency_' + target_stop + '.png'

records = []

gene_name = ''
seq = ''

fasta = open(input_file, 'r')

for line in fasta:
    line = line.rstrip()

    if line.startswith('>'):
        if gene_name != '':
            records.append((gene_name, seq))

        gene_name = line[1:].split()[0]
        seq = ''

    else:
        seq = seq + line

if gene_name != '':
    records.append((gene_name, seq))

fasta.close()

codon_counts = {}
genes_counted = 0

bases = 'ATCG'
all_codons = []

for a in bases:
    for b in bases:
        for c in bases:
            codon = a + b + c
            all_codons.append(codon)
            codon_counts[codon] = 0

for gene_name, seq in records:

    best_orf_codons = []

    for match in re.finditer(start, seq):
        start_pos = match.start()

        for stop_pos in range(start_pos + 3, len(seq) - 2, 3):
            codon = seq[stop_pos:stop_pos+3]

            if codon in all_stops:

                if codon == target_stop:
                    candidate_codons = []

                    for k in range(start_pos, stop_pos, 3):
                        candidate_codons.append(seq[k:k+3])

                    if len(candidate_codons) > len(best_orf_codons):
                        best_orf_codons = candidate_codons

                break

    if len(best_orf_codons) > 0:
        genes_counted = genes_counted + 1

        for codon in best_orf_codons:
            codon_counts[codon] = codon_counts[codon] + 1

print()
print('Selected stop codon:', target_stop)
print('Number of genes counted:', genes_counted)
print('Codon counts upstream of', target_stop)
print()

for codon in all_codons:
    print(codon, codon_counts[codon])

labels = []
values = []

for codon in all_codons:
    if codon_counts[codon] > 0:
        labels.append(codon + ': ' + str(codon_counts[codon]))
        values.append(codon_counts[codon])

if len(values) > 0:
    plt.figure(figsize=(18, 18))

    wedges, texts = plt.pie(
        values,
        startangle=90
    )

    plt.title('Codon frequency upstream of ' + target_stop)

    plt.legend(
        wedges,
        labels,
        title='Codon counts',
        loc='center left',
        bbox_to_anchor=(1, 0.5),
        fontsize=8
    )

    plt.savefig(output_chart, dpi=300, bbox_inches='tight')
    plt.close()

    print()
    print('Pie chart saved to:', output_chart)

else:
    print()
    print('No ORFs found for stop codon:', target_stop)

