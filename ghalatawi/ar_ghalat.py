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
from . import ghalat_const as ghconst


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
    word = araby.strip_tatweel(word);
    word_nm = araby.strip_tashkeel(word)
    for rule in ghconst.ReplacementTable:
        # rule[0]: pattern
        # rule[1]: replacement  
        result=rule[0].sub(rule[1],word_nm);
        # if the result changes, return True;
        if result!=word_nm:
            return result;
    #if all rules don't match, return False;
    return False;

def autocorrectByWordlist(word, word_list = ghconst.ArabicAutocorrectWordlist):
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
    for rule in ghconst.ReplacementTablePount:
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
    text = ghconst.pat_duplicate.sub(r'\1\1', text)
  
    # autocorrect words without diacritics 
    for rule in ghconst.ReplacementTableTypo:
        # rule[0]: pattern
        # rule[1]: replacement  
        text = rule[0].sub(rule[1],text);
        # if the result changes, return True;
    return text;

