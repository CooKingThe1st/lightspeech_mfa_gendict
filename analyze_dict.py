from dictionary import Dictionary
from mfa_merge_dict import gen_dict, process_textfile
from vPhon import trans as g2pvn
import re


dictionary=[]

dictionary = Dictionary()
dictionary.load("usea_tudientv_hnd_words.txt")

print("Wiki have Tổng số từ:", len(dictionary.words), "\n")

mfa_vn_dict = gen_dict(process_textfile('vietnamese_mfa.dict') , 5, None)
print('mfa current dict', len(mfa_vn_dict))

eng_dict_raw = open("/usr/share/dict/words", "r")
eng_dict = re.sub("[^\w]", " ",  eng_dict_raw.read()).split()
eng_dict_raw.close()
print('en current dict', len(eng_dict))

vn_mfa_dict = set()
vn_dict = set()
en_dict_pop = set()
vn_dict_sus = set()

def classify_lang(text):
	text=text.replace(',', '')
	if text in mfa_vn_dict: return 'vn_mfa'
	if '-' in text: return 'sus'	
	for x in text:
		if not (x.isascii() and x.isalpha()): 
			# unknown word
			phonelk = g2pvn(text, 's', 0, 0, 0, 0)
			if not (phonelk[0] is None):
				return 'vn'
			else:
				return 'sus'
	phonelk = g2pvn(text, 's', 0, 0, 0, 0)
	if not (phonelk[0] is None): return 'vn'
	# can't appear those should already in mfa_vn_dict: anh, em, a, ca, ba, lang, thang,
	# but could be vietnam abbreviation
	# especially pero pero, and local word
	if text.lower() in eng_dict: return 'en'
	
	return 'sus'

def process():
	# kind of stupid, already print set len
	count_dup = 0
	count_vn_new = 0
	count_en_pop = 0
	count_vn_sus = 0

	for word in dictionary.words:
		atoms = word.text.lower().split()
		for ele in atoms:
			word_lang = classify_lang(ele)
			if (word_lang == 'vn_mfa'):
				#already have, no need to furthur gen phoneme
				if not(ele in vn_mfa_dict):
					vn_mfa_dict.add(ele)
					count_dup += 1
			elif (word_lang == 'vn'):
				# totally new word, need to put mfa gen
				if not(ele in vn_dict):
					vn_dict.add(ele)
					count_vn_new += 1
			elif (word_lang == 'en'):
				# total eng word, put to cmu_dict then translate to viet_phone
				if not(ele in en_dict_pop):
					count_en_pop += 1
					en_dict_pop.add(ele)
			elif (word_lang == 'sus'):
				# unexpected, could be other lang like RUS, GER, but could also uncommon vietnam word, or even abbreviation
				
				# 提出: if long (> 5char, treated as eng, else break into char and read sore zore)
				if not(ele in vn_dict_sus):
					count_vn_sus += 1
					vn_dict_sus.add(ele)

	print("vn already {} vn new {} en pop {} sus {}".format(count_dup, count_vn_new, count_en_pop, count_vn_sus))
	return vn_mfa_dict, vn_dict, en_dict_pop, vn_dict_sus
	
if __name__ == '__main__':
	_, B, C, D = process()
	with open('vn_new.txt', 'w') as f:
		for token in B:
			f.write(token)
			f.write('\n')
	with open('en_pop.txt', 'w') as f:
		for token in C:
			f.write(token)
			f.write('\n')
	with open('vn_sus.txt', 'w') as f:
		for token in D:
			f.write(token)
			f.write('\n')
		
