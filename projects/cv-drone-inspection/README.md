{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # CV Drone Inspection 
\f1 \uc0\u8594 
\f0  Anomaly Detection\
\
Goal: build a **vision-based anomaly detection inspection system** validated on **FPV drone footage** (transferable to automotive inspection).\
\
## What this project produces\
- A dataset builder: video 
\f1 \uc0\u8594 
\f0  sampled frames 
\f1 \uc0\u8594 
\f0  clean/normalized frames + metadata\
- An anomaly detector: score + heatmap for \'93suspicious\'94 regions/frames\
- An inference API (FastAPI) + Docker container\
- Lightweight CI checks (tests/lint later)\
\
## Folder structure\
- `data_raw/` \'97 input videos (not committed)\
- `data_processed/` \'97 processed frames + metadata\
- `data_gold/` \'97 curated \'93best\'94 dataset split\
- `src/` \'97 reusable code (preprocessing, quality metrics, IO)\
- `api/` \'97 inference service\
- `docker/` \'97 container files\
- `tests/` \'97 unit tests\
- `docs/` \'97 design notes & decisions\
- `reports/` \'97 outputs, plots, evaluation summaries\
- `notebooks/` \'97 exploration only (keep logic in `src/`)\
\
## Rules\
- Keep heavy logic out of notebooks 
\f1 \uc0\u8594 
\f0  move into `src/`\
- Always save a `metadata.csv` for reproducibility\
- One block at a time 
\f1 \uc0\u8594 
\f0  commit/push after each block\
}