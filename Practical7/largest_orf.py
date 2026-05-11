seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG' 
start_codon = 'AUG'
stop_codon = {'UAA', 'UAG', 'UGA'}

longest_orf = ''

for i in range(len(seq)-2):
    if seq[i:i+3] == start_codon:
        for j in range(i+3, len(seq)-2, 3):
            codon = seq[j:j+3]
            if codon in stop_codon:
                ORF = seq[i:j+3]
                if len(ORF) > len(longest_orf):
                    longest_orf = ORF

                break

print('Length is', len(longest_orf))

