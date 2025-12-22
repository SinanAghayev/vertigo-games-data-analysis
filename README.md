# 📊 Project Overview

This project consists of two independent data analysis tasks.

- Task 1 compares two variants using a simple 7×2 table to determine the better-performing option.

- Task 2 analyzes a large dataset containing approximately 7 million rows to extract insights and draw data-driven conclusions.

Each task is approached independently and uses methods appropriate to the size and structure of its data.

> **Important note on data:**  
> The dataset used in this project is not included in the repository due to confidentiality constraints.  
> Please refer to the **General File Structure** section for the expected data layout.

# Table of Contents

- [Summary](#summary)
- [General File Structure](#general-file-structure)
- [Task 1](#task-1-ab-testing-analysis)
  - [Overview](#overview)
  - [Tech Used](#tech-used)
  - [Tools Used](#tools-used)
  - [File Structure](#file-structure)
  - [Methodology](#methodology)
  - [Assumptions](#assumptions)
  - [Results](#results)
- [Task 2](#task-2-data-analysis-and-visualization)
  - [Overview](#overview-1)
  - [Tech Used](#tech-used-1)
  - [Tools Used](#tools-used-1)
  - [File Structure](#file-structure-1)
  - [Methodology](#methodology-1)
  - [Anomalies](#anomalies)
  - [Results](#results-1)
    - [General Analysis](#general-analysis)
    - [First Day Segmented Analysis](#first-day-segmented-analysis)
    - [Country Segmented Analysis](#country-segmented-analysis)
    - [Install Day Segmented Analysis](#install-day-segmented-analysis)
    - [Platform Segmented Analysis](#platform-segmented-analysis)
    - [Power BI Insights](#power-bi-insights)
  - [Limitations](#limitations-of-this-dataset)

# Summary

**Task 1**

This part focuses on an A/B test comparing two game variants using retention-based modeling and revenue projections under multiple scenarios. Across all evaluated time horizons and assumptions, Variant B consistently outperforms Variant A, with revenue uplifts ranging from approximately 6% to 13%.

Additional scenarios, including time-limited sales and the introduction of a new acquisition source, increase overall revenue for both variants without changing the relative ranking. From a revenue-only perspective, introducing a new source yields the strongest impact.

**Task 2**

This part focuses on analysis of a large-scale dataset (~7 million rows) to understand player behavior, retention, engagement, and monetization patterns.

The analysis shows that early engagement strongly correlates with long-term playtime and revenue, platform differences are substantial (Android drives volume, iOS drives revenue), and player behavior varies meaningfully across countries and time-based segments.

# General file structure:

- **`src/`**: Contains utility functions
  - **[`stats_utils.py`](src/stats_utils.py)**: Statistical utility functions for analyzing and explaining data
  - **[`visual_utils.py`](src/visual_utils.py)**: Utility functions for data visualization
  - **[`process_data.py`](src/process_data.py)**: Processes raw data and writes it to CSV for use in other tools

Data files are not included in this repository due to confidentiality constraints.
However, the analysis expects the following directory structure:

- **`data/`**
  - **`raw/`**: Raw data files provided for the case study
  - **`processed/`**: Processed and aggregated data generated during analysis

### Task 1:

- **[`AB_testing.ipynb`](AB_testing.ipynb)**: Analysis for task 1

### Task 2:

- **[`general_analysis.ipynb`](general_analysis.ipynb)**: Overall analysis of data
- **[`first_day_segments.ipynb`](first_day_segments.ipynb)**: Analysis of data segmented by first-day behaviour
- **[`country_analysis.ipynb`](country_analysis.ipynb)**: Analysis of data segmented by countries
- **[`install_day_segments.ipynb`](install_day_segments.ipynb)**: Analysis of data segmented day of install

# Task 1: A/B Testing Analysis

## Overview

In this part, I performed **A/B testing** on two game variants to determine the more profitable option.

Implementation details are documented in Python scripts and the Jupyter notebooks.

## Tech Used

- Python **3.12**
- Matplotlib
- Scipy
- NumPy

## Tools Used

- Jupyter Notebook

## File Structure

Utility functions for this part are implemented in **[`stats_utils.py`](src/stats_utils.py)** and **[`visual_utils.py`](src/visual_utils.py)**.  
The main analysis is done in **[`AB_testing.ipynb`](AB_testing.ipynb)**.

## Methodology

Provided retention values was used to fit a general retention curve. Then the parameters of fitted curve was used to approximate missing values and calculate the needed values.

## Assumptions

- There are exactly 20,000 installs per day. (And another constant value in Part E)
- Average money spent by players is the same (or difference is negligible) for the variants.
- Sales does not affect anything other than purchase rate including average money spent by players, retentions, installs etc. (for Part D).
- Assuming There are no significant differences in cost, resource usage, or time required. (for Part F)

## Results

The following are fitted retention curves for variants.

![Retention curve variant A](images/task_1/retention-variant-A.png)
![Retention curve variant B](images/task_1/retention-variant-B.png)

---

### Part A

Daily active users after 15 days:

- Variant A: 50011
- Variant B: 54454

Percentage difference between the results is 8.88%

Verdict: Variant B is the better option.

---

### Part B

Assuming average money spent by players per day is the same (or difference is negligible) for the variants.

Total revenue by day 15 (not including that day):

- Variant A: 21054.21
- Variant B: 22383.04

Percentage difference between the results is 6.31%

Verdict: Variant B is the better option.

---

### Part C

Assuming average money spent by players per day is the same (or difference is negligible) for the variants.

Total revenue by day 30 (not including that day):

- Variant A: 52128.74
- Variant B: 58998.43

Percentage difference between the results is 13.18%

Verdict: Variant B is the better option.  
The choice is even stronger now, since the percentage difference doubled compared to 15 day result.

---

### Part D

Assuming sales does not affect anything other than purchase rate including average money spent by players, retentions, installs etc.

Total revenue by day 30 with a 10-day sale (days 15–24):

- Variant A: 57243.03
- Variant B: 64697.38

Percentage difference between the results is 13.02%

Revenue of both variants increased with this sale. Meaning that it was a good decision regardless of variants. Also, the variants are affected very similarly that percentage difference hardly changed.

Verdict:

- Variant B is still the better option.
- Sale was a success regardless of variant.

---

### Part E

Total revenue by day 30 with new source introduced on 20th:

- Variant A: 59392.37
- Variant B: 65906.49

Percentage difference between the results is 10.97%

The results are the best the variants have got so far. Variant A benefits more from this update since percentage difference between the variants have decreased.

Verdict:

- Variant B is still the better option.
- Source introduction was a good decision regardless of variant
- Variant A benefitted more.

---

### Part F

Assuming there are no significant differences in cost, resource usage, or time required.

Conclusion: Just from the revenue perspective, adding a new source is a better choice.

---

# Task 2: Data Analysis and Visualization

## Overview

In this part, the dataset was analyzed from multiple perspectives, visualized, and conclusions were drawn from the results.

Implementation details are documented in Python scripts and the Jupyter notebooks.

## Tech Used

- Python **3.12**
- Pandas
- Matplotlib

## Tools Used

- Jupyter Notebook
- Power BI

## File Structure

Utility functions for this part are implemented in **[`stats_utils.py`](src/stats_utils.py)** and **[`visual_utils.py`](src/visual_utils.py)**.

The analyses are done in **[`general_analysis.ipynb`](general_analysis.ipynb)**, **[`first_day_segments.ipynb`](first_day_segments.ipynb)**, **[`country_analysis.ipynb`](country_analysis.ipynb)** and **[`install_day_segments.ipynb`](install_day_segments.ipynb)**.

## Methodology

Firstly, a general analysis of the entire dataset was conducted to identify overall player behavior, such as retention patterns.

Then segmented analyses were performed on the data to compare behaviors across user groups.

Lastly, the data was aggregated at the player level, exported to a CSV file, and analyzed using Power BI.

## Anomalies

I identified a player who appears to have played the game **before installing it**.  
The user with `user_id: 7CD8D170771E5753` played the game on **2024-02-29** but installed it on **2024-03-01**.  
This record appears on **row 208,446** of the file **`000000000002.csv.gz`**.

There are several possible explanations for this inconsistency; however, investigating them is **out of scope** for this project.

Additionally, there are players with missing country information. This is occasionally observed in real-world datasets and was not investigated further.

## Results

### General Analysis

In this part, I conducted general analysis and exploration on dataset. I inspected basic statistics such as max, min, mean etc. And plotted some data.

---

The bar chart below shows daily active users by day of the week. As expected, player activity is significantly higher on weekends. We can see that in the chart below.

![DAU General](images/task_2/DAU-general.png)

I also looked at the retentions for the dataset. The retention values for the users who installed the game early in the month seem to have more retention. It may point to a sale or event present in that time of the month.

![D1 D3 D7 Retention General](images/task_2/d1-d3-d7-retention-general.png)

Session duration is another aspect I analysed. I calculated average session duration per session for days, and there is an oscillation rather than a one way trend.

![Per Session Duration General](images/task_2/per-session-duration-general.png)

However, there is an upwards trend in session duration `x` days after install. Although the varience naturally increases too much as the time goes, we can see that there is a general up trend.

![Per Session Duration After Install General](images/task_2/per-session-duration-after-install-general.png)

### First Day Segmented Analysis

In this part, I segmented users based on first-day engagement. The segments are always equally sized (approximately). And the players who played the game less than 100 seconds (assuming units of the data is seconds) are excluded from analysis.

The visuals I present will contain 3 segments ["Low", "Medium", "High"] segmented on "total_session_duration" for simplicity, but the code can be easily modified to include more segments.

---

First, I looked at retention values. Here are D1 retention charts for segments:

![D1 Retention Segmented](images/task_2/d1-retention-segmented.png)

I also plotted retentions for D3, D7 etc. The retention values are consistently higher for high engagement segments. The results are consistent with expectations and do not reveal additional insights.

---

Here is an interesting insight. We can see from the chart below that the players who played the game most in the install day tend to play it significantly more than the others. They also play more per session.

![Total Duration First Day Segmented](images/task_2/total-duration-first-day-segmented.png)

![Total Duration First Day Segmented](images/task_2/per-session-duration-first-day-segmented.png)

That is not limited to duration of play, but also revenue. Here are IAP and Ad revenue values for segments.

![Total IAP Revenue First Day Segmented](images/task_2/total-iap-revenue-first-day-segmented.png)

![Total Ad Revenue First Day Segmented](images/task_2/total-ad-revenue-first-day-segmented.png)

---

### Install Day Segmented Analysis

In this part, I segmented users based on week day they installed the game.

An interesting pattern arise when players are segmented this way: Players tend to play the most in the day of the week they started. For example, players who installed the game on Wednesday plays the game on wednesday more than other days of the week. And this is true for every day of the week.

It is important to understand that this may not be true for every individual player, but the pattern follows for the players as a whole.

Here is the line chart showing how many games were played each day by segments, but just including Monday and Tuesday for simplicity. The chart after that shows all days of the week.

![Monday Tuesday Match Count](images/task_2/monday-tuesday-match-count-install-day-segmented.png)

![Days of the week Match Count](images/task_2/days-of-week-match-count-install-day-segmented.png)

---

### Country Segmented Analysis

The following is per session duration for the countries with most player numbers.

![Per Session Duration By Country](images/task_2/per-session-duration-by-country.png)

---

### Platform Segmented Analysis

I segmented the data based on platforms. There are two platforms for this dataset: Android and iOS.

I plotted graphs for total revenue and match count. The results show that Android players play significantly more matches overall, while the iOS platform generates higher total revenue.

![Match Count By Platform](images/task_2/match-count-platform.png)
![Total Revenue By Platform](images/task_2/total-revenue-platform.png)

---

### Power BI Insights

Have a look at this dashboard:

![Country Dashboard](images/task_2/country-dashboard.png)

The upper-left chart is a treemap showing user count by country, the upper-right pie chart shows total playtime by country, and the bar chart at the bottom displays IAP and ad revenue by country.

We can see that there are no country that dominates all aspects at the same time.

Here are some quick insights from this dashboard:

- Brazil is the country with most players.
- Türkiye is the country where the game is played the most in total.
- United States is the country where most revenue comes from.
- Russia is a significant market, but revenue is very low.

**Russia vs the US on Player Behaviour**  
The user count and total session duration for the US and Russia is almost the same but revenue difference is huge.

The ad revenue changes vastly between countries, and the US is generally the most profitable in terms of ad revenue. This finding is largely driven by known differences in ad monetization and offers limited actionable insight given the available data.

IAP Revenue, on the other hand, is very important. It tells us about the purchasing behaviour of the people in the market. In this example, Russia and the US are exact opposite of each other. Total IAP revenue in the US is approximately 35x as high as in Russia.

Moreover, Russia is also an interesting market regarding purchasing behaviour. It is one of the two countries where ad revenue surpasses IAP revenue and total revenue is more than 100. The other being Mongolia.

---

**No Correlations**

These are some of the data pairs where no correlations were found:

- Victory count vs in app purchases

<img src="images/task_2/victory-iap-revenue.png" alt="Victory Count - In App Purchases" width="600">

- Defeat count vs in app purchases

<img src="images/task_2/defeat-iap-revenue.png" alt="Defeat Count - In App Purchases" width="600">

- Session count vs Total Revenue

<img src="images/task_2/session-count-total-revenue.png" alt="Session Count - Total Revenue" width="600">

- Session Duration vs Total Revenue

<img src="images/task_2/session-duration-total-revenue.png" alt="Session Duration - Total Revenue" width="600">

---

## Limitations of This Dataset

The dataset is big and contains valuable information. However, it has some limitations. Here are some of them and what could be done with more data.

1. No representation of sequential games  
   Player behaviour on different outcomes and sequences can be analyzed with that.
2. No representation of specific in app purchases  
   The player profile can be drawn better, who buys cheap products and who buys expensive ones.
