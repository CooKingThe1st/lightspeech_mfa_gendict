from mfa_merge_dict import gen_dict, process_textfile
from vPhon import trans as g2pvn
import re
from g2p_en import G2p
from cleaner import vn_cleaners

mfa_vn_dict = gen_dict(process_textfile('vietnamese_mfa_copy.dict') , 5, None)
print('mfa current dict', len(mfa_vn_dict))

eng_dict_raw = open("/usr/share/dict/words", "r")
eng_dict = re.sub("[^\w]", " ",  eng_dict_raw.read()).split()
eng_dict_raw.close()
print('en current dict', len(eng_dict))

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

en2mfa_dict = dict({('AA','a'),('AA0','a'),('AA1','a'),('AA2','a'),('AE','eː˨˨'),('AE0','eː˨˨'),('AE1','eː˨˨'),('AE2','eː˨˨'),('AH','a*˨˨'),('AH0','a*˨˨'),('AH1','a*˨˨'),('AH2','a*˨˨'),('AO','ɔ'),('AO0','ɔ'),('AO1','ɔ'),('AO2','ɔ'),('AW','aː˨˥ w'),('AW0','aː˨˥ w'),('AW1','aː˨˥ w'),('AW2','aː˨˥ w'),('AY','aː˨˨ j'),('AY0','aː˨˨ j'),('AY1','aː˨˨ j'),('AY2','aː˨˨ j'),('B','ɓ'),('CH','tɕ'),('D','ɗ'),('DH','ɣ'),('EH','ɛː˨˨'),('EH0','ɛː˨˨'),('EH1','ɛː˨˨'),('EH2','ɛː˨˨'),('ER','əː˦˥'),('ER0','əː˦˥'),('ER1','əː˦˥'),('ER2','əː˦˥'),('EY','eː˦˥'),('EY0','eː˦˥'),('EY1','eː˦˥'),('EY2','eː˦˥'),('F','f'),('G','ɡ'),('HH','h'),('IH','ɨ'),('IH0','ɨ'),('IH1','ɨ˦˥'),('IH2','ɨ˦˥'),('IY','i˨˨'),('IY0','i˨˨'),('IY1','i˨˨'),('IY2','i˨˨'),('JH','z'),('K','k'),('L','l'),('M','m'),('N','n'),('NG','ŋ'),('OW','o˦˥'),('OW0','o˦˥'),('OW1','o*˦˥'),('OW2','o*˦˥'),('OY','ɔː˨˨ j'),('OY0','ɔː˨˨ j'),('OY1','ɔː˨˨ j'),('OY2','ɔː˨˨ j'),('P','p'),('R','r'),('S','s'),('SH','s w'),('T','t'),('TH','tʰ'),('UH','uː˦˥'),('UH0','uː˦˥'),('UH1','u˦˥'),('UH2','u˦˥'),('UW','u˨˩˦'),('UW0','u˨˩˦'),('UW1','u˨˩˦'),('UW2','u˨˩˦'),('V','v'),('W','w'),('Y','j'),('Z','z'),('ZH','c')})
def en2mfa(en_phones):
	# input ['HH', 'IH1', 'V']
	# output mfa phone
	print("EN LIST", en_phones)
	tmp = [en2mfa_dict[u] for u in en_phones]
	return ' '.join(tmp)
	
def special2mfa(sus_text):
	return " ɨ˨˨ h ɨ˨˨ h "
	
def mfa_get_phone(word, tone):
	#compare vPhon and mfa actually to get the correct tone
	assert len(word.split()) == 1
