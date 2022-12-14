#central.py
#coding: utf-8

onsets = { 'b' : 'b', 't' : 't', 'th' : 'tʰ', 'đ' : 'd', 'ch' : 'c', 
'kh' : 'x', 'g' : 'ɣ', 'l' : 'l', 'm' : 'm', 'n': 'n', 
'ngh': 'ŋ', 'nh' : 'ɲ', 'ng' : 'ŋ', 'ph' : 'f', 'v' : 'j', 
'x' : 's', 'd' : 'j', 'h' : 'h', 'p' : 'p', 'q' : 'w',
'gi' : 'j', 'tr' : 'ʈ', 'k' : 'k', 'c' : 'k', 'gh' : 'ɣ',
'r' : 'ʐ', 's' : 'ʂ', 'gi' : 'j'
}
			  
nuclei = { 'a' : 'a', 'á' : 'a', 'à' : 'a', 'ả' : 'a', 'ã' : 'a', 'ạ' : 'a', 
'â' : 'ɤ̆', 'ấ' : 'ɤ̆', 'ầ' : 'ɤ̆', 'ẩ' : 'ɤ̆', 'ẫ' : 'ɤ̆', 'ậ' : 'ɤ̆',
'ă' : 'ă', 'ắ' : 'ă', 'ằ' : 'ă', 'ẳ' : 'ă', 'ẵ' : 'ă', 'ặ' : 'ă',
'e' : 'ɛ', 'é' : 'ɛ', 'è' : 'ɛ', 'ẻ' : 'ɛ', 'ẽ' : 'ɛ', 'ẹ' : 'ɛ',
'ê' : 'e', 'ế' : 'e', 'ề' : 'e', 'ể' : 'e', 'ễ' : 'e', 'ệ' : 'e',
'i' : 'i', 'í' : 'i', 'ì' : 'i', 'ỉ' : 'i', 'ĩ' : 'i', 'ị' : 'i',
'o' : 'ɔ', 'ó' : 'ɔ', 'ò' : 'ɔ', 'ỏ' : 'ɔ', 'õ' : 'ɔ', 'ọ' : 'ɔ',
'ô' : 'o', 'ố' : 'o', 'ồ' : 'o', 'ổ' : 'o', 'ỗ' : 'o', 'ộ' : 'o',
'ơ' : 'ɤ', 'ớ' : 'ɤ', 'ờ' : 'ɤ', 'ở' : 'ɤ', 'ỡ' : 'ɤ', 'ợ' : 'ɤ',
'' : '', 'ú' : '', 'ù' : '', 'ủ' : '', 'ũ' : '', 'ụ' : '',
'ư' : 'ɯ', 'ứ' : 'ɯ', 'ừ' : 'ɯ', 'ử' : 'ɯ', 'ữ' : 'ɯ', 'ự' : 'ɯ',
'y' : 'i', 'ý' : 'i', 'ỳ' : 'i', 'ỷ' : 'i', 'ỹ' : 'i', 'ỵ' : 'i',
				
'eo' : 'eo', 'éo' : 'eo', 'èo' : 'eo', 'ẻo' : 'eo', 'ẽo': 'eo', 'ẹo' : 'eo',
'ê' : 'ɛ', 'ế' : 'ɛ', 'ề' : 'ɛ', 'ể' : 'ɛ', 'ễ': 'ɛ', 'ệ' : 'ɛ',
'ia' : 'iə', 'ía' : 'iə', 'ìa' : 'iə', 'ỉa' : 'iə', 'ĩa' : 'iə', 'ịa' : 'iə',
'ia' : 'iə', 'iá' : 'iə', 'ià' : 'iə', 'iả' : 'iə', 'iã' : 'iə', 'iạ' : 'iə',
'iê' : 'iə', 'iế' : 'iə', 'iề' : 'iə', 'iể' : 'iə', 'iễ' : 'iə', 'iệ' : 'iə',
'oo' : 'ɔ', 'óo' : 'ɔ', 'òo' : 'ɔ', 'ỏo' : 'ɔ', 'õo' : 'ɔ', 'ọo' : 'ɔ',
'oo' : 'ɔ', 'oó' : 'ɔ', 'oò' : 'ɔ', 'oỏ' : 'ɔ', 'oõ' : 'ɔ', 'oọ' : 'ɔ',
'ôô' : 'o', 'ốô' : 'o', 'ồô' : 'o', 'ổô' : 'o', 'ỗô' : 'o', 'ộô' : 'o',				                 
'ôô' : 'o', 'ôố' : 'o', 'ôồ' : 'o', 'ôổ' : 'o', 'ôỗ' : 'o', 'ôộ' : 'o',				                  
'ua' : 'uə', 'úa' : 'uə', 'ùa' : 'uə', 'ủa' : 'uə', 'ũa' : 'uə', 'ụa' : 'uə',
'uô' : 'uə', 'uố' : 'uə', 'uồ' : 'uə', 'uổ' : 'uə', 'uỗ' : 'uə', 'uộ' : 'uə',
'ưa' : 'ɯə', 'ứa' : 'ɯə', 'ừa' : 'ɯə', 'ửa' : 'ɯə', 'ữa' : 'ɯə', 'ựa' : 'ɯə',
'ươ' : 'ɯə', 'ướ' : 'ɯə', 'ườ' : 'ɯə', 'ưở' : 'ɯə', 'ưỡ' : 'ɯə', 'ượ' : 'ɯə',
'yê' : 'iɛ', 'yế' : 'iɛ', 'yề' : 'iɛ', 'yể' : 'iɛ', 'yễ' : 'iɛ', 'yệ' : 'iɛ', 
'uơ' : 'uə',  'uở' : 'uə', 'uờ': 'uə', 'uở' : 'uə', 'uỡ' : 'uə', 'uợ' : 'uə',
}
				         
