# Trigger a R script to generate individual SFA results.

library(tidyverse)
library(frontier)

df_phones <- read_delim("Web_Scraping/data/df_clean.csv", delim = ";")

sfa <- sfa(
    log(price) ~ storage + induction + upgrade_storage + ram + screen_type + network + screen_size + brand + made_in + das_limbs + battery + ppi,
    data = df_phones
)

print(summary(sfa))

eff_df <- as_tibble(efficiencies(sfa))
new_df <- bind_cols(df_phones, eff_df)

brand_groups <- new_df |>
    select(brand, efficiency) |>
    group_by(brand)

print(brand_groups |> summarise(mean_eff = mean(efficiency), n_count = n()))
print(new_df |> select(model, efficiency, price) |> arrange(efficiency), n = 487)

write.csv(new_df, file = "Web_Scraping/data/sfa_results.csv")
