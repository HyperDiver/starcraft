import streamlit as st
grid_size = 5
if "grid_data" not in st.session_state:
    st.session_state.grid_data = [[{"unit": None} for _ in range(grid_size)] for _ in range(grid_size)]
if "resources" not in st.session_state:
    st.session_state.resources = {"晶礦": 500, "油礦": 300}
if "buildings" not in st.session_state:
    st.session_state.buildings = {"基地": 1, "訓練營": 0, "飛機場": 0}
if "units" not in st.session_state:
    st.session_state.units = {"工兵": 1, "陸戰隊": 0, "幽靈戰機": 0, "大和": 0}

st.title("星海簡化版：人類指揮官")

# 顯示資源
st.subheader("資源")
st.write(st.session_state.resources)

# 顯示建築
st.subheader("建築")
st.write(st.session_state.buildings)

# 顯示單位
st.subheader("單位")
st.write(st.session_state.units)

# 訓練功能
unit_costs = {
    "工兵": {"晶礦": 50, "油礦": 0, "訓練所": "基地"},
    "陸戰隊": {"晶礦": 100, "油礦": 20, "訓練所": "訓練營"},
    "幽靈戰機": {"晶礦": 200, "油礦": 100, "訓練所": "飛機場"},
    "大和": {"晶礦": 500, "油礦": 300, "訓練所": "飛機場"}
}
st.write("## 戰場網格")

# 模擬兵種圖片（可換成實際圖片網址或檔案）
unit_images = {
    "marine": "https://static.wikia.nocookie.net/starcraft/images/d/d9/Marine_SC2_CncArt1.jpg",
    "ghost": "https://static.wikia.nocookie.net/starcraft/images/e/e1/Ghost_SC2_Rend1.jpg",
    "yamato": "https://static.wikia.nocookie.net/starcraft/images/3/36/Battlecruiser_SC2_Rend1.jpg",
    None: "https://via.placeholder.com/80"
}

# 繪製網格
for row in range(grid_size):
    cols = st.columns(grid_size)
    for col in range(grid_size):
        cell = st.session_state.grid_data[row][col]
        with cols[col]:
            st.image(unit_images[cell["unit"]], width=80)
            if st.button(f"{row},{col} 選擇", key=f"btn_{row}_{col}"):
                st.session_state.selected = (row, col)

# 顯示選中的格子
if "selected" in st.session_state:
    row, col = st.session_state.selected
    st.markdown(f"### 選中格子：({row}, {col})")
    unit = st.selectbox("選擇兵種", ["marine", "ghost", "yamato", None])
    st.session_state.grid_data[row][col]["unit"] = unit
st.subheader("訓練單位")
for unit in unit_costs:
    cost = unit_costs[unit]
    if st.button(f"訓練 {unit}"):
        building = cost["訓練所"]
        if st.session_state.buildings[building] > 0:
            enough = all(st.session_state.resources[k] >= v for k, v in cost.items() if k in st.session_state.resources)
            if enough:
                for k, v in cost.items():
                    if k in st.session_state.resources:
                        st.session_state.resources[k] -= v
                st.session_state.units[unit] += 1
                st.success(f"{unit} 訓練完成！")
            else:
                st.error("資源不足")
        else:
            st.error(f"尚未建造 {building}")
