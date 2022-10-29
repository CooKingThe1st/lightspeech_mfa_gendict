import random
import numpy as np
import os

def process_textfile(path):
    with open(path, 'r', encoding='utf-8') as fh:
        text = []
        for line in fh:
            line = line.strip()
            line = line.split()
            line = [x for x in line if x not in ['', '_', '-']]
            if line:
                text.append(line)
    return text

def gen_dict(phone_dict, start_index = 1, end_index = None):
    temp_dict = dict()
    for word_phone in phone_dict:
        word = word_phone[0]
        phone = ' '.join(word_phone[start_index: end_index])
        if (temp_dict.get(word) is None):
            temp_dict[word] = list()
        temp_dict[word].append(phone)
    return temp_dict

def save_dictionary(dictionary, output_path):
    with open(output_path, 'w', encoding='utf8') as f:
        for k,v in sorted(dictionary.items()):
            if 'v' in k:
                print(k,v)
            for phones in v:
                f.write('{} {}\n'.format(k, phones))

def merge_dict(input_, base_, time_, default_value):
    import copy
    new_ = copy.deepcopy(base_)
    nt_ = copy.deepcopy(time_)
    skip_count = 0
    miss_count = 0
    new_count = 0

    print("BEFORE ", len(base_))
    for word in input_:   
        # check if already exist
        if not (base_.get(word) is None):

            for phones_trans in input_[word]:
                if phones_trans in base_[word]:
                    skip_count += 1
                else:
                    miss_count += 1
                    print("HAVE MISS ", word, ' ', phones_trans, ' already have ', base_[word])
                    new_[word].append(phones_trans)
                    nt_[word].append(default_value)
        else:
            new_count += 1
            new_[word] = input_[word]
            nt_[word] = [default_value for i in range(len(input_[word]))]
    print("AFTER have skip ",  skip_count, " missing ", miss_count, " new ", new_count, " with total ", len(new_))
    return new_, nt_

def write_dict(phone_dict, time_dict, dict_path):
    with open(dict_path, 'w', encoding='utf8') as f:
        for word,phone_list in sorted(phone_dict.items()):
            time_list = time_dict[word]
            assert len(time_list) == len(phone_list)
            for i in range(len(phone_list)):
                time_align = time_list[i].split()
                # f.write('{0:<8}{1:<8}{2:<8}{3:<8}{4:<8}{5:<8}\n'.format(word, time_align[0], time_align[1], time_align[2], time_align[3], phone_list[i]))
                f.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(word, time_align[0], time_align[1], time_align[2], time_align[3], phone_list[i]))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str,
                        required=True, help='input sub dict')
    parser.add_argument('--base', type=str,
                    required=True, help='base dict to merge ')
    args = parser.parse_args()
    input_dict = args.input
    base_dict = args.base

    # make copy
    from os import path
    import shutil

    base_name = path.basename(base_dict)
    copy_name = path.splitext(base_name)[0] + '_copy' + path.splitext(base_name)[-1]
    final_name = path.dirname(base_dict) + '/' + copy_name
    shutil.copyfile(base_dict, final_name)
    # check if output dir exist
    if not path.exists(input_dict):
        print("INPUT DICT NOT FOUND, EXITTING")
        exit()
    if not path.exists(base_dict):
        print("BASE DICT NOT FOUND, EXITTING")
        exit()

    # read split and begin to split
    input_dict_list = gen_dict(process_textfile(input_dict), 1, None)
    base_dict_list = gen_dict(process_textfile(base_dict) , 5, None)
    time_base_dict_list = gen_dict(process_textfile(base_dict) , 1, 5)
# ('/home/we/Documents/vietnam_dataset_text_dict.txt')
# ('/home/we/Documents/MFA/pretrained_models/dictionary/vietnamese_mfa.dict')

    # first, check if can create single txt file with wav name in output dir
    # testing
    default_value = '0.99 0.3 1.0 1.0'
    new_dict_list, time_dict_list = merge_dict(input_dict_list, base_dict_list, time_base_dict_list, default_value)
    write_dict(new_dict_list, time_dict_list , final_name)
    print(final_name, ' ', base_dict)