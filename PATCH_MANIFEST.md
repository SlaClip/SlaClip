# Patch Manifest

SlaClip prepends `SlaClip/patches` to `sys.path` so patched modules load before upstream Opacus. Upstream files are unchanged. Removing `SlaClip/` restores upstream behavior.

## Patched modules

- `opacus/__init__.py`
  - Extends package path and re-exports `PrivacyEngine`.

- `opacus/privacy_engine.py`
  - Routes paper methods and passes SlaClip parameters to the optimizer wrapper.

- `opacus/optimizers/__init__.py`
  - Extends optimizer package path and registers SlaClip/SlaClip-Q.

- `opacus/optimizers/slaclipoptimizer.py`
  - Implements Eq. (6)–(13) and Algorithm 1 exactly.

- `opacus/optimizers/adaclipoptimizer.py`
  - Uses matched-budget accounting for the Adap-Clip baseline.

