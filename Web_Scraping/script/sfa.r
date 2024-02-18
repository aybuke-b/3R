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
    select(c(price, ppi, screen_type, das_limbs, das_head, das_chest, upgrade_storage, screen_size, fast_charging, repairability_index, made_in, ram, storage, brand, induction, network))

print(df_phones)

loghedonic <- lm(log(price) ~ storage + brand + ram + induction + screen_size + made_in + upgrade_storage + das_head + das_limbs + das_chest + fast_charging + network + ppi,
    data = df_phones
)

scf <- sfa(log(price) ~ storage + brand + ram + induction + screen_size + made_in + upgrade_storage + das_head + das_limbs + fast_charging + das_chest + network + ppi,
    data = df_phones,
    truncNorm = FALSE,
    ineffDecrease = FALSE
)

# ATTENTION, inclure "screen_type" dans la Stochastic Cost Frontier la fait planter...

mu <- predict(loghedonic)
se <- predict(loghedonic, se.fit = TRUE)$se.fit

part_1 <- exp(mu + (se^2)/2) |> as_tibble()
part_2 <- exp(mu)

bind_cols(part_1, part_2) |> print(n=Inf)

loghedonic_df <- predict(loghedonic) |>
    as_tibble() |>
    exp() |>
    rename(prediction_loghedonic = value)

sfa_df <- fitted(scf) |>
    as_tibble() |>
    exp() |>
    rename(prediction_sfa = V1)

mu_sfa <- fitted(scf)
se_sfa <- predict(scf, se.fit = TRUE)

exp(residuals(scf))


eff_df <- as_tibble(efficiencies(scf))


new_df <- bind_cols(df_init, eff_df, sfa_df, loghedonic_df)

new_df

brand_groups <- new_df |>
    select(brand, efficiency) |>
    group_by(brand)

print(brand_groups |> summarise(mean_eff = mean(efficiency), n_count = n()) |> arrange(mean_eff))
print(new_df |> select(model, efficiency, price) |> arrange(efficiency), n = 487)

write.csv(new_df, file = "Web_Scraping/data/sfa_results.csv")
