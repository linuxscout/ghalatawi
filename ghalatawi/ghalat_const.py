#!/usr/bin/python
# -*- coding=utf-8 -*-
#************************************************************************
# $Id: ar_ghalat.py,v 0.7 2011/01/05 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2011, Arabtechies, Arabeyes Taha Zerrouki
#
#  Elementary function to detect and correct minor spell error for  arabic texte
#
# -----------------
# Revision Details:    (Updated by Revision Control System)
# -----------------
#  $Date: 2011/01/05 01:10:00 $
#  $Author: Taha Zerrouki $
#  $Revision: 0.2 $
#  $Source: ghalatawi.sourceforge.net
#
#  This program is written under the GPL License.
#
#***********************************************************************/
"""
Ghalatawi: Arabic AutoCorrection module
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies, Arabeyes,  Taha Zerrouki
@license: GPL
@date:2011/01/05
@version: 0.2
"""
import re
import pyarabic.araby as araby
"""
@var ArabicAutocorrectWordlist: Common error on stop words.
@var ReplacementTable: Table of regular expression to be treated.
"""
ArabicAutocorrectWordlist={
#common error on stop words
u'اذا':u'إذا',
u'او':u'أو',
u'فى':u'في',
u'هى':u'هي',
u'انت':u'أنت',
u'انتما':u'أنتما',
u'الى':u'إلى',
u'التى':u'التي',
u'الذى':u'الذي',
}



ReplacementTable=[
# removing kashida (Tatweel)
#(re.compile(r'([\u0621-\u063F\u0641-\u064A])\u0640+([\u0621-\u063F\u0641-\u064A])',re.UNICODE), r'\1\2'), 
# rules for انفعال
(re.compile(r'\b(و|ف|)(ك|ب|)(ال|)إن(\w\w)ا(\w)(ي|)(ين|ات|ة|تين|)\b',re.UNICODE), r'\1\2\3ان\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)(لل|)إن(\w\w)ا(\w)(ي|)(ين|ات|تين|ة|)\b',re.UNICODE), r'\1\2ان\3ا\4\5\6'),
(re.compile(r'\b(و|ف|)(ك|ب|ل|)إن(\w\w)ا(\w)(ي|)(هما|كما|هم|كم|هن|كن|نا|ه|ك|ها|تهما|تكما|تهم|تكم|تهن|تكن|تنا|ته|تها|تك|اتهما|اتكما|اتهم|اتكم|اتهن|اتكن|اتنا|اته|اتها|اتك|)\b',re.UNICODE), r'\1\2ان\3ا\4\5\6'),
(re.compile(r'\b(و|ف|)(ال|)إن(\w\w)ا(\w)(ي|)(ين|ان|تين|تان|ون|)\b',re.UNICODE), r'\1\2ان\3ا\4\5\6'),
(re.compile(r'\b(و|ف|)إن(\w\w)ا(\w)(ي|)(ًا|اً|ا|)\b',re.UNICODE), r'\1ان\2ا\3\4\5'),
# rules for افتعال
(re.compile(r'\b(و|ف|)(ك|ب|)(ال|)إ(\w)ت(\w)ا(\w)(ي|)(ين|ات|ة|تين|)\b',re.UNICODE), r'\1\2\3ا\4ت\5ا\6\7\8'),
(re.compile(r'\b(و|ف|)(لل|)إ(\w)ت(\w)ا(\w)(ي|)(ين|ات|تين|ة|)\b',re.UNICODE), r'\1\2ا\3ت\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)(ك|ب|ل|)إ(\w)ت(\w)ا(\w)(ي|)(هما|كما|هم|كم|هن|كن|نا|ه|ك|ها|تهما|تكما|تهم|تكم|تهن|تكن|تنا|ته|تها|تك|اتهما|اتكما|اتهم|اتكم|اتهن|اتكن|اتنا|اته|اتها|اتك|)\b',re.UNICODE), r'\1\2ا\3ت\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)(ال|)إ(\w)ت(\w)ا(\w)(ي|)(ين|ان|تين|تان|ون|)\b',re.UNICODE), r'\1\2ا\3ت\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)إ(\w)ت(\w)ا(\w)(ي|)(ًا|اً|ا|)\b',re.UNICODE), r'\1ا\2ت\3ا\4\5\6'),
# rules for افتعال التي تحوي ضط أو صط أو زد
(re.compile(r'\b(و|ف|)(ك|ب|)(ال|)إ(زد|ضط|صط)(\w)ا(\w)(ي|)(ين|ات|ة|تين|)\b',re.UNICODE), r'\1\2\3ا\4\5ا\6\7\8'),
(re.compile(r'\b(و|ف|)(لل|)إ(ﺯﺩ|ﺾﻃ|ﺺﻃ)(\w)ا(\w)(ي|)(ين|ات|تين|ة|)\b',re.UNICODE), r'\1\2ا\3\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)(ك|ب|ل|)إ(ﺯﺩ|ﺾﻃ|ﺺﻃ)(\w)ا(\w)(ي|)(هما|كما|هم|كم|هن|كن|نا|ه|ك|ها|تهما|تكما|تهم|تكم|تهن|تكن|تنا|ته|تها|تك|اتهما|اتكما|اتهم|اتكم|اتهن|اتكن|اتنا|اته|اتها|اتك|)\b',re.UNICODE), r'\1\2ا\3\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)(ال|)إ(ﺯﺩ|ﺾﻃ|ﺺﻃ)(\w)ا(\w)(ي|)(ين|ان|تين|تان|ون|)\b',re.UNICODE), r'\1\2ا\3\4ا\5\6\7'),
(re.compile(r'\b(و|ف|)إ(ﺯﺩ|ﺾﻃ|ﺺﻃ)(\w)ا(\w)(ي|)(ًا|اً|ا|)\b',re.UNICODE), r'\1ا\2\3ا\4\5\6'),
# حالة الألف المقصورة بعدها همزة في آخر الكلمة، وعادة مايكون البديل همزة على النبرة. 
(re.compile(r'ىء\b',re.UNICODE), r'ئ'),
# حالة الألف المقصورة ليست في آخر الكلمة، وعادة مايوضع بعدها فراغ 
(re.compile(r'ى([^ء]+)\b',re.UNICODE), r'ى \1'),
# حالة التاء المربوطة ليست في آخر الكلمة، وعادة مايوضع بعدها فراغ 
(re.compile(r'ة(\w+)\b',re.UNICODE), r'ة \1'),
# حالة الالف المكررة بعدها لام،يكون البديل بين اﻷلفين فراغ
#(re.compile(r'\bاال(\w+)\b',re.UNICODE), r'ال\1'),
#(re.compile(r'(\w+)اال(\w+)\b',re.UNICODE), r'\1ا ال\2'),
#(re.compile(r'(\w+)(ا+)(\w+)\b',re.UNICODE), r'\1ا\3'),
#(re.compile(r'ا(ا+)',re.UNICODE), r'ا'),
]

