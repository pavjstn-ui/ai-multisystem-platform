{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Project Brief (use in every chat)\
\
## One-liner\
Build an end-to-end **computer vision anomaly detection inspection system** (dataset 
\f1 \uc0\u8594 
\f0  model 
\f1 \uc0\u8594 
\f0  API 
\f1 \uc0\u8594 
\f0  Docker), validated on **FPV drone footage**, transferable to **automotive inspection**.\
\
## Why this exists (skills covered)\
- Data analysis & statistics on image/video data\
- Image preprocessing (OpenCV, NumPy), quality filtering\
- Anomaly detection (classical + DL), optional segmentation/heatmaps\
- Model deployment (FastAPI), containerization (Docker)\
- CI/CD mindset + Git workflow\
\
## Current phase\
Phase: Week 1 \'97 video 
\f1 \uc0\u8594 
\f0  clean, consistent frames dataset.\
\
## Inputs / outputs\
Input: `.mp4/.mov` FPV videos in `data_raw/` (never commit).\
Output:\
- `data_processed/frames/*.jpg`\
- `data_processed/metadata.csv` (frame_id, timestamp, blur_score, saved flag)\
\
## Definition of Done (Week 1)\
- CLI script that:\
  - samples frames at target FPS\
  - normalizes lighting\
  - denoises\
  - computes blur score + rejects low-quality frames\
  - writes metadata.csv\
- Reproducible run command documented in README.\
\
## Tech stack (initial)\
Python, OpenCV, NumPy, pandas (later: PyTorch, FastAPI, Docker, ONNX optional)\
\
## Constraints\
- Keep it simple, production-minded, testable.\
- Prefer deterministic preprocessing and stored metadata.\
}