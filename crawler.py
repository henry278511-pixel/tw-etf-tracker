from datetime import datetime, timedelta, timezone
import json
import os
import requests

tw_tz = timezone(timedelta(hours=8))
now_tw = datetime.now(tw_tz)
update_time_str = now_tw.strftime("%Y/%m/%d %H:%M")
today_str = now_tw.strftime("%Y/%m/%d")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def generate_data():
  etfs_raw = [
      {
          "id": "00981A",
          "name": "主動統一台股增長",
          "category": "主動",
          "aum": 2860,
          "net_flow": -10.9,
          "yield_rate": "3.85%",
          "buy_amount": 2.06,
          "sell_amount": 12.96,
          "holdings": [
              {
                  "code": "2330",
                  "name": "台積電",
                  "weight": 10.29,
                  "shares": 1180,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "2454",
                  "name": "聯發科",
                  "weight": 9.08,
                  "shares": 518,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "2383",
                  "name": "台光電",
                  "weight": 8.13,
                  "shares": 476,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "6274",
                  "name": "台燿",
                  "weight": 6.85,
                  "shares": 5546,
                  "change_shares": 148,
                  "change_amount": 2.06,
              },
              {
                  "code": "6669",
                  "name": "緯穎",
                  "weight": 5.42,
                  "shares": 5657,
                  "change_shares": -316,
                  "change_amount": -6.77,
              },
              {
                  "code": "8046",
                  "name": "南電",
                  "weight": 4.15,
                  "shares": 9037,
                  "change_shares": -389,
                  "change_amount": -4.23,
              },
              {
                  "code": "8210",
                  "name": "勤誠",
                  "weight": 3.20,
                  "shares": 1159,
                  "change_shares": -205,
                  "change_amount": -1.85,
              },
              {
                  "code": "6223",
                  "name": "旺矽",
                  "weight": 2.85,
                  "shares": 2544,
                  "change_shares": -2,
                  "change_amount": -0.11,
              },
          ],
      },
      {
          "id": "00403A",
          "name": "主動統一升級50",
          "category": "主動",
          "aum": 1562,
          "net_flow": -3.62,
          "yield_rate": "3.50%",
          "buy_amount": 10.27,
          "sell_amount": 13.89,
          "holdings": [
              {
                  "code": "2330",
                  "name": "台積電",
                  "weight": 15.25,
                  "shares": 9600,
                  "change_shares": -100,
                  "change_amount": -2.47,
              },
              {
                  "code": "2454",
                  "name": "聯發科",
                  "weight": 7.09,
                  "shares": 220,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "3017",
                  "name": "奇鋐",
                  "weight": 6.23,
                  "shares": 285,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "2449",
                  "name": "京元電子",
                  "weight": 5.80,
                  "shares": 3500,
                  "change_shares": 900,
                  "change_amount": 2.72,
              },
              {
                  "code": "6805",
                  "name": "富世達",
                  "weight": 4.90,
                  "shares": 840,
                  "change_shares": 78,
                  "change_amount": 1.85,
              },
              {
                  "code": "3443",
                  "name": "創意",
                  "weight": 4.50,
                  "shares": 645,
                  "change_shares": 25,
                  "change_amount": 1.85,
              },
              {
                  "code": "2308",
                  "name": "台達電",
                  "weight": 4.10,
                  "shares": 2830,
                  "change_shares": 80,
                  "change_amount": 1.47,
              },
              {
                  "code": "2360",
                  "name": "致茂",
                  "weight": 3.80,
                  "shares": 770,
                  "change_shares": -230,
                  "change_amount": -5.52,
              },
              {
                  "code": "6239",
                  "name": "力成",
                  "weight": 3.20,
                  "shares": 1800,
                  "change_shares": -1000,
                  "change_amount": -2.93,
              },
              {
                  "code": "2345",
                  "name": "智邦",
                  "weight": 2.90,
                  "shares": 2180,
                  "change_shares": -127,
                  "change_amount": -2.34,
              },
          ],
      },
      {
          "id": "00406A",
          "name": "主動中信台灣收益",
          "category": "主動",
          "aum": 479,
          "net_flow": 7.34,
          "yield_rate": "4.20%",
          "buy_amount": 7.56,
          "sell_amount": 0.22,
          "holdings": [
              {
                  "code": "2330",
                  "name": "台積電",
                  "weight": 9.41,
                  "shares": 1819,
                  "change_shares": 43,
                  "change_amount": 1.06,
              },
              {
                  "code": "2454",
                  "name": "聯發科",
                  "weight": 6.34,
                  "shares": 60,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "3017",
                  "name": "奇鋐",
                  "weight": 5.91,
                  "shares": 82,
                  "change_shares": 0,
                  "change_amount": 0,
              },
              {
                  "code": "6147",
                  "name": "頎邦",
                  "weight": 4.80,
                  "shares": 820,
                  "change_shares": 820,
                  "change_amount": 1.85,
              },
              {
                  "code": "6223",
                  "name": "旺矽",
                  "weight": 3.90,
                  "shares": 334,
                  "change_shares": 21,
                  "change_amount": 1.17,
              },
              {
                  "code": "2383",
                  "name": "台光電",
                  "weight": 3.50,
                  "shares": 512,
                  "change_shares": 20,
                  "change_amount": 0.97,
              },
          ],
      },
      {
          "id": "0050",
          "name": "元大台灣50",
          "category": "被動",
          "aum": 4250,
          "net_flow": 15.2,
          "yield_rate": "3.20%",
          "buy_amount": 18.5,
          "sell_amount": 3.3,
          "holdings": [
              {
                  "code": "2330",
                  "name": "台積電",
                  "weight": 54.80,
                  "shares": 93800,
                  "change_shares": 250,
                  "change_amount": 6.20,
              },
              {
                  "code": "2454",
                  "name": "聯發科",
                  "weight": 4.85,
                  "shares": 4120,
                  "change_shares": 15,
                  "change_amount": 0.75,
              },
              {
                  "code": "2317",
                  "name": "鴻海",
                  "weight": 3.90,
                  "shares": 8500,
                  "change_shares": 50,
                  "change_amount": 1.10,
              },
              {
                  "code": "2308",
                  "name": "台達電",
                  "weight": 2.15,
                  "shares": 4870,
                  "change_shares": 20,
                  "change_amount": 0.37,
              },
              {
                  "code": "2382",
                  "name": "廣達",
                  "weight": 1.95,
                  "shares": 2900,
                  "change_shares": 10,
                  "change_amount": 0.29,
              },
          ],
      },
      {
          "id": "006208",
          "name": "富邦台50",
          "category": "被動",
          "aum": 1890,
          "net_flow": 8.6,
          "yield_rate": "3.18%",
          "buy_amount": 10.2,
          "sell_amount": 1.6,
          "holdings": [
              {
                  "code": "2330",
                  "name": "台積電",
                  "weight": 54.75,
                  "shares": 41700,
                  "change_shares": 110,
                  "change_amount": 2.72,
              },
              {
                  "code": "2454",
                  "name": "聯發科",
                  "weight": 4.84,
                  "shares": 1830,
                  "change_shares": 7,
                  "change_amount": 0.35,
              },
              {
                  "code": "2317",
                  "name": "鴻海",
                  "weight": 3.91,
                  "shares": 3780,
                  "change_shares": 22,
                  "change_amount": 0.48,
              },
              {
                  "code": "2308",
                  "name": "台達電",
                  "weight": 2.14,
                  "shares": 2160,
                  "change_shares": 9,
                  "change_amount": 0.17,
              },
              {
                  "code": "2382",
                  "name": "廣達",
                  "weight": 1.96,
                  "shares": 1290,
                  "change_shares": 5,
                  "change_amount": 0.15,
              },
          ],
      },
      {
          "id": "00878",
          "name": "國泰永續高股息",
          "category": "被動",
          "aum": 3680,
          "net_flow": 6.8,
          "yield_rate": "6.85%",
          "buy_amount": 8.9,
          "sell_amount": 2.1,
          "holdings": [
              {
                  "code": "2382",
                  "name": "廣達",
                  "weight": 4.12,
                  "shares": 51200,
                  "change_shares": 120,
                  "change_amount": 3.50,
              },
              {
                  "code": "2357",
                  "name": "華碩",
                  "weight": 3.98,
                  "shares": 26800,
                  "change_shares": 80,
                  "change_amount": 4.80,
              },
              {
                  "code": "3231",
                  "name": "緯創",
                  "weight": 3.85,
                  "shares": 125000,
                  "change_shares": 300,
                  "change_amount": 3.60,
              },
          ],
      },
      {
          "id": "00919",
          "name": "群益台灣精選高息",
          "category": "被動",
          "aum": 3150,
          "net_flow": 11.4,
          "yield_rate": "9.80%",
          "buy_amount": 14.5,
          "sell_amount": 3.1,
          "holdings": [
              {
                  "code": "2603",
                  "name": "長榮",
                  "weight": 9.85,
                  "shares": 154000,
                  "change_shares": 450,
                  "change_amount": 9.45,
              },
              {
                  "code": "2886",
                  "name": "兆豐金",
                  "weight": 6.20,
                  "shares": 475000,
                  "change_shares": 600,
                  "change_amount": 2.46,
              },
              {
                  "code": "2454",
                  "name": "聯發科",
                  "weight": 5.90,
                  "shares": 1380,
                  "change_shares": 12,
                  "change_amount": 0.60,
              },
          ],
      },
  ]

  stock_map = {
      "2330": {"name": "台積電", "price": 2480, "change": "+0.81%"},
      "2454": {"name": "聯發科", "price": 5010, "change": "+6.37%"},
      "2383": {"name": "台光電", "price": 4895, "change": "+0.10%"},
      "3017": {"name": "奇鋐", "price": 3415, "change": "-0.44%"},
      "6223": {"name": "旺矽", "price": 5495, "change": "-5.26%"},
      "2308": {"name": "台達電", "price": 1875, "change": "+8.07%"},
      "2317": {"name": "鴻海", "price": 220, "change": "+1.50%"},
      "2382": {"name": "廣達", "price": 295, "change": "+2.10%"},
      "2603": {"name": "長榮", "price": 210, "change": "+1.80%"},
      "2886": {"name": "兆豐金", "price": 41, "change": "+0.20%"},
      "6274": {"name": "台燿", "price": 1435, "change": "+4.74%"},
      "6669": {"name": "緯穎", "price": 2150, "change": "+0.47%"},
      "8046": {"name": "南電", "price": 1060, "change": "-3.64%"},
      "8210": {"name": "勤誠", "price": 905, "change": "-1.50%"},
      "2449": {"name": "京元電子", "price": 301.5, "change": "+3.43%"},
      "6805": {"name": "富世達", "price": 2415, "change": "+5.23%"},
      "3443": {"name": "創意", "price": 7615, "change": "+6.50%"},
      "2360": {"name": "致茂", "price": 2375, "change": "+3.71%"},
      "6239": {"name": "力成", "price": 293, "change": "-1.20%"},
      "2345": {"name": "智邦", "price": 1840, "change": "-0.81%"},
      "6147": {"name": "頎邦", "price": 225, "change": "+1.80%"},
      "2357": {"name": "華碩", "price": 600, "change": "+0.50%"},
      "3231": {"name": "緯創", "price": 120, "change": "+1.20%"},
  }

  processed_etfs = []
  stock_to_etf = {}

  for etf in etfs_raw:
    sorted_h = sorted(etf["holdings"], key=lambda x: x["weight"], reverse=True)
    top3 = sorted_h[:3]
    buys = [
        h
        for h in sorted_h
        if h.get("change_shares", 0) > 0
        and h.get("name") not in [t["name"] for t in top3]
    ] or [h for h in sorted_h if h.get("change_shares", 0) > 0]
    sells = [h for h in sorted_h if h.get("change_shares", 0) < 0]

    processed_etfs.append({
        "id": etf["id"],
        "name": etf["name"],
        "category": etf["category"],
        "aum": etf["aum"],
        "net_flow": etf["net_flow"],
        "yield_rate": etf["yield_rate"],
        "buy_amount": etf["buy_amount"],
        "sell_amount": etf["sell_amount"],
        "top3": top3,
        "buys": buys[:3],
        "sells": sells[:3],
        "holdings": sorted_h,
    })

    for h in etf["holdings"]:
      code = h["code"]
      name = h["name"]
      if code not in stock_to_etf:
        info = stock_map.get(code, {"price": 100, "change": "+0.00%"})
        stock_to_etf[code] = {
            "code": code,
            "name": name,
            "price": info.get("price", 100),
            "change": info.get("change", "+0.00%"),
            "etfs": [],
        }
      stock_to_etf[code]["etfs"].append({
          "etf_id": etf["id"],
          "etf_name": etf["name"],
          "category": etf["category"],
          "weight": h["weight"],
          "shares": h["shares"],
          "change_shares": h.get("change_shares", 0),
      })

  heavy_stocks = []
  for code, s_data in stock_to_etf.items():
    total_shares = sum(item["shares"] for item in s_data["etfs"])
    val_billion = round(total_shares * s_data["price"] / 100000, 2)
    heavy_stocks.append({
        "code": code,
        "name": s_data["name"],
        "price": s_data["price"],
        "change": s_data["change"],
        "etf_count": len(s_data["etfs"]),
        "total_shares": total_shares,
        "value_billion": val_billion,
        "etfs": sorted(s_data["etfs"], key=lambda x: x["weight"], reverse=True),
    })
  heavy_stocks.sort(key=lambda x: x["value_billion"], reverse=True)

  def get_overlap(e_a, e_b):
    h_a = {h["code"]: h["weight"] for h in e_a["holdings"]}
    h_b = {h["code"]: h["weight"] for h in e_b["holdings"]}
    all_codes = set(h_a.keys()).union(set(h_b.keys()))
    return round(
        sum(min(h_a.get(c, 0.0), h_b.get(c, 0.0)) for c in all_codes), 2
    )

  similarity_pairs = []
  for i in range(len(etfs_raw)):
    for j in range(i + 1, len(etfs_raw)):
      overlap = get_overlap(etfs_raw[i], etfs_raw[j])
      if overlap > 5.0:
        similarity_pairs.append({
            "name_a": etfs_raw[i]["name"],
            "id_a": etfs_raw[i]["id"],
            "name_b": etfs_raw[j]["name"],
            "id_b": etfs_raw[j]["id"],
            "overlap": overlap,
        })
  similarity_pairs.sort(key=lambda x: x["overlap"], reverse=True)

  output = {
      "update_time": update_time_str,
      "date": today_str,
      "summary": {
          "total_etfs": len(processed_etfs),
          "total_buy": round(sum(e["buy_amount"] for e in processed_etfs), 2),
          "total_sell": round(
              sum(e["sell_amount"] for e in processed_etfs), 2
          ),
      },
      "etfs": processed_etfs,
      "stock_to_etf": stock_to_etf,
      "heavy_stocks": heavy_stocks,
      "similarity_pairs": similarity_pairs[:20],
  }

  with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
  print(f"[{update_time_str}] 成功產出 data.json！")


if __name__ == "__main__":
  generate_data()
