# Must Be Kept at /bert_score/bert_score folder

from score import score
import numpy as np
from nltk import ngrams
import argparse


pred_drive_path = '/content/gdrive/MyDrive/Test Result/prediction.bn'
source_drive_path = '/content/gdrive/MyDrive/Test Result/source.bn'

with open(pred_drive_path) as f:
    cands = [line.strip() for line in f]

with open(source_drive_path) as f:
    refs = [line.strip() for line in f]


P, R, F1 = score(cands, refs, lang='bn', verbose=True)

# sanity check
print(len(F1))


P_mean = P.mean()
R_mean = R.mean()
F1_mean= F1.mean()

print(f"System level precision: {P_mean :.3f}")
print(f"System level recall: {R_mean:.3f}")
print(f"System level F1 score: {F1_mean:.3f}")


# np.savetxt('/content/drive/MyDrive/OpenNmt/data/run/inference-data/F1_final.txt', P.numpy())
# np.savetxt('/content/drive/MyDrive/OpenNmt/data/run/inference-data/F1_final.txt', R.numpy())
# np.savetxt('/content/drive/MyDrive/OpenNmt/data/run/inference-data/F1_final.txt', F1.numpy())




# buffer_length = 5000
# BERT_THRESHOLD = 0.83
# total_F1, total_P, total_R = [], [], []


# def calculate_bertscore():

#     with open("/home/akil/Work/Work/Research/thesis/paraphrasing/Experiments/Exp-3/Test Result/prediction.bn") as f:
#         cands = [line.strip() for line in f]

#     with open("/home/akil/Work/Work/Research/thesis/paraphrasing/Experiments/Exp-3/Test Result/source.bn") as f:
#         refs = [line.strip() for line in f]

#     print(len(cands), len(refs))

#     print('Calculating Bert Score')
#     lines_processed = 0
#     loop_counter = 0

#     for index in range(0, len(cands), buffer_length):

#         lines_processed += buffer_length
#         loop_counter += 1

#         print(f'Calculating Bert Score for {lines_processed} data')

#         if(lines_processed > len(cands)):
#             lines_processed -= buffer_length
#             loop_counter -= 1
#             print('Exceeded amount, breaking loop')
#             break

#         P, R, F1 = score(refs[buffer_length * (loop_counter - 1): buffer_length * loop_counter],
#                          cands[buffer_length * (loop_counter - 1): buffer_length * loop_counter], lang='bn', verbose=False)

#         print(
#             f'Done! for {buffer_length * (loop_counter - 1)} to {(buffer_length * loop_counter) - 1}')

#         print(f'F1 length: {F1.shape}')

#         P_list = P.tolist()
#         R_list = R.tolist()
#         F1_list = F1.tolist()


#         total_P.extend(P_list)
#         total_R.extend(R_list)
#         total_F1.extend(F1_list)

#     print('sum : ', lines_processed)
#     print('loop_counter: ', loop_counter)
#     print('data left: ', len(cands) - lines_processed)

#     print(
#         f'Calculating Bert Score for remaining: {len(cands) - lines_processed}')

#     P_remaining, R_remaining, F1_remaining = score(
#         cands[lines_processed:], refs[lines_processed:], lang='bn', verbose=False)

#     remaining_F1_list = F1_remaining.tolist()
#     remaining_P_list = P_remaining.tolist()
#     remaining_R_list = R_remaining.tolist()

#     total_P.extend(remaining_P_list)
#     total_R.extend(remaining_R_list)
#     total_F1.extend(remaining_F1_list)

#     print(f"System level precision: {np.mean((total_P)) :.3f}")
#     print(f"System level recall: {np.mean((total_R)):.3f}")
#     print(f"System level F1 score: {np.mean((total_F1)):.3f}")


#     np.savetxt('/content/drive/MyDrive/OpenNmt/data/run/inference-data/F1_final.txt', P.numpy())
#     np.savetxt('/content/drive/MyDrive/OpenNmt/data/run/inference-data/F1_final.txt', R.numpy())
#     np.savetxt('/content/drive/MyDrive/OpenNmt/data/run/inference-data/F1_final.txt', F1.numpy())
#     #check_bert_threshold(remaining_F1_list, refs, cands)


# calculate_bertscore()
