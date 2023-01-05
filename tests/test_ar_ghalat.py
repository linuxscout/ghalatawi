#!/usr/bin/python
# -*- coding=utf-8 -*-
import unittest
import os.path
import sys
sys.path.append("../")
import ghalatawi.ar_ghalat as gh

class ghalatawiTestCase(unittest.TestCase):
    """Tests for `number.py`."""

    def test_isArabicWord(self):
        """
        Test isArabicWord
        """
        self.assertEqual(gh.isArabicword("english"), False)

    def test_autocorrectByRegex(self):
        """
        Test autocorrectByRegex
        """
        word = "الإجتماعية"
        correct = "الاجتماعية"
        self.assertEqual(gh.autocorrectByRegex(word),correct)
    def test_autocorrectByWordlist(self):
        """
        Test autocorrectByWordlist 
        """
        autocorrectlist={
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
        word=u"اذا"
        self.assertEqual(gh.autocorrectByWordlist(word, autocorrectlist), "إذا")
    
    def test_loadAutocorrectWordlistFromFile(self):
        """
        Test autocorrectByWordlist from file
        """
        path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/arabic0.2.acl")
        autocorrectlist=gh.loadAutocorrectWordlistFromFile(path)
        self.assertNotEqual(autocorrectlist, False)
        word=u"اذا"
        self.assertEqual(gh.autocorrectByWordlist(word, autocorrectlist), "إذا")
        
    def test_ajust_pounct(self):
        """
        Test ajust pounctuation
        """

        text = "قال : للصائم فرحتان : فرحة حين يفطر ، وفرحة حين يلقى ربه  ."
        correct_text = 'قال: للصائم فرحتان: فرحة حين يفطر، وفرحة حين يلقى ربه.'
        self.assertEqual(gh.ajust_pounct(text), correct_text)
        
    def test_ajust_typo(self):
        """
        Test ajust typo
        """

        text = "اشتريت الخبز و الحليب و الخضر و قليلا من الفاكهة."
        correct_text = "اشتريت الخبز والحليب والخضر وقليلا من الفاكهة."
        self.assertEqual(gh.ajust_typo(text), correct_text)
            
if __name__ == '__main__':
    unittest.main()
