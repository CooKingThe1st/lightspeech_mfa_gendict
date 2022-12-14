# south.py
# coding: utf-8
# Modified by Marc Brunelle 04-10-2016 (not final)

onsets = {'b':'b','t':'t','th':'tʰ','đ':'d','ch':'c',
         'kh':'x','g':'g','l':'l','m':'m','n':'n',
         'ngh':'ŋ','nh':'ɲ','ng':'ŋ','ph':'f','v':['j','v'],
         'x':'s','d':'j','h':'h','p':'p','qu':'w',
         'gi':'j','tr':'ʈ','k':'k','c':'k','gh':'g',
         'r':'r','s':'s'
          }

nuclei = {'a':'a','á':'a','à':'a','ả':'a','ã':'a','ạ':'a',
         'â':'ă','ấ':'ă','ầ':'ă','ẩ':'ă','ẫ':'ă','ậ':'ă',
         'ă':'ă','ắ':'ă','ằ':'ă','ẳ':'ă','ẵ':'ă','ặ':'ă',
         'e':'ɛ','é':'ɛ','è':'ɛ','ẻ':'ɛ','ẽ':'ɛ','ẹ':'ɛ',
         'ê':'e','ế':'e','ề':'e','ể':'e','ễ':'e','ệ':'e',
         'i':'i','í':'i','ì':'i','ỉ':'i','ĩ':'i','ị':'i',
         'o':'ɔ','ó':'ɔ','ò':'ɔ','ỏ':'ɔ','õ':'ɔ','ọ':'ɔ',
         'ô':'o','ố':'o','ồ':'o','ổ':'o','ỗ':'o','ộ':'o',
         'ơ':'ɤ','ớ':'ɤ','ờ':'ɤ','ở':'ɤ','ỡ':'ɤ','ợ':'ɤ',
         'u':'u','ú':'u','ù':'u','ủ':'u','ũ':'u','ụ':'u',
         'ư':'ɯ','ứ':'ɯ','ừ':'ɯ','ử':'ɯ','ữ':'ɯ','ự':'ɯ',
         'y':'i','ý':'i','ỳ':'i','ỷ':'i','ỹ':'i','ỵ':'i',

         'ia':'iə','ía':'iə','ìa':'iə','ỉa':'iə','ĩa':'iə','ịa':'iə',
         'ia':'iə','iá':'iə','ià':'iə','iả':'iə','iã':'iə','iạ':'iə',
         'iê':'iə','iế':'iə','iề':'iə','iể':'iə','iễ':'iə','iệ':'iə',
         'oo':'ɔ','óo':'ɔ','òo':'ɔ','ỏo':'ɔ','õo':'ɔ','ọo':'ɔ',
         'oo':'ɔ','oó':'ɔ','oò':'ɔ','oỏ':'ɔ','oõ':'ɔ','oọ':'ɔ',
         'ôô':'o','ốô':'o','ồô':'o','ổô':'o','ỗô':'o','ộô':'o',
         'ôô':'o','ôố':'o','ôồ':'o','ôổ':'o','ôỗ':'o','ôộ':'o',
         'ua':'uə','úa':'ua','ùa':'uə','ủa':'uə','ũa':'uə','ụa':'uə',
         'uô':'uə','uố':'uə','uồ':'uə','uổ':'uə','uỗ':'uə','uộ':'uə',
         'ưa':'ɯə','ứa':'ɯə','ừa':'ɯə','ửa':'ɯə','ữa':'ɯə','ựa':'ɯə',
         'ươ':'ɯə','ướ':'ɯə','ườ':'ɯə','ưở':'ɯə','ưỡ':'ɯə','ượ':'ɯə',
         'yê':'iɛ','yế':'iɛ','yề':'iɛ','yể':'iɛ','yễ':'iɛ','yệ':'iɛ',
         'uơ':'uə','uở':'uə','uờ':'uə','uở':'uə','uỡ':'uə','uợ':'uə',
          }

