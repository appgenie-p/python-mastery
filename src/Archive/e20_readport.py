import csv

Portfolio = list[dict[str, str | int | float]]


# a function that reads a file into a list of dicts
def read_portfolio(filename: str) -> Portfolio:
    portfolio: Portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        _: list[str] = next(rows)
        for row in rows:
            record = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(record)
    return portfolio


if __name__ == "__main__":
    portfolio = read_portfolio("Data/portfolio.csv")
    from pprint import pprint

    pprint(portfolio)
