# CV Drone Inspection – Setup & Reproducible Workflow

This document captures **all steps** required to reproduce the working setup for the CV Drone Inspection project (OpenCV pipeline + Jupyter). Use it as a **bootstrap guide** for this or any future CV project.

---

## 0. Project context

**Repo type:** monorepo  
**Project path:**
```
ai-multisystem-platform/projects/cv-drone-inspection/
```

This folder is the **project root**. All commands below assume you are inside it.

---

## 1. Folder structure (expected)

```
cv-drone-inspection/
├── api/
├── data_raw/
├── data_processed/
├── data_gold/
├── docker/
├── docs/
├── notebooks/
├── reports/
├── src/
│   ├── io/
│   ├── preprocessing/
│   ├── quality/
│   └── utils/
├── tests/
└── README.md
```

**Rule:** Always run Python commands from this folder.

---

## 2. Python environment (clean & stable)

We use a **dedicated Conda environment** to avoid macOS multimedia library conflicts.

### 2.1 Create environment

```bash
conda create -n cv-drone python=3.11 -y
conda activate cv-drone
```

### 2.2 Install core dependencies

```bash
conda install -c conda-forge opencv numpy -y
```

### 2.3 Verify OpenCV

```bash
python -c "import cv2; print(cv2.__version__)"
```

Expected: a version number (e.g. `4.11.0`).

---

## 3. Python package structure (critical)

For `python -m ...` to work, `src/` must be a **proper Python package**.

Create these files **once**:

```bash
touch src/__init__.py
touch src/io/__init__.py
touch src/preprocessing/__init__.py
touch src/quality/__init__.py
touch src/utils/__init__.py
```

Why: Python only imports folders that are marked as packages.

---

## 4. Dataset preprocessing pipeline (CLI)

### 4.1 Command (run from project root)

```bash
python -m src.preprocessing.preprocess_video \
  --video data_raw/drfoot.mp4 \
  --out data_processed/test_run \
  --target-fps 3
```

### 4.2 Expected output

```
data_processed/test_run/
├── frames/
│   ├── frame_00000000.jpg
│   ├── frame_00000010.jpg
│   └── ...
└── metadata.csv
```

Terminal output should end with:
```
Preprocessing complete.
```

---

## 5. JupyterLab integration (without breaking anything)

**Key idea:** Jupyter ≠ Python environment. One JupyterLab can serve many kernels.

### 5.1 Install JupyterLab in this env

```bash
python -m pip install jupyterlab ipykernel
```

### 5.2 Register kernel

```bash
python -m ipykernel install \
  --user \
  --name cv-drone \
  --display-name "Python (cv-drone)"
```

### 5.3 Launch JupyterLab

```bash
jupyter lab
```

In the notebook UI:
- Kernel → Select **Python (cv-drone)**

Verification cell:
```python
import cv2
cv2.__version__
```

---

## 6. Common pitfalls (and how we avoided them)

### ❌ `ModuleNotFoundError: src`
Cause: running from wrong folder.  
Fix: always run from `cv-drone-inspection/`.

### ❌ OpenCV dylib / FFmpeg errors on macOS
Cause: mixed multimedia libraries in base env.  
Fix: clean conda env + conda-forge OpenCV.

### ❌ Jupyter missing `cv2`
Cause: wrong kernel selected.  
Fix: switch kernel to **Python (cv-drone)**.

---

## 7. Reuse checklist (copy-paste)

For any new CV project:
1. Create project folder
2. Create `src/` + submodules
3. Add `__init__.py` files
4. Create dedicated conda env
5. Install OpenCV from conda-forge
6. Register Jupyter kernel
7. Run one short test video

---

## Status

✅ Environment stable  
✅ OpenCV working  
✅ CLI pipeline tested  
✅ Jupyter kernel registered  

This setup is **production-safe and reusable**.

