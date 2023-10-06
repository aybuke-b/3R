# Résumés Papiers de Recherche

## <u>Liste des articles</u>


- [Résumés Papiers de Recherche](#résumés-papiers-de-recherche)
  - [Liste des articles](#liste-des-articles)
  - [TODO List](#todo-list)
  - [`Running Shoes in Spain`: *Arrrondo et Al*](#running-shoes-in-spain-arrrondo-et-al)
    - [Hypothèses](#hypothèses)
    - [Modèle](#modèle)
    - [Confirmation Hypothèses](#confirmation-hypothèses)
  - [`Hedonic wine price functions with different price`](#hedonic-wine-price-functions-with-different-price)
  - [`A New Approach To Consumer Theory`: *Kevin Lancaster*](#a-new-approach-to-consumer-theory-kevin-lancaster)
    - [Hypothèses](#hypothèses-1)
  - [`Hedonic Housing Prices and the demand for clean air`: *Harrison et Rubinfeld*](#hedonic-housing-prices-and-the-demand-for-clean-air-harrison-et-rubinfeld)
  - [`Stochastic Frontier Analysis using STATA BOOK`: *Kumbhakar*](#stochastic-frontier-analysis-using-stata-book-kumbhakar)

## TODO List

- [ ] Hedonic Pricing Rosen à lire et résumer : `Corentin`
- [ ] The demand for clean air à lire et résumer : `Aybuke`
- [ ] Hedonic price functions with incomplete info à lire et résumer : `Corentin`
## `Running Shoes in Spain`: *Arrrondo et Al*

But de l'article : **déterminer les composantes principales des prix des sneakers en Espagne**

*Innovation* : Utilisation d'un modèle SFA & de pricing Hedonic $\Rightarrow$ possibilité d'inclure la notion de produit innefficient (trop cher). Cette méthodologie peut être appliquée dans d'autres axes 

- Produit = décomposition en bundle d'attributs ~ cf `Kevin Lancaster`

- Les vendeurs combinent un grand nombre d'attributs dans leurs biens pour pouvoir se différencier des entreprises concurrentes. Le but est que les acheteurs se focalisent sur ces attributs pour faire le choix de leur produit préféré.

- Les sneakers sont des biens hautement différenciés : elles se vendent à des prix qui varient selon une marge très vaste.

- La méthode de pricing hédonique estime que la différence de prix des sneakers est due à ses caractéristiques.

- En estimant l'efficacité des produits, le papier pointe les produits overprice pour prédire le montant des réductions à leur accorder afin d'atteindre la frontière compétitive pour ces produits.

- Les sneakers sont des `biens d'expérience` dont la qualité et la correspondance aux attentes ne peut être évaluée qu'après leur utilisation. Dès lors, pour effectuer un choix rationnel, les consos s'orientent vers des recommandations d'amateurs & experts sur des caractéristiques comme : *response*, *stability*, *duration* et *flexibility*.

### Hypothèses

1. Les réductions de prix seront d'autant plus grandes que les produits sont inefficaces selon le modèle, toutes choses égales par ailleurs, indépendamment de la marque.

2. Les évaluations des experts sont positivement corrélées avec l'efficacité des produits.

### Modèle

$$Log(Pik)=\alpha_k+\beta X_{ik}+e_{ik}$$

- $\alpha_k=$ Effet de la marque $k$ sur le prix du produit (*dummies*)
- $\beta=$ Vecteur des coefficients associés aux attributs du produit
- $X_{ik}=$ Vecteur des attributs d'un produit d'une marque $k$
- $e_{ik}=$ Erreur aléatoire

> Dans ce modèle de base, on ne peut pas déterminer si des produits sont overprice (innefficients) !

**Prise en compte de la frontière stochastique:**

- Erreur composite $\epsilon_{ik}= \{u_{ik} + v_{ik}\}$  avec $v_{ik}$ normalement distribué et $u_{ik}$

- $u_{ik}$ sont distribués indépendamment de $v_{ik}$

> L'index d'efficacité d'un produit est $\theta_{ik} = e^{-u_{ik}} \in (0,1]$

- Un $u_{ik}$ grand signifie que le prix fixé est très au dessus de la frontière optimale, dès lors, le produit sera d'autant plus inefficace et l'index proche de 0. Un $u_{ik}$ proche ou $=0$ indique que le produit est proche de la frontière optimale de pricing.

***

**Index d'efficacité** selon les marques des chaussures.

- Index d'efficacité moyen toutes sneakers confondues = 0.85 donc les sneakers sont 15% overprice en moyenne.

<center>

| Brand                 | Average |
| --------------------- | ------- |
| Adidas ($n=$ 28)      | 0.832   |
| Asics ($n=$ 35)       | 0.864   |
| Saucony ($n=$ 15)     | 0.875   |
| Nike ($n=$ 25)        | 0.824   |
| Brooks ($n=$ 16)      | 0.860   |
| Mizuno ($n=$ 29)      | 0.858   |
| New Balance ($n=$ 18) | 0.848   |
| Reebok ($n=$ 5)       | 0.859   |

</center>

<center>

|                 | Coefficient | t       |
| --------------- | ----------- | ------- |
| Lightness       | 0.007       | 0.24    |
| Cushioning      | 0.064       | 2.54**  |
| Flexibility     | 0.058       | 2.17**  |
| Response        | 0.050       | 1.65*   |
| Stability       | 0.070       | 2.74*** |
| Grip            | -0.045      | -1.59   |
| `Brand dummies` |             |         |
| Adidas          | 2.697       | 6.71*** |
| Asics           | 2.679       | 6.88*** |
| Saucony         | 2.779       | 6.89*** |
| Nike            | 2.714       | 6.43*** |
| Brooks          | 2.834       | 7.01*** |
| Mizuno          | 2.524       | 6.36*** |
| New Balance     | 2.544       | 6.21*** |
| Reebok          | 2.522       | 6.26*** |

</center>

- Toutes les caractéristiques ne sont pas significatives dans la régression, par exemple : Grip & Lightness n'influent pas sur le prix car les coefficients associés ne sont pas statistiquement significatifs.

- De manière plus intéressante, les dummies de marques sont elles toutes significatives au seuil de 1%, et ce sont elles qui "drivent" le prix dans une importance beaucoup plus grande que les caractéristiques associés aux chaussures.

### Confirmation Hypothèses

- Confirmation $H_1$ : Relation inverse entre l'efficacité du produit et la réduction de prix. La réduction de prix est donc d'autant plus grande que la sneakers est overprice !

- Le modèle permet une bonne prédiction des réductions de prix pour rendre compétitifs les sneakers overprice !

## `Hedonic wine price functions with different price`

Relation entre les prix proposés sur le marché et les **RRP**

**RRP** = Recommended Retail Price

## `A New Approach To Consumer Theory`: *Kevin Lancaster*

**But du modèle poroposé : remplacer l'approche traditionnelle par une approche pratique et plus proche du comportement des consommateurs**

- **L'approche traditionnelle de la théorie du consommateur en microéconomie** : les consommateurs préfèrent certains biens et ces préférences vont permettre de construire leur fonction d'utilité $u(x)$ qu'ils vont chercher à maximiser. Dans ce cas, les biens sont consommés parce qu'ils procurent de l'utilité. 
  - *Exemple* : Un ordinateur peut fournir de l'utilité à un conso, quand un autre peut lui préférer une voiture.

- **Nouvelle approche** : Cette fois, ce ne sont pas les biens eux-mêmes qui procurent de l'utilité, mais les caractéristiques des biens. Les biens sont des *inputs* et ce sont les caractéristiques de ces biens qui sont des *outputs*. En général, même uun bien "seul" possède plus d'une caractéristique.
  - *Exemple* : Ce n'est pas le fait de posséder un ordinateur qui procure de l'utilité à un consommateur, mais le fait de pouvoir naviguer sur internet, programmer, jouer, etc.

- L'ajout d'un nouveau bien dans ce modèle est très simple : si un nouveau bien possède des caractéristiques dans les mêmes niveaux de proportions qu'un ancien bien, alors : 
  
    $\Rightarrow$ A) Il ne sera pas vendu si son prix est trop cher. 

    $\Rightarrow$ B) Il remplacera l'ancien bien si son prix est suffisamment compétitif.

### Hypothèses

1. Le bien par lui même ne donne pas d'utilité au consommateur; il possède des caractéristiques et ce sont celles-ci qui procurent de l'utilité.
2. Un bien possède plus d'une caractéristique, et la plupart des caractéristiques seront partagées par un ou plusieurs biens.
3. Une combinaison de biens peut posséder des caractéristiques différentes que des biens consommés séparément. *Exemple* : Achat d'un costume complet ou seulement d'un pantalon de costume.


## `Hedonic Housing Prices and the demand for clean air`: *Harrison et Rubinfeld*

**WTP** : Le prix maximum qu'un consommateur est prêt à payer pour un bien. Si les consos sont probablement prêts à payer moins que cette frontière, ils ne sont pas prêts à payer plus.

## `Stochastic Frontier Analysis using STATA BOOK`: *Kumbhakar*

- L'**efficacité technique** peut soit être modélisée comme *output-orientée* ou *input-orientée*
- On se concentre sur l'efficacité technique output-orientée

Dans ce cas, un modèle de frontière de production stochastique avec efficacité technique output-orientée peut s'écrire :

> $(1)$ - $\text{ln } y_i = \text{ln }y_i^*-u_i, \text{ } u_i\geq0$ 

> $(2)$ - avec $\text{ln }y_i^* = f(x_i;\beta) + v_i$

- $i$ sont ici les observations (entreprises, individus,etc.)
- $y_i=$ output observé
- $y_i^*=$ output maximum
- $x_i= J\times 1$ vecteur des inputs variables
- $\beta= J\times 1$ vecteur des coefficients associés aux input variables
- $v_i=$ est une erreur aléatoire $\Rightarrow$ variation inexpliquée par les variables indépendantes du modèle $-$ cette erreur n'a pas de biais et peut être positive comme négative d'où le $E(v_i)=0$, la valeur attendue de ces erreurs sur un grand nombre d'observations est donc égal à 0.
- $u_i=$ innefficacité productive $\geq$ 0 $\Leftrightarrow u_i = \ln y_i^* - \ln y_i$ $-$ *en réarrangeant l'équation $(1)$*. $u_i$ correspond donc à la log-différence entre l'output réel et l'output maximum. **Dès lors, $u_i \times 100 \%$ donne le pourcentage d'output perdu à cause de l'innefficacité technique.**

L'équation $(2)$ définit la fonction de la frontière stochastique de production. Étant donné $x$, la frontière donne le niveau de production maximum possible et est stochastique à cause de $v_i \Rightarrow$ 
« stochastique » fait référence à l'inclusion du caractère aléatoire ou de la variabilité non observée dans le modèle pour tenir compte de facteurs qui affectent la production ou la rentabilité mais qui ne sont pas directement observables.

- Puisque $u_i \geq 0$, l'output observé $y_i$ est limité en dessous du niveau de production frontière $y_i^*$

> Etant donné l'équation $(1)$ et $(2)$, on peut ré-écrire le modèle de cette façon :

$$
\begin{cases}
\ln y_i = \ln y_i^* - u_i\\
\ln y_i^* = f(x_i, \beta) + v_i
\end{cases}
$$

- On substitue alors $\ln y_i^*$ dans l'équation $(1)$ et on trouve :

$$\ln y_i = f(x_i, \beta) - u_i + v_i$$
$$\ln y_i = f(x_i, \beta) + \epsilon_i$$

- Avec le terme d'erreur composé $\epsilon_i = v_i - u_i$

> En réarrangeant l'équation $(1)$ :

$$
\ln y_i = \ln y_i^* - u_i\\
\Leftrightarrow \ln y_i - \ln y_i^* = -u_i\\
\Leftrightarrow \ln \left(\frac{y_i}{y_i^*}\right)= -u_i\\
\Leftrightarrow \exp \ln \left(\frac{y_i}{y_i^*}\right)= \exp(-u_i)\\
\Leftrightarrow  \frac{y_i}{y_i^*}= \exp(-u_i)\\
\Leftrightarrow \exp(-u_i) = \frac{y_i}{y_i^*}\\
$$

- On voit ici que $\exp(-u_i)$ donne le ratio d'output produit sur l'output maximum possible. Le ratio se réfère à l'efficacité technique de la firme $i$.