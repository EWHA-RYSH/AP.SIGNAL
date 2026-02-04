# ======================================================
# 공통 디자인 상수 정의
# ======================================================

# ======================================================
# 브랜드 컬러
# ======================================================
BRAND_COLORS = {
    "primary": "#1F5795", # Amore Blue
    "deep": "#001C58", # Pacific Blue
    "gray": "#7D7D7D",
    "black": "#000000", 
    "white": "#FFFFFF", 
    "bg": "#F7F8FA" 
}

# ======================================================
# 텍스트 컬러
# ======================================================
TEXT_COLORS = {
    "primary": "#111827",      # 기본 텍스트 
    "secondary": "#374151",    # 보조 텍스트
    "tertiary": "#6B7280",     # 연한 회색
    "muted": "#9CA3AF",       # 비활성/뮤트 텍스트
    "accent": "#1F5795",      # 강조 텍스트 (브랜드 컬러)
    "white": "#FFFFFF",        # 흰색 텍스트
}

# ======================================================
# 배경 컬러
# ======================================================
BG_COLORS = {
    "white": "#FFFFFF",
    "light": "#F9FAFB",
    "lighter": "#F5F7FA",
    "gray": "#F3F4F6",
    "primary": "#1F5795",
}

# ======================================================
# 테두리 컬러
# ======================================================
BORDER_COLORS = {
    "default": "#E5E7EB",
    "light": "#D1D5DB",
    "lighter": "#E0E4EA",
    "accent": "#1F5795",
}

# ======================================================
# 폰트 크기
# ======================================================
FONT_SIZES = {
    "xs": "11px",
    "sm": "12px",
    "base": "13px",
    "md": "14px",
    "lg": "16px",
    "xl": "18px",
    "2xl": "20px",
    "3xl": "24px",
    "4xl": "28px",
    "5xl": "36px",
    "6xl": "40px",
}

# ======================================================
# 폰트 굵기
# ======================================================
FONT_WEIGHTS = {
    "normal": "400",
    "medium": "500",
    "semibold": "600",
    "bold": "700",
    "extrabold": "800",
}

# ======================================================
# 폰트 패밀리
# ======================================================
FONT_FAMILIES = {
    "medium": "Arita-Dotum-Medium, Arita-dotum-Medium, sans-serif",
    "bold": "Arita-Dotum-Bold, Arita-Dotum-Medium, Arita-dotum-Medium, sans-serif",
    "sans": "Arita-Sans-Medium, sans-serif",
}

# ======================================================
# 간격 (Spacing)
# ======================================================
SPACING = {
    "xs": "4px",
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "xl": "20px",
    "2xl": "24px",
    "3xl": "32px",
    "4xl": "40px",
    "5xl": "48px",
}

# ======================================================
# 보더 반경
# ======================================================
BORDER_RADIUS = {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "14px",
    "full": "999px",
}

# ======================================================
# 헬퍼 함수: 스타일 문자열 생성
# ======================================================
def get_text_style(
    size: str = "md",
    color: str = "primary",
    weight: str = None,
    family: str = "medium"
) -> str:
    """
    텍스트 스타일 문자열을 생성합니다.
    
    Args:
        size: FONT_SIZES 키 
        color: TEXT_COLORS 키 
        weight: FONT_WEIGHTS 키 (None이면 family에 따라 자동 설정)
        family: FONT_FAMILIES 키 (bold면 굵기 자동 적용)
    
    Returns:
        CSS 스타일 문자열
    """
    # family가 bold면 굵기 자동 설정 (weight 파라미터 무시)
    if family == "bold" and weight is None:
        weight = "bold"
    elif weight is None:
        weight = "normal"
    
    # bold family를 사용하면 font-weight는 생략 (폰트 자체가 굵음)
    font_weight = ""
    if family != "bold":
        font_weight = f"font-weight: {FONT_WEIGHTS.get(weight, FONT_WEIGHTS['normal'])}; "
    
    return (
        f"font-size: {FONT_SIZES.get(size, FONT_SIZES['md'])}; "
        f"color: {TEXT_COLORS.get(color, TEXT_COLORS['primary'])}; "
        f"{font_weight}"
        f"font-family: {FONT_FAMILIES.get(family, FONT_FAMILIES['medium'])} !important;"
    )

def get_bg_style(color: str = "white") -> str:
    """배경 색상 스타일 문자열을 생성합니다."""
    return f"background-color: {BG_COLORS.get(color, BG_COLORS['white'])};"

def get_border_style(color: str = "default", width: str = "1px") -> str:
    """테두리 스타일 문자열을 생성합니다."""
    return f"border: {width} solid {BORDER_COLORS.get(color, BORDER_COLORS['default'])};"

