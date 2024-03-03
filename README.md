# Data Science Challenge: Generative modeling of self exciting processes
##### Authors : Lucas Morisset, Danilo Fernandes, Frederico Testa, Omar Elkhalifi, Sébastion Vol, Cyprien Raffi

## Challenge Overview

Predicting earthquakes in Japan holds paramount importance due to the country's high susceptibility to seismic activities as part of the Pacific "Ring of Fire." The ability to forecast such natural disasters, even with limited precision or information, plays a critical role in ensuring public safety, protecting infrastructure, maintaining economic stability, ensuring nuclear safety, advancing scientific research, and building community resilience. Japan's frequent encounters with earthquakes necessitate preparedness and mitigation efforts that can significantly benefit from advancements in prediction capabilities. 

In this challenge, our objective is to leverage the self-exciting nature of earthquakes to attempt predictions regarding the timing and magnitude of future seismic events. The primary challenge lies in relying solely on historical earthquake data from Japan, without incorporating the country's geological characteristics into our predictive models.

## Data Description

Created by an act of Congress in 1879, the [USGS](https://www.usgs.gov/) provides science for a changing world, which reflects and responds to society’s continuously evolving needs. As the science arm of the US Department of the Interior, the USGS brings an array of earth, water, biological, and mapping data and expertise to bear in support of decision-making on environmental, resource, and public safety issues.

The dataset provided to participants was scrapped from the USGS' API, and can be found [here](https://earthquake.usgs.gov/fdsnws/event/1/). It contains all historical earthquake data in Japan between 2018 and 2023, and consists of :
- **Timestamps**: A column of timestamps indicating when earthquake occurred.
- **Magnitudes**: A column of magnitude associated with each earthquake.
- **Latitude**: Latitude of the epicenter.
- **Longitude**: Longitude of the epicenter.

Participants are expected to use this data only to train their models.

## Guidelines

The participants are expected to submit a generative model $G$ that generate timestamps and magnitudes data. Mathematicaly, from a random noises $(Z_i)_i \in \mathbb{R}^d_{latent}$, the participant must generate $(G(Z_i))_i = ((T_i,M_i))_i$. Note that the randomness can be an intrinsic part of the model's design (for exemple one can use a Poisson point process to generate the $(T_i)_i$ sequence). 

## Evaluation Metric

Evaluation of models will be based on two key metrics:
- The **Anderson-Darling** metric between the generated magnitudes and the empirical magnitudes in the training dataset. This metric emphasizes differences in the distributions' extremes, placing greater emphasis on the tails that represent higher magnitudes and more destructive earthquakes. Given a sample of magnitudes $M_1, ..., M_n$, let us denote its empirical cumulative distribution function ( or c.d.f.) as
$$
\widehat{F}_n(x) = \frac{1}{n}\sum_{i=1}^{n} \mathbbm{1}\left\{ M_i \le x \right\}
$$
The Anderson-Darling distance (A.D. distance) has the following expression:
$$
W_n=n \int_{-\infty}^{\infty} \frac{\left(\widehat{F}_n(x)-F(x)\right)^2}{F(x)(1-F(x))} d F(x)
$$
which consists essentially in a weighted square difference between the theoretical cumulative distribution function of the considered distribution and the empirical c.d.f. of an i.i.d. sample with that same distribution. To evaluate the performance of submission we propose an empirical version of the Anderson-Darling distance. We refer to $M_{1, n} \leq \cdots \leq X_{n, n}$ as the order statistics. For a generated sample $\tilde{M}_i$ we define the following
$$
\tilde{u}_{i, n}=\frac{1}{n+2}\left(\sum_{j=1}^n \mathbbm{1}\left\{M_j\leq \tilde{M}_{i, n}\right\}+1\right) \approx \widehat{F}_n^M(\tilde{M}_{i, n}) \approx \mathbb{P}_{M\sim\mu}\left( M \le \tilde{M}_{i, n} \right)
$$
which represents the model probability of a generated variable (with small corrections to avoid having $\tilde{u}_{i, n}=0,1$).
The way we compute the Anderson-Darling distance is then
$$
AD((M_1,\ldots M_n),(\tilde{M}_1,\ldots \tilde{M}_n))=-n-\frac{1}{n} \sum_{i=1}^n(2 i-1)\left(\log \left(\widetilde{u}_{i, n}^\tau\right)+\log \left(1-\widetilde{u}_{n-i+1, n}^\tau\right)\right).
$$

- The **Wassertein distance** of the generated inter-arrival times and magnitudes vector $(v_i)_i = ((T_{i}-T_{i-1},M_i,\cdots,T_{i+k-1}-T_{i+k-2},M_{i+k-1}))_i$, in $\mathbb{R}^{2k}$ and its empirical counterpart. This measurement ensures the model captures both the self-exciting properties of earthquake occurrences and the correlations between earthquake magnitudes and frequencies.


Denote $\mu_{M}$ the marginal distribution of the generated magnitudes, $\mu_{IA}$ the marginal distribution of the generated inter_arrival and magnitude vectors $(v_i)_i$, as well as $\hat{\mu}_{M}$ and $\hat{\mu}_{IA}$ their empirical couterparts in the test dataset. Then the final metric used to rank the participants is :
$$ \mathcal{L}(G) = AD(\mu_{M}, \hat{\mu_{M}}) + W_2(\mu_{IA}, \hat{\mu_{IA}})$$

The participants' goal should be to minimize $\mathcal{L}$.

For more details on any of these two metrics we refer to [Wikipedia:Anderson-Darling](https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test) and [Wikipedia:W2](https://en.wikipedia.org/wiki/Wasserstein_metric). For for further details on the formulation of the Andesron-Darling distance in particular, we refer to [Asymptotic Theory of Certain "Goodness of Fit" Criteria Based on Stochastic Processes](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-23/issue-2/Asymptotic-Theory-of-Certain-Goodness-of-Fit-Criteria-Based-on/10.1214/aoms/1177729437.full) and [Tests of Goodness-of-Fit](https://link.springer.com/referenceworkentry/10.1007/978-3-642-04898-2_118).


## Baseline Model

As a starting point, we have provided a baseline Epidemic Type Aftershock Sequence (ETAS) model based on **Marked Hawkes Processes**. This model is a historical model used by geologists for earthquakes modelization and is further described in [Yosihiko Ogata & al.](https://link.springer.com/article/10.1023/A:1003403601725) The baseline model utilizes the temporal dependencies and the mark information in the data to make predictions. Participants are encouraged to explore beyond this baseline, incorporating innovative techniques and methodologies to improve upon the baseline performance.

We look forward to seeing your innovative solutions to this challenge. Good luck!