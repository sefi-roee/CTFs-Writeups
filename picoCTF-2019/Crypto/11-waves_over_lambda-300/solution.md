# Problem
We made alot of substitutions to encrypt this. Can you decrypt it? Connect with nc 2019shell1.picoctf.com 12288.

## Hints:

Flag is not in the usual flag format

## Solution:

Let's connect:
```bash
nc 2019shell1.picoctf.com 12288

-------------------------------------------------------------------------------
ezugplsn yrpr jn vzxp bolg - bprkxruev_jn_e_zarp_olwfql_qpswsuqqot
-------------------------------------------------------------------------------
ylajug ylq nzwr sjwr ls wv qjniznlo tyru ju ozuqzu, j ylq ajnjsrq syr fpjsjny wxnrxw, luq wlqr nrlpey lwzug syr fzzmn luq wlin ju syr ojfplpv prglpqjug splunvoalujl; js ylq nspxem wr syls nzwr bzprmuztorqgr zb syr ezxuspv ezxoq ylpqov bljo sz ylar nzwr jwizpsluer ju qrlojug tjsy l uzforwlu zb syls ezxuspv. j bjuq syls syr qjnspjes yr ulwrq jn ju syr rcsprwr rlns zb syr ezxuspv, dxns zu syr fzpqrpn zb syprr nslsrn, splunvoalujl, wzoqlajl luq fxmzajul, ju syr wjqns zb syr elpilsyjlu wzxusljun; zur zb syr tjoqrns luq orlns muztu izpsjzun zb rxpzir. j tln uzs lfor sz ojgys zu luv wli zp tzpm gjajug syr rcles ozelojsv zb syr elnsor qplexol, ln syrpr lpr uz wlin zb syjn ezxuspv ln vrs sz ezwilpr tjsy zxp ztu zpquluer nxparv wlin; fxs j bzxuq syls fjnspjsh, syr izns sztu ulwrq fv ezxus qplexol, jn l bljpov troo-muztu ioler. j nyloo rusrp yrpr nzwr zb wv uzsrn, ln syrv wlv prbprny wv wrwzpv tyru j slom zarp wv splaron tjsy wjul.
```

As the hint suggests, this is a substitution cipher. Let's use some [online solver](https://www.guballa.de/substitution-solver), we get:
```bash
congrats here is your flag - frequency_is_c_over_lambda_drtmtnddlw
-------------------------------------------------------------------------------
having had some time at my disposal when in london, i had visited the british museum, and made search among the books and maps in the library regarding transylvania; it had struck me that some foreknowledge of the country could hardly fail to have some importance in dealing with a nobleman of that country. i find that the district he named is in the extreme east of the country, just on the borders of three states, transylvania, moldavia and bukovina, in the midst of the carpathian mountains; one of the wildest and least known portions of europe. i was not able to light on any map or work giving the exact locality of the castle dracula, as there are no maps of this country as yet to compare with our own ordnance survey maps; but i found that bistritz, the post town named by count dracula, is a fairly well-known place. i shall enter here some of my notes, as they may refresh my memory when i talk over my travels with mina.
```

Simple :)

Flag: frequency_is_c_over_lambda_drtmtnddlw
