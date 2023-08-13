# A/B Testing for Website Themes

This project analyzes the performance of two different themes for a website using A/B testing. The goal is to determine which theme yields better user engagement, purchases, and conversion rates.

## Dataset

The dataset contains the following metrics for each theme:

-   [x] Click Through Rate
-   [x]  Conversion Rate
-   [x]  Bounce Rate

## Hypothesis Testing

We performed a t-test for each metric to compare the means of the two groups (Light Theme and Dark Theme). We calculated the mean, standard deviation, t-statistic, p-value, and effect size for each metric.

Based on the results of the hypothesis tests, we cannot conclude that one theme yields better user engagement, purchases, and conversion rates than the other. For Click Through Rate and Bounce Rate, the Dark Theme had a higher mean than the Light Theme, but the difference was not statistically significant (p-value \> 0.05). For Conversion Rate, there was no statistically significant difference between the two themes (p-value \> 0.05).

## Conclusion

We cannot make a definitive conclusion about which theme is better based on these results. However, you can use these results to inform your decision about which theme to use for your website.

## Requirements

-   [x] Python 3.x
-   [x] Pandas
-   [x] Scipy
-   [x] Numpy
-   [x] Matplotlib

## Usage

1.  Clone the repository

``` bash
git clone https://github.com/Mfundo-debug/theme_casestudy.git
```

2.  Install the required packages using

``` python
pip install -r requirements.txt
```

3.  Run the `ab_test.py` script to perform the hypothesis tests and print the results.

## License

This project is licensed under the MIT License