offglides = {'ai':'aj','ái':'aj','ài':'aj','ải':'aj','ãi':'aj','ại':'aj',
            'ay':'aj','áy':'aj','ày':'aj','ảy':'aj','ãy':'aj','ạy':'aj',
            'ao':'aw','áo':'aw','ào':'aw','ảo':'aw','ão':'aw','ạo':'aw',
            'au':'aw','áu':'aw','àu':'aw','ảu':'aw','ãu':'aw','ạu':'aw',
            'ây':'ɛj','ấy':'ɛj','ầy':'ɛj','ẩy':'ɛj','ẫy':'ɛj','ậy':'ɛj',
            'âu':'ɔw','ấu':'ɔw','ầu':'ɔw','ẩu':'ɔw','ẫu':'ɔw','ậu':'ɔw',
            'eo':'ɛw','éo':'ɛw','èo':'ɛw','ẻo':'ɛw','ẽo':'ɛw','ẹo':'ɛw',
            'êu':'ew','ếu':'ew','ều':'ew','ểu':'ew','ễu':'ew','ệu':'ew',
            'iu':'iw','íu':'iw','ìu':'iw','ỉu':'iw','ĩu':'iw','ịu':'iw',
            'oi':'ɔj','ói':'ɔj','òi':'ɔj','ỏi':'ɔj','õi':'ɔj','ọi':'ɔj',
            'ôi':'oj','ối':'oj','ồi':'oj','ổi':'oj','ỗi':'oj','ội':'oj',
            'ui':'uj','úi':'uj','ùi':'uj','ủi':'uj','ũi':'uj','ụi':'uj',
            'ơi':'ɤj','ới':'ɤj','ời':'ɤj','ởi':'ɤj','ỡi':'ɤj','ợi':'ɤj',
            'ưi':'ɯj','ứi':'ɯj','ừi':'ɯj','ửi':'ɯj','ữi':'ɯj','ựi':'ɯj',
            'ưu':'ɯw','ứu':'ɯw','ừu':'ɯw','ửu':'ɯw','ữu':'ɯw','ựu':'ɯw',

            'iêu':'iəw','iếu':'iəw','iều':'iəw','iểu':'iəw','iễu':'iəw','iệu':'iəw',
            'yêu':'iəw','yếu':'iəw','yều':'iəw','yểu':'iəw','yễu':'iəw','yệu':'iəw',
            'uôi':'uəj','uối':'uəj','uồi':'uəj','uổi':'uəj','uỗi':'uəj','uội':'uəj',
            'ươi':'ɯəj','ưới':'ɯəj','ười':'ɯəj','ưởi':'ɯəj','ưỡi':'ɯəj','ượi':'ɯəj',
            'ươu':'ɯəw','ướu':'ɯəw','ườu':'ɯəw','ưởu':'ɯəw', 'ưỡu':'ɯəw','ượu':'ɯəw'
             }

onglides = {'oa':'a','oá':'a','oà':'a','oả':'a','oã':'a','oạ':'a',
           'oă':'ă','oắ':'ă','oằ':'ă','oẳ':'ă','oẵ':'ă','oặ':'ă',
           'oe':'e','oé':'e','oè':'e','oẻ':'e','oẽ':'e','oẹ':'e',
           'oe':'e','óe':'e','òe':'e','ỏe':'e','õe':'e','ọe':'e',
           'ua':'a','uá':'a','uà':'a','uả':'a','uã':'a','uạ':'a',
           'uă':'ă','uắ':'ă','uằ':'ă','uẳ':'ă','uẵ':'ă','uặ':'ă',
           'uâ':'ɤ̆','uấ':'ɤ̆','uầ':'ɤ̆','uẩ':'ɤ̆','uẫ':'ɤ̆','uậ':'ɤ̆',
           'ue':'ɛ','ué':'ɛ','uè':'ɛ','uẻ':'ɛ','uẽ':'ɛ','uẹ':'ɛ',
           'uê':'e','uế':'e','uề':'e','uể':'e','uễ':'e','uệ':'e',
           'uơ':'ɤ','uớ':'ɤ','uờ':'ɤ','uở':'ɤ','uỡ':'ɤ','uợ':'ɤ',
           'uy':'i','uý':'i','uỳ':'i','uỷ':'i','uỹ':'i','uỵ':'i',
           'uya':'iə','uyá':'iə','uyà':'iə','uyả':'iə','uyã':'iə','uyạ':'iə',
           'uyê':'iə','uyế':'iə','uyề':'iə','uyể':'iə','uyễ':'iə','uyệ':'iə',
           'uyu':'iu','uyú':'iu','uyù':'iu','uyủ':'iu','uyũ':'iu','uyụ':'iu',
           'uyu':'iu','uýu':'iu','uỳu':'iu','uỷu':'iu','uỹu':'iu','uỵu':'iu',
           'oen':'en','oén':'en','oèn':'en','oẻn':'en','oẽn':'en','oẹn':'en',
           'oet':'et','oét':'et','oèt':'et','oẻt':'et','oẽt':'et','oẹt':'et'
            }

