# Instacart Reorder Prediction

## Overview
This project aims to predict the possibility of a given user reorder a given product.

## Introduction
This project uses Random Forest Classifier for prediction. Several extra columns are added to the for feature engineering to give more information to the model. Since the dataset is too large, downsampling is applied. However, GroupSplit is used instead of the classical train test split to avoid data leakage. Grid search is also used to find the best hyperparameters of the model.

## Dataset
Instacart Market Basket Analysis is used for the model training. Due to the maximum value of github, datasets cannot be included in this repository. Users should download the dataset themselves and put them in ```resources/data/raw/```.

## Set-up
### Prerequisites 
- Python
- Jupyter

Users can use Anaconda to facilitate the set up.

To download the required libraries
```
pip install -r requirement.txt
```

## Contributions
Thank you to Ethan Tran and Bill Huang for their contribution in this project.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for full details.