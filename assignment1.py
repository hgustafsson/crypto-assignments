__version__ = "1.0"

from IPython import get_ipython
from IPython.display import display, Markdown, HTML
import hashlib, random, re, collections, itertools
from sage.plot.graphics import Graphics


from sage.all import *

Graphics.SHOW_OPTIONS.update({
    'dpi': 100,
    'figsize': (8,4),
})



def sha(x):
    return int(hashlib.sha256(repr(x).encode()).hexdigest(),16)

def selection(salt, ID, lst):
    return lst[sha(ID + salt) % len(lst)]

class Exercise1():

    def _repr_markdown_(self):
        return fr"For the folloing exercise the user **{self.parent.ID}** should use: $n = {self.n}$, $a = {self.a}$ and the ciphertext `{self.ciphertext}` stored in the variables `e1.n`, `e1.a` and `e1.ciphertext`"
    
    def __init__(self, parent):
        self.parent = parent
        ID = parent.ID

        self.n = selection("e1_n", ID, list(map(Integer, [14,15,16,18,20,22,24])))
        self.a = selection("e1_a", ID, Zmod(self.n).list_of_elements_of_multiplicative_group()[1:-1])
        self.ciphertext = selection("e1_cipher", ID, ['MRMZGYCMGQKTHMFM',
                                                     'YVYLMWEYMGUZBYXY',
                                                     'OJOBUCYOUKQHTOVO',
                                                     'FVYCYCACMGZMFKMCCASM',
                                                     'QSWPOPOREHUARTSF',
                                                     'KYCCYQNAGGQKTHYCVMJ',
                                                     'ISRRHYNSEYMQYRXSHKB',
                                                     'YVMYBBYNXBOFGNY',
                                                     'SMOOMINAQQISDXMORGL',
                                                     'MUKVEVEDQPCADLUH',
                                                     'VFCYCYAYOUBOVQOYYAIO',
                                                     'JRMOMOAOGQTGJSGOOAWG',
                                                     'KYCCYQNAGGQKTHYCVMJ',
                                                     'KQFFZENQSECUEFTQZGL',
                                                     'LPGUGUAUQIDQLWQUUAYQ',
                                                     'UQIJYJYFSZMAFBQD',
                                                     'LPQLDQAUCDQGUHECNZ',
                                                     'PLKPXKAGYXKUGTWYNB',
                                                     'SECZGZGLYDQALXER',
                                                     'SIJJTCNIWCOKCJDITQZ',
                                                     'GPGTQMOGQISDXGJG',
                                                     'KYCCYQNAGGQKTHYCVMJ',
                                                     'GKSRCRCVIBOAVZKX',
                                                     'EYMHKHKBOFSABVYL',
                                                     'ISRRHYNSEYMQYRXSHKB',
                                                     'KZKXSUGKSWEFVKPK',
                                                     'XDYXLYAEQLYWERGQNF',
                                                     'CFCPOEWCOUGBZCDC',
                                                     'IOMMOSNAKKSIXDOMJUP',
                                                     'GKSRCRCVIBOAVZKX',
                                                     'OMHHJQNMUQICQHLMJYF',
                                                     'RJOMOMAMUKHURIUMMAEU',
                                                     'VFCYCYAYOUBOVQOYYAIO',
                                                     'YQKKQCNAEECYRJQKBIT',
                                                     'IHEIJJINZJWTCNI',
                                                     'XDWEWEAEYMLYXUYEEAKY',
                                                     'KZKXSUGKSWEFVKPK',
                                                     'EVWRZCMVARBWECOVKI',
                                                     'OJOBUCYOUKQHTOVO',
                                                     'GUDDPSNUQSWMSDBUPOR'])
        
class Exercise2():
    def _repr_markdown_(self):
        return f"For the folloing exercise the user **{self.parent.ID}** should use: the function `e2.coin_toss()` to simulate unfair coin tosses showing `H` with probability $p = {self.p}$ and `T` with probability $1-p$."
    
    def __init__(self, parent):
        self.parent = parent
        ID = parent.ID

        self.p = selection("e2_p", ID, [1/Integer(3),1/Integer(4),2/Integer(5),3/Integer(5),3/Integer(4),4/Integer(5)])

    def coin_toss(self):
        if random() < self.p:
            return "H"
        else:
            return "T"

