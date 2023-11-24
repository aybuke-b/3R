library(dplyr)
library(frontier)
library(leaps)
library(tidyverse)
library(glmulti)
library(stargazer)
library(FactoMineR)

df_init <- read_delim("Web_Scraping/data/df_clean.csv", delim = ";")

df_init |>
    print()

df_phones <- df_init |>
    select(-c(logprice, cpu, model, sensor, screen_tech, stars, reviews, color, cam_1, cam_2, cam_3))


sub <- regsubsets(
    price ~ .,
    data = df_phones,
    nbest = 1,
    nvmax = 30,
    really.big = TRUE,
    method = "backward"
)

# Pour éviter l'overfitting, il ne faut pas sélectionner trop de variables sinon
# on risque de modéliser le noise du dataset scrapé.

results <- summary(sub)
print(results$which)
print(results$adjr2)

# le graphique avec les carrés pour le R^2 ajusté


plot(sub, scale = "adjr2")

# res2 <- glmulti(price ~ ., data = df_phones, level = 1, method = "g", fitfunction = lm, crit = "bic")
# res_2 <- summary(res2)
# print(res_2)
# f <- res_2$bestmodel
# level_linreg <- lm(f, data = df_phones)
level_linreg <- lm(price ~ screen_type + das_limbs + das_head + upgrade_storage + screen_size + fast_charging + repairability_index + made_in + ram + storage + brand + induction, data = df_phones)
log_linreg <- lm(log(price) ~ screen_type + das_limbs + das_head + upgrade_storage + screen_size + fast_charging + repairability_index + made_in + ram + storage + brand + induction, data = df_phones)

stargazer(level_linreg, log_linreg, type = "text")

residuals_plot <- ggplot(data = df_phones, aes(x = fitted(level_linreg), y = resid(level_linreg))) +
    geom_point() +
    geom_smooth(method = "loess", se = FALSE, linetype = "dashed") +
    labs(x = "Fitted Values", y = "Residuals") +
    ggtitle("Residuals vs Fitted Values") +
    theme_minimal()
print(residuals_plot)
print(bptest(level_linreg))

# les résidus sont hétéroscédastiques ! cf le bptest & le residuals_plot.

qqnorm(df_phones$price, pch = 1, frame = FALSE)
qqline(df_phones$price, col = "steelblue", lwd = 2)

# le qqplot montre quant à lui que le prix ne suit pas une distribution normale
# plot(res2, type = "s")

df_pca <- df_phones |> select(where(is.numeric))

res_pca <- PCA(df_pca)

print(res_pca$eig)

plot(res_pca, choix = "var")


# La valeur de l’importance d’une variable est égale à la somme des poids divisées
# par les probabilités des modèles dans lesquels la variable apparaît.
# Ainsi, une variable qui apparaît dans beaucoup de modèles avec de grands poids aura une grande valeur d’importance.
# La ligne rouge verticale est tracée à .80 (80%)
# est utilisé comme une limite pour différencier les variables importantes et celles qui le sont moins.
# 11 variables sont à 1 => elles apparaissent dans tous les modèles.
