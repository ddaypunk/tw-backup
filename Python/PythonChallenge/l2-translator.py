import string
#below creates two lists for a FROM and TO cipher
# from is a-z, to is c-a (loops around)
alpha_from = string.ascii_lowercase
alpha_to = string.ascii_lowercase[2:]+string.ascii_lowercase[:2]
orig_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. \
             rfyrq ufyr amknsrcpq ypc dmp. bmgle gr \
             gl zw fylb gq glcddgagclr ylb rfyr'q ufw \
             rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() \
             gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#create the translation table             
trans_table = string.maketrans(alpha_from,alpha_to)

#translate the orig_text into plain words
trans_text = string.translate(orig_text,trans_table)

print trans_text