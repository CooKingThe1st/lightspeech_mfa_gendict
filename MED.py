from vPhon import trans as g2plowkey
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
# numpy.set_printoptions(threshold = False) 

DEBUG = 0

INF = 100000

def med_word(base_word, ref_word):
    base_phones = np.array(g2plowkey(base_word.lower(), 's', 0, 0, 0, 0), dtype=object)
    ref_phones = np.array(g2plowkey(ref_word.lower(), 's', 0, 0, 0, 0), dtype=object)
    # always 4 phones
    # assert len(base_phones) == len(ref_phones)
    total_diff = np.sum((base_phones != ref_phones))
    # print(base_word, ' ', ref_word, ' ', total_diff)
    # if (DEBUG and total_diff <= 1): print(base_word, ' ', ref_word, ' ', total_diff)
    return int(total_diff > 1)

def str2list(sent):
    if not(type(sent) == list):
        sent = sent.split()
    return sent

def med_sent(base_sent, ref_sent):
    base_sent = str2list(base_sent)
    ref_sent = str2list(ref_sent)
    n = len(base_sent) + 1
    m = len(ref_sent) + 1
    lever_dist = np.empty( (n, m) )
    lever_dist.fill(INF)
    lever_dist[0][0] = 0
    for i in range(1, n): lever_dist[i][0] = i
    for i in range(1, m): lever_dist[0][i] = i

    for col in range(1, n):
        for row in range(1, m):
            lever_dist[col][row] = min(lever_dist[col - 1][row] + 1, lever_dist[col][row - 1] + 1, lever_dist[col - 1][row - 1] + med_word( base_sent[col - 1].lower(), ref_sent[row - 1].lower() ) )

    # if (DEBUG): print(lever_dist)
    return lever_dist[n-1][m-1]

def med_para(base_para, ref_sent, allow_delete, get_id = 1):
    base_para = str2list(base_para)
    ref_sent = str2list(ref_sent)
    para_len = len(base_para) + 1
    sent_len = len(ref_sent) + 1
    lever_dist = np.empty( (para_len, sent_len) )
    lever_dist.fill(INF)
    lever_dist[0][0] = 0
    for i in range(1, sent_len): lever_dist[0][i] = i
    for i in range(1, para_len): lever_dist[i][0] = 0
    for col in range(1, para_len):
        for row in range(1, sent_len):
            # dont add ref word to base para
            if (allow_delete == 1):
                lever_dist[col][row] = min(lever_dist[col - 1][row] + 1,  lever_dist[col][row - 1] + 1, lever_dist[col - 1][row - 1] + med_word( base_para[col - 1].lower(), ref_sent[row - 1].lower() ) )
            else:
                lever_dist[col][row] = min(lever_dist[col - 1][row] + 1, lever_dist[col - 1][row - 1] + med_word( base_para[col - 1].lower(), ref_sent[row - 1].lower() ) )

    if (DEBUG): print(lever_dist)
    # return lever_dist
    if (get_id == 1):
        right_bound = np.argmin(lever_dist[:, sent_len-1])
        return base_para[right_bound - sent_len + 1: right_bound], right_bound, lever_dist[right_bound][sent_len-1]
    else:
        return min(lever_dist[:, sent_len-1])

if __name__ == '__main__':
    print(med_para(list(('ở', 'nhà', 'có', 'tôi', 'biết', 'có', 'anh', 'có', 'ai', 'hay', 'là')), list(('co', 'tôi', 'bay', 'chó')), 1, 1))
