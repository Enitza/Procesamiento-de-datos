import numpy as np
import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
edades = np.array(data["age"])
promedio_edad = np.mean(edades)

print("Promedio de edad es:", promedio_edad)

##Parte 2

df = pd.DataFrame(data)

perecieron = df[df['is_dead'] == 1]
no_perecieron = df[df['is_dead'] == 0]

promedio_edad_dead = perecieron['age'].mean()
promedio_edad_not_dead = no_perecieron['age'].mean()

print("Promedio edad de las personas que perecieron:", promedio_edad_dead)
print("Promedio edad de las personas que NO perecieron:", promedio_edad_not_dead)

