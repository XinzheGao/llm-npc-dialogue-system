import math



def distance(
target,
generated
):


    sum=0


    for key in [
        "E",
        "A",
        "C",
        "N",
        "O"
    ]:


        diff=(
        target[key]
        -
        generated[key]
        )


        sum+=diff**2



    return math.sqrt(sum)