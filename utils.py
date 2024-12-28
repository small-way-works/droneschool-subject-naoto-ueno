import argparse
import json
import math

FACTOR = 111320.0

# 樹木のxy座標を緯度経度に変換
def get_center_lat_lon(lat, lon, x, y):
  lat_to_meter = FACTOR
  lon_to_meter = FACTOR * math.cos(math.radians(lat))

  delta_lat = y / lat_to_meter
  delta_lon = x / lon_to_meter

  new_lat = lat + delta_lat
  new_lon = lon + delta_lon

  return new_lat, new_lon

# 樹木の周りに縁を描くウェイポイントを生成
def create_circle(
  center_lat,
  center_lon,
  radius,
  altitute,
  points=36
):
  waypoints = []
  for i in range(points):
    angle = 2 * math.pi * i / points
    dlat = radius * math.cos(angle) / FACTOR
    dlon = radius * math.sin(angle) / (FACTOR * math.cos(math.radians(center_lat)))
    waypoints.append((center_lat + dlat, center_lon + dlon, altitute))
  return waypoints

# 樹木の座標を読み込む
def load_tree_positions_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['trees']

# コマンドライン引数の処理
def process_cmd():
  parser = argparse.ArgumentParser(description="Tree point for flight control")
  parser.add_argument('--tree_file', type=str, help='Path to the tree positions file (JSON format)')
  args = parser.parse_args()
  return args

# 樹木の座標データを取得
def get_tree_data():
  args = process_cmd()
  if args.tree_file:
      trees = load_tree_positions_from_file(args.tree_file)
  else:
    trees = [
        [-7, 8],
        [1, 4],
        [10, 15],
    ]
  return trees