onoffglides = {'oe':'ej','oé':'ej','oè':'ej','oẻ':'ej','oẽ':'ej','oẹ':'ej',
              'oai':'aj','oái':'aj','oài':'aj','oải':'aj','oãi':'aj','oại':'aj',
              'oay':'ăj','oáy':'ăj','oày':'ăj','oảy':'ăj','oãy':'ăj','oạy':'ăj',
              'oao':'aw','oáo':'aw','oào':'aw','oảo':'aw','oão':'aw','oạo':'aw',
              'oeo':'ew','oéo':'ew','oèo':'ew','oẻo':'ew','oẽo':'ew','oẹo':'ew',
              'oeo':'ew','óeo':'ew','òeo':'ew','ỏeo':'ew','õeo':'ew','ọeo':'ew',
              'ueo':'ew','uéo':'ew','uèo':'ew','uẻo':'ew','uẽo':'ew','uẹo':'ew',
              'uai':'aj','uái':'aj','uài':'aj','uải':'aj','uãi':'aj','uại':'aj',
              'uay':'ăj','uáy':'ăj','uày':'ăj','uảy':'ăj','uãy':'ăj','uạy':'ăj',
              'uây':'ɤ̆j','uấy':'ɤ̆j','uầy':'ɤ̆j','uẩy':'ɤ̆j','uẫy':'ɤ̆j','uậy':'ɤ̆j'
               }

codas = {'p':'p','t':'t','c':'k','m':'m','n':'ŋ','ng':'ŋ','nh':'n','ch':'t'}

tones = {'á': 45,'à': 32,'ả': 214,'ã': 214,'ạ': 212,
        'ấ': 45,'ầ': 32,'ẩ': 214,'ẫ': 214,'ậ': 212,
        'ắ': 45,'ằ': 32,'ẳ': 214,'ẵ': 214,'ặ': 212,
        'é': 45,'è': 32,'ẻ': 214,'ẽ': 214,'ẹ': 212,
        'ế': 45,'ề': 32,'ể': 214,'ễ': 214,'ệ': 212,
        'í': 45,'ì': 32,'ỉ': 214,'ĩ': 214,'ị': 212,
        'ó': 45,'ò': 32,'ỏ': 214,'õ': 214,'ọ': 212,
        'ố': 45,'ồ': 32,'ổ': 214,'ỗ': 214,'ộ': 212,
        'ớ': 45,'ờ': 32,'ở': 214,'ỡ': 214,'ợ': 212,
        'ú': 45,'ù': 32,'ủ': 214,'ũ': 214,'ụ': 212,
        'ứ': 45,'ừ': 32,'ử': 214,'ữ': 214,'ự': 212,
        'ý': 45,'ỳ': 32,'ỷ': 214,'ỹ': 214,'ỵ': 212,
         }

tones_p = {'á': 5,'à': 2,'ả': 4,'ã': 4,'ạ': 6,
          'ấ': 5,'ầ': 2,'ẩ': 4,'ẫ': 4,'ậ': 6,
          'ắ': 5,'ằ': 2,'ẳ': 4,'ẵ': 4,'ặ': 6,
          'é': 5,'è': 2,'ẻ': 4,'ẽ': 4,'ẹ': 6,
          'ế': 5,'ề': 2,'ể': 4,'ễ': 4,'ệ': 6,
          'í': 5,'ì': 2,'ỉ': 4,'ĩ': 4,'ị': 6,
          'ó': 5,'ò': 2,'ỏ': 4,'õ': 4,'ọ': 6,
          'ố': 5,'ồ': 2,'ổ': 4,'ỗ': 4,'ộ': 6,
          'ớ': 5,'ờ': 2,'ở': 4,'ỡ': 4,'ợ': 6,
          'ú': 5,'ù': 2,'ủ': 4,'ũ': 4,'ụ': 6,
          'ứ': 5,'ừ': 2,'ử': 4,'ữ': 4,'ự': 6,
          'ý': 5,'ỳ': 2,'ỷ': 4,'ỹ': 4,'ỵ': 6,
           }

gi = {'gi':'ji','gí':'ji','gì':'ji','gì':'ji','gĩ':'ji','gị':'ji'}

qu = {'quy':'wi','qúy':'wi','qùy':'wi','qủy':'wi','qũy':'wi','qụy':'wi'}

