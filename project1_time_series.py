import pandas as pd
import matplotlib.pyplot as plt
dates=pd.date_range(start='2025-01-01',periods=180,freq="D")
categories=["electronics","clothing","furniture"]
data={
    "Date":dates,
    "category":[categories[i%3] for i in range(180)],
    "Sales":[200+(i%50)for i in range(180)]
}
df=pd.DataFrame(data)
#save dataset 
df.to_csv("sales_data.csv",index=False)
df.to_excel("sales_data.xlsx",index=False)
df=pd.read_csv("sales_data.csv")
df['Date']=pd.to_datetime(df['Date'])
monthly_sales=df.resample("M",on="Date")["Sales"].sum()
quaterly_sales=df.resample("Q",on="Date")["Sales"].sum()
plt.figure()
monthly_sales.plot()
plt.title("Monthly sales trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()
plt.figure()
quaterly_sales.plot()
plt.title("Quarterly sales trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("quarterly_sales.png")
plt.close()
category_sales=df.groupby("category")["Sales"].sum()
plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_sales_bar.png")
plt.close()
plt.figure()
category_sales.plot(kind="pie",autopct="%1.1f%%,startangle=90")
plt.title("category sales share")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales_pie.png")
plt.close()
summary_text = """
PROJECT 1: TIME SERIES & CATEGORY CHARTS

- Monthly and quarterly line charts show overall sales trends.
- Bar chart compares total sales across categories.
- Pie chart shows percentage share of each category.
- Proper labels, legends, and axis formatting improve readability.

Generated Files:
- sales_data.csv
- sales_data.xlsx
- monthly_sales.png
- quarterly_sales.png
- category_sales_bar.png
- category_sales_pie.png
""" 
with open("Summary.txt","w") as f:
    f.write(summary_text)
    print("project completed successfully")