#	LK = g2pvn(word.lower(), 's', 0, 0, 0, 0)
	all_choice_mfa = mfa_vn_dict.get(word)
	
	def get_lk_tone(word):
		# ngang 0, sac 1, hoi 2, huyen 3, nga 4, nang 5
		# vPhon dont diffrentiate hoi and nga
		tone_dict_ngang = set(['a', 'â', 'ă', 'e', 'ê', 'i', 'u', 'ư', 'o', 'ô', 'ơ', 'y'])
		tone_dict_sac   = set(['á', 'ấ', 'ắ', 'é', 'ế', 'í', 'ú', 'ứ', 'ó', 'ố', 'ớ', 'ý'])
		tone_dict_hoi   = set(['ả', 'ẩ', 'ẳn', 'ẻ', 'ể', 'ỉ', 'ủ', 'ử', 'ỏ', 'ổ', 'ở' ,'ỷ'])
		tone_dict_huyen = set(['à', 'ầ', 'ằ', 'è', 'ề', 'ì', 'ù', 'ừ', 'ò', 'ồ', 'ờ' ,'ỳ'])
		tone_dict_nga   = set(['ã', 'ẫ', 'ẵ', 'ẽ', 'ễ', 'ĩ', 'ũ', 'ữ', 'õ', 'ỗ', 'ỡ' ,'ỹ'])
		tone_dict_nang  = set(['ạ', 'ậ', 'ặ', 'ẹ', 'ệ', 'ị', 'ụ', 'ự', 'ọ', 'ộ', 'ợ' ,'ỵ'])
		for x in word:
			if x in tone_dict_ngang: return 0
			if x in tone_dict_sac:   return 1
			if x in tone_dict_hoi:   return 2
			if x in tone_dict_huyen: return 3
			if x in tone_dict_nga:   return 4
			if x in tone_dict_nang:  return 5
			
	def get_mfa_tone(mfaphone):
	# need testing, https://mfa-models.readthedocs.io/en/latest/dictionary/Vietnamese/Vietnamese%20%28Hanoi%29%20MFA%20dictionary%20v2_0_0a.html#vietnamese-hanoi-mfa-dictionary-v2-0-0a
		tone_dict_mfa = [('ː˧', 0),('ː˨˨',0),('˨ˀ˥',4),('˨˨',3),('˨˨ˀ',2),('˨˩ˀ',5),('˨˩˨',5),('˧˩˧',2),('˨˩˦',4), ('˨˨ ', 0),('˧˥',1),('˨˦',1),('˨˩',5), ('˨˥', 1), ('˦˨', 3),('˦˥', 1) ,('˨ˀ˦', 1), ('j', 0)]
		for g, t in tone_dict_mfa:
			if g in mfaphone:
				return t
				
		print("NANI ", mfaphone)
		assert False
	
	if (tone == 'keep'):
		org_tone = get_lk_tone(word)
		#randome in maxes
		best_dist = 1000
		current_choice = ''
		for word in all_choice_mfa:
			if abs(get_mfa_tone(word) - org_tone) < best_dist:
				best_dist = get_mfa_tone(word) - org_tone
				current_choice = word
		return current_choice
	else:
		assert False
	
def get_phone(text, forced_lang = 'vn'):
	g2p = G2p()
	vn_dict = set()
	# cleaner se thay the number, dollar
	text = vn_cleaners(text).split()
	print("text ", text)
	output_phone = ""
	for word_raw in text:
	# nho them cac break
		word = word_raw.lower()
		word_lang = classify_lang(word)
		print(word, ' ', word_lang)
		
		if (forced_lang == 'en'): 
			output_phone = output_phone + en2mfa(g2p(word))
		elif (word_lang == 'vn_mfa'):
			#already have, no need to furthur gen phoneme
			output_phone = output_phone + mfa_get_phone(word = word, tone = 'keep')
		elif (word_lang == 'vn'):
			# totally new word, 2 choice here, 
			# or  to put in mfa g2p and create new file, then read again
			# or  to map from vPhon to our MFA (not that hard)
			# current is pass a MARUMARU
			if not(ele in vn_dict):
				vn_dict.add(ele)
				count_vn_new += 1
			ourput_phone = output_phone + " ɨ˨˨ h ɨ˨˨ h  "
		elif (word_lang == 'en'):
			# total eng word, put to cmu_dict then translate to viet_phone
			output_phone = output_phone + en2mfa(g2p(word))
		elif (word_lang == 'sus'):
			# unexpected, could be other lang like RUS, GER, but could also uncommon vietnam word, or even abbreviation
			
			# 提出: if long (> 5char, treated as eng, else break into char and read sore zore)
			# current is pass a MARUMARU
			if ('-' in word): word = word.split('-') 
			output_phone = output_phone + special2mfa(word)
		output_phone = output_phone + " | "
	output_phone = output_phone.replace("ː", "*").replace("˨ˀ˥","ʮ").replace("˨ˀ˦","ʯ")
	return output_phone
	
if __name__ == '__main__':
	pass
