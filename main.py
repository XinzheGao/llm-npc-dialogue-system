import json
import os


from npc_personality import NPCS
from prompts import npc_prompt
from llm_api import generate
from config import *



os.makedirs(
"results",
exist_ok=True
)


results=[]



for model in MODELS:


    print(
    "MODEL:",
    model
    )


    for session in range(
        SESSION_NUM
    ):


        history=[]



        for turn in range(
            TURN_NUM
        ):


            for npc,personality in NPCS.items():


                prompt=npc_prompt(
                    npc,
                    personality,
                    history
                )



                text=generate(
                    model,
                    prompt
                )



                item={

                "model":model,

                "session":session,

                "turn":turn,

                "npc":npc,

                "text":text

                }



                results.append(item)



                history.append(

                npc+
                ":"+
                text

                )



                print(
                model,
                session,
                turn,
                npc
                )





with open(
"results/dialogue.json",
"w",
encoding="utf-8"
) as f:


    json.dump(
        results,
        f,
        ensure_ascii=False,
        indent=2
    )



print(
"Dialogue generation finished"
)