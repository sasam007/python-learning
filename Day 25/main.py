import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_counts = data["Primary Fur Color"].value_counts()

summary = pandas.DataFrame({
    "color": ["gray", "black", "cinnamon"],
    "number": [
        fur_counts.get("Gray", 0),
        fur_counts.get("Black", 0),
        fur_counts.get("Cinnamon", 0),
    ],
})
summary.to_csv("squirrel_data.csv", index=False)
