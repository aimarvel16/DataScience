import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ CSV ----
df = pd.read_csv('Pokemon.csv')
df.columns=df.columns.str.replace(' ','')
# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
type1 = st.sidebar.multiselect(
    "Select the Type 1:",
    options=df["Type1"].unique(),
    default=df["Type1"].unique()
)

type2 = st.sidebar.multiselect(
    "Select the Type 2:",
    options=df["Type2"].unique(),
    default=df["Type2"].unique()
)

df_selection=df.query('Type1==@type1 & Type2==@type2')


# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_HP = round(df_selection["HP"].mean(), 1)
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_HP}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["Type1"]).sum()[["Total"]].sort_values(by="Total")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]
sales_by_type2 = df_selection.groupby(by=["Type2"]).sum()[["Total"]]
fig_type2_sales = px.bar(
    sales_by_type2,
    x=sales_by_type2.index,
    y="Total",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_type2),
    template="plotly_white",
)
fig_type2_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_product_sales, use_container_width=True)
right_column.plotly_chart(fig_type2_sales, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
