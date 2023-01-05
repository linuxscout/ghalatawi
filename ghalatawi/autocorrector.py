#!/usr/bin/python
# -*- coding=utf-8 -*-
#************************************************************************
# $Id: autocorrecter.py,v 0.7 2011/01/05 01:10:00 Taha Zerrouki $
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
@date:2023/01/05
@version: 0.3
"""
import re
import os 
import pyarabic.araby as araby
from . import ghalat_const as ghconst
WORDLIST_FILENAME = "data/arabic0.2.acl"

class AutoCorrector:
    """
    Class to autocorect Arabic string
    """
    def __init__(self, wordlist_filename = ""):
        """
        Create an autocorrector class, with optional wordlist_file
        @param wordlist_filename : file name to load a word list for autocrecction
        @type wordlist_filename : str     
        """
        if wordlist_filename:
            
            self.replace_list = self.load_wordlist(wordlist_filename)
        else:
            # load default file of autocorrection word list
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), WORDLIST_FILENAME)
            self.replace_list = self.load_wordlist(path)
        self.config = {"regex":True,
        "wordlist":True,
        "punct":True,
        "typo":True,
        }
        self.allow_regex    = True
        self.allow_wordlist = True
        self.allow_punct    = True
        self.allow_typo     = True            
        
            
    def is_arabicword(self, word):
        """ Checks for a valid Arabic word.
        An Arabic word not contains spaces, digits and pounctuation
        avoid some spelling error,  TEH_MARBUTA must be at the end.
        @param word: input word
        @type word: unicode
        @return: True if all charaters are in Arabic block
        @rtype: Boolean
        """
        return araby.is_arabicword(word);

    def autocorrect_by_regex(self, word):
        """
        Autocorrect by using regular expression from remplacement table.
        
        Example:
            >>> from ghalatawi.autocorrector import AutoCorrector
            >>> autoco = AutoCorrector()            
            >>> word=u"الإجتماعية"
            >>> autoco.autocorrect_by_regex(word)
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

    def autocorrect_by_wordlist(self, word, word_list= []):
        """
        Autocorrect by using word list.
        the default list is ArabicAutocorrectWordlist.
        
        Example:
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
            >>> autoco.autocorrect_by_wordlist(word)
            'إذا'

        @param word: the input word.
        @type word: unicode.
        @return: corrected word, if the word is common error, or False.
        @rtype: unicode or False.
        """
        if not word:
            return False
        if not word_list and not self.replace_list:
            return False
        elif not word_list and  self.replace_list:
            word_list = self.replace_list
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
                
            
    def load_wordlist(self, filename):
        """
        Load Autocorrect list from a file, to the global list autocorrect_arabic_list.
        
        Example:
            >>> from ghalatawi.autocorrector import AutoCorrector
            >>> autoco = AutoCorrector()                    
            >>> autocorrectlist = autoco.load_wordlist("data/arabic.acl")
            >>> word=u"اذا"
            >>> autoco.autocorrect_by_wordlist(word, autocorrectlist)
             إذا
        
        @param filename: the input word.
        @type filename: unicode.
        @return: wordlist, if loaded, else False.
        @rtype: Boolean.
        """
        # load autolist from file
        try:
            fl=open(filename, encoding="utf8");
        except:
            raise Exception(__file__, ": IOException: Can't open auto correction file ", filename)
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
        
        self.replace_list = auto_list
        return auto_list;

    def adjust_pounct(self, text):
        """
        adjust pountuation in text.
        
        Example:
            >>> from ghalatawi.autocorrector import AutoCorrector
            >>> autoco = AutoCorrector()
            >>> text = "قال : للصائم فرحتان : فرحة حين يفطر ، وفرحة حين يلقى ربه  ."
            >>> autoco.adjust_pounct(text)
    'قال: للصائم فرحتان: فرحة حين يفطر، وفرحة حين يلقى ربه.'
        
        @param text: the input text.
        @type text: unicode.
        @return: adjusted text.
        @rtype: unicode.
        """
        # autocorrect words without diacritics 
        for rule in ghconst.ReplacementTablePount:
            # rule[0]: pattern
            # rule[1]: replacement  
            text = rule[0].sub(rule[1],text);
            # if the result changes, return True;
        return text;
    def adjust_typo(self, text):
        """
        adjust typo errors in text.
        
        Example:
            >>> from ghalatawi.autocorrector import AutoCorrector
            >>> autoco = AutoCorrector()        
            >>> text = "اشتريت الخبز و الحليب و الخضر و قليلا من الفاكهة."
            >>> autoco.adjust_typo(text)
    'اشتريت الخبز والحليب والخضر وقليلا من الفاكهة.'

        
        @param text: the input text.
        @type text: unicode.
        @return: adjusted text.
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
    def spell(self, text):
        """
        Auto correct text.
        adjust typo errors in text.
        
        Example:
            >>> from ghalatawi.autocorrector import AutoCorrector()
            >>> autoco = AutoCorrector()
            >>> text = 'اذا أردت إستعارة كتاب ، اذهب الى المكتبه او الادارة فى الضهيرة .'
            >>> autoco.spell(text)
    'إذا أردت استعارة كتاب، اذهب إلى المكتبة أو الادارة في الظهيرة.'

        @param text: the input text.
        @type text: string.
        @return: corrected text.
        @rtype: string
        """        
        # tokenize
        if not text:
            return text
        
        tokens = araby.tokenize(text)

        if self.config.get("regex",False):
            tmp_tokens = []
            for tok in tokens:
                tok_correct = self.autocorrect_by_regex(tok)
                # if there is a correction append if
                # else append original token
                if tok_correct:
                    tmp_tokens.append(tok_correct)
                else:
                    tmp_tokens.append(tok)
            tokens = tmp_tokens

        if self.config.get("wordlist",False):
            tmp_tokens = []
            for tok in tokens:
                tok_correct = self.autocorrect_by_wordlist(tok)
                # if there is a correction append if
                # else append original token
                if tok_correct:
                    tmp_tokens.append(tok_correct)
                else:
                    tmp_tokens.append(tok)
            tokens = tmp_tokens
        new_text = " ".join(tokens)
        if self.config.get("punct",False):
            new_text = self.adjust_pounct(new_text)
        if self.config.get("typo",False):
            new_text = self.adjust_typo(new_text)
        
        return new_text


    
     
    def allow_all(self):
        """
        Enable all methods for autocorrector, in spell() method
        """
        for name in self.config:
            self.config[name] = True
    def unallow_all(self):
        """
        Disable all methods for autocorrector, in spell() method
        """
        for name in self.config:
            self.config[name] = False            
    def set_allow(self, name):
        """
        Enable using 'name' method for autocorrector, in spell() method
        """
        if name in self.config:
            self.config[name] = True
    def unset_allow(self, name):
        """
        Diasble using 'name' method for autocorrector, in spell() method
        """
        if name in self.config:
            self.config[name] = False
    def get_allow(self, name):
        """
        Get value of 'name' method for autocorrector, used in spell() method
        """
        return self.config.get(name, None)
    
    def show_config(self):
        """
        Show methods used for autocorrector, in spell() method
        """
        return self.config
   