offglides =  { 'ai' : 'aj', 'ái' : 'aj', 'ài' : 'aj', 'ải' : 'aj', 'ãi' : 'aj', 'ại' : 'aj',
'ay' : 'ăj', 'áy' : 'ăj', 'ày' : 'ăj', 'ảy' : 'ăj', 'ãy' : 'ăj', 'ạy' : 'ăj',
'ao' : 'aw', 'áo' : 'aw', 'ào' : 'aw', 'ảo' : 'aw', 'ão' : 'aw', 'ạo' : 'aw',
'a' : 'ăw', 'á' : 'ăw', 'à' : 'ăw', 'ả' : 'ăw', 'ã' : 'ăw', 'ạ' : 'ăw',
'ây' : 'ɤ̆j',  'ấy' : 'ɤ̆j',  'ầy' : 'ɤ̆j', 'ẩy' : 'ɤ̆j', 'ẫy' : 'ɤ̆j', 'ậy' : 'ɤ̆j', 
'â' : 'ɤ̆w', 'ấ' : 'ɤ̆w', 'ầ': 'ɤ̆w', 'ẩ' : 'ɤ̆w', 'ẫ' : 'ɤ̆w', 'ậ' : 'ɤ̆w',
'eo' : 'ew', 'éo' : 'ew', 'èo' : 'ew', 'ẻo' : 'ew', 'ẽo' : 'ew', 'ẹo' : 'ew',
'i' : 'iw', 'í' : 'iw', 'ì' : 'iw', 'ỉ' : 'iw', 'ĩ' : 'iw', 'ị' : 'iw',
'oi' : 'ɔj', 'ói' : 'ɔj', 'òi' : 'ɔj', 'ỏi' : 'ɔj', 'õi' : 'ɔj', 'ọi' : 'ɔj',
'ôi' : 'oj', 'ối' : 'oj', 'ồi' : 'oj', 'ổi' : 'oj', 'ỗi' : 'oj', 'ội' : 'oj',
'ui' : 'uj', 'úi' : 'uj', 'ùi' : 'uj', 'ủi' : 'uj', 'ũi' : 'uj', 'ụi' : 'uj', 
'uy' : 'uj', 'úy' : 'uj', 'ùy' : 'uj', 'ủy' : 'uj', 'ũy' : 'uj', 'ụy' : 'uj', 
'ơi' : 'ɤj', 'ới' : 'ɤj', 'ời' : 'ɤj', 'ởi' : 'ɤj', 'ỡi' : 'ɤj', 'ợi' : 'ɤj', 
'ưi' : 'ɯj', 'ứi' : 'ɯj', 'ừi' : 'ɯj', 'ửi' : 'ɯj', 'ữi' : 'ɯj', 'ựi' : 'ɯj', 
'ư' : 'ɯw', 'ứ' : 'ɯw', 'ừ' : 'ɯw', 'ử' : 'ɯw', 'ữ' : 'ɯw', 'ự' : 'ɯw',

'iê' : 'iəw', 'iế' : 'iəw', 'iề' : 'iəw', 'iể' : 'iəw', 'iễ' : 'iəw', 'iệ' : 'iəw',
'yê' : 'iəw', 'yế' : 'iəw', 'yề' : 'iəw', 'yể' : 'iəw', 'yễ' : 'iəw', 'yệ' : 'iəw', 
'uôi' : 'uəj', 'uối' : 'uəj', 'uồi' : 'uəj', 'uổi' : 'uəj', 'uỗi' : 'uəj', 'uội' : 'uəj', 
'ươi' : 'ɯəj', 'ưới' : 'ɯəj', 'ười' : 'ɯəj', 'ưởi' : 'ɯəj', 'ưỡi' : 'ɯəj', 'ượi' : 'ɯəj', 
'ươ' : 'ɯəw', 'ướ' : 'ɯəw', 'ườ' : 'ɯəw', 'ưở' : 'ɯəw', 'ưỡ' : 'ɯəw', 'ượ' : 'ɯəw'	 
}
				
