pip install streamlit
pip install altair
pip install pandas
pip install plotly

import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

# px 모듈이 없다고 에러가 나는 경우에만 아래 방법으로 plotly 라이브러리 설치
# File > New > Terminal 선택 후, 창에 다음 구분 실행 pip install plotly

st.header("Unit 3. Streamlit Simple chart")

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv 읽고 확인하기
path = "https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv"
chart_data = pd.read_csv(path)


st.subheader("3-1. Simple Line chart")
# use_container_width=True 가로로 화면에 꽉 채워 줌
st.line_chart(chart_data, use_container_width=True)

# st.subheader('3-2. Simple Bar chart')
st.bar_chart(chart_data)

# st.subheader('3-3. Simple area chart')
st.area_chart(chart_data)

st.header("Unit 4. Altair chart")
# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv 읽고
# # melt 함수를 사용하여 데이터프레임 unpivot하기
path = "https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv"

df = pd.read_csv(path)
df_melted = pd.melt(df, id_vars="date", var_name="teams", value_name="sales")

#


# # columns 함수를 이용하여 좌-원본 데이터, 우-변환 데이터 확인하기

# with col1:
#     st.text('원본 데이터')
#     st.dataframe(df)
# with col2:
#     st.text('변경 데이터')
#     st.dataframe(df_melted)


# st.subheader('4-1. Altair Line chart')
my_chart1 = (
    alt.Chart(df_melted, title="일별 팀 매출 비교", mark="line")
    .encode(x="date", y="sales", color="teams", strokeDash="teams")
    .properties(width=650, height=350)
)

st.altair_chart(my_chart1, use_container_width=True)
# chart = alt.Chart(

# st.altair_chart(


# st.subheader('4-2. Altair Bar chart')
my_chart2 = (
    alt.Chart(df_melted, title="일별 팀 매출 비교", mark="bar")
    .encode(x="date", y=alt.Y("sales", stack="zero"), color="teams", strokeDash="teams")
    .properties(width=650, height=350)
)
my_text = (
    alt.Chart(df_melted)
    .mark_text(dx=0, dy=0, color="black")
    .encode(
        x="date",
        y=alt.Y("sales", stack="zero"),
        detail="teams",
        text=alt.Text("sales:Q"),
    )
)
st.altair_chart(my_chart2 + my_text)
# chart = alt.Chart


# text = alt.Chart(


# st.altair_chart(


# st.subheader('4-3. Altair Scatter chart')

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 확인하기
path = "https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv"
iris = pd.read_csv(path)
st.dataframe(iris)


# # caption으로 'sepal:꽃받침, petal:꽃잎' 설명 출력하기
st.caption("sepal:꽃받침, petal:꽃잎")

# # petal_length, petal_width로 Altair Circle chart 그리기
chart = alt.Chart(data=iris, mark="circle", width=650, height=350).encode(
    x="petal_length", y="petal_width", color="species"
)
st.altair_chart(chart, use_container_width=True)

st.header('Unit 5. Plotly chart')

# https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv 읽고 확인하기
path = 'https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv'
medal = pd.read_csv(path)
print(medal)

st.subheader('5-1. Plotly Pie/Donut chart')
# import plotly.express as px
fig = px.pie(medal, values= 'gold', names = 'nation', title = '올림픽 양궁 금메달 현황')
fig.update_traces(textposition = 'inside', textinfo = 'percent+label+value')
fig.update_layout(font = dict(size = 16))

st.plotly_chart(fig)
                
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# go.
# fig = make_subplots(rows=1, cols=2)
# fig1 = go.pie(medal, values= 'gold', names = 'nation', title = '올림픽 양궁 금메달 현황')
# fig1.update_traces(textposition = 'inside', textinfo = 'percent+label+value')
# fig1.update_layout(font = dict(size = 16))
# fig.add_trace(fig1, row = 1, col = 1)
# fig2 = go.pie(medal, values= 'silver', names = 'nation', title = '올림픽 양궁 은메달 현황')
# fig2.update_traces(textposition = 'inside', textinfo = 'percent+label+value')
# fig2.update_layout(font = dict(size = 16))
# st.plotly_chart(fig)


# fig.update_traces(
# fig.update_layout(
# # fig.update(layout_showlegend=False)  # 범례 표시 제거
# st.plotly_chart(

# st.subheader('5-2. Plotly Bar chart')
# # text_auto=True 값 표시 여부
# fig =


# st.plotly_chart(

# # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-2.chart.py
