def generate(
model,
prompt
):


    if model=="deepseek":

        return deepseek(prompt)


    elif model=="gemini":

        return gemini(prompt)


    elif model=="claude":

        return claude(prompt)