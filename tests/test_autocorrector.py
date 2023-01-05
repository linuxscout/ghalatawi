#!/usr/bin/python
# -*- coding=utf-8 -*-
import unittest
import os.path
import sys
sys.path.append("../")
import ghalatawi.ar_ghalat as gh
import ghalatawi.autocorrector 

class ghalatawiTestCase(unittest.TestCase):
    """Tests for `number.py`."""
    def __init__(self, *args, **kwargs):
        """
        initial autocorrector
        """
        super(ghalatawiTestCase, self).__init__(*args, **kwargs)
        # init autocorrector
        self.autoco = ghalatawi.autocorrector.AutoCorrector()

    def test_isArabicWord(self):
        """
        Test isArabicWord
        """
        self.assertEqual(self.autoco.is_arabicword("english"), False)

    def test_autocorrectByRegex(self):
        """
        Test autocorrectByRegex
        """
        word = "الإجتماعية"
        correct = "الاجتماعية"
        self.assertEqual(self.autoco.autocorrect_by_regex(word),correct)
        
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
        self.assertEqual(self.autoco.autocorrect_by_wordlist(word, autocorrectlist), "إذا")
    
    def test_loadAutocorrectWordlistFromFile(self):
        """
        Test autocorrectByWordlist from file
        """
        path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/arabic0.2.acl")
        autocorrectlist = self.autoco.load_wordlist(path)
        self.assertNotEqual(autocorrectlist, False)
        word=u"اذا"
        self.assertEqual(self.autoco.autocorrect_by_wordlist(word, autocorrectlist), "إذا")
        self.assertEqual(self.autoco.autocorrect_by_wordlist(word), "إذا")
        
    def test_ajust_pounct(self):
        """
        Test ajust pounctuation
        """

        text = "قال : للصائم فرحتان : فرحة حين يفطر ، وفرحة حين يلقى ربه  ."
        correct_text = 'قال: للصائم فرحتان: فرحة حين يفطر، وفرحة حين يلقى ربه.'
        self.assertEqual(self.autoco.ajust_pounct(text), correct_text)
        
    def test_ajust_typo(self):
        """
        Test ajust typo
        """

        text = "اشتريت الخبز و الحليب و الخضر و قليلا من الفاكهة."
        correct_text = "اشتريت الخبز والحليب والخضر وقليلا من الفاكهة."
        self.assertEqual(self.autoco.ajust_typo(text), correct_text)
            
if __name__ == '__main__':
    unittest.main()
