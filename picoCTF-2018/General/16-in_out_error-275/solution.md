# Problem
Can you utlize stdin, stdout, and stderr to get the flag from this [program](https://2018shell1.picoctf.com/static/0ca075b3119417f95a13236d763b4b50/in-out-error)? You can also find it in /problems/in-out-error_2_c33e2a987fbd0f75e78481b14bfd15f4 on the shell server

## Hints:
Maybe you can split the stdout and stderr output?

## Solution:

First, we download the file and try to execute it
```bash
wget https://2018shell1.picoctf.com/static/0ca075b3119417f95a13236d763b4b50/in-out-error
chmod +x ./in-out-error
./in-out-error

Hey There!
If you want the flag you have to ask nicely for it.
Enter the phrase "Please may I have the flag?" into stdin and you shall receive.
Please may I have the flag?
Thank you for asking so nicely!

pWiec'orCeT Fn{op 1spt1rnagn_g1eSr_s4 _t7oh 1lnogv_eb
6Yfo5ua 7k8n8o}wp itchoeC TrFu{lpe1sp 1anngd_ 1sSo_ 4d_o7 hI1
nAg _fbu6lfl5 ac7o8m8m}iptimceonCtT'Fs{ pw1hpa1tn gI_'1mS _t4h_i7nhk1inngg_ bo6ff
5Yao7u8 8w}opuilcdonC'TtF {gpe1tp 1tnhgi_s1 Sf_r4o_m7 ha1nnyg _obt6hfe5ra 7g8u8y}
p
iIc ojCuTsFt{ pw1apn1nnag _t1eSl_l4 _y7ohu1 nhgo_wb 6If'5ma 7f8e8e}lpiincgo
CGToFt{tpa1 pm1ankge_ 1ySo_u4 _u7nhd1enrgs_tba6nfd5
a
7N8e8v}epri cgooCnTnFa{ pg1ipv1en gy_o1uS _u4p_
7Nhe1vnegr_ bg6ofn5naa7 8l8e}tp iycoouC TdFo{wpn1
pN1envge_r1 Sg_o4n_n7ah 1rnugn_ ba6rfo5uan7d8 8a}npdi cdoeCsTeFr{tp 1ypo1un
gN_e1vSe_r4 _g7ohn1nnag _mba6kfe5 ay7o8u8 }cpriyc
oNCeTvFe{rp 1gpo1nnnga_ 1sSa_y4 _g7oho1dnbgy_eb
6Nfe5vae7r8 8g}opnincao CtTeFl{lp 1ap 1lnige_ 1aSn_d4 _h7uhr1tn gy_obu6
f
5Wae7'8v8e} pkincoowCnT Fe{apc1hp 1ontgh_e1rS _f4o_r7 hs1on gl_obn6gf
5Yao7u8r8 }hpeiacrotC'TsF {bpe1epn1 nagc_h1iSn_g4,_ 7bhu1tn
gY_obu6'fr5ea 7t8o8o} psihcyo CtToF {spa1yp 1intg
_I1nSs_i4d_e7,h 1wneg _bbo6tfh5 ak7n8o8w} pwihcaotC'TsF {bpe1epn1 nggo_i1nSg_ 4o_n7
hW1en gk_nbo6wf 5tah7e8 8g}apmiec oaCnTdF {wpe1'pr1en gg_o1nSn_a4 _p7lha1yn gi_tb
6
fA5nad7 8i8f} pyiocuo CaTsFk{ pm1ep 1hnogw_ 1IS'_m4 _f7ehe1lnign_gb
6Dfo5na'7t8 8t}eplilc omCeT Fy{opu1'pr1en gt_o1oS _b4l_i7nhd1 ntgo_ bs6efe5
a
7N8e8v}epri cgooCnTnFa{ pg1ipv1en gy_o1uS _u4p_
7Nhe1vnegr_ bg6ofn5naa7 8l8e}tp iycoouC TdFo{wpn1
pN1envge_r1 Sg_o4n_n7ah 1rnugn_ ba6rfo5uan7d8 8a}npdi cdoeCsTeFr{tp 1ypo1un
gN_e1vSe_r4 _g7ohn1nnag _mba6kfe5 ay7o8u8 }cpriyc
oNCeTvFe{rp 1gpo1nnnga_ 1sSa_y4 _g7oho1dnbgy_eb
6Nfe5vae7r8 8g}opnincao CtTeFl{lp 1ap 1lnige_ 1aSn_d4 _h7uhr1tn gy_obu6
f
5Nae7v8e8r} pgiocnonCaT Fg{ipv1ep 1ynogu_ 1uSp_
4N_e7vhe1rn gg_obn6nfa5 al7e8t8 }ypoiuc odCoTwFn{
pN1epv1enrg _g1oSn_n4a_ 7rhu1nn ga_rbo6ufn5da 7a8n8d} pdiecsoeCrTtF {ypo1up
1Nnegv_e1rS _g4o_n7nha1 nmga_kbe6 fy5oau7 8c8r}yp
iNceovCeTrF {gpo1npn1an gs_a1yS _g4o_o7dhb1yneg
_Nbe6vfe5ra 7g8o8n}npai ctoeClTlF {ap 1lpi1en ga_n1dS _h4u_r7th 1ynogu_
b(6Ofo5ha,7 8g8i}vpei cyooCuT Fu{pp)1
p(1Onogh_,1 Sg_i4v_e7 hy1onug _ubp6)f
5Nae7v8e8r} pgiocnonCaT Fg{ipv1ep,1 nnge_v1eSr_ 4g_o7nhn1an gg_ibv6ef
5(aG7i8v8e} pyiocuo CuTpF){
pN1epv1enrg _g1oSn_n4a_ 7ghi1vneg,_ bn6efv5ear7 8g8o}npniac ogCiTvFe{
p(1Gpi1vneg _y1oSu_ 4u_p7)h
1
nWge_'bv6ef 5kan7o8w8n} peiaccohC ToFt{hpe1rp 1fnogr_ 1sSo_ 4l_o7nhg1
nYgo_ubr6 fh5eaa7r8t8'}sp ibceoeCnT Fa{cph1ipn1gn,g _b1uSt_
4Y_o7uh'1rneg _tbo6of 5sah7y8 8t}op iscaoyC TiFt{
pI1nps1indge_,1 Sw_e4 _b7oht1hn gk_nbo6wf 5wah7a8t8'}sp ibceoeCnT Fg{opi1npg1 nogn_
1WSe_ 4k_n7ohw1 ntgh_eb 6gfa5mae7 8a8n}dp iwceo'CrTeF {gpo1npn1an gp_l1aSy_ 4i_t7
h
1In gj_ubs6tf 5waa7n8n8a} ptieclolC TyFo{up 1hpo1wn gI_'1mS _f4e_e7lhi1nngg
_Gbo6tft5aa 7m8a8k}ep iycoouC TuFn{dpe1rps1tnagn_d1
S
_N4e_v7ehr1 nggo_nbn6af 5gai7v8e8 }ypoiuc ouCpT
FN{epv1epr1 nggo_n1nSa_ 4l_e7th 1ynogu_ bd6ofw5na
7N8e8v}epri cgooCnTnFa{ pr1upn1 nagr_o1uSn_d4 _a7nhd1 ndge_sbe6rft5 ay7o8u8
}NpeivceorC TgFo{npn1ap 1mnagk_e1 Sy_o4u_ 7chr1yn
gN_ebv6efr5 ag7o8n8n}ap iscaoyC TgFo{opd1bpy1en
gN_e1vSe_r4 _g7ohn1nnag _tbe6lfl5 aa7 8l8i}ep iacnodC ThFu{rpt1 py1onug
_
1NSe_v4e_r7 hg1onngn_ab 6gfi5vae7 8y8o}up iucpo
CNTeFv{epr1 pg1onngn_a1 Sl_e4t_ 7yho1un gd_obw6nf
5Nae7v8e8r} pgiocnonCaT Fr{upn1 pa1rnogu_n1dS _a4n_d7 hd1ensge_rbt6 fy5oau7
8N8e}vpeirc ogCoTnFn{ap 1mpa1kneg _y1oSu_ 4c_r7yh
1Nnegv_ebr6 fg5oan7n8a8 }spaiyc ogCoToFd{bpy1ep
1Nnegv_e1rS _g4o_n7nha1 ntge_lbl6 fa5 al7i8e8 }apnidc ohCuTrFt{ py1opu1
n
gN_e1vSe_r4 _g7ohn1nnag _gbi6vfe5 ay7o8u8 }uppi
cNoeCvTeFr{ pg1opn1nnag _l1eSt_ 4y_o7uh 1dnogw_nb
6Nfe5vae7r8 8g}opnincao CrTuFn{ pa1rpo1unngd_ 1aSn_d4 _d7ehs1enrgt_ by6ofu5
aN7e8v8e}rp igcoonCnTaF {mpa1kpe1 nygo_u1 Sc_r4y_
7Nhe1vnegr_ bg6ofn5naa7 8s8a}yp igcoooCdTbFy{ep
1Npe1vnegr_ 1gSo_n4n_a7 ht1enlgl_ ba6 fl5iae7 8a8n}dp ihcuorCtT Fy{opu1
p
```

A lot of stuff, the hint say to split stdout and stderr.

```bash
echo "Please may I have the flag?" | ./in-out-error 2 > /dev/null

Please may I have the flag?
picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p
```

No idea what's went wrong, but we got the flag.

Flag: picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}