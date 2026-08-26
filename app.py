import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Threads Golf Match",
    page_icon="⛳",
    layout="centered"
)

# レスポンシブ対応＆デザインCSS
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
    .gear-card {
        background: #ffffff;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 10px;
        font-size: 13px;
    }
    .gear-title {
        font-weight: 700;
        color: #0f1419;
        margin-bottom: 3px;
    }
    .gear-desc {
        color: #536471;
        font-size: 12px;
        line-height: 1.4;
        margin-bottom: 6px;
    }
    .gear-link {
        display: inline-block;
        background-color: #0f1419;
        color: #ffffff !important;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 600;
        text-decoration: none;
    }
    .gear-link:hover {
        background-color: #272c30;
    }
    .badge-sample {
        background-color: #fff3bf;
        color: #d9480f;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        border: 1px solid #ffe066;
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

# 47都道府県と主な市の完全データ
prefectures_cities = {
    "北海道": ["札幌市", "函館市", "旭川市", "釧路市", "帯広市", "苫小牧市"],
    "青森県": ["青森市", "弘前市", "八戸市"],
    "岩手県": ["盛岡市", "花巻市", "奥州市"],
    "宮城県": ["仙台市", "石巻市", "大崎市"],
    "秋田県": ["秋田市", "横手市", "由利本荘市"],
    "山形県": ["山形市", "米沢市", "鶴岡市"],
    "福島県": ["福島市", "会津若松市", "郡山市", "いわき市"],
    "茨城県": ["水戸市", "つくば市", "日立市", "土浦市"],
    "栃木県": ["宇都宮市", "小山市", "足利市"],
    "群馬県": ["前橋市", "高崎市", "太田市"],
    "埼玉県": ["さいたま市", "川越市", "川口市", "所沢市", "越谷市"],
    "千葉県": ["千葉市", "船橋市", "柏市", "松戸市", "市川市"],
    "東京都": ["千代田区", "新宿区", "渋谷区", "港区", "八王子市", "町田市", "世田谷区", "練馬区"],
    "神奈川県": ["横浜市", "川崎市", "相模原市", "藤沢市", "鎌倉市", "横須賀市"],
    "新潟県": ["新潟市", "長岡市", "上越市"],
    "富山県": ["富山市", "高岡市"],
    "石川県": ["金沢市", "小松市"],
    "福井県": ["福井市", "敦賀市"],
    "山梨県": ["甲府市", "甲斐市", "富士吉田市"],
    "長野県": ["長野市", "松本市", "上田市"],
    "岐阜県": ["岐阜市", "大垣市", "高山市", "各務原市"],
    "静岡県": ["静岡市", "浜松市", "沼津市", "富士市"],
    "愛知県": ["名古屋市", "豊田市", "岡崎市", "一宮市", "春日井市"],
    "三重県": ["津市", "四日市市", "鈴鹿市"],
    "滋賀県": ["大津市", "草津市", "彦根市"],
    "京都府": ["京都市", "宇治市", "亀岡市", "福知山市"],
    "大阪府": ["大阪市", "堺市", "豊中市", "枚方市", "高槻市", "東大阪市"],
    "兵庫県": ["神戸市", "姫路市", "尼崎市", "明石市", "西宮市", "加古川市", "宝塚市", "三木市", "小野市", "豊岡市"],
    "奈良県": ["奈良市", "橿原市", "生駒市"],
    "和歌山県": ["和歌山市", "田辺市", "紀の川市"],
    "鳥取県": ["鳥取市", "米子市"],
    "島根県": ["松江市", "出雲市"],
    "岡山県": ["岡山市", "倉敷市", "津山市"],
    "広島県": ["広島市", "福山市", "呉市", "尾道市"],
    "山口県": ["下関市", "山口市", "宇部市"],
    "徳島県": ["徳島市", "阿南市"],
    "香川県": ["高松市", "丸亀市"],
    "愛媛県": ["松山市", "今治市", "新居浜市"],
    "高知県": ["高知市", "南国市"],
    "福岡県": ["福岡市", "北九州市", "久留米市", "飯塚市"],
    "佐賀県": ["佐賀市", "唐津市"],
    "長崎県": ["長崎市", "佐世保市", "諫早市"],
    "熊本県": ["熊本市", "八代市", "天草市"],
    "大分県": ["大分市", "別府市", "中津市"],
    "宮崎県": ["宮崎市", "都城市", "延岡市"],
    "鹿児島県": ["鹿児島市", "霧島市", "鹿屋市"],
    "沖縄県": ["那覇市", "沖縄市", "うるま市", "宜野湾市"]
}

# セッション状態の初期化
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "is_sample": True,
            "host": "ryu_golf300yd", 
            "course": "姫路周辺のゴルフ場", 
            "score": "90台", 
            "composition": "男女混合・異性OK", 
            "pref": "兵庫県",
            "city": "姫路市", 
            "current_members": 2,
            "max_members": 4,
            "comment": "【投稿例】姫路周辺で楽しくラウンドしましょう！お気軽にコメントください！",
            "threads": "https://www.threads.net/@ryu_golf300yd",
            "comments": [["sakura_golf", "参加希望です！よろしくお願いします！（※コメント例）"]]
        }
    ]

