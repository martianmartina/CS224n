# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
from tqdm import tqdm
predictions = []
for line in tqdm(open('birth_dev.tsv')):
    predictions.append('London')
total, correct = utils.evaluate_places('birth_dev.tsv', predictions)
print("Accuracy: ",100*correct/total,"% (",correct," out of ",total,")",sep='')