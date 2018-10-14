# Problem
Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with ```nc 2018shell1.picoctf.com 43324```.

## Hints:
NOTE: Flag is not in the usual flag format

## Solution:

This is just a simple substitution cipher.

Connect to the remote server and obtain ciphertext

```bash
nc 2018shell1.picoctf.com 43324

-------------------------------------------------------------------------------
nykfgsoc ezgz dc hylg vasf - clqcodolodyk_ndxezgc_sgz_cyamsqaz_rpzoovzcmk
-------------------------------------------------------------------------------
dk s mdaasfz yv as rsknes, oez ksrz yv pedne d esmz ky uzcdgz oy nsaa oy
rdku, oezgz admzu kyo aykf cdknz ykz yv oeycz fzkoazrzk oeso wzzx s asknz
dk oez asknz-gsnw, sk yau qlnwazg, s azsk esnw, sku s fgzheylku vyg
nylgcdkf. sk yaas yv gsoezg rygz qzzv oesk rlooyk, s csasu yk ryco
kdfeoc, cngsxc yk csolgushc, azkodac yk vgdushc, sku s xdfzyk yg cy zbogs
yk clkushc, rsuz spsh pdoe oegzz-tlsgozgc yv edc dknyrz. oez gzco yv do
pzko dk s uylqazo yv vdkz nayoe sku mzamzo qgzznezc sku ceyzc oy rsone
vyg eyadushc, pedaz yk pzzw-ushc ez rsuz s qgsmz vdflgz dk edc qzco
eyrzcxlk. ez esu dk edc eylcz s eylczwzzxzg xsco vygoh, s kdznz lkuzg
opzkoh, sku s asu vyg oez vdzau sku rsgwzo-xasnz, pey lczu oy csuuaz oez
esnw sc pzaa sc eskuaz oez qdaa-eyyw. oez sfz yv oedc fzkoazrsk yv ylgc
psc qyguzgdkf yk vdvoh; ez psc yv s esguh esqdo, cxsgz, fslko-vzsolgzu, s
mzgh zsgah gdczg sku s fgzso cxygocrsk. oezh pdaa esmz do edc clgksrz psc
tldbsus yg tlzcsus (vyg ezgz oezgz dc cyrz udvvzgzknz yv yxdkdyk srykf
oez sloeygc pey pgdoz yk oez clqjzno), saoeylfe vgyr gzscyksqaz
nykjznolgzc do czzrc xasdk oeso ez psc nsaazu tlzbsks. oedc, eypzmzg, dc
yv qlo adooaz drxygosknz oy ylg osaz; do pdaa qz zkylfe kyo oy cogsh s
esdg'c qgzsuoe vgyr oez ogloe dk oez ozaadkf yv do.

hyl rlco wkyp, oezk, oeso oez sqymz-ksrzu fzkoazrsk pezkzmzg ez psc so
azdclgz (pedne psc rycoah saa oez hzsg gylku) fsmz edrczav lx oy gzsudkf
qyywc yv nedmsagh pdoe clne sguylg sku smdudoh oeso ez saryco zkodgzah
kzfaznozu oez xlgcldo yv edc vdzau-cxygoc, sku zmzk oez rsksfzrzko yv edc
xgyxzgoh; sku oy clne s xdone udu edc zsfzgkzcc sku dkvsolsodyk fy oeso
ez cyau rskh sk sngz yv odaasfzasku oy qlh qyywc yv nedmsagh oy gzsu, sku
qgylfeo eyrz sc rskh yv oezr sc ez nylau fzo. qlo yv saa oezgz pzgz kykz
ez adwzu cy pzaa sc oeycz yv oez vsrylc vzadndsky uz cdams'c nyrxycdodyk,
vyg oezdg alndudoh yv cohaz sku nyrxadnsozu nyknzdoc pzgz sc xzsgac dk
edc cdfeo, xsgodnlasgah pezk dk edc gzsudkf ez nsrz lxyk nylgocedxc sku
nsgozac, pezgz ez yvozk vylku xsccsfzc adwz "oez gzscyk yv oez lkgzscyk
pdoe pedne rh gzscyk dc svvadnozu cy pzswzkc rh gzscyk oeso pdoe gzscyk d
rlgrlg so hylg qzsloh;" yg sfsdk, "oez edfe ezsmzkc, oeso yv hylg
udmdkdoh udmdkzah vygodvh hyl pdoe oez cosgc, gzkuzg hyl uzczgmdkf yv oez
uzczgo hylg fgzsokzcc uzczgmzc." ymzg nyknzdoc yv oedc cygo oez xyyg
fzkoazrsk ayco edc pdoc, sku lczu oy adz spswz cogdmdkf oy lkuzgcosku
oezr sku pygr oez rzskdkf ylo yv oezr; peso sgdcoyoaz edrczav nylau kyo
esmz rsuz ylo yg zbogsnozu esu ez nyrz oy advz sfsdk vyg oeso cxzndsa
xlgxycz. ez psc kyo so saa zsch sqylo oez pylkuc pedne uyk qzadskdc fsmz
sku oyyw, qznslcz do czzrzu oy edr oeso, fgzso sc pzgz oez clgfzykc pey
esu nlgzu edr, ez rlco esmz esu edc vsnz sku qyuh nymzgzu saa ymzg pdoe
czsrc sku cnsgc. ez nyrrzkuzu, eypzmzg, oez sloeyg'c psh yv zkudkf edc
qyyw pdoe oez xgyrdcz yv oeso dkozgrdksqaz sumzkolgz, sku rskh s odrz psc
ez ozrxozu oy oswz lx edc xzk sku vdkdce do xgyxzgah sc dc oezgz
xgyxyczu, pedne ky uylqo ez pylau esmz uykz, sku rsuz s clnnzccvla xdznz
yv pygw yv do oyy, esu kyo fgzsozg sku rygz sqcygqdkf oeylfeoc xgzmzkozu
edr.
```