onglides =   { 'oa' : 'a', 'oá' : 'a', 'oà' : 'a', 'oả' : 'a', 'oã' : 'a', 'oạ' : 'a', 
'óa' : 'a', 'òa' : 'a', 'ỏa' : 'a', 'õa' : 'a', 'ọa' : 'a', 
'oă' : 'ă', 'oắ' : 'ă', 'oằ' : 'ă', 'oẳ' : 'ă', 'oẵ' : 'ă', 'oặ' : 'ă', 	
'oe' : 'e', 'oé' : 'e', 'oè' : 'e', 'oẻ' : 'e', 'oẽ' : 'e', 'oẹ' : 'e', 	
'oe' : 'e', 'óe' : 'e', 'òe' : 'e', 'ỏe' : 'e', 'õe' : 'e', 'ọe' : 'e', 	
'ua' : 'a', 'uá' : 'a', 'uà' : 'a', 'uả' : 'a', 'uã' : 'a', 'uạ' : 'a', 
'uă' : 'ă', 'uắ' : 'ă', 'uằ' : 'ă', 'uẳ' : 'ă', 'uẵ' : 'ă', 'uặ' : 'ă', 	
'uâ' : 'ɤ̆', 'uấ' : 'ɤ̆', 'uầ' : 'ɤ̆', 'uẩ' : 'ɤ̆', 'uẫ' : 'ɤ̆', 'uậ' : 'ɤ̆', 
'ue' : 'ɛ', 'ué' : 'ɛ', 'uè' : 'ɛ', 'uẻ' : 'ɛ', 'uẽ' : 'ɛ', 'uẹ' : 'ɛ', 
'uê' : 'e', 'uế' : 'e', 'uề' : 'e', 'uể' : 'e', 'uễ' : 'e', 'uệ' : 'e', 
'uơ' : 'ɤ', 'uớ' : 'ɤ', 'uờ' : 'ɤ', 'uở' : 'ɤ', 'uỡ' : 'ɤ', 'uợ' : 'ɤ', 
'uy' : 'i', 'uý' : 'i', 'uỳ' : 'i', 'uỷ' : 'i', 'uỹ' : 'i', 'uỵ' : 'i',
'uya' : 'iə', 'uyá' : 'iə', 'uyà' : 'iə', 'uyả' : 'iə', 'uyã' : 'iə', 'uyạ' : 'iə', 
'uyê' : 'iə', 'uyế' : 'iə', 'uyề' : 'iə', 'uyể' : 'iə', 'uyễ' : 'iə', 'uyệ' : 'iə', 
'uy' : 'i', 'uyú' : 'i', 'uyù' : 'i', 'uyủ' : 'i', 'uyũ' : 'i', 'uyụ' : 'i', 
'uy' : 'i', 'uý' : 'i', 'uỳ' : 'i', 'uỷ' : 'i', 'uỹ' : 'i', 'uỵ' : 'i',
'oen' : 'en', 'oén' : 'en', 'oèn' : 'en', 'oẻn' : 'en', 'oẽn' : 'en', 'oẹn' : 'en', 	
'oet' : 'et', 'oét' : 'et', 'oèt' : 'et', 'oẻt' : 'et', 'oẽt' : 'et', 'oẹt' : 'et' 	
}

onoffglides = { 'oe' : 'ej', 'oé' : 'ej', 'oè' : 'ej', 'oẻ' : 'ej', 'oẽ' : 'ej', 'oẹ' : 'ej', 
'oai' : 'aj', 'oái' : 'aj', 'oài' : 'aj', 'oải' : 'aj', 'oãi' : 'aj', 'oại' : 'aj',
'oay' : 'ăj', 'oáy' : 'ăj', 'oày' : 'ăj', 'oảy' : 'ăj', 'oãy' : 'ăj', 'oạy' : 'ăj',
'oao' : 'aw', 'oáo' : 'aw', 'oào' : 'aw', 'oảo' : 'aw', 'oão' : 'aw', 'oạo' : 'aw',
'oeo' : 'ew', 'oéo' : 'ew', 'oèo' : 'ew', 'oẻo' : 'ew', 'oẽo' : 'ew', 'oẹo' : 'ew',
'oeo' : 'ew', 'óeo' : 'ew', 'òeo' : 'ew', 'ỏeo' : 'ew', 'õeo' : 'ew', 'ọeo' : 'ew',
'ueo' : 'ew', 'uéo' : 'ew', 'uèo' : 'ew', 'uẻo' : 'ew', 'uẽo' : 'ew', 'uẹo' : 'ew',
'uai' : 'aj', 'uái' : 'aj', 'uài' : 'aj', 'uải' : 'aj', 'uãi' : 'aj', 'uại' : 'aj',
'uay' : 'ăj', 'uáy' : 'ăj', 'uày' : 'ăj', 'uảy' : 'ăj', 'uãy' : 'ăj', 'uạy' : 'ăj',
'uây' : 'ɤ̆j', 'uấy' : 'ɤ̆j', 'uầy' : 'ɤ̆j', 'uẩy' : 'ɤ̆j', 'uẫy' : 'ɤ̆j', 'uậy' : 'ɤ̆j'
}

