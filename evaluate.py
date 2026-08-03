def evaluation_prompt(npc, text):
    return f"""

以下のNPC発言をBig Five人格モデルで評価してください。


NPC:
{npc}


発言:

{text}



1〜7で評価してください。


E:
A:
C:
N:
O:


"""