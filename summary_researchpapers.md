# Résumés Papiers de Recherche

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

## Confirmation Hypothèses

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