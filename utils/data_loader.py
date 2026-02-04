# ======================================================
# Data Loader — 엑셀 로드, 전처리
# ======================================================

import streamlit as st
import pandas as pd
import numpy as np
import os

# 데이터 파일 경로
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

PRIMARY_DATA_FILENAME = "결과물고도화.xlsx"
FALLBACK_REFERENCE_FILENAME = "agent6_final_reg_db.xlsx"
FALLBACK_META_FILENAME = "agent6_final_db.xlsx"

def _safe_read_excel(path: str) -> pd.DataFrame:
    """엑셀 파일 읽기 (파일 없음/읽기 실패 시 예외를 그대로 올림)"""
    return pd.read_excel(path)

def _standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    서로 다른 원천 엑셀 스키마를 앱에서 사용하는 공통 스키마로 맞춤
    기대 컬럼:
      - country, img_type, likes, comments, eng_rate(참여 '율' 또는 참여 '점수'), followers(없으면 NaN)
    """
    df = df.copy()

    # 1) img_type
    if "img_type" not in df.columns:
        if "main_type" in df.columns:
            df["img_type"] = df["main_type"]
        elif "image_type" in df.columns:
            df["img_type"] = df["image_type"]

    # 2) likes/comments
    if "likes" in df.columns:
        df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
    if "comments" in df.columns:
        df["comments"] = pd.to_numeric(df["comments"], errors="coerce")

    # 3) eng_rate: 기존 파일은 eng_rate, 결과물고도화는 engagement(= likes+comments)
    if "eng_rate" not in df.columns or df["eng_rate"].isna().all():
        if "engagement" in df.columns:
            df["eng_rate"] = pd.to_numeric(df["engagement"], errors="coerce")
        elif "likes" in df.columns and "comments" in df.columns:
            df["eng_rate"] = (df["likes"].fillna(0) + df["comments"].fillna(0))

    # 4) followers: 없으면 NaN으로 생성 (eng_rate가 이미 있으면 downstream에서 사용 가능)
    if "followers" not in df.columns:
        df["followers"] = np.nan

    # 5) img_type 정규화 & 유효 범위 필터링 (앱은 Type 1~6 기준 자산/가이드 사용)
    if "img_type" in df.columns:
        df["img_type"] = pd.to_numeric(df["img_type"], errors="coerce")
        df = df.dropna(subset=["img_type"])
        df["img_type"] = df["img_type"].astype(int)
        df = df[df["img_type"].between(1, 6)]

    return df

@st.cache_data
def load_base_df() -> pd.DataFrame:
    """
    앱 전반에서 사용하는 기본 데이터 로드:
    우선순위: data/결과물고도화.xlsx → (fallback) 기존 엑셀 파일
    """
    primary_path = os.path.join(DATA_DIR, PRIMARY_DATA_FILENAME)
    if os.path.exists(primary_path):
        df = _safe_read_excel(primary_path)
        return _standardize_columns(df)

    # fallback: 기존 파일이 남아있는 환경 대응
    meta_path = os.path.join(DATA_DIR, FALLBACK_META_FILENAME)
    if os.path.exists(meta_path):
        df = _safe_read_excel(meta_path)
        return _standardize_columns(df)

    raise FileNotFoundError(
        f"데이터 파일을 찾을 수 없습니다. "
        f"'{PRIMARY_DATA_FILENAME}' 또는 '{FALLBACK_META_FILENAME}'를 data/에 배치해주세요."
    )

@st.cache_data
def load_reference_df():
    """ECDF 계산을 위한 참조 데이터 로드"""
    df = load_base_df()
    df["log_eng"] = np.log1p(pd.to_numeric(df["eng_rate"], errors="coerce"))
    return df

@st.cache_data
def load_meta_df():
    """메타데이터 로드"""
    return load_base_df()

def get_countries(df_meta):
    """국가 목록 반환"""
    return sorted(df_meta["country"].unique())



