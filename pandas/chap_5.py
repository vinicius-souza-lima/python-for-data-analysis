#%%
import pandas as pd
#%%
obj = pd.Series([4,7,-5,3])
# %%
obj.array
# %%
obj2 = pd.Series([4,7,-5,3], index = ["d","b","a","c"])
# %%
obj2["a"]
# %%
obj2["d"] = 6
# %%
obj2[["c","a","d"]]