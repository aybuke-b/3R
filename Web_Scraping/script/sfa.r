# Trigger a R script to generate individual SFA results.

library(dplyr)
library(frontier)
library(tidyverse)
library(janitor)
library(glmulti)

df_init <- read_delim("Web_Scraping/data/df_clean_2.csv", delim = ";")

# Erreur de boulanger, le stockage est en réalité à 128Go et non à 8
# De meme, le Z fold 3 est pliable.
df_init <- df_init |> mutate(
    storage = case_when(storage == 8 ~ 128, .default = as.double(storage)),
    screen_type = case_when(model == "Samsung Galaxy Z Fold 3" ~ "Pliable", .default = as.character(screen_type))
)

df_phones <- df_init |>
    select(c(price, ppi, screen_type, das_limbs, das_head, das_chest, upgrade_storage, screen_size, fast_charging, repairability_index, made_in, ram, storage, brand, induction, network))

print(df_phones)

loghedonic <- lm(
    log(price) ~ storage + brand + ram + induction + screen_size + screen_type + made_in + upgrade_storage + das_limbs + network + ppi,
    data = df_phones
)

scf <- sfa(
    log(price) ~ storage + brand + ram + induction + screen_size + screen_type + made_in + upgrade_storage + das_limbs + network + ppi,
    data = df_phones,
    truncNorm = FALSE,
    ineffDecrease = FALSE
)

sfa_res <- summary(scf)$mleParam |>
    data.frame() |>
    rownames_to_column(var = "Variables") |>
    clean_names()

eff_df <- as_tibble(efficiencies(scf))

new_df <- bind_cols(df_init, eff_df)

arrow::write_parquet(sfa_res, "Web_Scraping/data/sfa_coefs.parquet")
arrow::write_parquet(new_df, "Web_Scraping/data/sfa_results_app.parquet")
