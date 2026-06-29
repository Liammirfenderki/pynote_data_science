**3-Month Roadmap (Pareto 20% Focus)**

**Month 1: Foundation & Production Workflow (Weeks 1-4)**

- **Week 1: Environment & Core Arrays**
  - ★ *Set up Conda/Mamba environments & .gitignore.*
  - ★ *Master Numpy broadcasting, fancy indexing, and `einsum`.*
  - Master Pandas `read_csv`, `df.info()`, `df.describe()`.
  - Master Pandas boolean indexing and `loc`/`iloc`.

- **Week 2: Data Wrangling & Viz**
  - ★ *Master Pandas `groupby` + `agg` + `transform`.*
  - ★ *Master `pd.merge` (joins) and `pd.concat`.*
  - ★ *Master Matplotlib `plt.subplots()` and figure customization.*
  - Master Seaborn `pairplot`, `heatmap`, and `boxplot`.

- **Week 3: Sklearn API & Preprocessing**
  - ★ *Master `sklearn.pipeline.Pipeline`.*
  - ★ *Master `sklearn.compose.ColumnTransformer`.*
  - Master `StandardScaler`, `OneHotEncoder`, and `SimpleImputer`.
  - Implement custom `FunctionTransformer` for statistical transformations.

- **Week 4: Validation Framework**
  - ★ *Master `sklearn.model_selection.KFold` and `StratifiedKFold`.*
  - ★ *Master `GridSearchCV` and `RandomizedSearchCV`.*
  - Master custom scoring metrics using `make_scorer`.
  - Implement learning curves and validation curves.

**Month 2: Core Modeling & Statistical Rigor (Weeks 5-8)**

- **Week 5: Interpretable Statistics**
  - ★ *Master `statsmodels.api.OLS` and GLM families.*
  - ★ *Extract p-values, confidence intervals, and AIC/BIC.*
  - Master diagnostic plots (QQ, residual vs fitted) in Statsmodels.
  - Implement Robust/Huber regression.

- **Week 6: Ensemble & Feature Importance**
  - ★ *Master `xgboost.XGBClassifier`/`Regressor`.*
  - ★ *Master feature importance (Gain, Weight, Cover) and SHAP summary plots.*
  - Implement `RFECV` (Recursive Feature Elimination with CV).
  - Tune `n_estimators`, `max_depth`, `learning_rate` via Bayesian Opt (Optuna).

- **Week 7: Dimensionality & Clustering**
  - ★ *Master `sklearn.decomposition.PCA` (variance explained ratio).*
  - Master `sklearn.cluster.KMeans` and `DBSCAN`.
  - Master silhouette score and Davies-Bouldin index.
  - Implement pipeline for PCA + Logistic Regression.

- **Week 8: PyTorch Fundamentals**
  - ★ *Master `torch.Tensor` and `torch.autograd` basics.*
  - ★ *Master `torch.nn.Module` inheritance structure.*
  - Master `torch.nn.Linear`, `ReLU`, `Dropout`.
  - Implement a basic 3-layer MLP from scratch.

**Month 3: Advanced Implementation & Research Code (Weeks 9-12)**

- **Week 9: Training Loop & DataLoader**
  - ★ *Master `torch.utils.data.Dataset` and `DataLoader`.*
  - ★ *Write standard train/validation/eval loop with `tqdm`.*
  - Master saving/loading model checkpoints (`state_dict`).
  - Implement learning rate schedulers (`ReduceLROnPlateau`, `CosineAnnealing`).

- **Week 10: Custom Statistical Losses & Metrics**
  - ★ *Implement custom loss functions (e.g., Weighted BCE, Quantile Loss, Negative Log-Likelihood) using `torch.nn.Module`.*
  - ★ *Implement custom evaluation metrics using `torch.no_grad()`.*
  - Implement early stopping callback based on validation loss.
  - Implement gradient clipping and monitoring.

- **Week 11: Probabilistic Programming (Bayesian)**
  - ★ *Master `pymc.Model()` context and `pymc.Normal`, `pm.Bernoulli`.*
  - ★ *Master MCMC sampling (`pm.sample`) and trace plots.*
  - Implement Posterior Predictive Checks (`pm.sample_posterior_predictive`).
  - Implement `arviz` for R-hat and effective sample size diagnostics.

- **Week 12: Reproducibility & Final Integration**
  - ★ *Refactor entire codebase into modular Python scripts (`src/`, `notebooks/`, `tests/`).*
  - ★ *Implement `hydra` or `argparse` for configuration management.*
  - Set up fixed random seeds globally (Python, Numpy, Torch, Sklearn).
  - Run final ablation study: Baseline (Stats) vs ML (Sklearn) vs DL (PyTorch) on your PhD dataset.
