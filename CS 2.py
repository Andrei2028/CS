from collections import Counter
import string

# The intercepted message
ciphertext = """Odixgj tss wqvpv fvtip, hifuwnsnjf rtp thbdxixgj t wtxgw wqtw sxgjvipvkvg wnotf—wqv
hngkxhwxng xg wqv zxgop nc ztgf uvnusv wqtw hifuwnsnjfxp t asthl tiw, t cniz nc nhhdswxpz rqnpv
uithwxwxngvi zdpw, xg Rxssxtz C.Cixvoztg'p tuw uqitpv, "uvicnihv hnzzdgv otxsf rxwq otil puxixwp
wnthhnzusxpq qxp cvtwp nc zvgwts exd-exwpd."Xg utiw xw xp t lxgo nc jdxsw af tppnhxtwxng.
Cinz wqv vtisf otfp nc xwpvyxpwvghv, hifuwnsnjf qto pvikvo wn naphdiv hixwxhts uniwxngp nc
rixwxgjpovtsxgj rxwq wqv unwvgw pdaevhw nc ztjxh—oxkxgtwxngp, puvssp, hdipvp,rqtwvkvi
hngcviivo pduvigtwdits unrvip ng xwp pnihvivip. Tgnwqvixzuniwtgw cthwni rtp wqv hngcdpxng nc
hifuwnsnjf rxwq wqv Evrxpqltaatstq.Adw, xzuniwtgw tp tss wqvpv rviv, wqv kxvr wqtw hifuwnsnjf
xp asthlztjxh xg xwpvsc puixgjp dswxztwvsf cinz t pduvicxhxts ivpvzastghv avwrvvghifuwnsnjf tgo
oxkxgtwxng. Vywithwxgj tg xgwvssxjxasv zvpptjv cinzhxuqviwvyw pvvzvo wn av vythwsf wqv ptzv
wqxgj tp nawtxgxgj lgnrsvojvaf vytzxgxgj wqv csxjqw nc axiop, wqv snhtwxng nc pwtip tgo
ustgvwp, wqvsvgjwq tgo xgwvipvhwxngp nc sxgvp xg wqv qtgo, wqv vgwitxsp nc pqvvu,
wqvunpxwxng nc oivjp xg t wvthdu. Xg tss nc wqvpv, wqv rxmtio-sxlv nuvitwnioitrp pvgpv cinz
jinwvpbdv, dgctzxsxti, tgo tuutivgwsf zvtgxgjsvpppxjgp. Qv ztlvp lgnrg wqv dglgnrg.Tss wqxp
pwtxgvo hifuwnsnjf pn ovvusf rxwq wqv otil qdvp nc vpnwvixpzwqtw pnzv nc wqvz pwxss uvipxpw,
gnwxhvtasf hnsnixgj wqv udasxh xztjv nchifuwnsnjf. Uvnusv pwxss wqxgl hifuwtgtsfpxp
zfpwvixndp. Annl ovtsvip pwxsssxpw hifuwnsnjf dgovi "nhhdsw." Tgo xg 1940 wqv Dgxwvo
Pwtwvp hngcviivodung xwp Etutgvpv oxusnztwxh hifuwtgtsfpvp wqv hnovgtzv ZTJXH. Xg gngv nc
wqv pvhivw rixwxgj wqdp cti rtp wqviv tgf pdpwtxgvohifuwtgtsfpxp. Nhhtpxngts htpvp, fvp. Adw
nc tgf phxvghv nc hifuwtgtsfpxp,wqviv rtp gnwqxgj. Ngsf hifuwnjituqf vyxpwvo. Tgo wqvivcniv
hifuwnsnjf,rqxhq xgknskvp anwq hifuwnjituqf tgo hifuwtgtsfpxp, qto gnw fvw hnzv xgwn avxgj pncti
tp tss wqvpv hdswdivp—xghsdoxgj wqv Rvpwvig —rviv hnghvigvo.Hifuwnsnjf rtp anig tzngj wqv
Titap. Wqvf rviv wqv cxipw wn oxphnkvitgo rixwv onrg wqv zvwqnop nc hifuwtgtsfpxp. Wqv
uvnusv wqtw vyusnovondw nc Titaxt xg wqv 600p tgo cstzvo nkvi ktpw tivtp nc wqv lgnrg
rnisoprxcwsf vgjvgovivo ngv nc wqv qxjqvpw hxkxsxmtwxngp wqtw qxpwnif -qto fvwpvvg.
Phxvghv csnrvivo. Tita zvoxhxgv tgo ztwqvztwxhp avhtzv wqv avpwxg wqv rniso—cinz wqv
stwwvi, xg cthw, hnzvp wqv rnio "hxuqvi." Uithwxhtstiwp csndixpqvo. Tozxgxpwitwxkv
wvhqgxbdvp ovkvsnuvo. Wqv vydavitgwhivtwxkv vgvijxvp nc pdhq t hdswdiv, vyhsdovo af xwp
ivsxjxng cinz utxgwxgjni phdsuwdiv, tgo xgpuxivo af xw wn tg vyusxhtwxng nc wqv Qnsf
Lnitg,undivo xgwn sxwvitif udipdxwp. Pwnifwvssxgj, vyvzusxcxvo af Pqvqvitmtov'pWqndptgo tgo
Ngv Gxjqwp, rnio-ixoosvp, ivadpvp, udgp, tgtjitzp, tgopxzxsti jtzvp tandgovo; jitzzti avhtzv t zteni
pwdof. Tgo xghsdovortp pvhivw rixwxgj.Tcwvi vyustxgxgj wqtw ngv ztf rixwv xg tg dglgnrg stgjdtjv
wn nawtxgpvhivhf, Xag to-Oditxqxz, thhnioxgj wn Btsbtpqtgox, jtkv pvkvg pfpwvzpnc hxuqvip.
Wqxp sxpw vghnzutppvo, cni wqv cxipw wxzv xg hifuwnjituqf, anwqwitgpunpxwxng tgo
pdapwxwdwxng hxuqvip. Znivnkvi, ngv pfpwvz xp wqv cxipwlgnrg hxuqvi vkvi wn uinkxov zniv
wqtg ngv pdapwxwdwv cni t ustxgwvywsvwwvi. Ivztiltasv tgo xzuniwtgw tp wqxp xp, qnrvkvi, xw
xp nkvipqtonrvo af rqtw cnssnrp— wqv cxipwvyunpxwxng ng hifuwtgtsfpxp xg qxpwnif"""