# --- サイドバー：ログインと新規投稿 ---
st.sidebar.markdown("### 👤 ログイン設定")
logged_in_user = st.sidebar.text_input("Threads ID（例: ryu_golf300yd）", value="ryu_golf300yd")
st.sidebar.markdown(f"ログイン中: **@{logged_in_user}**")

st.sidebar.markdown("---")
st.sidebar.markdown("### ✍️ 新規メンバー募集")

reg_pref = st.sidebar.selectbox("都道府県", list(prefectures_cities.keys()), key="form_pref")
reg_city = st.sidebar.selectbox("市", prefectures_cities[reg_pref], key="form_city")

with st.sidebar.form("create_post_form", clear_on_submit=False):
    target_course = st.text_input("ゴルフ場名", value="", placeholder="例: 〇〇カントリークラブ")
    user_score = st.text_input("希望スコア帯", "90台")
    composition_type = st.selectbox("メンバー構成", ["男女混合・異性OK", "女子ゴルフ（女子のみ）"])
    max_m = st.slider("募集人数（最大4人）", 2, 4, 4)
    current_m = st.slider("現在の人数（主催者含む）", 1, 3, 1)
    post_comment = st.text_area("ひとことメッセージ", "楽しく回りましょう！")
    
    submitted = st.form_submit_button("募集を投稿する")
    if submitted:
        # 空欄チェック
        if not target_course.strip():
            target_course = "指定なし"
        
        new_id = len(st.session_state.posts) + 1
        st.session_state.posts.insert(0, {
            "id": new_id,
            "is_sample": False,
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

# --- サイドバー：おすすめゴルフギア ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 おすすめゴルフギア")
st.sidebar.markdown("<span style='font-size: 12px; color: #536471;'>ラウンドや自宅練習で本当に役立つ厳選アイテム</span>", unsafe_allow_html=True)

st.sidebar.markdown("""<div class="gear-card">
<div class="gear-title">🔭 Laser Sniper ELUA</div>
<div class="gear-desc">軽量・超高速計測＆高低差対応。コスパ最強の人気レーザー距離計。</div>
<a href="https://a.r10.to/hRKltx" target="_blank" class="gear-link">楽天で見る ↗</a>
</div>
<div class="gear-card">
<div class="gear-title">⛳ ツアーティー（TOUR TEE）</div>
<div class="gear-desc">折れにくく抵抗を極限まで削減。飛びと耐久性を両立した定番ティー。</div>
<a href="https://a.r10.to/hPjMLQ" target="_blank" class="gear-link">楽天で見る ↗</a>
</div>
<div class="gear-card">
<div class="gear-title">🏌️ ダイヤスイング（練習器具）</div>
<div class="gear-desc">自宅で理想のタメとインパクトの加速ポイントが身につくロングセラー器具。</div>
<a href="https://a.r10.to/hPjqew" target="_blank" class="gear-link">楽天で見る ↗</a>
</div>
<div class="gear-card">
<div class="gear-title">⚡ タイトリスト PRO V1</div>
<div class="gear-desc">世界中のツアープロが認める圧倒的スピン性能と直進性。</div>
<a href="https://a.r10.to/hP8EcH" target="_blank" class="gear-link">楽天で見る ↗</a>
</div>""", unsafe_allow_html=True)

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
    is_sample_badge = "<span class='badge-sample'>📌 投稿例（サンプル）</span>" if post.get("is_sample") else ""
    
    card_html = f"""<div class="golf-card">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 6px;">
<span style="font-weight: 700; font-size: 15px; color: #0f1419;">🏌️ 主催: @{post['host']}</span>
<div style="display: flex; gap: 6px; align-items: center;">
{is_sample_badge}
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
</div>"""
    st.markdown(card_html, unsafe_allow_html=True)
    
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
