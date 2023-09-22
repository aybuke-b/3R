# **3R**

`3R` course: [Aybuke Bicat]() & [Corentin Ducloux]()

## <u>Table of Contents</u>
- [**3R**](#3r)
  - [Table of Contents](#table-of-contents)
  - [TODO LIST](#todo-list)
  - [`Research`](#research)
    - [Our Subject](#our-subject)
    - [References](#references)
    - [Price comparators](#price-comparators)
    - [Key Definitions](#key-definitions)
    - [Topics Covered](#topics-covered)
  - [`Realization`](#realization)
    - [Datasources](#datasources)
    - [Data Storage](#data-storage)
    - [Integration and Portability](#integration-and-portability)
    - [Application](#application)
  - [`Restitution`](#restitution)

## TODO LIST

- [ ] Add all references

## `Research`


### Our Subject

> **Econométrie de la production de la demande et modèles frontière de production** : application des modèles SFA (stochastic frontier Analysis) à l’́etude des prix.

### References

- [*Arondo R*, *Garcia N*, *Gonzales E* (2018): **Estimating product efficiency through a
hedonic pricing best pratice frontier**, Business Research Quaterly vol 21 Issue 4,
215-224](https://journals.sagepub.com/doi/full/10.1016/j.brq.2018.08.005)

- [**Méthodologie Qui est le moins cher E. Leclerc**](https://www.quiestlemoinscher.leclerc/pdf/methodologie_202306.pdf)

### Price comparators

- [**Autokoo.com**](https://www.autokoo.com/voiture-neuve/comparateur)
- [**Qui est le moins cher ?**](https://www.quiestlemoinscher.leclerc)

### Key Definitions

- *Hedonic Pricing*: The hedonic pricing methodology considers that the difference in the price of a product is due to its underlying characteristics. A product becomes a *"bundle"* of attributes. Thus, the hedonic price indicates the maximum price that the consumer could be willing to pay if he/she wants to enjoy the portfolio of characteristics associated with that product.
- *Frontier Analysis*: Efficient units are deemed to be those operating on the cost or production frontier, while inefficient units are those that, in the case of a production frontier, operate below the frontier or, in the case of a cost frontier, operate above the frontier.
- *Product efficiency*
- *Product attributes* 
- Valuation of the characteristics of a product
- *Comparative advertising*: Advertisement that compares alternative brands on objectively measurable attributes or price, and identifies the alternative brand by name, illustration or other distinctive information.
- Processing cost (related to asymetric information)
- *Experience goods*: product features or attributes about which the customer has full information when purchasing.
- *Search goods*: information about relevant product features of experience goods cannot be learned before purchasing and
using the product.
- *Semielasticity*: The percentage change in a function with regards to an absolute change in it's parameter. Algebraically, the semi-elasticity of a function $f$ at point $x$ is $\dfrac{f'(x)}{f(x)} \Rightarrow$ in Hedonic Pricing models, the coefficients associated with $\beta_x$ are semielasticies. Hence, the larger the coef., the larger the impact on price $-$ provided that the coef. is statistically significative $\left(p<0.05\right)$.

### Topics Covered

A larger price would be considered
just too high, and would negatively affect demand for the
product and, therefore, business performance.

***

SFA + Hedonic Pricing: The advantage of this combination is that we are able
to consider the possibility of product inefficiency in pricing.
Conventional hedonic pricing considers that prices are right
for the merits of the product (apart from randomness). In our
case, we explicitly account for the possibility of overpriced
(inefficient) products. This combined methodology can also
be applied to the study of pricing in many other product
categories.

***

Result: to identify
overpriced products to predict the magnitude of required discounts in order to reach the competitive
frontier $\Rightarrow$ can guide the pricing policy of manufacturers when sales are detected to be below expectations.

***
 
Brand name confers the product an implicit guarantee of quality and incorporates the image that companies build through marketing efforts such as promotion.

***

This differential
effect exists when the consumer reacts differently to the
branded product than to a similar (same technical features) unnamed version of the product. Customer-based
brand equity can therefore have a significant effect on
the willingness to pay for a product and therefore on
its market price, which is independent of technical features.

***

Hypothesis 1. Price discounts will be higher for the least
efficient products, ceteris paribus the brand name.

Hypothesis 2. Expert evaluations will be positively correlated with product efficiency

## `Realization`

### Datasources

- Various product prices and information about their attributes
- (❓ Potentially gather other prices w/ webscraping)

### Data Storage

- Use of DuckDB to populate a fast analytical OLAP database

### Integration and Portability

- Versionning with Git
- Containerisation with Docker
- Unit and integration tests
- Modularisation

### Application

- **SFA** package: `pysfa` on python
- Either `Streamlit` or `Dash` for the app
- Streamlit would be better in my opinion: using yet another framework is useful to challenge our knowledge

## `Restitution`
