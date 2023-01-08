# Ghalatawi غلطاوي
Ghalatawi: Arabic Autocorrect library
مكتبة للتصحيح التلقائي للغة العربية


![ghalatawi logo](doc/ghalatawi_header.png  "ghalatawi logo")

![PyPI - Downloads](https://img.shields.io/pypi/dm/ghalatawi)


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com


Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/ghalatawi/main/AUTHORS.md)
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/ghalatawi/main/LICENSE)
Tracker  |[linuxscout/ghalatawi/Issues](https://github.com/linuxscout/ghalatawi/issues)
Source  |[Github](http://github.com/linuxscout/ghalatawi)
Website  |[https://pypi.python.org/pypi/ghalatawi](https://pypi.python.org/pypi/ghala)
Doc  |[package Documentaion](https://ghalatawi.readthedocs.io/)
Download  |[pypi.python.org](https://pypi.python.org/pypi/ghalatawi)
Download  | َAutocorrect Wordslist for [OpenOffice.org](http://sourceforge.net/projects/ghalatawi/files/acor_ar.dat/download)
Feedbacks  |[Comments](https://github.com/linuxscout/ghalatawi/)
Accounts  |[@Twitter](https://twitter.com/linuxscout))

## Description

ghalatawi: Arabic Autocorrect library

 التصحيح الإملائي من أهم الأدوات المستعملة في النشر والكتابة الإلكترونية، وتستعمل في البحث والاستعلامات، كما يعد من أهم الأدوات المرافقة للبرامج المكتبية. وفي بعض الحالات نحتاج لما يسمى بالتصحيح التلقائي للكلمات، وهو اقتراح تصحيح لأخطاء شائعة في الكتابة، مثل قلب حرفين، أو عدم الضغط على زر ما لإعطاء كلمة خاطئة، وتشيع في الكتابة بالعربية بعض الأخطاء مثل عدم التفريق بين همزة الوصل وهمزة القطع، والخلط بين الضاد والظاء، وإغفال نقطتي الياء، وكتابة التاء المربوطة هاء.

يهدف هذا المشروع إلى وضع قائمة للكلمات الخاطئة الشائعة وتصحيحها التلقائي، وكذا وضع التعبيرات المنتظمة التي تعبّر عن بعض الحالات. 

AutoCorrect (Text replacement, Replace as you type) is a software function commonly found in word processors such as OpenOffice.org/LibreOffice. Its principal purpose is to correct common spelling or typing errors, saving time for the user. It is also used to automatically format text or insert special characters by recognizing particular character usage, saving the user from having to use more tedious functions[cf. wikipedia].
The common errors in Arabic, are confusion between Alef forms ( Alef with Hamza, Alef without Hamza), missig the Yeh dots, and missing the Teh-Marbuta dots.

This Project aims to construct a word list and a list of regular expressions for Arabic auto-correction. 


## Releases: الإصدارات

* قائمة الكلمات للتصحيح التلقائي، بصيغة  [OpenOffice.org](http://sourceforge.net/projects/ghalatawi/files/acor_ar.dat/download)
* قائمة الكلمات صيغة نصية [ملف مضغوط](http://sourceforge.net/projects/ghalatawi/files/ghalatawi-arabicautocorrect0.1.zip/download)
* قائمة الكلمات صيغة [بيانات SQL](http://sourceforge.net/projects/ghalatawi/files/arabicautocorrect.sql.zip/download)
* مكتبة غلطاوي، لتصحيح الكلمات بواسطة التعابير المنتظمة، وقائمة الكلمات [متن بايثون](الرابط)

 


### Applications تطبيقات

- قائمة التصحيح التلقائي في البرامج المكتبة OpenOffice/LibreOffice
- تدقيق الأخطاء الشائعة في المواقع ذات المحتوى الضخم، مثل ويكيبيديا.
- مساعدة الكاتب في برامج المراسلات، والترجمة، وغيرها.
- تدقيق المدوّنات اللغوية (corpus).
- تصحيح استعلامات البحث.
- تصحيح الكتابة في الأجهزة المحمولة كالهواتف الذكية.

- AutoCorrect for word processors like OpenOffice/LibreOffice
- Huge content site Autocorrection, like Wikipedia.
- Writres and translators assitantance .
- Corpora Autocorrection.


## تثبيت قائمة التصحيح التلقائي في ليبر أوفيس:

1.نزّل قائمة التصحيح التلقائي  بصيغة  [acor_ar.dat](http://sourceforge.net/projects/ghalatawi/files/acor_ar.dat/download)

2. تحقق من مسار التصحيح التلقائي من القائمة ( أدوات/خيارات/ليبرأوفيس/مسارات/ تصحيح تلقائي)  للنسخة الإنجليزية  استعملMenu/Tools /Options/ LibreOffice/paths
3.  اذهب إلى المجلد المذكور في المسار أعلاه: مثلا "~/.config/libreoffice/4/user/autocorr/"
4. انسخ ملف acor_ar.dat، 
5. يمكن تسميته حسب المحليات لديك، مثلا  'acor_ar-DZ.dat' للعربية -الجزائر أو  'acor_ar-EG.dat' للعربية(مصر).
6. أعد تشغيل ليبرأوفيس، وجرب كتابة "اذا" دون همزة، ستصحح تلقائيا إلى "إذا".
7. جرّب كتابة الجملة الآتية، (كتابتها بدلا من نسخها) "اذا رحت الى الادارة فى الضهيرة"
8. ستحصل على " إذا  رحت إلى  الإدارة  في  الظهيرة "

### Usage on LibreOffice:

1. Download the Autocorrect List in LibreOffice format from  [acor_ar.dat](http://sourceforge.net/projects/ghalatawi/files/acor_ar.dat/download)

2. Check paths for Autocorrection in Menu/Tools /Options/ LibreOffice/paths
3. Go to the folder given in paths; it can be "~/.config/libreoffice/4/user/autocorr/
4. Copy the acor_ar.dat on the given path.
5. You can rename the file into your Arabic locale, like 'acor_ar-DZ.dat' or 'acor_ar-EG.dat'.
6. Open LibreOffice and try to write "اذا" it will be automatically corrected to "إذا"
7. Try typing (rather than copying) the following phrase:  اذا رحت الى الادارة فى الضهيرة
8. You will get إذا  رحت إلى  الإدارة  في  الظهيرة  

### Library Usage
### install
```shell
pip install ghalatawi
```
#### [requirement]
```
pyarabic>=0.6.8
```

#### import
```python
>>> from ghalatawi.autocorrector import AutoCorrector
```
## Examples

Detailed examples and features in [Features](doc/features.md) 

* Autocorrect a text

```python
from ghalatawi.autocorrector import AutoCorrector
autoco = AutoCorrector()
text = 'اذا أردت إستعارة كتاب ، اذهب الى المكتبه او الادارة فى الضهيرة .'
autoco.spell(text)
```

output 

````python
'إذا أردت استعارة كتاب، اذهب إلى المكتبة أو الادارة في الظهيرة.'
````



* Show methods used in spelling

```python
from ghalatawi.autocorrector import AutoCorrector
autoco = AutoCorrector()
autoco.show_config()
```

```python
{'regex': True, 'wordlist': True, 'punct': True, 'typo': True}
```

* Allow/disallow methods used in spelling

```python
from ghalatawi.autocorrector import AutoCorrector
autoco = AutoCorrector()
# remove regex method from spelling
autoco.unset_allow("regex") 
text = 'اذا أردت إستعارة كتاب ، اذهب الى المكتبه او الادارة فى الضهيرة .'
# The word إستعارة will no be corrected
expected_text = 'إذا أردت إستعارة كتاب، اذهب إلى المكتبة أو الادارة في الظهيرة.'
result_text = autoco.spell(text)
bool(result_text == expected_text)
# Allow regex 
autoco.set_allow("regex") 
expected_text = 'إذا أردت استعارة كتاب، اذهب إلى المكتبة أو الادارة في الظهيرة.'
result_text = autoco.spell(text)
bool(result_text == expected_text)
```

```python
True
True
```

* Adjust punctuations in text

  ```python
  >>> from ghalatawi.autocorrector import AutoCorrector
  >>> autoco = AutoCorrector()
  >>> text = "قال : للصائم فرحتان : فرحة حين يفطر ، وفرحة حين يلقى ربه  ."
  >>> autoco.adjust_pounct(text)
  'قال: للصائم فرحتان: فرحة حين يفطر، وفرحة حين يلقى ربه.'
  ```

  

* Adjust typos in text

  ```python
  >>> from ghalatawi.autocorrector import AutoCorrector
  >>> autoco = AutoCorrector()        
  >>> text = "اشتريت الخبز و الحليب و الخضر و قليلا من الفاكهة."
  >>> autoco.adjust_typo(text)
      'اشتريت الخبز والحليب والخضر وقليلا من الفاكهة.'
  ```

  

* Autocorrect a word by regex

  ```python
  >>> from ghalatawi.autocorrector import AutoCorrector
  >>> autoco = AutoCorrector()            
  >>> word=u"الإجتماعية"
  >>> autoco.autocorrect_by_regex(word)
  الاجتماعية
  ```

* Autocorrect a word by autucorrection word list; with given word list

  ```python
  >>> from ghalatawi.autocorrector import AutoCorrector
  >>> autoco = AutoCorrector()            
  >>> autocorrectlist={
  ...                 u'اذا':u'إذا',
  ...                 u'او':u'أو',
  ...                 u'فى':u'في',
  ...                 u'هى':u'هي',
  ...                 u'انت':u'أنت',
  ...                 u'انتما':u'أنتما',
  ...                 u'الى':u'إلى',
  ...                 u'التى':u'التي',
  ...                 u'الذى':u'الذي',
  ...                 }
  >>> word=u"اذا"
  >>> autoco.autocorrect_by_wordlist(word, autocorrectlist)
  'إذا'
  ```

  

* Autocorrect a word by autucorrection word list; with default word list

  

  ```python
  >>> from ghalatawi.autocorrector import AutoCorrector
  >>> autoco = AutoCorrector()                    
  >>> word=u"اذا"
  >>> # default word list
  >>> autoco.autocorrect_by_wordlist(word)
  إذا
  ```

* Load a specific wordlist Autocorrect a word by autucorrection word list

```python
>>> from ghalatawi.autocorrector import AutoCorrector
>>> autoco = AutoCorrector()                    
>>> autocorrectlist = autoco.load_wordlist("data/arabic.acl")
>>> word=u"اذا"
>>> autoco.autocorrect_by_wordlist(word, autocorrectlist)
إذا
```

