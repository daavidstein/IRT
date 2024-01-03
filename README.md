# IRT (Item Response Theory)

This project contains materials related to a presentation I gave at the Tampa Bay Data Science Group on December 13, 2023.

```
├──  notebooks
    ├── Computing_SEm.ipynb
    ├── discrimination_and_SEm.ipynb
```
- `Computing_SEm.ipynb` illustrates two methods of determining the uncertainty of an observed test score: SEm and SE_est.
  - For SEm, we review the definition given by Frederic M. Lord in his 1984 paper before computing it from real LSAT responses.
  - We then introduce the Item Information Function before using it to compute the standard error of the estimate (SE_est) for each ability level using the same data as above.
  
- `discrimination_and_SEm.ipynb` illustrates the relationship between the average discrimination of an item and the overall standard error of the test. We use simulated data to generate items and responses for tests with different average discriminations, then plot those vs. SEm to see the relationship. (Spoiler alert: the two are inversely related)


- The Google Slides corresponding to the presentation can be found  [here](https://docs.google.com/presentation/d/1xE4xlYuvzHlPWDJP1sxRv-k8NSzCTxiElYU4K6zbIUI/edit?usp=sharing).


- You may also want to check out my "Test Buckets" app [here](https://testbuckets.streamlit.app/) and the associated repo [here](https://github.com/daavidstein/standardized_test_dashboard)