ReplacementTableTypo = [
(re.compile(r" و ", re.UNICODE) , r" و"),
(re.compile(r"^و ", re.UNICODE) , r"و"),
]
ReplacementTablePount =[

# punctuation

(re.compile(r" ([.?!,:;)”—]($| ))", re.UNICODE) , r"\1"), # Extra space before punctuation.
(re.compile(r"([(“—]) ", re.UNICODE) , r"\1"), # Extra space after punctuation.
#~(re.compile(r"([\w%s]+)([ ]?;)"% u"".join(araby.TASHKEEL), re.UNICODE) , r"\1؛"),
#~(re.compile(r"([\w%s]+)([ ]?,)"% u"".join(araby.TASHKEEL), re.UNICODE) , r"\1،"),
(re.compile(r"(.*\w[^a-zA-Z\W\d])([ ]?;)", re.UNICODE) , r"\1؛"),
(re.compile(r"(.*\w[^a-zA-Z\W\d])([ ]?,)", re.UNICODE) , r"\1،"),
#~r"([\w%s]+)" % u"".join(TASHKEEL)
(re.compile(r"\([ ]*", re.UNICODE) , r"("),
(re.compile(r"[ ]*\)", re.UNICODE) , r")"),
(re.compile(r"^[\ ]*$", re.UNICODE) , r""),
(re.compile(r"^[\ ]*", re.UNICODE) , r""),
(re.compile(r"[\ ]*$", re.UNICODE) , r""),
(re.compile(r"[ ]+", re.UNICODE) , r" "),
(re.compile(r" :", re.UNICODE) , r":"),
(re.compile(r" ؛", re.UNICODE) , r"؛"),
(re.compile(r" ،", re.UNICODE) , r"،"),
(re.compile(r" \.", re.UNICODE) , r"."),
(re.compile(r" !", re.UNICODE) , r"!"),
(re.compile(r" ؟", re.UNICODE) , r"؟"),
(re.compile(r" و ", re.UNICODE) , r" و"),
(re.compile(r"^و ", re.UNICODE) , r"و"),
(re.compile(r"ـ", re.UNICODE) , r""),
# definitions
#~abc [a-z]+
#~ABC [A-Z]+
#~Abc [a-zA-Z]+
#~punct [?!,:;%‰‱˚“”‘]
#~
#~{Abc}{punct}{Abc} -> {Abc}{punct} {Abc}    # Missing space?
#~{abc}[.]{ABC} -> {abc}. {ABC}        # Missing space?

# typography
(re.compile(r"[.]{3}", re.UNICODE) , u"…"    ),         # Three dot character.

(re.compile(r"(^|\b|{punct}|[.]) {2,3}(\b|$)", re.UNICODE) , r"\1 " ),# Extra space.
]
pat_duplicate =re.compile(r'(\w)\1{2,}',  re.UNICODE)

