    for k in dico_lv1old :
        L1 = dico_lv1[k]
        if sup_usr in L1 :
            sup_lv1 = k
            LLV1 = dico_lv1[sup_lv1]
            LLV1.remove(sup_usr)
            del dico_lv1[sup_lv1]
            dico_lv1[sup_lv1] = LLV1
            bdd = 'data/data_lv1.txt'
            gen.save_valtuple (bdd, dico_lv1)

    # Suppression de l'utilisateur de la base data_LV2
    data_lv2=open('data/data_lv2.txt','r')
    dico_lv2 = gen.decoup_valtuple (data_lv2)
    dico_lv2old = gen.decoup_valtuple (data_lv2)
    data_lv2.close()
    for k in dico_lv2old :
        L2 = dico_lv2[k]
        if sup_usr in L2 :
            sup_lv2 = k
            LLV2 = dico_lv2[sup_lv2]
            LLV2.remove(sup_usr)
            del dico_lv2[sup_lv2]
            dico_lv2[sup_lv2] = LLV2
            bdd = 'data/data_lv2.txt'
            gen.save_valtuple (bdd, dico_lv2)

    # Suppression de l'utilisateur de la base data_SPE
    data_spe=open('data/data_spe.txt','r')
    dico_spe = gen.decoup_valtuple (data_spe)
    dico_speold = gen.decoup_valtuple (data_spe)
    data_spe.close()
    for k in dico_speold :
        LS = dico_spe[k]
        if sup_usr in LS :
            sup_spe = k
            LSPE = dico_spe[sup_spe]
            LSPE.remove(sup_usr)
            del dico_spe[sup_spe]
            dico_spe[sup_spe] = LSPE
            bdd = 'data/data_spe.txt'
            gen.save_valtuple (bdd, dico_spe)

    # Suppression de l'utilisateur (Professeur exclusivement) de la base data_com
    data_com=open('data/data_com.txt','r')
    dico_com = gen.decoup_valtuple (data_com)
    dico_comold = gen.decoup_valtuple (data_com)
    data_com.close()
    for k in dico_comold :
        LC = dico_com[k]
        if sup_usr in LC :
            LCOM = dico_com[sup_com]
            LCOM.remove(sup_usr)
            del dico_com[sup_com]
            dico_com[sup_com] = LCOM
            bdd = 'data/data_com.txt'
            gen.save_valtuple (bdd, dico_com)

