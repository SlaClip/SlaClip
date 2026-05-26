# SlaClip

Official code for the ICML 2026 paper **“SlaClip: Gradient Norm Slacks can be Indicator for Adaptive Clipping in DP-SGD.”**

- **ICML Poster:** https://icml.cc/virtual/2026/poster/66390
- **Paper:** TBA
- **Code:** https://github.com/<your-github-username>/SlaClip

This repository is a self-contained overlay for the official [Opacus](https://github.com/pytorch/opacus) repository. It adds SlaClip and paper baselines without modifying upstream files. Remove `SlaClip/` to restore upstream behavior.

## Quick start
1. `git clone` the official Opacus repo, then copy this `SlaClip/` folder into the repo root. Run all commands from the opacus repo root (see Requirements).
2. Create and activate a clean environment, then install dependencies (see Install).
3. Run the CLI to reproduce experiments (default uses MNIST; you can switch datasets, models, and baselines).
4. Interpreting results:
   - `epsilon` is the privacy budget at the **last batch of each epoch**.
   - `test_accuracy` is computed on the test set.
   - The warning “Secure RNG turned off” means we use a faster non‑cryptographic RNG for convenience.
     For strict paper‑grade runs, set `secure_mode=True` in `PrivacyEngine`.
   - `_events.csv` records epsilon milestones at the first step where ε reaches or exceeds the target.

## Requirements
Install the Opacus repo directly from the source:
```
git clone https://github.com/pytorch/opacus.git
cd opacus
```
The Opacus version specified in `SlaClip/OPACUS_BASE_VERSION.txt`.

## Install
From the Opacus repo root:
```
conda env create -f SlaClip/environment.yml
conda activate opacus
pip install -e .
python SlaClip/verify_install.py
```

Notes:
- `environment.yml` installs PyTorch via pip. GPU support depends on installing CUDA wheels; if you get a CPU build, reinstall PyTorch with the CUDA wheel index, e.g.:
  `pip install --index-url https://download.pytorch.org/whl/cu121 torch torchvision torchaudio`


## Methods
Use `--method` with one of:
- `slaclip`
- `slaclip-q`
- `vanilla-clip`
- `adap-clip`
- `dc-sgd-e`
- `autoclip`

## Datasets
Use `--dataset` with one of:
- `mnist`
- `fmnist`
- `cifar10`
- `imdb`
- `names`

## Default CLI (SlaClip-Cifar10)
```

python SlaClip/run_exp.py \
  --method slaclip \
  --dataset cifar10 \
  --seed 42 \
  --epochs 120 \
  --K 50 \
  --C0 5 \
  --c-min 0.2 \
  --c-max 50 \
  --eta 0.2 \
  --sigma 1.538 \
  --delta 1e-5 \
  --grad-sample-mode hooks \
  --batch-size 2048 \
  --batch-size-test 2048 \
  --optim SGD \
  --lr 0.2 \
  --momentum 0.9 \
  --weight-decay 5e-4 \
  --lr-schedule cos \
  --workers 8 \
  --run-name slaclip_cifar10_eps8_sd42_B2048_C5_lr0.2_cos_K50_sigma1.538

```

## Outputs
Outputs are written to `SlaClip/outputs/`:
- `<run_name>.csv` (epoch, epsilon, test_accuracy, C_t, dataset, method, seed)
- `<run_name>.json` (same fields)
- `<run_name>_events.csv` (epsilon milestones at: 0.1–0.9 step 0.1, then 1.0/1.5/2.0/2.5/3.0, then 4.0/5.0/6.0)

## Overlay details
See `SlaClip/PATCH_MANIFEST.md`.

## Citation

This codebase is built as an overlay on top of the official Opacus repository.  
If you use this repository, please also cite Opacus (see the Opacus README for the official BibTeX entry).


