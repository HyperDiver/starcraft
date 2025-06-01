import streamlit as st

# 初始化狀態
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
