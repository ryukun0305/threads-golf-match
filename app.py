import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Threads Golf Match",
    page_icon="⛳",
    layout="centered"
)

# レスポンシブ対応＆デザインを洗練させたCSS
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff !important;
        color: #0f1419 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    section[data-testid="stSidebar"] {
        background-color: #f7f9f9 !important;
    }
    .app-title {
        text-align: center;
        color: #0f1419;
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 2px;
    }
    .app-subtitle {
        text-align: center;
        color: #536471;
        font-size: 14px;
        margin-bottom: 20px;
    }
    .golf-card {
        background: #ffffff;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #efeef2;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
        margin-bottom: 16px;
        width: 100%;
    }
    .badge-mix {
        background-color: #e7f5ff;
        color: #0c8599;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }
    .badge-women {
        background-color: #fff0f3;
        color: #c92a2a;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }
    .status-badge {
        background-color: #f1f3f5;
        color: #495057;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }
    /* 入力ボックスの背景を白、文字を黒に固定 */
    input, textarea, div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #0f1419 !important;
        -webkit-text-fill-color: #0f1419 !important;
    }
    label, p, span, h1, h2, h3 {
        color: #0f1419 !important;
    }
    .app-subtitle {
        color: #536471 !important;
    }
    /* ボタンの共通デザイン（文字白・背景黒） */
    .stButton button, button {
        border-radius: 20px !important;
        font-weight: 600 !important;
        background-color: #0f1419 !important;
        color: #ffffff !important;
        border: none !important;
    }
    .stButton button *, button * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .stButton button:hover, button:hover {
        background-color: #272c30 !important;
    }

    /* スマホ画面（幅768px以下）でのレスポンシブ調整 */
    @media (max-width: 768px) {
        .app-title {
            font-size: 24px;
        }
        .golf-card {
            padding: 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown("<div class='app-title'>⛳ Threads Golf Match</div>", unsafe_allow_html=True)
st.markdown("<div class='app-subtitle'>Threadsアカウントで繋がる、ゴルフラウンドマッチング</div>", unsafe_allow_html=True)

st.markdown("---")

# 47都道府県と主な市のデータ
prefectures_cities = {
    "東京都": ["千代田区", "新宿区", "渋谷区", "港区", "八王子市", "町田市"],
    "大阪府": ["大阪市", "堺市", "豊中市", "枚方市", "高槻市"],
    "兵庫県": ["神戸市", "姫路市", "尼崎市", "明石市", "西宮市", "加古川市", "宝塚市", "三木市", "小野市"],
    "京都府": ["京都市", "宇治市", "亀岡市", "福知山市"],
    "神奈川県": ["横浜市", "川崎市", "相模原市", "藤沢市", "鎌倉市"],
    "愛知県": ["名古屋市", "豊田市", "岡崎市", "一宮市"],
    "福岡県": ["福岡市", "北九州市", "久留米市"],
    "北海道": ["札幌市", "函館市", "旭川市"]
}

# セッション状態の初期化
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "host": "ryu_golf300yd", 
            "course": "姫路周辺のゴルフ場", 
            "score": "90台", 
            "composition": "男女混合・異性OK", 
            "pref": "兵庫県",
            "city": "姫路市", 
            "current_members": 2,
            "max_members": 4,
            "comment": "姫路周辺で楽しくラウンドしましょう！",
            "threads": "https://www.threads.net/@ryu_golf300yd",
            "comments": [["sakura_golf", "参加したいです！よろしくお願いします！"]]
        }
    ]

# --- サイドバー：ログインと新規投稿 ---
st.sidebar.markdown("### 👤 ログイン設定")
logged_in_user = st.sidebar.text_input("Threads ID（例: ryu_golf300yd）", value="ryu_golf300yd")
st.sidebar.markdown(f"ログイン中: **@{logged_in_user}**")

st.sidebar.markdown("---")
st.sidebar.markdown("### ✍️ 新規メンバー募集")
with st.sidebar.form("create_post_form", clear_on_submit=True):
    reg_pref = st.selectbox("都道府県", list(prefectures_cities.keys()))
    reg_city = st.selectbox("市", prefectures_cities[reg_pref])
    target_course = st.text_input("ゴルフ場名", "姫路周辺のコース")
    user_score = st.text_input("希望スコア帯", "90台")
    composition_type = st.selectbox("メンバー構成", ["男女混合・異性OK", "女子ゴルフ（女子のみ）"])
    max_m = st.slider("募集人数（最大4人）", 2, 4, 4)
    current_m = st.slider("現在の人数（主催者含む）", 1, 3, 1)
    post_comment = st.text_area("ひとことメッセージ", "楽しく回りましょう！")
    
    submitted = st.form_submit_button("募集を投稿する")
    if submitted:
        new_id = len(st.session_state.posts) + 1
        st.session_state.posts.insert(0, {
            "id": new_id,
            "host": logged_in_user,
            "course": target_course,
            "score": user_score,
            "composition": composition_type,
            "pref": reg_pref,
            "city": reg_city,
            "current_members": current_m,
            "max_members": max_m,
            "comment": post_comment,
            "threads": f"https://www.threads.net/@{logged_in_user}",
            "comments": []
        })
        st.sidebar.success("投稿しました！")

# --- メイン画面：検索と募集一覧 ---
st.markdown("### 🔍 ラウンド募集を検索")
col1, col2 = st.columns(2)
with col1:
    sel_pref = st.selectbox("都道府県で絞り込み", ["すべて"] + list(prefectures_cities.keys()))
with col2:
    if sel_pref != "すべて":
        city_opts = ["すべて"] + prefectures_cities[sel_pref]
    else:
        city_opts = ["すべて"]
    sel_city = st.selectbox("市で絞り込み", city_opts)

# フィルター処理
filtered_posts = st.session_state.posts
if sel_pref != "すべて":
    filtered_posts = [p for p in filtered_posts if p["pref"] == sel_pref]
if sel_city != "すべて":
    filtered_posts = [p for p in filtered_posts if p["city"] == sel_city]

st.markdown(f"### 📋 募集一覧 ({len(filtered_posts)}件)")

# 各募集カードの表示
for post in filtered_posts:
    badge_class = "badge-mix" if post['composition'] == "男女混合・異性OK" else "badge-women"
    is_full = post['current_members'] >= post['max_members']
    status_text = "🔴 満員" if is_full else f"🟢 募集中 ({post['current_members']}/{post['max_members']}人)"
    
    st.markdown(f"""
    <div class="golf-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 6px;">
            <span style="font-weight: 700; font-size: 15px; color: #0f1419;">🏌️ 主催: @{post['host']}</span>
            <div>
                <span class="status-badge">{status_text}</span>
                <span class="{badge_class}">{post['composition']}</span>
            </div>
        </div>
        <div style="color: #536471; font-size: 13px; margin-bottom: 8px; font-weight: 500;">
            📍 <b>エリア:</b> {post['pref']} {post['city']} &nbsp;|&nbsp; ⛳ <b>コース:</b> {post['course']} &nbsp;|&nbsp; 🎯 <b>スコア:</b> {post['score']}
        </div>
        <div style="background-color: #f7f9f9; padding: 12px; border-radius: 12px; color: #0f1419; font-size: 14px; margin-bottom: 10px;">
            "{post['comment']}"
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # コメント一覧
    if post['comments']:
        st.markdown("<span style='font-size: 13px; color: #536471;'>💬 コメント</span>", unsafe_allow_html=True)
        for c_user, c_text in post['comments']:
            st.markdown(f"<span style='font-size: 13px; color: #0f1419;'>- **@{c_user}**: {c_text}</span>", unsafe_allow_html=True)
    
    # コメント投稿フォーム
    with st.form(f"comment_form_{post['id']}"):
        c_input = st.text_input("コメントを入力（参加希望や質問など）", key=f"input_{post['id']}")
        c_sub = st.form_submit_button("コメントする")
        if c_sub and c_input:
            post['comments'].append([logged_in_user, c_input])
            st.rerun()

    # 削除ボタン
    if post['host'] == logged_in_user:
        if st.button("🗑️ この募集を削除する", key=f"del_{post['id']}"):
            st.session_state.posts = [p for p in st.session_state.posts if p['id'] != post['id']]
            st.success("募集を削除しました。")
            st.rerun()

    st.markdown("---")