def isArabicword(word):
    """ Checks for a valid Arabic word.
    An Arabic word not contains spaces, digits and pounctuation
    avoid some spelling error,  TEH_MARBUTA must be at the end.
    @param word: input word
    @type word: unicode
    @return: True if all charaters are in Arabic block
    @rtype: Boolean
    """
    return araby.is_arabicword(word);

def autocorrectByRegex(word):
    """
    Autocorrect by using regular expression from remplacement table.
    
    Example:
        >>> word=u"الإجتماعية"
        >>> autocorrectByRegex(word)
         الاجتماعية
    
    @param word: the input word.
    @type word: unicode.
    @return: corrected word, if the word is common error, or False.
    @rtype: unicode or False.
    """
    # autocorrect words without diacritics 
    word=araby.strip_tatweel(word);
    word_nm=araby.strip_tashkeel(word)
    for rule in ReplacementTable:
        # rule[0]: pattern
        # rule[1]: replacement  
        result=rule[0].sub(rule[1],word_nm);
        # if the result changes, return True;
        if result!=word_nm:
            return result;
    #if all rules don't match, return False;
    return False;

def autocorrectByWordlist(word, word_list = ArabicAutocorrectWordlist):
    """
    Autocorrect by using word list.
    the default list is ArabicAutocorrectWordlist.
    
    Example:
        >>> autocorrectlist={
            u'اذا':u'إذا',
            u'او':u'أو',
            u'فى':u'في',
            u'هى':u'هي',
            u'انت':u'أنت',
            u'انتما':u'أنتما',
            u'الى':u'إلى',
            u'التى':u'التي',
            u'الذى':u'الذي',
            }
        >>> word=u"اذا"
        >>> autocorrectByWordlist(word, autocorrectlist)
         إذا
    
    @param word: the input word.
    @type word: unicode.
    @return: corrected word, if the word is common error, or False.
    @rtype: unicode or False.
    """
    if not word:
        return False
    if not word_list:
        return False 
    # autocorrect words from a list 
    # autocorrect words without diacritics
    word = araby.strip_tatweel(word);
    word_nm = araby.strip_tashkeel(word)
    if not word_nm:
        return False
    #~print "word list", type(word_list)
    if word_nm in word_list:
        return word_list[word];
    else: 
        return False;
    return False;
            
        
def loadAutocorrectWordlistFromFile(myfile):
    """
    Load Autocorrect list from a file, to the global list autocorrect_arabic_list.
    
    Example:
        >>> autocorrectlist=loadAutocorrectWordlistFromFile("data/arabic.acl")
        >>> word=u"اذا"
        >>> autocorrectByWordlist(word, autocorrectlist)
         إذا
    
    @param myfile: the input word.
    @type myfile: unicode.
    @return: wordlist, if loaded, else False.
    @rtype: Boolean.
    """
    # load autolist from file
    try:
        fl=open(myfile, encoding="utf8");
    except:
        # file not found
        return False;
    line=fl.readline();
    nb_field = 2;
    auto_list = {}
    while line :
        line=line.strip("\n");
        if not line.startswith("#"):
            liste=line.split("\t");
            if len(liste)>=nb_field:
                auto_list[liste[0]]=liste[1];
        line=fl.readline();
    fl.close();
    return auto_list;

def ajust_pounct(text):
    """
    ajust pountuation in text.
    
    Example:
        >>> 
        >>> text = "قال : للصائم فرحتان : فرحة حين يفطر ، وفرحة حين يلقى ربه  ."
        >>> ajust_pounct(text)
'قال: للصائم فرحتان: فرحة حين يفطر، وفرحة حين يلقى ربه.'
    
    @param text: the input text.
    @type text: unicode.
    @return: ajusted text.
    @rtype: unicode.
    """
    # autocorrect words without diacritics 
    for rule in ReplacementTablePount:
        # rule[0]: pattern
        # rule[1]: replacement  
        text = rule[0].sub(rule[1],text);
        # if the result changes, return True;
    return text;

def ajust_typo(text):
    """
    ajust typo errors in text.
    
    Example:
        >>> text = "اشتريت الخبز و الحليب و الخضر و قليلا من الفاكهة."
        >>> ajust_typo(text)
'اشتريت الخبز والحليب والخضر وقليلا من الفاكهة.'

    
    @param text: the input text.
    @type text: unicode.
    @return: ajusted text.
    @rtype: unicode.
    """
    # remove redendent more than 2 times
    text = pat_duplicate.sub(r'\1\1', text)
  
    # autocorrect words without diacritics 
    for rule in ReplacementTableTypo:
        # rule[0]: pattern
        # rule[1]: replacement  
        text = rule[0].sub(rule[1],text);
        # if the result changes, return True;
    return text;

