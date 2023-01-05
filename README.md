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
Feedbacks  |[Comments](https://github.com/linuxscout/ghalatawi/)
Accounts  |[@Twitter](https://twitter.com/linuxscout))


## Citation
If you would cite it in academic work, can you use this citation
```
Zerrouki, Taha, Khaled Alhawiti, and Amar Balla. "Autocorrection of arabic common errors for large text corpus." Proceedings of the EMNLP 2014 workshop on arabic natural language processing (ANLP). 2014.‏
```
```
Zaghouani, Wajdi, Taha Zerrouki, and Amar Balla. "SAHSOH@ QALB-2015 Shared Task: A rule-based correction method of common Arabic native and non-native speakers’ errors." Proceedings of the Second Workshop on Arabic Natural Language Processing. 2015.‏
```
or in bibtex format

```bibtex
@inproceedings{zerrouki2014autocorrection,
  title={Autocorrection of arabic common errors for large text corpus},
  author={Zerrouki, Taha and Alhawiti, Khaled and Balla, Amar},
  booktitle={Proceedings of the EMNLP 2014 workshop on arabic natural language processing (ANLP)},
  pages={127--131},
  year={2014}
}

@inproceedings{zaghouani2015sahsoh,
  title={SAHSOH@ QALB-2015 Shared Task: A rule-based correction method of common Arabic native and non-native speakers’ errors},
  author={Zaghouani, Wajdi and Zerrouki, Taha and Balla, Amar},
  booktitle={Proceedings of the Second Workshop on Arabic Natural Language Processing},
  pages={155--160},
  year={2015}
}

```

## Description

ghalatawi: Arabic Autocorrect library

 التصحيح الإملائي من أهم الأدوات المستعملة في النشر والكتابة الإلكترونية، وتستعمل في البحث والاستعلامات، كما يعد من أهم الأدوات المرافقة للبرامج المكتبية. وفي بعض الحالات نحتاج لما يسمى بالتصحيح التلقائي للكلمات، وهو اقتراح تصحيح لأخطاء شائعة في الكتابة، مثل قلب حرفين، أو عدم الضغط على زر ما لإعطاء كلمة خاطئة، وتشيع في الكتابة بالعربية بعض الأخطاء مثل عدم التفريق بين همزة الوصل وهمزة القطع، والخلط بين الضاد والظاء، وإغفال نقطتي الياء، وكتابة التاء المربوطة هاء.

يهدف هذا المشروع إلى وضع قائمة للكلمات الخاطئة الشائعة وتصحيحها التلقائي، وكذا وضع التعبيرات المنتظمة التي تعبّر عن بعض الحالات. 

AutoCorrect (Text replacement, Replace as you type) is a software function commonly found in word processors such as OpenOffice.org/LibreOffice. Its principal purpose is to correct common spelling or typing errors, saving time for the user. It is also used to automatically format text or insert special characters by recognizing particular character usage, saving the user from having to use more tedious functions[cf. wikipedia].
The common errors in Arabic, are confusion between Alef forms ( Alef with Hamza, Alef without Hamza), missig the Yeh dots, and missing the Teh-Marbuta dots.

This Project aims to construct a word list and a list of regular expressions for Arabic auto-correction. 



###  مزايا:



 


### Applications تطبيقات

- قائمة التصحيح التلقائي في البرامج المكتبة OpenOffice/LibreOffice
- تدقيق الأخطاء الشائعة في المواقع ذات المحتوى الضخم، مثل ويكيبيديا.
- مساعدة الكاتب في برامج المراسلات، والترجمة، وغيرها.
- تدقيق المدوّنات اللغوية (corpus).
- تصحيح استعلامات البحث.
- تصحيح الكتابة في الأجهزة المحمولة كالهوتاف الذكية.

- AutoCorrect for word processors like OpenOffice/LibreOffice
- Huge content site Autocorrection, like Wikipedia.
- Writres and translators assitantance .
- Corpora Autocorrection.


# الإصدارات

- قائمة الكلمات للتصحيح التلقائي، بصيغة OpenOffice.org
- قائمة الكلمات صيغة نصية ملف مضغوط
- قائمة الكلمات صيغة بيانات SQL
- برنامج غلطاوي، لتصحيح الكلمات بواسطة التعابير المنتظمة، وقائمة الكلمات متن بايثون


### Usage

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
>>> import ghalatawi.autocorrect
```
## Examples

Detailed examples and features in [Features](doc/features.md) 