# Function to perform frequency analysis
def frequency_analysis(text):
    text = text.lower()
    # Count the frequency of each letter (ignore non-letter characters)
    frequency = Counter(c for c in text if c in string.ascii_lowercase)
    return frequency.most_common()


# Function to create a decryption map based on English letter frequencies
def create_decryption_map(cipher_freq):
    english_freq = "etaoinshrdlcumwfgypbvkjxqz"  # Common letters in English sorted by frequency
    decryption_map = {}

    for (cipher_char, _), eng_char in zip(cipher_freq, english_freq):
        decryption_map[cipher_char] = eng_char

    return decryption_map


# Function to decrypt the message
def decrypt_message(ciphertext, decryption_map):
    decrypted_message = []
    for char in ciphertext:
        if char.lower() in decryption_map:
            # Replace char based on decryption map, maintain case
            new_char = decryption_map[char.lower()]
            if char.isupper():
                new_char = new_char.upper()
            decrypted_message.append(new_char)
        else:
            decrypted_message.append(char)  # Non-letter characters remain the same
    return ''.join(decrypted_message)


# Perform frequency analysis on the ciphertext
cipher_frequency = frequency_analysis(ciphertext)
# Create a decryption map
decryption_map = create_decryption_map(cipher_frequency)
# Decrypt the message
decrypted_message = decrypt_message(ciphertext, decryption_map)

# Display the decrypted message
print(decrypted_message)
