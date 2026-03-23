Gene = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print('the initial dictionary: ', Gene)
Gene['MYC'] = 11.6
print("add MYC gene: ", Gene)

import matplotlib.pyplot as plt
x = ['TP53', 'EGFR', 'BRCA1', 'PTEN', 'ESR1', 'MYC']
y = [12.4, 15.1, 8.2, 5.3, 10, 11.6]
plt.bar(x, y)
# add the number on the bar chart
for i, value in enumerate(Gene.values()):
    plt.text(i, value, str(value), ha='center', va='bottom')
plt.ylabel('expression level')
plt.title('Gene Expression')
#to ensure that the picture will not break the whole process, I move plt.show() to the end.

gene_of_interest = 'MYC' #This is where you can change your interested gene.
if gene_of_interest in Gene:
    print(Gene[gene_of_interest])
else:
    print('This Gene is not in the dataset.')

average_gene_expression = (sum(Gene.values()) / 6)
print('The average gene expression level across all genes is ', average_gene_expression)

plt.show()