class Exercise3():

    def _repr_markdown_(self):
        return fr"For the folloing exercise the user **{self.parent.ID}** should break the ciphertext stored in the variable `e3.ciphertext`"

    
    def __init__(self, parent):
        self.parent = parent
        ID = parent.ID

        self.ciphertext = selection("e3_cipher", ID, ['OPMWCRYXQDNYFPHXXTAIPPLIETJLGCMGCYVIXPLCFTZJKNOPVEIFTPUODFNXJPSETPHSVFHFTPUOCMFICDGEPJZMTDNXJZOKJECJAZOYUPMSOPWPGGYVUEUXKDNMEDCXKDJSUDCFNPNSHTLWVROIUDNLGVYCNPHKVSOWKYAXJPCRFPRSHNIMPNCHGYWIQYWIAZOOPZQXJPEIAWYRIEBCQFWEPNIQRLLIFTZJGCYRVDOFUELMPRMGQCLIUAIRFTHKVZXMHQYVGYNPGENITDCRVSYOGJQMVSNLGXOXWLFMPOYBQQWSKYWMFPHGGACGMTHKVSYGCDYWYSYVGEBMUTHHGICWNLLKGHCPNRCZGJIYEWOIULVSWELINLNMXPMLKQNWDPNAGPHHKQZITPHXNPNXGCMMPEBIMPSAQCXCQFQMNWNLGYBEXPNSUZFZGLMCUEYQQQYUWLNMQYMXQZVXCTHXJPMLKQNWCYXLQAYJWWFCAZOAKWFRQEBEXPUGQYXMVTIRVSUXKDQVQYAFWECXELHLCAJIPDIQGECQGDCLQAYCQFLICONLGTHWVCOGVTIRULHHWDYHVSYFWTFXKYZYPNNMQYUPKESMPDUKGEIWQWPINTHICCMCUEYQUZZISFUXKZHWVSYVGHCPNMYEVWYEUEIRGFHOPZQRUSCJVMOXKQCXKDIRNJIRGTNMUAIWUTVPGEIXTJUPNAIWUTVMNTNMGDIVVZOWGQLISFYRALHENJMMUTZCQFWEPYIATPUHVSCWVPRXAZOLCGYHQYYEXPLCIZIHLZVEPOWSOAFIVPXXJTMHKQZMEFFXVLMOXPLCYPFPFZHI',
 'YEYACSEZWUFUJMPFVOOGZEXMEUPNMTECGVDQVKZAPILNKOURBVABXMCWBABVTEEITQNUBWZBXMCWAHTGMSSIPKFOZUFTNWWSHZQHKOACUQSUUGOLKDGDSZIVUSZQEEIZQUBOYAKNLKBQRIXAVSUKAUFHKSGKLKVIFHAAKZGZPGUNJMZAFIWKZCOLGZCKWPOEEWWWNUEVTEQMAXETOVTYUCEMNIWOBAXMFUFLMTQNZAWNSZZKZGYKQDRKARANJQPSTULKRFKZGZTRMVFEXAKZTNMMQYCQVTTNMOGTAINUNJMZAFIWKZCOLGZCKXKOKOVIFHKKCEEYEJQRKBJUSOVFQXOANMRMMYULROKHEEWWOLAMUMBUCVDERIVUVKAJUFZADQTCMGZDONHQRKVVXEZBGDSOVVTEQMAIOXLAAUCQNXTNMPTABMVASUTXQAYGUFESWHQQAIVUOTAVAOHBCUNZPGEHONVEATLJAPKNWXLEGQGWOTNZOZPCHEGKQZDOBKANZPCFIYETANMJWFIZKCZHGXRQNYWOQTOUGEINWRQYUCTQAJBJQITAVDUIBKANYIPPUYMFFHKJWULZQPRUTKVUOTINUTEQPEAMMVASUTXQLOVGMRYGUFESAQREWCCFIUVUFHKZGIIRTDQAZTGMSZWPQUTSPAWTAJUFZJWFILQVUSUVNKOTMKFIYXQESOJNQTUBTKARTRASYQDULOBKQSUZVAUYMHDEWCGZYGVCXYYQUUFEWWOATVQIRKIFFHOAVQXZGQGHGDGPOTMCHEXGIAOJRQNATLEAMVTGFEJBJUSJQHRIICNFTGAMHEXGYQLRLQZE',
 'PVSYOTHKOYHHGVNZJVJVNKFRFZPNSEVTATPRYVRERVIWIIIYWKOHFRDBBAHGKVYGFRQFTABOUVAQOOOVAYANQPFOFFWKHUITKKILMBXLSKGBPVCRSIHISZOGLJTOQFLKIYDBVJIHZRWFFOFFWXUKGFWYEQSLOVNMHUXJITUGKVITRRAFFICVQTIJSAFVOTQRBFUQBBZKHKYRBCETUGKPOAQNQTOSDNUVDOTSHIETHFXSSZFVQXSICEUVSVCAGZNMHBGZFLSEHETRSGWVRYWAWYEQSLZZTNHUHDUZINOZNJSKRWCUWAFZDKBPHGIIYVQXTNSPDJEYKUHIEZVVVZNJSKLJLGFTHNIRZTLMEECHFCUKGNEFUZFRORTOJRVYILHFEVTCSRQUILTRUVNZZRWKEXGVQKHKYRBNOXRLRLWOZYWYETVNYVTUGBOMEGGLVKESCSHHUGHVRESZCBEKAOBGKVSNWSWJATRURGELIYOPYUIJLCLTCGKRVKOPREDOHVRETNOGLJWXCAJSUZWGFRNNOCSVNYCZHKISSFLYOVSLRLRKOQWYEOBFWIUIHVRESGBQXJEJHUHSUOZGLEFABPWZOTOYLKYOBFDXEZCFRCVKZVQVAXGLVKESGBIVQAOGLFNYHUHIECWYOSEGHYHRSZCAHLNQBBZESNWSWSUZWSLKIYCAOPOTSVWZSVCFVZBRSGRKREOYOGOYGVEZLOHVHJOXHBXJELFRTLETMNQRLEGVVZFECHFRNTCJUVAJHULJTKLGBFUNOIHUOTSNYVREUBRUJUPNQUCUACOVTKRGKZSJWSIZCAZGWRSQJRUPWKZYGFNK',
 'SSDVGUPWUGEXJSYWBWRHTSCHIWAKKFDFGBMHBSCBJWQIOQFOZHZEXSLNHIEWNSJDXSYRZIYEXSLNGPWHGGXDTMQLXGEWNCFJNHTIECFXYSDRSSNOKJPUYHLWOGELIGTWOGARYGTERSERLWCVZUFHYGEKKYPBRSYJZVFVOBRWNSTQJSIRLQZLTQTGKBNHUBNHECFNTCHWNSVHEZPQMHSBUINDTQZPVOCHJWQIKFPQZGFEYHCLTUDFUFCHYDZQJWYJZCOLLTPUKBEOKHEHXGTQZVPNKMHLZVEKKAFWAOWLTRPAUTNROBNLJSYFKDTFQWYJZVPFGGPVCVPUKHSLYWYGKLTVROCJKKTORUTYKMZXIZFHYOMRAHCHROELBSDKOTEVHSEZKSYGOTQHXSYWRSEWKFDLTHSHQSJZUFOBUIHLRZEKKBSDBSERYCWYKODBYHPPUTPTAOELUBDWUCMWGWYWNSDKOTEVGBOKUDPIAZWBECFZOZWQUHSDBSLFUBOLZWZQZVLWOGHUUBREAHTWIOYKGDAHTGZPKHTPKGTKUDPBUICHGREKKWYVZFFFZWZQYOYGAGPGZVPEAWWWOBQXTQELUBLOOHJLTGLJKHZVUZGHRWYHGFDBYHPPYCQHWILWOCYVZVPUKKTORPPDZZPDYHZQKIYNTCHQYVTIZPFWOTTWOGZQRMZQKWELYDZVYWMOKHZWXMLORDZVYWMLRWELKGZUZCFVKTCHWIPQEOYDRMDLYWQBUINDTBZZXSLGZVTVZSIWECFKGJPGUBPDBSCBMCZGPCMDTRNRSDWHZSOWNWDGOTQLIIWWZODNBSCBCSWOJCYH']) 


class Assignment1():    
    def __init__(self, ID):
        self.ID = ID

        self.exercise1 = Exercise1(self)
        self.exercise2 = Exercise2(self)
        self.exercise3 = Exercise3(self)

        display(HTML("""
        <style>
            @media print {
                body {
                    zoom: 0.75;
                }
                pre {
                  white-space: pre-wrap;
                  overflow-wrap: anywhere;
                  word-break: break-word;
                }
            }
        </style>""" + f"Module version: {__version__}</br>User ID: <b>{ID}</b>"))
        


