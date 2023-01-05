Ghalatawi غلطاوي
================

Ghalatawi: Arabic Autocorrect library مكتبة للتصحيح التلقائي للغة
العربية

.. figure:: ystatic/ghalatawi_header.png
   :alt: ghalatawi logo

   ghalatawi logo

.. figure:: https://img.shields.io/pypi/dm/ghalatawi
   :alt: PyPI - Downloads

   PyPI - Downloads

Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com

+------+---------------------------------------------------------------+
| Feat | value                                                         |
| ures |                                                               |
+------+---------------------------------------------------------------+
| Aut  |  Authors.md                                                   |
| hors |  <https://github.com/linuxscout/ghalatawi/main/AUTHORS.md>    |
+------+---------------------------------------------------------------+
| Rel  | 0.1                                                           |
| ease |                                                               |
+------+---------------------------------------------------------------+
| Lic  | `                                                             |
| ense | GPL <https://github.com/linuxscout/ghalatawi/main/LICENSE>`__ |
+------+---------------------------------------------------------------+
| Tra  | `linuxscout/ghalata                                           |
| cker | wi/Issues <https://github.com/linuxscout/ghalatawi/issues>`__ |
+------+---------------------------------------------------------------+
| So   | `Github <http://github.com/linuxscout/ghalatawi>`__           |
| urce |                                                               |
+------+---------------------------------------------------------------+
| F    | `Comments <https://github.com/linuxscout/ghalatawi/>`__       |
| eedb |                                                               |
| acks |                                                               |
+------+---------------------------------------------------------------+
| Acco | `@Twitter <https://twitter.com/linuxscout>`__)                |
| unts |                                                               |
+------+---------------------------------------------------------------+

Description
-----------

ghalatawi: Arabic Autocorrect library

التصحيح الإملائي من أهم الأدوات المستعملة في النشر والكتابة الإلكترونية،
وتستعمل في البحث والاستعلامات، كما يعد من أهم الأدوات المرافقة للبرامج
المكتبية. وفي بعض الحالات نحتاج لما يسمى بالتصحيح التلقائي للكلمات، وهو
اقتراح تصحيح لأخطاء شائعة في الكتابة، مثل قلب حرفين، أو عدم الضغط على زر
ما لإعطاء كلمة خاطئة، وتشيع في الكتابة بالعربية بعض الأخطاء مثل عدم
التفريق بين همزة الوصل وهمزة القطع، والخلط بين الضاد والظاء، وإغفال
نقطتي الياء، وكتابة التاء المربوطة هاء.

يهدف هذا المشروع إلى وضع قائمة للكلمات الخاطئة الشائعة وتصحيحها
التلقائي، وكذا وضع التعبيرات المنتظمة التي تعبّر عن بعض الحالات.

AutoCorrect (Text replacement, Replace as you type) is a software
function commonly found in word processors such as
OpenOffice.org/LibreOffice. Its principal purpose is to correct common
spelling or typing errors, saving time for the user. It is also used to
automatically format text or insert special characters by recognizing
particular character usage, saving the user from having to use more
tedious functions[cf. wikipedia]. The common errors in Arabic, are
confusion between Alef forms ( Alef with Hamza, Alef without Hamza),
missig the Yeh dots, and missing the Teh-Marbuta dots.

This Project aims to construct a word list and a list of regular
expressions for Arabic auto-correction.

مزايا:
~~~~~~

Applications تطبيقات
~~~~~~~~~~~~~~~~~~~~

-  قائمة التصحيح التلقائي في البرامج المكتبة OpenOffice/LibreOffice

-  تدقيق الأخطاء الشائعة في المواقع ذات المحتوى الضخم، مثل ويكيبيديا.

-  مساعدة الكاتب في برامج المراسلات، والترجمة، وغيرها.

-  تدقيق المدوّنات اللغوية (corpus).

-  تصحيح استعلامات البحث.

-  تصحيح الكتابة في الأجهزة المحمولة كالهوتاف الذكية.

-  AutoCorrect for word processors like OpenOffice/LibreOffice

-  Huge content site Autocorrection, like Wikipedia.

-  Writres and translators assitantance .

-  Corpora Autocorrection.

Usage
~~~~~

install
~~~~~~~

.. code:: shell

   pip install ghalatawi

[requirement]
^^^^^^^^^^^^^

::

   pyarabic>=0.6.8

import
^^^^^^

.. code:: python

   >>> from ghalatawi.autocorrector import AutoCorrector

Examples
--------

Detailed examples and features in `Features <doc/features.md>`__

-  Autocorrect a text

.. code:: python

   from ghalatawi.autocorrector import AutoCorrector
   autoco = AutoCorrector()
   text = 'اذا أردت إستعارة كتاب ، اذهب الى المكتبه او الادارة فى الضهيرة .'
   autoco.spell(text)

output

.. code:: python

   'إذا أردت استعارة كتاب، اذهب إلى المكتبة أو الادارة في الظهيرة.'

-  Show methods used in spelling

.. code:: python

   from ghalatawi.autocorrector import AutoCorrector
   autoco = AutoCorrector()
   autoco.show_config()

.. code:: python

   {'regex': True, 'wordlist': True, 'punct': True, 'typo': True}

-  Allow/disallow methods used in spelling

.. code:: python

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

.. code:: python

   True
   True

-  Adjust punctuations in text

   .. code:: python

      >>> from ghalatawi.autocorrector import AutoCorrector
      >>> autoco = AutoCorrector()
      >>> text = "قال : للصائم فرحتان : فرحة حين يفطر ، وفرحة حين يلقى ربه  ."
      >>> autoco.adjust_pounct(text)
      'قال: للصائم فرحتان: فرحة حين يفطر، وفرحة حين يلقى ربه.'

-  Adjust typos in text

   .. code:: python

      >>> from ghalatawi.autocorrector import AutoCorrector
      >>> autoco = AutoCorrector()        
      >>> text = "اشتريت الخبز و الحليب و الخضر و قليلا من الفاكهة."
      >>> autoco.adjust_typo(text)
          'اشتريت الخبز والحليب والخضر وقليلا من الفاكهة.'

-  Autocorrect a word by regex

   .. code:: python

      >>> from ghalatawi.autocorrector import AutoCorrector
      >>> autoco = AutoCorrector()            
      >>> word=u"الإجتماعية"
      >>> autoco.autocorrect_by_regex(word)
      الاجتماعية

-  Autocorrect a word by autucorrection word list; with given word list

   .. code:: python

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

-  Autocorrect a word by autucorrection word list; with default word
   list

   .. code:: python

      >>> from ghalatawi.autocorrector import AutoCorrector
      >>> autoco = AutoCorrector()                    
      >>> word=u"اذا"
      >>> # default word list
      >>> autoco.autocorrect_by_wordlist(word)
      إذا

-  Load a specific wordlist Autocorrect a word by autucorrection word
   list

.. code:: python

   >>> from ghalatawi.autocorrector import AutoCorrector
   >>> autoco = AutoCorrector()                    
   >>> autocorrectlist = autoco.load_wordlist("data/arabic.acl")
   >>> word=u"اذا"
   >>> autoco.autocorrect_by_wordlist(word, autocorrectlist)
   إذا
