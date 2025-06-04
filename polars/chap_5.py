#%%
import polars as pl
#%%
obj = pl.Series([4,7,-5,3])
# %%
obj
# %%
obj2 = pl.DataFrame(obj).with_columns(
    pl.Series(["d","b","a","c"]).alias("id")
)
# %%
obj2
# %%
obj2.filter(pl.col("id") == "a")
# %%
obj2.with_columns(
    pl.when(pl.col("id") == "d")
    .then()
)