codas = { 'p' : 'p', 't' : 'k', 'c' : 'k', 'm' : 'm', 'n' : 'ŋ', 'ng' : 'ŋ', 'nh' : 'n', 'ch' : 'k' }

# See Alves 2007 (SEALS XII), Vũ 1982
tones = { 'á' : 13, 'à' : 42, 'ả' : 312, 'ã' : 312, 'ạ' : '21g', 
          'ấ' : 13, 'ầ' : 42, 'ẩ' : 312, 'ẫ' : 312, 'ậ' : '21g',
          'ắ' : 13, 'ằ' : 42, 'ẳ' : 312, 'ẵ' : 312, 'ặ' : '21g',
          'é' : 13, 'è' : 42, 'ẻ' : 312, 'ẽ' : 312, 'ẹ' : '21g',
          'ế' : 13, 'ề' : 42, 'ể' : 312, 'ễ' : 312, 'ệ' : '21g',
          'í' : 13, 'ì' : 42, 'ỉ' : 312, 'ĩ' : 312, 'ị' : '21g',
          'ó' : 13, 'ò' : 42, 'ỏ' : 312, 'õ' : 312, 'ọ' : '21g',
          'ố' : 13, 'ồ' : 42, 'ổ' : 312, 'ỗ' : 312, 'ộ' : '21g',
          'ớ' : 13, 'ờ' : 42, 'ở' : 312, 'ỡ' : 312, 'ợ' : '21g',
          'ú' : 13, 'ù' : 42, 'ủ' : 312, 'ũ' : 312, 'ụ' : '21g',
          'ứ' : 13, 'ừ' : 42, 'ử' : 312, 'ữ' : 312, 'ự' : '21g',
          'ý' : 13, 'ỳ' : 42, 'ỷ' : 312, 'ỹ' : 312, 'ỵ' : '21g',
          }

# used to use \u02C0 for raised glottal instead of g

tones_p = { 'á' : 5, 'à' : 2, 'ả' : 4, 'ã' : 4, 'ạ' : 6,
'ấ' : 5, 'ầ' : 2, 'ẩ' : 4, 'ẫ' : 4, 'ậ' : 6,
'ắ' : 5, 'ằ' : 2, 'ẳ' : 4, 'ẵ' : 4, 'ặ' : 6,
'é' : 5, 'è' : 2, 'ẻ' : 4, 'ẽ' : 4, 'ẹ' : 6,
'ế' : 5, 'ề' : 2, 'ể' : 4, 'ễ' : 4, 'ệ' : 6,
'í' : 5, 'ì' : 2, 'ỉ' : 4, 'ĩ' : 4, 'ị' : 6,
'ó' : 5, 'ò' : 2, 'ỏ' : 4, 'õ' : 4, 'ọ' : 6,
'ố' : 5, 'ồ' : 2, 'ổ' : 4, 'ỗ' : 4, 'ộ' : 6,
'ớ' : 5, 'ờ' : 2, 'ở' : 4, 'ỡ' : 4, 'ợ' : 6, 
'ú' : 5, 'ù' : 2, 'ủ' : 4, 'ũ' : 4, 'ụ' : 6,
'ứ' : 5, 'ừ' : 2, 'ử' : 4, 'ữ' : 4, 'ự' : 6, 
'ý' : 5, 'ỳ' : 2, 'ỷ' : 4, 'ỹ' : 4, 'ỵ' : 6,
}

gi = { 'gi' : 'ji', 'gí': 'ji', 'gì' : 'ji', 'gì' : 'ji', 'gĩ' : 'ji', 'gị' : 'ji' }

qu = {'quy' : 'wi', 'qúy' : 'wi', 'qùy' : 'wi', 'qủy' : 'wi', 'qũy' : 'wi', 'qụy' : 'wi'}
