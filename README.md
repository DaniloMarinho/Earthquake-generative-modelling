# Data Science Challenge: Earthquake prediction in Japan
##### Authors : Morisset Lucas, Danilo Fernandes, Frederico Testa, Omar Elkhalifi, Sébastion Vol

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

## Evaluation Metric

 TODO

## Baseline Model

As a starting point, we have provided a baseline Epidemic Type Aftershock Sequence (ETAS) model based on **Marked Hawkes Processes**. This model is a historical model used by geologists for earthquakes modelization and is further described in [Yosihiko Ogata & al.](https://link.springer.com/article/10.1023/A:1003403601725) The baseline model utilizes the temporal dependencies and the mark information in the data to make predictions. Participants are encouraged to explore beyond this baseline, incorporating innovative techniques and methodologies to improve upon the baseline performance.

## Submission Guidelines

TODO 

We look forward to seeing your innovative solutions to this challenge. Good luck!