Go to [https://quipqiup.com/](https://quipqiup.com/) and paste the cipertext, this website can almost solve this automatically.

We can use a simple "clues" there (in this puzzle: h=y m=v p=w), We get:

```
------------------------------------------------------------------------------- congrats here is your flag - substitution_ciphers_are_solvable_mwettfesvn ------------------------------------------------------------------------------- in a village of la mancha, the name of which i have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. an olla of rather more beef than mutton, a salad on most nights, scraps on saturdays, lentils on fridays, and a pigeon or so e?tra on sundays, made away with three-?uarters of his income. the rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays, while on week-days he made a brave figure in his best homespun. he had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place, who used to saddle the hack as well as handle the bill-hook. the age of this gentleman of ours was bordering on fifty; he was of a hardy habit, spare, gaunt-featured, a very early riser and a great sportsman. they will have it his surname was ?ui?ada or ?uesada (for here there is some difference of opinion among the authors who write on the sub?ect), although from reasonable con?ectures it seems plain that he was called ?ue?ana. this, however, is of but little importance to our tale; it will be enough not to stray a hair's breadth from the truth in the telling of it. you must know, then, that the above-named gentleman whenever he was at leisure (which was mostly all the year round) gave himself up to reading books of chivalry with such ardour and avidity that he almost entirely neglected the pursuit of his field-sports, and even the management of his property; and to such a pitch did his eagerness and infatuation go that he sold many an acre of tillageland to buy books of chivalry to read, and brought home as many of them as he could get. but of all there were none he liked so well as those of the famous feliciano de silva's composition, for their lucidity of style and complicated conceits were as pearls in his sight, particularly when in his reading he came upon courtships and cartels, where he often found passages like "the reason of the unreason with which my reason is afflicted so weakens my reason that with reason i murmur at your beauty;" or again, "the high heavens, that of your divinity divinely fortify you with the stars, render you deserving of the desert your greatness deserves." over conceits of this sort the poor gentleman lost his wits, and used to lie awake striving to understand them and worm the meaning out of them; what aristotle himself could not have made out or e?tracted had he come to life again for that special purpose. he was not at all easy about the wounds which don belianis gave and took, because it seemed to him that, great as were the surgeons who had cured him, he must have had his face and body covered all over with seams and scars. he commended, however, the author's way of ending his book with the promise of that interminable adventure, and many a time was he tempted to take up his pen and finish it properly as is there proposed, which no doubt he would have done, and made a successful piece of work of it too, had not greater and more absorbing thoughts prevented him.
```

Flag: substitution_ciphers_are_solvable_mwettfesvn
