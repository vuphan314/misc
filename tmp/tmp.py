import itertools
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        palindromeIndexPairs = []
        numWords = len(words)
        indexPairs = itertools.permutations(range(numWords), 2)
        for indexPair in indexPairs:
            i, j = indexPair
            string = words[i] + words[j]
            if self.isPalindrome(string):
                palindromeIndexPairs.append(indexPair)
        return palindromeIndexPairs
    def isPalindrome(self, string):
        length = len(string)
        mid = length // 2
        for dist in range(mid):
            if string[dist] != string[-1 - dist]:
                return False
        return True
############################################################
"""
import unittest
class Test(unittest.TestCase):
    def test(self):
        inputs = (
            ["abcd", "dcba", "lls", "s", "sssll"],
            ["djejb","hciii","ea","jggiaieifhigfhhbd","iacgb","h","gbjahbedfhdfcjjgce","dfcefe","egd","hbab","ejbddgiificideiijje","giicgajijdcihef","fehghgjccfggahgjj","gdjjbfjje","dacff","idhabh","ieaciahjcbebdejf","biigjihbdfjhcfffie","dgfahaa","jjdjghfefbbbhcadid","cbjcjiebdfe","dedbgefgjhaffehagg","cghdidchgffd","bahcggebbg","ebaijijddbbgcacjj","idjb","aejhhhjgceccbigaabd","bgh","gedffgg","ebhjhdahfbi","dibd","gjchdbfchafei","ahdfjiiabiffabhca","ad","cijhcca","cdccdb","ciiijgafadgiecgb","eeej","ebhbcegh","ceg","cjchfeacebeheecdbg","fbd","ihd","bichfbdcehidf","djcegdjdgeda","agdhggcfhebfggcbca","afj","aicbjaj","cgdgg","igeajdfbh","gggfehefbbdigijfcid","ecciibdgcadjgbfgjbfj","aeedhbfeed","biccehabcdfdabc","jdjejchcifgif","ebgdachbjhja","jaacdf","fgicdcb","ggecg","hbeifd","dbbjdhech","fede","dfafbhijjfgdagbfcc","jbe","dhadiehefgh","iadhbejdjjiegebhfg","egddjjbiaigdgab","acjfajj","gdjbjbcdcgiabbfgcji","e","ijfe","a","cdgadcjahddib","jaifjhddhdddaedb","j","feiafchicb","djji","fgeabh","cbejbehb","jaj","cehaffgjjfdjb","jcfdaabahajaejg","jhaicda","gcjgheahaicgcageeja","chej","cjejfcfgbahieiibjhd","hgbgjhf","cd","dcffjcdihgbdfjjfdf","b","ejgfhccabjjaiajag","hfhihg","iddhhbiddhjdjajgf","fhijjijh","egfhgbgfi","jfcbbag","hfa","fdgbfjdghadigghjgghb","ejha","ijbdc","ebhdidifdfefcegjjahb","dgiejcgfgfjgdbd","bhhafabcj","gijgjjgfhifjihidha","bjdieie","hfbbafgejidded","he","fdeghfchcafbaf","diihcdgiidiejdiabee","iagbb","fbbdgh","bccbgegbabghhggiij","bc","daiijbjbfjgajde","hgfjaabggeaeh","dc","eedficedihfc","dbibgchaddidceg","fagigfefbbccgdbjfcgi","egjiifachdhabadcchi","iciiiadfaahbej","jgbbfd","ibcbicgi","gffcdecciffefibebfg","idbfcifbgifiaca","dfg","cb","bgbb","fchdjj","ffbfffacbg","bagh","ccdc","ieadegicagbf","icdjjgic","eihdeeaeeefbjgeaefi","hfbj","fajcbffedjeebfahjb","bfa","hffeeidajgcf","ahfbjafib","aiggcafjdhi","fdfebcehjcdefia","ichgbdfghjghab","bgbhgjgfhbb","bdaehgabdfcihibfa","caahaecggi","geadiaiibhjgjcb","gefjeicbhgbbcafg","hdfgbcijaef","chigiefahceeebifbijc","jbcccfgihddcjg","gcbcjdfbhegfjfba","jagddjjhji","cg","bhecffha","jbabcdaghe","ggjcjdfbgdijdagieg","hjedhedibbjjbbfge","bhgajjdbja","hcjeihch","bcgjaicfc","ceabfj","fdh","aijbifajh","ieicdhja","dedbaifddhideea","ahaci","hj","cbhcagg","fbbfddi","ehabiieifcbhagda","iiief","gbdiabgbabaccgef","afajjcjgfdjgjghjei","cbjiaecjgghc","agccjgcahcicacajia","fbjfebgffebdafhh","dcchgbaid","ddaadiedgcagie","ebjbb","gbbbidhgfjfcbccia","jjfaijbej","fhee","ah","bghbgjfbde","i","ijgbjccjcegigegjfdie","iafd","fbfacfhididac","hhhcghhd","ihccfiaefhffg","jjcf","heidahegjg","ihfcjgghchgdjc","icaiifjihjfhgjjej","bdfdjdegdee","icgei","eadagadcbhehadijahb","c","edcaee","gbjca","gcjajhe","fdaacegbcafdai","ceihdhceehdidada","djcjajgbgbihhi","eebdcfdg","fiijdjcb","efjfgjcaf","cfddbaagagdj","hegfd","bfchgee","aajffhd","gbgjbdbibjhfeiajffd","cgbedhhcjjab","iegbhaaecabcciicjbf","hiddhgbdifeg","figafefdijfheh","cjgb","ifjcdfdjddaeh","aiccbdfbiighcfbj","jb","fhgf","dhcgffeaijj","ajc","gdcfffjecefhgcja","aih","dehchjeaif","egcfeaiicebhah","cbdhhaehaef","ecceebcddeehh","iiafbdj","ahbegi","bibeihgehjjjjajaeeci","ehjccdajjdaediiijcfi","abieccdeihfiddfjde","jihhj","hbajbddaabifgcdb","ffbdfgcdgdfcdi","g","aiga","eaceeeeededee","bhhdiaebdbhba","igdjeicehcce","ihhbdjhidcfgf","fcc","bejghijjecfccd","efbgbi","ffhbcffbegagjdgj","de","giaigagfbj","jhiicdcjjb","hhbgeieacfgdgbgd","hbgaibjic","dagdciaddgdahgab","dcciigdcaih","becdagbgcfgfjfggbbf","gbd","ijhbgdbjgdcjig","edddfgaifbbea","iaidbeeddaecheg","haheicahbcdjfbahjj","cjcaeaaabjjdghh","jbaaefajacfb","jcbcaahe","edeideaichafeabcijf","ggbjbhhaacijfji","hbehhhfcgagaiehe","cbjcadaggeedacchd","cdfcegb","ihiiicahdh","hcehijaea","cedfjgbeafajef","ahhdfgjbh","bgjbdhjicecahccdg","hibehd","feefabggde","ahdcic","bchdbhdgjffgdiihfgdi","fjbbejijfecbdjehab","aeacjfcechi","hfcechceehdfjb","iifhhif","edghfgajae","fhaieieee","ijcaj","jfgbhdgbie","caaaihg","cjfbjcigbcejdbcha","igjdadcjgcibib","hgeaffiehjeajeichf","bhhcadjiebfibchh","fahhi","bfefhjaa","hgifjbajgeii","giebbjbgbdagea","ejigdbjddeec","jbacea","hhfihb","jhaaj","adeddbdagjacaej","ged","ecfjjdaaahbggedg","cfcihcbdgjiafa","eigjbahbgahgejihfe","bjgggcjha","cfafbibg","hjjhiihhh","ddg","icjidiic","f","febiajgg","geihfigdchidfgfgdjc","hgfac","ehfbg","aciabbedgacgabecahe","figdiafagffaidhgc","fjdcadhiaede","ejgaeddgdgidfjighaje","idji","hejceiccfee","hifif","debhdiee","fbjh","jhb","gihceeaahehfggahb","jbdeabg","iaijjcgjh","efibheehhgjggfj","gbcjagfifegdjf","fijjgjigdcacecgddhhd","gbicjcihdbid","jjfifcf","idhhia","eiccfhajeb","bbhgbfiddj","jejeacaghjbgdcihcec","bgciagggdf","giifiebcchfhedaggjj","hdhiajehagjgdahhahib","adbcc","edibeic","hi","febiagcihhicgefjd","ghdhbcheecc","bigacagci","icbbgcd","bbhccjeabjh","hejgdihgbfbficjbafg","ijbghfgfgjjej","ffeiggafaggcaaihehia","ghaeicjidfciifcha","eeaiijbcb","gbbdijafcca","fceb","cbb","jicjeaafbehgi","aea","eejcgfcbijjh","abbahgbfeecge","ffgbagdcjjjifee","caacfe","gabbjihbhiia","ejcjjjbbdabehcidfcjj","cbgfjgeiihje","d","bifg","efajiebahbdai","bddcdcfghgi","cejdccfa","iaaeabfigagbabihihda"]
        ,)
        outputs = (
            [[0, 1], [1, 0], [3, 2], [2, 4]],
            []
        ,)
        for i in range(1, len(inputs)):
            self.assertEqual(
                Solution().palindromePairs(inputs[i]),
                outputs[i]
            )
if __name__ == '__main__':
    unittest.main()
"""
