# Trigger a R script to generate individual SFA results.

library(dplyr)
library(frontier)
library(leaps)
library(tidyverse)
library(glmulti)

df_init <- read_delim("Web_Scraping/data/df_clean.csv", delim = ";")

df_init |>
    print()

df_phones <- df_init |>
    select(c(price, screen_type, das_limbs, das_head, upgrade_storage, screen_size, fast_charging, repairability_index, made_in, ram, storage, brand, induction))

print(df_phones)

spf <- sfa(
    log(price) ~ screen_type + das_head + das_limbs + upgrade_storage + screen_size + fast_charging + repairability_index + made_in + ram + storage + brand + induction,
    data = df_phones,
    truncNorm = FALSE,
    ineffDecrease = TRUE
) # spf => Stochastic Production Function

# ATTENTION, inclure "screen_type" dans la Stochastic Cost Frontier la fait planter...

scf <- sfa(
    log(price) ~ das_head + das_limbs + upgrade_storage + screen_size + fast_charging + repairability_index + made_in + ram + storage + brand + induction,
    data = df_phones,
    truncNorm = TRUE, # TRUE ou FALSE, à voir.
    ineffDecrease = FALSE
) # scf => Stochastic Cost Function

# A typical stochastic frontier model involves a parametric frontier
# subject to a composite error term, which is a convolution of a non-negative inefficiency
# and a random error.

# le paramètre truncNorm contrôle le type de distribution.
# si `truncNorm` = TRUE alors on a une distribution normale tronquée.
# si `truncNorm` = FALSE alors on a une dsitribution

# print(summary(spf))
print(summary(scf))
print(resettestFrontier(scf))
# print(residuals(spf))

eff_df <- as_tibble(efficiencies(scf))
new_df <- bind_cols(df_init, eff_df)

brand_groups <- new_df |>
    select(brand, efficiency) |>
    group_by(brand)

print(brand_groups |> summarise(mean_eff = mean(efficiency), n_count = n()) |> arrange(mean_eff))
print(new_df |> select(model, efficiency, price) |> arrange(efficiency), n = 487)

# write.csv(new_df, file = "Web_Scraping/data/sfa_results.csv")
